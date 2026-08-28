"""
Bridge — SMA outfit → event horizon → capitulation/accumulation/bottom

Wires the three adapters together and gives the dashboard/calendar a single
call to answer: "Did this outfit firing mark a capitulation that resolved
into accumulation by OPEX?"

Example: DOG Mar 4-5 2026 (bearish vehicle, shocks Dow lower) → Triple Witching
Mar 20 → IXIC accumulation/bottom. The bridge joins:
  firing_ticker=DOG, outfit SMA, firing_date → inverse_map → index (DJI) →
  cross-index check (IXIC/SPX) → OPEX horizon → regime label.

All inputs are plain dicts/lists so the dashboard can POST JSON without
pandas, and the engine can call it from Influx results.

No network except optional Influx/TradeStation when caller asks for live bars.
"""
from __future__ import annotations
import datetime
from typing import Optional, List
from adapters.opex import resolve_event_horizon
from adapters.inverse_map import get_inverse_pair, MAJOR_INDEXES
from adapters.regime import label_regime

def bridge_outfit_to_horizon(
    firing_ticker: str,
    firing_date: str,  # YYYY-MM-DD
    outfit_name: Optional[str] = None,
    sma_period: Optional[int] = None,
    closes: Optional[List[float]] = None,
    volumes: Optional[List[float]] = None,
    sma_values: Optional[List[float]] = None,
    accumulation_index: str = "IXIC",  # user's Mar 2026 example: DOG → IXIC
) -> dict:
    """
    One call the UI or a backtest can use.

    If closes/volumes/sma_values are supplied, regime is labeled; otherwise
    regime is 'unknown' and the horizon math still works (so the calendar can
    link entries without live bars).

    Returns a JSON-serializable dict with unified error shape: {ok, error, ...}.
    """
    try:
        # 1. Inverse pair
        pair = get_inverse_pair(firing_ticker)
        if not pair:
            return {"ok": False, "error": f"Unknown vehicle ticker '{firing_ticker}' — add to inverse_map.py", "code": "UNKNOWN_TICKER"}

        # 2. OPEX horizon
        try:
            horizon = resolve_event_horizon(firing_date)
        except Exception as e:
            return {"ok": False, "error": f"Bad firing_date '{firing_date}': {e}", "code": "BAD_DATE"}

        # 3. Regime (if bars supplied)
        regime = None
        if closes is not None and volumes is not None and sma_values is not None:
            try:
                r = label_regime(closes, volumes, sma_values, sma_period=sma_period)
                regime = {"regime": r.regime, "confidence": r.confidence, "reason": r.reason,
                          "closes_below_sma": r.closes_below_sma, "closes_above_sma": r.closes_above_sma,
                          "avg_volume_ratio": r.avg_volume_ratio, "max_distance_sigma": r.max_distance_sigma}
            except Exception as e:
                regime = {"regime": "unknown", "confidence": 0.0, "reason": f"regime error: {e}"}
        else:
            regime = {"regime": "unknown", "confidence": 0.0, "reason": "no bars supplied — horizon only"}

        # 4. Inverse correlation note
        target_idx = MAJOR_INDEXES.get(accumulation_index.upper(), accumulation_index)
        is_inverse = pair.direction == "inverse"

        # 5. Narrative for the UI
        firing_kind = "bearish vehicle (inverse)" if is_inverse else "leveraged/long vehicle"
        narrative = (
            f"{firing_ticker} ({pair.leverage} {pair.underlying}) is a {firing_kind} on {pair.index}. "
            f"Firing on {firing_date} ({outfit_name or 'SMA outfit'}"
            f"{f' MA{sma_period}' if sma_period else ''}) → event horizon {horizon['event_horizon']} "
            f"({horizon['event_horizon_kind']}, {horizon['days_to_horizon']}d). "
            f"Accumulation target: {accumulation_index} ({target_idx}). "
            f"Regime: {regime['regime']} ({regime['confidence']:.0%}) — {regime['reason']}."
        )

        # Simple heuristic for "bottom signal" — mirrors user's thesis
        is_bottom_candidate = (
            regime["regime"] in ("capitulation", "accumulation") and horizon["days_to_horizon"] is not None and horizon["days_to_horizon"] <= 25
        )
        thesis = "capitulation → OPEX pin → accumulation" if is_bottom_candidate else "pending / distribution side"

        return {
            "ok": True,
            "firing_ticker": firing_ticker.upper(),
            "outfit": outfit_name,
            "sma_period": sma_period,
            "vehicle": {"ticker": pair.vehicle, "underlying": pair.underlying, "index": pair.index, "leverage": pair.leverage, "direction": pair.direction, "index_symbol_ts": pair.index_symbol_ts},
            "accumulation_target": {"index": accumulation_index.upper(), "ts_symbol": target_idx},
            "inverse_correlation": f"{pair.vehicle} ↑ ↔ {pair.index} ↓" if is_inverse else f"{pair.vehicle} ↔ {pair.index} (leveraged)",
            "horizon": horizon,
            "regime": regime,
            "thesis": thesis,
            "is_bottom_candidate": is_bottom_candidate,
            "narrative": narrative,
        }
    except Exception as e:
        return {"ok": False, "error": str(e), "code": "BRIDGE_ERROR"}

# CLI smoke: python bridge.py DOG 2026-03-05 --outfit "DOG" --sma 56 --target IXIC
if __name__ == "__main__":
    import argparse, json
    ap = argparse.ArgumentParser(description="Bridge DOG→IXIC example")
    ap.add_argument("ticker", nargs="?", default="DOG")
    ap.add_argument("date", nargs="?", default="2026-03-05")
    ap.add_argument("--outfit", default=None)
    ap.add_argument("--sma", type=int, default=None)
    ap.add_argument("--target", default="IXIC")
    args = ap.parse_args()
    print(json.dumps(bridge_outfit_to_horizon(args.ticker, args.date, args.outfit, args.sma, accumulation_index=args.target), indent=2))
