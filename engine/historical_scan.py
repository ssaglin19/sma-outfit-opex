"""
Historical SMA Outfit Scanner v4 — 2-Week Lookback
====================================================
Scans 2 weeks of bars per ticker/timeframe to find ALL triggers.
For PBA: tracks whether program is still active (hard stop not breached).
Uses TradeStation API. Detection logic matches engine.

OPTIMIZATION: Pre-computes all SMA columns, then vectorized scan finds
bars with exact penny matches FIRST, then runs full detection logic
only on those candidate bars.

Index tickers (SPX, IXIC, DJI): single system timeframe
Non-index tickers (ETFs): all 11 outfit timeframes (1m thru 4h)
"""

import pandas as pd
import numpy as np
from datetime import datetime
from ts_client import TradeStationClient, yf_to_ts_symbol
import warnings
warnings.filterwarnings('ignore')

PENNY = 0.01
LOOKBACK_DAYS = 14  # 2 weeks

# === CONFIG (mirrors engine exactly) ===

SMA_OUTFITS = {
    "S&P 500 System": {"smas": [10, 50, 200], "is_system": True, "positive_rule": {"short": 10, "long": 50}, "vol_shift_level": 50, "key_level": 200},
    "NASDAQ System": {"smas": [20, 100, 250], "is_system": True, "positive_rule": {"short": 20, "long": 100}, "vol_shift_level": 100, "key_level": 250},
    "Dow Jones System": {"smas": [30, 60, 90, 300, 600, 900], "is_system": True, "positive_rule": {"short": 90, "long": 300}, "vol_shift_level": 300, "key_level": 900},
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

TICKER_GROUPS = {
    "S&P 500": ["^GSPC", "SPY", "UPRO", "SPXU", "SPXL", "SSO", "SDS", "SPXS", "SH"],
    "NASDAQ": ["^IXIC", "QQQ", "TQQQ", "SQQQ", "QLD", "QID", "PSQ"],
    "Dow Jones": ["^DJI", "DIA", "UDOW", "SDOW", "DDM", "DXD", "DOG"],
    "Russell 2000": ["IWM", "UWM", "TNA", "RWM"],
    "VIX": ["^VIX", "VXX", "SVIX", "UVXY", "SVXY"],
}

TICKERS = [t for group in TICKER_GROUPS.values() for t in group]
TICKER_DISPLAY = {"^GSPC": "SPX", "^IXIC": "IXIC", "^DJI": "DJI", "^VIX": "VIX"}
TICKER_TO_GROUP = {}
for _grp, _tickers in TICKER_GROUPS.items():
    for _t in _tickers:
        TICKER_TO_GROUP[_t] = _grp
TICKER_SYSTEM_MAP = {}
for _t in TICKER_GROUPS["S&P 500"]:
    TICKER_SYSTEM_MAP[_t] = "S&P 500 System"
for _t in TICKER_GROUPS["NASDAQ"]:
    TICKER_SYSTEM_MAP[_t] = "NASDAQ System"
for _t in TICKER_GROUPS["Dow Jones"]:
    TICKER_SYSTEM_MAP[_t] = "Dow Jones System"
SYSTEM_PRIMARY_TICKERS = {"S&P 500 System": "^GSPC", "NASDAQ System": "^IXIC", "Dow Jones System": "^DJI"}

# Timeframes
SYSTEM_TIMEFRAMES = {"^GSPC": 30, "^IXIC": 30, "^DJI": 15}
OUTFIT_TIMEFRAMES = [1, 2, 3, 5, 10, 15, 20, 30, 60, 120, 240]

# Collect all unique SMA periods across all outfits
ALL_SMA_PERIODS = sorted(set(p for outfit in SMA_OUTFITS.values() for p in outfit["smas"]))
MAX_SMA = max(ALL_SMA_PERIODS)

# Reverse map: SMA period -> list of outfit names that use it
SMA_TO_OUTFITS = {}
for outfit_name, outfit in SMA_OUTFITS.items():
    for p in outfit["smas"]:
        if p not in SMA_TO_OUTFITS:
            SMA_TO_OUTFITS[p] = []
        SMA_TO_OUTFITS[p].append(outfit_name)


def compute_lookback_bars(interval_minutes):
    """How many bars = 2 weeks with USEQ24Hour session (~22 bars/day at 30M)."""
    # 24-hour session: ~22 bars/day at 30M = 660 min of bars per day
    minutes_per_session_day = 660
    trading_days = LOOKBACK_DAYS / 7 * 5 + 2  # weekdays + buffer for boundary
    total_minutes = trading_days * minutes_per_session_day
    return int(total_minutes / interval_minutes)


def compute_all_smas(df):
    for p in ALL_SMA_PERIODS:
        col = f"SMA_{p}"
        if len(df) >= p:
            df[col] = df['Close'].rolling(window=p).mean().round(2)


def get_sma_at(df, period, idx):
    col = f"SMA_{period}"
    if col in df.columns and 0 <= idx < len(df):
        val = df[col].iloc[idx]
        if not pd.isna(val):
            return float(val)
    return None


def evaluate_system_state(df, system_config, high_vol):
    rule = system_config.get("positive_rule")
    if not rule:
        return None
    short_p = rule["short"]
    long_p = rule["long"]
    short_val = get_sma_at(df, short_p, -1)
    long_val = get_sma_at(df, long_p, -1)
    if short_val is None or long_val is None:
        return None
    price = round(float(df['Close'].iloc[-1]), 2)
    if high_vol:
        vol_level = system_config.get("vol_shift_level", long_p)
        vol_sma = get_sma_at(df, vol_level, -1)
        if vol_sma is None:
            vol_sma = long_val
        state = "POSITIVE" if price > vol_sma else "NEGATIVE"
        detail = f"Close {price:.2f} {'>' if state == 'POSITIVE' else '<'} SMA{vol_level} {vol_sma:.2f} (vol regime)"
    else:
        state = "POSITIVE" if short_val > long_val else "NEGATIVE"
        detail = f"SMA{short_p} {short_val:.2f} {'>' if state == 'POSITIVE' else '<'} SMA{long_p} {long_val:.2f}"
    return {"state": state, "detail": detail}


# === VECTORIZED PENNY MATCH FINDER ===

def find_penny_matches(df, scan_start):
    """
    For each bar in scan window, find which SMA periods have an exact penny match
    against any of OHLC. Returns dict: bar_idx -> set of sma_periods with matches.

    This is the KEY optimization: instead of looping bar x outfit x sma,
    we vectorize the match check using numpy.
    """
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

        # Check each OHLC field against SMA — vectorized
        for price_arr in [o, h, l, c]:
            # Round both to 2 decimals then compare
            price_r = np.round(price_arr, 2)
            sma_r = np.round(sma, 2)
            diff = np.abs(price_r - sma_r)
            diff_r = np.round(diff, 2)

            # Find indices where diff == 0.0 within scan window
            hit_mask = (diff_r == 0.0)
            hit_mask[:scan_start] = False  # ignore bars before scan window
            # Also mask NaN SMAs
            nan_mask = np.isnan(sma)
            hit_mask[nan_mask] = False

            hit_indices = np.where(hit_mask)[0]
            for idx in hit_indices:
                if idx not in matches:
                    matches[idx] = set()
                matches[idx].add(p)

    return matches


# === DETECTION FUNCTIONS — bar-index versions ===

def detect_pba_at_bar(df, sma_period, bar_idx):
    """PBA at a specific bar index."""
    col = f"SMA_{sma_period}"
    if bar_idx < max(20, sma_period + 5):
        return None

    sma_rounded = float(df[col].iloc[bar_idx])
    o = round(float(df['Open'].iloc[bar_idx]), 2)
    h = round(float(df['High'].iloc[bar_idx]), 2)
    l = round(float(df['Low'].iloc[bar_idx]), 2)
    c = round(float(df['Close'].iloc[bar_idx]), 2)

    # Identify which OHLC fields match
    ohlc_touches = []
    for label, val in [("Open", o), ("High", h), ("Low", l), ("Close", c)]:
        if round(abs(val - sma_rounded), 2) == 0.0:
            ohlc_touches.append((label, val))
    if not ohlc_touches:
        return None

    # Close >= SMA (support held)
    if c < sma_rounded:
        return None

    # Pre-drawdown: avg prior closes ABOVE SMA
    pre_start = max(0, bar_idx - 10)
    pre_end = max(0, bar_idx - 2)
    if pre_end <= pre_start:
        return None
    pre_closes = df['Close'].iloc[pre_start:pre_end]
    if len(pre_closes) < 3:
        return None
    if float(pre_closes.mean()) <= sma_rounded:
        return None

    # Drawdown %
    lookback = min(40, bar_idx)
    s_idx = max(0, bar_idx - lookback)
    recent_high = float(df['High'].iloc[s_idx:bar_idx].max())
    dd_pct = (recent_high - sma_rounded) / recent_high if recent_high > 0 else 0
    if dd_pct < 0.005:
        return None

    touch_str = ", ".join(f"{t[0]}={t[1]:.2f}" for t in ohlc_touches)
    hard_stop = round(sma_rounded - PENNY, 2)

    return {
        "type": "precision_buy_algorithm",
        "sma_period": sma_period,
        "sma_value": sma_rounded,
        "ohlc_touches": touch_str,
        "close": c,
        "bar_time": str(df.index[bar_idx]),
        "bar_idx": bar_idx,
        "drawdown_pct": round(dd_pct * 100, 2),
        "hard_stop": hard_stop,
    }


def detect_aso_at_bar(df, sma_period, bar_idx):
    """ASO at a specific bar index."""
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

    # Close <= SMA (resistance)
    if c > sma_rounded:
        return None

    # Pre-period: avg prior closes BELOW SMA (approaching from below)
    pre_start = max(0, bar_idx - 10)
    pre_end = max(0, bar_idx - 2)
    if pre_end <= pre_start:
        return None
    pre_closes = df['Close'].iloc[pre_start:pre_end]
    if len(pre_closes) < 3:
        return None
    if float(pre_closes.mean()) >= sma_rounded:
        return None

    touch_str = ", ".join(f"{t[0]}={t[1]:.2f}" for t in ohlc_touches)

    return {
        "type": "automated_short_order",
        "sma_period": sma_period,
        "sma_value": sma_rounded,
        "ohlc_touches": touch_str,
        "close": c,
        "bar_time": str(df.index[bar_idx]),
        "bar_idx": bar_idx,
    }


def check_pba_still_active(df, trigger_bar_idx, hard_stop):
    """After PBA triggers, check if any subsequent bar closed below hard stop."""
    for i in range(trigger_bar_idx + 1, len(df)):
        close_val = round(float(df['Close'].iloc[i]), 2)
        if close_val < hard_stop:
            return False, str(df.index[i])
    return True, None


# === MAIN SCAN ===

def main():
    ts = TradeStationClient()

    print("=" * 70)
    print("  SMA OUTFIT SCANNER v4 — 2-Week Historical Lookback")
    print(f"  {len(TICKERS)} tickers × {len(SMA_OUTFITS)} outfits × {len(OUTFIT_TIMEFRAMES)} timeframes")
    print(f"  Lookback: {LOOKBACK_DAYS} days | {len(ALL_SMA_PERIODS)} unique SMA periods")
    print(f"  Timeframes: {', '.join(str(t)+'m' if t < 60 else str(t//60)+'h' for t in OUTFIT_TIMEFRAMES)}")
    print(f"  Scan date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 70)

    # VIX
    high_vol = False
    try:
        vix_df = ts.get_bars('$VIX.X', 1, 'Daily', 5)
        if not vix_df.empty:
            vix_level = float(vix_df['Close'].iloc[-1])
            high_vol = vix_level > 20
            print(f"\n  VIX: {vix_level:.2f} — {'HIGH VOLATILITY' if high_vol else 'NORMAL'}")
    except Exception as e:
        print(f"\n  VIX fetch failed: {e}")

    # System states
    system_states = {}
    print(f"\n  Evaluating system states (current)...")
    for sys_name, primary in SYSTEM_PRIMARY_TICKERS.items():
        try:
            ts_sym = yf_to_ts_symbol(primary)
            tf = SYSTEM_TIMEFRAMES[primary]
            df = ts.get_bars(ts_sym, tf, 'Minute', 1200)
            if df.empty:
                print(f"    {sys_name}: NO DATA for {ts_sym}")
                continue
            compute_all_smas(df)
            config = SMA_OUTFITS[sys_name]
            state = evaluate_system_state(df, config, high_vol)
            if state:
                system_states[sys_name] = state
                print(f"    {sys_name}: {state['state']} — {state['detail']}")
        except Exception as e:
            print(f"    {sys_name}: ERROR — {e}")

    any_negative = any(s.get("state") == "NEGATIVE" for s in system_states.values())
    print(f"\n  Any system negative: {any_negative}")

    # Scan all tickers
    all_detections = []

    for ticker in TICKERS:
        display = TICKER_DISPLAY.get(ticker, ticker)
        sys_name = TICKER_SYSTEM_MAP.get(ticker)
        ts_sym = yf_to_ts_symbol(ticker)

        if ticker in SYSTEM_TIMEFRAMES:
            timeframes = [SYSTEM_TIMEFRAMES[ticker]]
        else:
            timeframes = OUTFIT_TIMEFRAMES

        ticker_dets = []

        for tf in timeframes:
            tf_label = f"{tf}M" if tf < 60 else f"{tf // 60}H"

            lookback_bars = compute_lookback_bars(tf)
            total_bars_needed = lookback_bars + MAX_SMA + 50
            fetch_bars = min(total_bars_needed, 57600)

            try:
                df = ts.get_bars(ts_sym, tf, 'Minute', fetch_bars)
                if df.empty or len(df) < 50:
                    continue

                compute_all_smas(df)

                # Scan window
                scan_start = max(MAX_SMA + 10, len(df) - lookback_bars)
                if scan_start >= len(df):
                    continue

                # === VECTORIZED: find all penny matches in scan window ===
                penny_matches = find_penny_matches(df, scan_start)

                if not penny_matches:
                    continue

                # === Run detection logic ONLY on bars with penny matches ===
                # Track first PBA trigger per SMA to avoid duplicates
                pba_first = {}   # sma_period -> detection dict
                aso_latest = {}  # sma_period -> detection dict

                for bar_idx in sorted(penny_matches.keys()):
                    matched_smas = penny_matches[bar_idx]

                    for sma_p in matched_smas:
                        # --- PBA ---
                        if sma_p not in pba_first:
                            pba = detect_pba_at_bar(df, sma_p, bar_idx)
                            if pba:
                                still_active, breach_time = check_pba_still_active(
                                    df, bar_idx, pba["hard_stop"]
                                )
                                pba["still_active"] = still_active
                                pba["breach_time"] = breach_time
                                pba["ticker"] = display
                                pba["timeframe"] = tf_label
                                # Map to all outfits that use this SMA
                                for outfit_name in SMA_TO_OUTFITS.get(sma_p, []):
                                    det = dict(pba)
                                    det["outfit"] = outfit_name
                                    status = "ACTIVE" if still_active else f"STOPPED {breach_time}"
                                    det["description"] = (
                                        f"PBA — SMA{sma_p} at {pba['sma_value']:.2f} | "
                                        f"{pba['ohlc_touches']} | Close {pba['close']:.2f} | "
                                        f"Stop {pba['hard_stop']:.2f} | DD {pba['drawdown_pct']:.1f}% | "
                                        f"Triggered {pba['bar_time']} | {status} | TF: {tf_label}"
                                    )
                                    ticker_dets.append(det)
                                pba_first[sma_p] = pba

                        # --- ASO ---
                        if sys_name and any_negative:
                            aso = detect_aso_at_bar(df, sma_p, bar_idx)
                            if aso:
                                aso["ticker"] = display
                                aso["timeframe"] = tf_label
                                # Keep latest per SMA
                                aso_latest[sma_p] = aso

                # Add latest ASO detections
                for sma_p, aso in aso_latest.items():
                    for outfit_name in SMA_TO_OUTFITS.get(sma_p, []):
                        det = dict(aso)
                        det["outfit"] = outfit_name
                        det["description"] = (
                            f"ASO — SMA{sma_p} at {aso['sma_value']:.2f} | "
                            f"{aso['ohlc_touches']} | Close {aso['close']:.2f} | "
                            f"SYSTEM NEGATIVE | Latest {aso['bar_time']} | TF: {tf_label}"
                        )
                        ticker_dets.append(det)

            except Exception as e:
                print(f"  [ERR] {display} {tf_label}: {e}")

        all_detections.extend(ticker_dets)
        tf_str = ", ".join(f"{t}m" if t < 60 else f"{t//60}h" for t in timeframes)
        if ticker_dets:
            active_pbas = sum(1 for d in ticker_dets if d["type"] == "precision_buy_algorithm" and d.get("still_active"))
            print(f"  [OK] {display} — {len(ticker_dets)} detections ({active_pbas} active PBAs) [{tf_str}]")
        else:
            print(f"  [--] {display} [{tf_str}]")

    # === REPORT ===
    print("\n" + "=" * 70)
    print("  RESULTS: 2-WEEK HISTORICAL SCAN")
    print("=" * 70)

    if not all_detections:
        print("\n  NO DETECTIONS in 2-week lookback.")
        return

    active_pbas = [d for d in all_detections if d["type"] == "precision_buy_algorithm" and d.get("still_active")]
    stopped_pbas = [d for d in all_detections if d["type"] == "precision_buy_algorithm" and not d.get("still_active")]
    asos = [d for d in all_detections if d["type"] == "automated_short_order"]

    # === ACTIVE PBA PROGRAMS ===
    print(f"\n  {'='*60}")
    print(f"  ACTIVE PBA PROGRAMS ({len(active_pbas)})")
    print(f"  Triggered in last 2 weeks, hard stop NOT breached.")
    print(f"  {'='*60}")
    if active_pbas:
        by_ticker = {}
        for d in active_pbas:
            tk = d["ticker"]
            if tk not in by_ticker:
                by_ticker[tk] = []
            by_ticker[tk].append(d)
        for tk in sorted(by_ticker):
            print(f"\n  {tk}:")
            for d in sorted(by_ticker[tk], key=lambda x: x.get("bar_time", "")):
                print(f"    -> [{d['outfit']}] {d['description']}")
    else:
        print("\n  None.")

    # === STOPPED PBA PROGRAMS ===
    print(f"\n  {'='*60}")
    print(f"  STOPPED PBA PROGRAMS ({len(stopped_pbas)})")
    print(f"  Triggered but hard stop was subsequently breached.")
    print(f"  {'='*60}")
    if stopped_pbas:
        by_ticker = {}
        for d in stopped_pbas:
            tk = d["ticker"]
            if tk not in by_ticker:
                by_ticker[tk] = []
            by_ticker[tk].append(d)
        for tk in sorted(by_ticker):
            print(f"\n  {tk}:")
            for d in sorted(by_ticker[tk], key=lambda x: x.get("bar_time", "")):
                print(f"    -> [{d['outfit']}] {d['description']}")
    else:
        print("\n  None.")

    # === ASO DETECTIONS ===
    print(f"\n  {'='*60}")
    print(f"  ASO DETECTIONS ({len(asos)}) — most recent per SMA/ticker/TF")
    print(f"  {'='*60}")
    if asos:
        by_ticker = {}
        for d in asos:
            tk = d["ticker"]
            if tk not in by_ticker:
                by_ticker[tk] = []
            by_ticker[tk].append(d)
        for tk in sorted(by_ticker):
            print(f"\n  {tk}:")
            for d in sorted(by_ticker[tk], key=lambda x: x.get("bar_time", "")):
                print(f"    -> [{d['outfit']}] {d['description']}")
    else:
        print("\n  None.")

    # === SUMMARY ===
    print(f"\n  {'='*60}")
    print(f"  SUMMARY")
    print(f"  {'='*60}")
    print(f"  Active PBAs:  {len(active_pbas)}")
    print(f"  Stopped PBAs: {len(stopped_pbas)}")
    print(f"  ASOs:         {len(asos)}")
    print(f"  TOTAL:        {len(all_detections)}")

    outfits_hit = set(d["outfit"] for d in all_detections)
    print(f"\n  Outfits with detections: {len(outfits_hit)} of {len(SMA_OUTFITS)}")
    tickers_hit = set(d["ticker"] for d in all_detections)
    print(f"  Tickers with detections: {len(tickers_hit)} of {len(TICKERS)}")


if __name__ == "__main__":
    main()
