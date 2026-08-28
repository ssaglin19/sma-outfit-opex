"""
Backtest: SPXU on March 2, 2026
================================
Focus: MA720 ($48.78) on the 180 outfit.
Question: Was there institutional ABSORPTION at this reversal level?

REVERSAL SIGNAL LOGIC (180 = 180° flip):
At an SMA reversal level, the institutional footprint is NOT aggressive buying.
It's PASSIVE buying absorbing AGGRESSIVE selling. The tells:

Signal 1 — ABSORPTION: High volume + negative delta + price holds above SMA.
           Sellers hammered it, someone ate every share, price didn't break.
           Score: volume_ratio * (1 + abs(negative_delta)) — MORE selling + MORE volume = MORE absorption.

Signal 2 — REJECTION WICK: Low pierces below MA, Close finishes above MA.
           The wick IS the institutional bid. Price tried to break, got rejected.
           Score: binary (did it wick below and close above?) + wick depth bonus.

Signal 3 — VOLUME CONCENTRATION: What % of the day's total volume printed at this one level?
           If a disproportionate chunk of volume concentrated at MA720, someone was working an order.
           Score: (volume_at_level / day_volume) normalized.

Signal 4 — TRADE SIZE: Volume/TotalTicks at level bars vs non-level bars.
           Large avg trade = block orders. Small avg trade = retail noise.
           Score: sigma above mean.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import json
import statistics
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from ts_client import TradeStationClient
from config import SMA_OUTFITS
PENNY = 0.01  # canonical, same as detector.py:47 / historical_scan.py:23
try:
    from detector import compute_all_smas, count_ohlc_interactions  # type: ignore
except ImportError:
    try:
        from historical_scan import compute_all_smas  # type: ignore
        from detector import count_ohlc_interactions  # type: ignore
    except ImportError:
        # Last resort: legacy retired engine still holds count_ohlc_interactions at archive/old_system
        import os as _os, sys as _sys
        _sys.path.insert(0, _os.path.join(_os.path.dirname(__file__), '..', 'archive', 'old_system'))
        from sma_alert_engine import compute_all_smas, count_ohlc_interactions  # type: ignore


SYMBOL = 'SPXU'
TARGET_DATE = '2026-03-02'
INTERVAL = 30
UNIT = 'Minute'
FIRSTDATE = '2025-06-01'
LASTDATE = '2026-03-03'
PROXIMITY_DOLLARS = 0.25


def score_bar(bar, day_baselines):
    """
    Score a single bar at the MA720 level for reversal/absorption signals.
    Returns dict with individual signal scores and a composite score.
    """
    scores = {}

    vol_ratio = bar['vol_ratio']
    delta_pct = bar['delta_pct']  # negative = sellers aggressive
    ma720 = bar['ma720']
    low = bar['low']
    close = bar['close']
    high = bar['high']
    volume = bar['volume']
    avg_trade = bar['avg_trade_size']
    sigma = bar['trade_size_sigma']
    day_vol = day_baselines['day_total_volume']

    # ---- SIGNAL 1: ABSORPTION ----
    # High volume + negative delta + price holds/closes above MA = absorption
    # The WORSE the delta and the HIGHER the volume, the MORE absorption
    absorption_score = 0.0
    absorbed = False
    if delta_pct < -3 and close >= ma720 - 0.05:
        # Sellers were aggressive but price held — someone absorbed
        # Scale: more volume * more negative delta = stronger absorption
        sell_intensity = min(abs(delta_pct) / 15, 1.0)  # cap at 15%
        vol_factor = min(vol_ratio / 2.0, 1.0)  # cap at 2x avg
        absorption_score = sell_intensity * vol_factor
        absorbed = True
    elif delta_pct < -3 and close >= ma720 - PROXIMITY_DOLLARS:
        # Partial absorption — closed slightly below but didn't collapse
        sell_intensity = min(abs(delta_pct) / 15, 1.0)
        vol_factor = min(vol_ratio / 2.5, 0.7)
        absorption_score = sell_intensity * vol_factor * 0.5
        absorbed = True

    scores['absorption'] = {
        'score': round(absorption_score, 3),
        'delta_pct': delta_pct,
        'vol_ratio': vol_ratio,
        'close_vs_ma': round(close - ma720, 4),
        'absorbed': absorbed,
    }

    # ---- SIGNAL 2: REJECTION WICK ----
    # Low pierces below MA720, Close finishes above MA720
    rejection_score = 0.0
    wick_below = low < ma720
    closed_above = close > ma720
    if wick_below and closed_above:
        wick_depth = ma720 - low  # how far below MA it wicked
        body_recovery = close - ma720  # how far above MA it closed
        rejection_score = min(1.0, (wick_depth / ma720 * 200) + (body_recovery / ma720 * 100))
    elif wick_below and close >= ma720 - 0.05:
        # Wicked below but closed ~at the level (not quite above)
        wick_depth = ma720 - low
        rejection_score = min(0.5, wick_depth / ma720 * 100)

    scores['rejection_wick'] = {
        'score': round(rejection_score, 3),
        'wick_below': wick_below,
        'closed_above': closed_above,
        'low': low,
        'close': close,
        'ma720': ma720,
        'wick_depth': round(ma720 - low, 4) if wick_below else 0,
    }

    # ---- SIGNAL 3: VOLUME CONCENTRATION ----
    # What % of the day's volume printed on this bar at the level?
    vol_concentration = volume / max(1, day_vol)
    # If >5% of the day's volume printed on one 30M bar at the SMA, that's notable
    # If >10%, that's significant
    concentration_score = 0.0
    if vol_concentration > 0.10:
        concentration_score = 1.0
    elif vol_concentration > 0.05:
        concentration_score = vol_concentration / 0.10
    elif vol_concentration > 0.03:
        concentration_score = vol_concentration / 0.15

    scores['volume_concentration'] = {
        'score': round(concentration_score, 3),
        'bar_volume': volume,
        'day_volume': day_vol,
        'pct_of_day': round(vol_concentration * 100, 2),
    }

    # ---- SIGNAL 4: TRADE SIZE ----
    # Avg trade size at level vs day average — large = block orders
    trade_score = 0.0
    if sigma >= 2.0:
        trade_score = 1.0
    elif sigma >= 1.5:
        trade_score = 0.7
    elif sigma >= 1.0:
        trade_score = 0.4
    elif sigma >= 0.5:
        trade_score = 0.15

    scores['trade_size'] = {
        'score': round(trade_score, 3),
        'avg_trade': avg_trade,
        'day_avg': day_baselines['day_avg_trade_size'],
        'sigma': sigma,
    }

    # ---- COMPOSITE ----
    composite = (
        absorption_score * 0.35 +
        rejection_score * 0.30 +
        concentration_score * 0.20 +
        trade_score * 0.15
    )

    scores['_composite'] = round(composite, 3)
    scores['_max'] = 1.0

    return scores


def main():
    print(f"=" * 70)
    print(f"BACKTEST: {SYMBOL} | {TARGET_DATE} | {INTERVAL}M | 180 Outfit MA720")
    print(f"REVERSAL ABSORPTION ANALYSIS")
    print(f"=" * 70)

    # --- Fetch ---
    print(f"\n[1] Fetching {SYMBOL} {INTERVAL}M bars...")
    ts = TradeStationClient()
    df = ts.get_bars(SYMBOL, INTERVAL, UNIT, firstdate=FIRSTDATE, lastdate=LASTDATE)
    if df.empty:
        print("  ERROR: No data.")
        return

    df.index = df.index.tz_convert('US/Eastern')
    print(f"  {len(df)} bars | {df.index[0]} to {df.index[-1]}")

    inst_cols = ['UpVolume', 'DownVolume', 'UpTicks', 'DownTicks', 'TotalTicks']
    present = [c for c in inst_cols if c in df.columns and df[c].sum() > 0]
    print(f"  Institutional columns: {present}")

    # --- Filter ---
    target = pd.Timestamp(TARGET_DATE, tz='US/Eastern')
    target_end = target + timedelta(days=1)
    df_through = df[df.index < target_end].copy()
    df_day = df_through[df_through.index >= target].copy()

    if df_day.empty:
        print(f"  ERROR: No bars on {TARGET_DATE}")
        return

    print(f"  Target day: {len(df_day)} bars ({df_day.index[0]} to {df_day.index[-1]})")

    # --- Compute SMAs ---
    print(f"\n[2] Computing SMAs...")
    sma_values = compute_all_smas(df_through)

    # --- Outfit ranking ---
    scan_bars = len(df_day)
    outfit_counts = count_ohlc_interactions(df_through, scan_bars=scan_bars)
    ranked = sorted(outfit_counts.items(), key=lambda x: -x[1])
    print(f"\n  Outfit rankings:")
    for i, (name, hits) in enumerate(ranked[:5], 1):
        print(f"    {i}. {name}: {hits} hits")

    # --- Day baselines ---
    sma_col = 'SMA_720'
    if sma_col not in df_through.columns:
        print("  ERROR: SMA_720 not computed")
        return

    day_slice = df_through.iloc[-scan_bars:]
    has_ticks = 'TotalTicks' in day_slice.columns and day_slice['TotalTicks'].sum() > 0
    day_avg_volume = day_slice['Volume'].mean()
    day_total_volume = int(day_slice['Volume'].sum())
    day_total_up = int(day_slice['UpVolume'].sum()) if 'UpVolume' in day_slice.columns else 0
    day_total_down = int(day_slice['DownVolume'].sum()) if 'DownVolume' in day_slice.columns else 0
    day_avg_trade_size = 0
    day_std_trade_size = 0

    per_bar_trade_sizes = []
    if has_ticks:
        for i in range(len(day_slice)):
            row = day_slice.iloc[i]
            t = int(row.get('TotalTicks', 0))
            v = int(row.get('Volume', 0))
            if t > 0:
                per_bar_trade_sizes.append(v / t)
        if per_bar_trade_sizes:
            day_avg_trade_size = statistics.mean(per_bar_trade_sizes)
            day_std_trade_size = statistics.stdev(per_bar_trade_sizes) if len(per_bar_trade_sizes) > 1 else day_avg_trade_size * 0.3

    day_baselines = {
        'day_avg_volume': round(day_avg_volume, 0),
        'day_total_volume': day_total_volume,
        'day_avg_trade_size': round(day_avg_trade_size, 1),
        'day_std_trade_size': round(day_std_trade_size, 1),
    }

    print(f"\n  Day baselines:")
    print(f"    Total volume: {day_total_volume:,}")
    print(f"    Avg vol/bar: {day_avg_volume:,.0f}")
    print(f"    Avg trade size: {day_avg_trade_size:,.1f}")
    print(f"    UpVol: {day_total_up:,} | DownVol: {day_total_down:,}")

    # --- Per-bar analysis at MA720 ---
    print(f"\n[3] Reversal absorption analysis at MA720 (±${PROXIMITY_DOLLARS})...")

    bar_analysis = []
    for i in range(len(day_slice)):
        row = day_slice.iloc[i]
        ma720 = row.get(sma_col)
        if pd.isna(ma720):
            continue
        ma720 = float(ma720)

        prices = {
            'Open': float(row['Open']), 'High': float(row['High']),
            'Low': float(row['Low']), 'Close': float(row['Close']),
        }
        min_dist = min(abs(p - ma720) for p in prices.values())
        spans_ma = prices['Low'] <= ma720 <= prices['High']
        near_ma = min_dist <= PROXIMITY_DOLLARS

        if not near_ma and not spans_ma:
            continue

        volume = int(row['Volume'])
        ticks = int(row.get('TotalTicks', 0))
        up_vol = int(row.get('UpVolume', 0))
        down_vol = int(row.get('DownVolume', 0))
        up_ticks = int(row.get('UpTicks', 0))
        down_ticks = int(row.get('DownTicks', 0))
        avg_trade = volume / max(1, ticks) if ticks > 0 else 0

        vol_ratio = volume / max(1, day_avg_volume)
        trade_size_ratio = avg_trade / max(0.01, day_avg_trade_size) if day_avg_trade_size > 0 else 0
        sigma = (avg_trade - day_avg_trade_size) / max(0.01, day_std_trade_size) if has_ticks and day_std_trade_size > 0 else 0
        net_delta = up_vol - down_vol
        delta_pct = net_delta / max(1, volume) * 100

        entry = {
            'time': day_slice.index[i].isoformat(),
            'time_et': day_slice.index[i].strftime('%H:%M'),
            'open': prices['Open'], 'high': prices['High'],
            'low': prices['Low'], 'close': prices['Close'],
            'ma720': round(ma720, 2),
            'min_distance': round(min_dist, 4),
            'spans_ma': spans_ma,
            'volume': volume,
            'vol_ratio': round(vol_ratio, 2),
            'avg_trade_size': round(avg_trade, 1),
            'trade_size_ratio': round(trade_size_ratio, 2),
            'trade_size_sigma': round(sigma, 2),
            'up_volume': up_vol, 'down_volume': down_vol,
            'net_delta': net_delta,
            'delta_pct': round(delta_pct, 1),
            'up_ticks': up_ticks, 'down_ticks': down_ticks,
            'ticks_total': ticks,
        }

        # Score this bar
        scores = score_bar(entry, day_baselines)
        entry['scores'] = scores

        bar_analysis.append(entry)

    # Print results
    print(f"\n  Bars at/near MA720: {len(bar_analysis)}")
    print(f"\n  {'Time':<7} {'Vol':>8} {'VRatio':>6} {'Delta%':>7} {'Absorp':>7} "
          f"{'Reject':>7} {'VolConc':>7} {'TrdSz':>6} {'TOTAL':>7}")
    print(f"  {'-'*7} {'-'*8} {'-'*6} {'-'*7} {'-'*7} {'-'*7} {'-'*7} {'-'*6} {'-'*7}")

    for b in bar_analysis:
        s = b['scores']
        flags = []
        if s['absorption']['absorbed']:
            flags.append('ABSORBED')
        if s['rejection_wick']['wick_below'] and s['rejection_wick']['closed_above']:
            flags.append('WICK REJECT')
        if s['volume_concentration']['pct_of_day'] > 5:
            flags.append(f"{s['volume_concentration']['pct_of_day']:.1f}% DAY VOL")
        flag_str = ' | '.join(flags)

        print(f"  {b['time_et']:<7} {b['volume']:>8,} {b['vol_ratio']:>5.1f}x "
              f"{b['delta_pct']:>+6.1f}% "
              f"{s['absorption']['score']:>7.3f} {s['rejection_wick']['score']:>7.3f} "
              f"{s['volume_concentration']['score']:>7.3f} {s['trade_size']['score']:>6.3f} "
              f"{s['_composite']:>7.3f}  {flag_str}")

    # Level summary
    if bar_analysis:
        total_vol = sum(b['volume'] for b in bar_analysis)
        total_up = sum(b['up_volume'] for b in bar_analysis)
        total_down = sum(b['down_volume'] for b in bar_analysis)
        best_bar = max(bar_analysis, key=lambda b: b['scores']['_composite'])
        avg_composite = statistics.mean([b['scores']['_composite'] for b in bar_analysis])

        print(f"\n  === REVERSAL ABSORPTION VERDICT ===")
        print(f"  Level: MA720 ${bar_analysis[0]['ma720']}")
        print(f"  Volume at level: {total_vol:,} ({total_vol/max(1,day_total_volume)*100:.1f}% of day)")
        print(f"  Buy vol: {total_up:,} | Sell vol: {total_down:,} | Net: {total_up-total_down:+,}")
        print(f"  Best bar: {best_bar['time_et']} (composite: {best_bar['scores']['_composite']:.3f})")
        print(f"  Avg composite: {avg_composite:.3f}")

        # Did absorption happen?
        absorbed_bars = [b for b in bar_analysis if b['scores']['absorption']['absorbed']]
        wick_bars = [b for b in bar_analysis if b['scores']['rejection_wick']['score'] > 0]
        high_vol_bars = [b for b in bar_analysis if b['vol_ratio'] >= 1.5]

        print(f"\n  Absorption detected:     {len(absorbed_bars)} bars")
        print(f"  Rejection wicks:         {len(wick_bars)} bars")
        print(f"  High volume (>=1.5x):    {len(high_vol_bars)} bars")

        if absorbed_bars and wick_bars:
            print(f"\n  ** INSTITUTIONAL REVERSAL SIGNAL: STRONG **")
            print(f"     Sellers were absorbed at MA720 with rejection wicks.")
            print(f"     Consistent with passive institutional bid at the 180-outfit level.")
        elif absorbed_bars:
            print(f"\n  ** INSTITUTIONAL REVERSAL SIGNAL: MODERATE **")
            print(f"     Absorption detected but no clean rejection wick.")
        elif wick_bars:
            print(f"\n  ** INSTITUTIONAL REVERSAL SIGNAL: MODERATE **")
            print(f"     Rejection wicks present but delta not strongly absorbed.")
        else:
            print(f"\n  ** INSTITUTIONAL REVERSAL SIGNAL: WEAK **")
            print(f"     No clear absorption or rejection at this level.")

    # --- Export JSON ---
    print(f"\n[4] Exporting...")

    candles = []
    for ts_idx, row in df_day.iterrows():
        candles.append({
            'time': ts_idx.isoformat(),
            'open': round(float(row['Open']), 2),
            'high': round(float(row['High']), 2),
            'low': round(float(row['Low']), 2),
            'close': round(float(row['Close']), 2),
            'volume': int(row['Volume']),
        })

    top_periods = SMA_OUTFITS['180']["smas"]
    sma_lines = {}
    for sma_p in top_periods:
        col = f"SMA_{sma_p}"
        if col in df_through.columns:
            vals = []
            for ts_idx in df_day.index:
                if ts_idx in df_through.index:
                    v = df_through.loc[ts_idx, col]
                    if not pd.isna(v):
                        vals.append({'time': ts_idx.isoformat(), 'value': round(float(v), 2)})
            if vals:
                sma_lines[str(sma_p)] = vals

    interactions = []
    window = df_through.iloc[-scan_bars:]
    for outfit_name, hits in ranked:
        for sma_p in SMA_OUTFITS[outfit_name]["smas"]:
            col = f"SMA_{sma_p}"
            if col not in df_through.columns:
                continue
            for i in range(len(window)):
                row = window.iloc[i]
                if pd.isna(row.get(col)):
                    continue
                sma_at_bar = round(float(row[col]), 2)
                for field in ['Open', 'High', 'Low', 'Close']:
                    val = round(float(row[field]), 2)
                    if val == sma_at_bar:
                        interactions.append({
                            'time': window.index[i].isoformat(),
                            'price': val,
                            'sma_period': sma_p,
                            'ohlc_field': field,
                            'outfit': outfit_name,
                        })

    rankings = [{'outfit': name, 'hits': hits, 'periods': SMA_OUTFITS[name]["smas"]}
                for name, hits in ranked]

    # Serialize bar scores for chart
    for b in bar_analysis:
        # Make scores JSON-safe (already are, just ensure)
        pass

    export = {
        'symbol': SYMBOL,
        'date': TARGET_DATE,
        'interval': f'{INTERVAL}M',
        'timezone': 'US/Eastern',
        'candles': candles,
        'sma_lines': sma_lines,
        'top_outfit': '180',
        'interactions': interactions,
        'rankings': rankings,
        'ma720_analysis': bar_analysis,
        'ma720_baselines': day_baselines,
    }

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backtest_data.json')
    with open(out_path, 'w') as f:
        json.dump(export, f, indent=2)
    print(f"  Saved to {out_path}")

    print(f"\n{'='*70}")
    print(f"BACKTEST COMPLETE")
    print(f"{'='*70}")


if __name__ == '__main__':
    main()
