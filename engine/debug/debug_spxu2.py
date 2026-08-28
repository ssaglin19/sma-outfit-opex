"""
Isolated scan: SPXU only, all 11 timeframes, 2-week lookback.
"""
import pandas as pd
import numpy as np
from datetime import datetime
from ts_client import TradeStationClient, yf_to_ts_symbol
import warnings
warnings.filterwarnings('ignore')

PENNY = 0.01
LOOKBACK_DAYS = 14

SMA_OUTFITS = {
    "S&P 500 System": {"smas": [10, 50, 200], "is_system": True, "positive_rule": {"short": 10, "long": 50}, "vol_shift_level": 50, "key_level": 200},
    "NASDAQ System": {"smas": [20, 100, 250], "is_system": True},
    "Dow Jones System": {"smas": [30, 60, 90, 300, 600, 900], "is_system": True},
    "EVIL (666)": {"smas": [33, 66, 99, 333, 666, 999]},
    "ICKY WOODS (888)": {"smas": [11, 44, 88, 111, 444, 888]},
    "LUCKY (777)": {"smas": [22, 55, 77, 222, 555, 777]},
    "Waring's Problem": {"smas": [19, 37, 73, 143, 279, 548]},
    "Regression (432)": {"smas": [27, 54, 108, 216, 432, 864]},
    "180": {"smas": [30, 60, 90, 180, 360, 720]},
    "Time (365)": {"smas": [23, 46, 91, 183, 365, 730]},
    "Time (366)": {"smas": [23, 46, 92, 183, 366, 732]},
    "Time (144)": {"smas": [18, 36, 72, 144, 288, 576]},
    "President 45": {"smas": [29, 57, 114, 227, 455, 911]},
    "President 46": {"smas": [23, 46, 92, 184, 368, 736]},
    "President 47": {"smas": [24, 47, 94, 188, 376, 752]},
    "WTC (911)": {"smas": [28, 57, 114, 228, 456, 911]},
    "SVIX (211)": {"smas": [26, 52, 106, 211, 422, 844]},
    "Resource Missing (404)": {"smas": [25, 51, 101, 202, 404, 808]},
}

ALL_SMA_PERIODS = sorted(set(p for outfit in SMA_OUTFITS.values() for p in outfit["smas"]))
MAX_SMA = max(ALL_SMA_PERIODS)

SMA_TO_OUTFITS = {}
for outfit_name, outfit in SMA_OUTFITS.items():
    for p in outfit["smas"]:
        if p not in SMA_TO_OUTFITS:
            SMA_TO_OUTFITS[p] = []
        SMA_TO_OUTFITS[p].append(outfit_name)

OUTFIT_TIMEFRAMES = [1, 2, 3, 5, 10, 15, 20, 30, 60, 120, 240]


def compute_lookback_bars(interval_minutes):
    trading_minutes_per_day = 390
    total_minutes = LOOKBACK_DAYS / 7 * 5 * trading_minutes_per_day
    return int(total_minutes / interval_minutes)


def compute_all_smas(df):
    for p in ALL_SMA_PERIODS:
        col = f"SMA_{p}"
        if len(df) >= p:
            df[col] = df['Close'].rolling(window=p).mean().round(2)


def find_penny_matches(df, scan_start):
    matches = {}
    o = df['Open'].values
    h = df['High'].values
    l = df['Low'].values
    c = df['Close'].values
    for p in ALL_SMA_PERIODS:
        col = f"SMA_{p}"
        if col not in df.columns:
            continue
        sma = df[col].values
        for price_arr in [o, h, l, c]:
            price_r = np.round(price_arr, 2)
            sma_r = np.round(sma, 2)
            diff = np.abs(price_r - sma_r)
            diff_r = np.round(diff, 2)
            hit_mask = (diff_r == 0.0)
            hit_mask[:scan_start] = False
            nan_mask = np.isnan(sma)
            hit_mask[nan_mask] = False
            for idx in np.where(hit_mask)[0]:
                if idx not in matches:
                    matches[idx] = set()
                matches[idx].add(p)
    return matches


def detect_pba_at_bar(df, sma_period, bar_idx):
    col = f"SMA_{sma_period}"
    if bar_idx < max(20, sma_period + 5):
        return None
    sma_rounded = float(df[col].iloc[bar_idx])
    o = round(float(df['Open'].iloc[bar_idx]), 2)
    h = round(float(df['High'].iloc[bar_idx]), 2)
    l = round(float(df['Low'].iloc[bar_idx]), 2)
    c = round(float(df['Close'].iloc[bar_idx]), 2)
    ohlc_touches = []
    for label, val in [("Open", o), ("High", h), ("Low", l), ("Close", c)]:
        if round(abs(val - sma_rounded), 2) == 0.0:
            ohlc_touches.append((label, val))
    if not ohlc_touches:
        return None
    if c < sma_rounded:
        return None
    pre_start = max(0, bar_idx - 10)
    pre_end = max(0, bar_idx - 2)
    if pre_end <= pre_start:
        return None
    pre_closes = df['Close'].iloc[pre_start:pre_end]
    if len(pre_closes) < 3:
        return None
    if float(pre_closes.mean()) <= sma_rounded:
        return None
    lookback = min(40, bar_idx)
    s_idx = max(0, bar_idx - lookback)
    recent_high = float(df['High'].iloc[s_idx:bar_idx].max())
    dd_pct = (recent_high - sma_rounded) / recent_high if recent_high > 0 else 0
    if dd_pct < 0.005:
        return None
    touch_str = ", ".join(f"{t[0]}={t[1]:.2f}" for t in ohlc_touches)
    hard_stop = round(sma_rounded - PENNY, 2)
    return {
        "type": "PBA",
        "sma_period": sma_period,
        "sma_value": sma_rounded,
        "ohlc_touches": touch_str,
        "close": c,
        "bar_time": str(df.index[bar_idx]),
        "bar_idx": bar_idx,
        "drawdown_pct": round(dd_pct * 100, 2),
        "hard_stop": hard_stop,
    }


def check_pba_still_active(df, trigger_bar_idx, hard_stop):
    for i in range(trigger_bar_idx + 1, len(df)):
        close_val = round(float(df['Close'].iloc[i]), 2)
        if close_val < hard_stop:
            return False, str(df.index[i])
    return True, None


def main():
    ts = TradeStationClient()
    symbol = "SPXU"

    print(f"=== ISOLATED SCAN: {symbol} ONLY ===")
    print(f"Lookback: {LOOKBACK_DAYS} days | {len(ALL_SMA_PERIODS)} unique SMAs | {len(OUTFIT_TIMEFRAMES)} timeframes")
    print(f"Scan date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    all_dets = []

    for tf in OUTFIT_TIMEFRAMES:
        tf_label = f"{tf}M" if tf < 60 else f"{tf // 60}H"
        lookback_bars = compute_lookback_bars(tf)
        total_bars_needed = lookback_bars + MAX_SMA + 50
        fetch_bars = min(total_bars_needed, 57600)

        try:
            df = ts.get_bars(symbol, tf, 'Minute', fetch_bars)
            if df.empty or len(df) < 50:
                print(f"  {tf_label}: no data or insufficient bars ({len(df)})")
                continue

            compute_all_smas(df)

            scan_start = max(MAX_SMA + 10, len(df) - lookback_bars)
            if scan_start >= len(df):
                print(f"  {tf_label}: scan_start ({scan_start}) >= len ({len(df)}), skipping")
                continue

            penny_matches = find_penny_matches(df, scan_start)

            if not penny_matches:
                print(f"  {tf_label}: {len(df)} bars, scan window [{scan_start}:{len(df)}] = {len(df)-scan_start} bars, 0 penny matches")
                continue

            print(f"  {tf_label}: {len(df)} bars, scan window = {len(df)-scan_start} bars, {len(penny_matches)} bars with penny matches")

            pba_first = {}
            tf_dets = []

            for bar_idx in sorted(penny_matches.keys()):
                matched_smas = penny_matches[bar_idx]
                for sma_p in matched_smas:
                    if sma_p not in pba_first:
                        pba = detect_pba_at_bar(df, sma_p, bar_idx)
                        if pba:
                            still_active, breach_time = check_pba_still_active(df, bar_idx, pba["hard_stop"])
                            pba["still_active"] = still_active
                            pba["breach_time"] = breach_time
                            pba["timeframe"] = tf_label
                            for outfit_name in SMA_TO_OUTFITS.get(sma_p, []):
                                det = dict(pba)
                                det["outfit"] = outfit_name
                                status = "ACTIVE" if still_active else f"STOPPED {breach_time}"
                                det["desc"] = (
                                    f"[{outfit_name}] SMA{sma_p} at {pba['sma_value']:.2f} | "
                                    f"{pba['ohlc_touches']} | Close {pba['close']:.2f} | "
                                    f"Stop {pba['hard_stop']:.2f} | DD {pba['drawdown_pct']:.1f}% | "
                                    f"Triggered {pba['bar_time']} | {status}"
                                )
                                tf_dets.append(det)
                            pba_first[sma_p] = pba

            active = [d for d in tf_dets if d.get("still_active")]
            stopped = [d for d in tf_dets if not d.get("still_active")]
            print(f"    → {len(active)} active PBAs, {len(stopped)} stopped PBAs")
            all_dets.extend(tf_dets)

        except Exception as e:
            print(f"  {tf_label}: ERROR — {e}")

    # Report
    active_all = [d for d in all_dets if d.get("still_active")]
    stopped_all = [d for d in all_dets if not d.get("still_active")]

    print(f"\n{'='*70}")
    print(f"ACTIVE PBAs ({len(active_all)}):")
    print(f"{'='*70}")
    for d in sorted(active_all, key=lambda x: x.get("bar_time", "")):
        print(f"  {d['timeframe']:>4} | {d['desc']}")

    print(f"\n{'='*70}")
    print(f"STOPPED PBAs ({len(stopped_all)}):")
    print(f"{'='*70}")
    for d in sorted(stopped_all, key=lambda x: x.get("bar_time", "")):
        print(f"  {d['timeframe']:>4} | {d['desc']}")

    print(f"\nTOTAL: {len(active_all)} active, {len(stopped_all)} stopped")


if __name__ == "__main__":
    main()
