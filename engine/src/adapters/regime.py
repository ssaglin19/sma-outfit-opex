"""
Regime labeling — capitulation / accumulation / distribution / blow-off top

This is intentionally lightweight and stdlib-only so it can run without pandas.
It operates on a window of bars (list of dicts with OHLCV + SMA values) and
returns a label that the bridge can use to decide if an SMA firing marked a
real bottom or was noise.

Signals (mirrors build_ixic_chart.py + detector.py intuition, but at regime scale):
  capitulation:  price < key SMA, high volume, wide range, close near low
  accumulation:  high volume, price holds SMA, tight close, absorption wicks
  distribution:  price > key SMA, high volume, close weak vs high (late-stage)
  blow_off_top:  parabolic distance > 3σ above SMA, exhaustion wick

The detector already emits PBA/ASO/OBA per-bar; this module aggregates those
into a multi-bar regime so the OPEX horizon has something to resolve.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import List, Literal, Optional
import statistics

Regime = Literal["capitulation", "accumulation", "distribution", "blow_off_top", "neutral", "unknown"]

@dataclass(frozen=True)
class RegimeResult:
    regime: Regime
    confidence: float  # 0..1
    closes_below_sma: int
    closes_above_sma: int
    avg_volume_ratio: float
    max_distance_sigma: float
    reason: str

def _sma_distance_pct(close: float, sma: float) -> float:
    return (close - sma) / sma * 100 if sma else 0.0

def label_regime(
    closes: List[float],
    volumes: List[float],
    sma_values: List[float],
    highs: Optional[List[float]] = None,
    lows: Optional[List[float]] = None,
    sma_period: Optional[int] = None,
) -> RegimeResult:
    """
    Label the regime of the window. All lists same length, oldest→newest.
    sma_values may contain None for warmup bars — they are skipped.
    """
    if not closes or not volumes or not sma_values or len(closes) < 5:
        return RegimeResult("unknown", 0.0, 0, 0, 0.0, 0.0, "insufficient bars")

    # Align to bars where SMA is available
    triples = [(c, v, s) for c, v, s in zip(closes, volumes, sma_values) if s is not None and s > 0]
    if len(triples) < 5:
        return RegimeResult("unknown", 0.0, 0, 0, 0.0, 0.0, "insufficient SMA coverage")

    closes_a = [t[0] for t in triples]
    vols_a = [t[1] for t in triples]
    smas_a = [t[2] for t in triples]

    n = len(closes_a)
    below = sum(1 for c, s in zip(closes_a, smas_a) if c < s)
    above = n - below

    # Volume ratio vs median
    med_vol = statistics.median(vols_a) if vols_a else 1
    vol_ratios = [v / med_vol if med_vol else 1 for v in vols_a]
    avg_vol_ratio = statistics.mean(vol_ratios) if vol_ratios else 1.0

    # Distance in % and sigma
    distances = [_sma_distance_pct(c, s) for c, s in zip(closes_a, smas_a)]
    mean_d = statistics.mean(distances)
    stdev_d = statistics.pstdev(distances) if len(distances) > 1 else 1.0
    # sigma of the most extreme bar
    max_sigma = max(abs(d - mean_d) / (stdev_d or 1) for d in distances)

    # Blow-off top: large positive distance + sigma
    max_dist = max(distances)
    min_dist = min(distances)

    # Heuristic thresholds — tuned to be conservative; bridge can raise confidence threshold
    last_close = closes_a[-1]
    last_sma = smas_a[-1]
    last_dist = _sma_distance_pct(last_close, last_sma)

    # Capitulation: majority below SMA, last dist strongly negative, high volume
    if below / n >= 0.6 and last_dist < -1.5 and avg_vol_ratio > 1.3:
        conf = min(0.55 + (abs(last_dist) / 10) + (avg_vol_ratio - 1) * 0.2, 0.92)
        return RegimeResult("capitulation", round(conf, 2), below, above, round(avg_vol_ratio, 2), round(max_sigma, 2),
                            f"{below}/{n} closes below SMA, last {last_dist:.1f}% below, vol {avg_vol_ratio:.1f}×")

    # Accumulation: price holds / reclaims SMA after capitulation, volume still elevated, distance near 0
    if abs(last_dist) < 1.2 and avg_vol_ratio > 1.2 and below >= 2 and above >= 2:
        conf = min(0.5 + (avg_vol_ratio - 1) * 0.25, 0.88)
        return RegimeResult("accumulation", round(conf, 2), below, above, round(avg_vol_ratio, 2), round(max_sigma, 2),
                            f"reclaim: last {last_dist:+.1f}% vs SMA, mixed closes, vol {avg_vol_ratio:.1f}×")

    # Blow-off top: extreme positive distance, high sigma
    if max_dist > 4.0 and max_sigma > 2.2 and last_dist > 2.0:
        conf = min(0.5 + (max_dist / 10) + (max_sigma - 2) * 0.15, 0.90)
        return RegimeResult("blow_off_top", round(conf, 2), below, above, round(avg_vol_ratio, 2), round(max_sigma, 2),
                            f"max +{max_dist:.1f}% above SMA ({max_sigma:.1f}σ), last +{last_dist:.1f}%")

    # Distribution: majority above SMA, volume elevated, closes weakening (last dist smaller than max)
    if above / n >= 0.6 and max_dist > 1.5 and last_dist < max_dist - 0.8 and avg_vol_ratio > 1.15:
        conf = min(0.5 + (max_dist - last_dist) * 0.08, 0.85)
        return RegimeResult("distribution", round(conf, 2), below, above, round(avg_vol_ratio, 2), round(max_sigma, 2),
                            f"{above}/{n} above SMA, faded from +{max_dist:.1f}% to +{last_dist:.1f}%, vol {avg_vol_ratio:.1f}×")

    # Neutral
    return RegimeResult("neutral", 0.45, below, above, round(avg_vol_ratio, 2), round(max_sigma, 2),
                        f"balanced: {below} below / {above} above, last {last_dist:+.1f}%, vol {avg_vol_ratio:.1f}×")
