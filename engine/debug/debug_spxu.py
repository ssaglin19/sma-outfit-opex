"""
Debug: Why isn't SPXU 180/MA720/30M being detected?
Active program per @unfairmarket: SPXU PBA 180 outfit MA720 30M
"""
from ts_client import TradeStationClient, yf_to_ts_symbol
import pandas as pd
import numpy as np

PENNY = 0.01
ts = TradeStationClient()

symbol = "SPXU"
ts_sym = yf_to_ts_symbol(symbol)
interval = 30  # 30M
barsback = 1200

print(f"=== DEBUG: SPXU 180/MA720/30M ===")
print(f"Symbol: {symbol} -> {ts_sym}")
print(f"Timeframe: {interval}M, barsback={barsback}")
print()

# Fetch bars
df = ts.get_bars(ts_sym, interval, 'Minute', barsback)
print(f"Bars returned: {len(df)}")
if len(df) > 0:
    print(f"Date range: {df.index[0]} to {df.index[-1]}")
    print(f"Current bar OHLCV: O={df['Open'].iloc[-1]:.2f} H={df['High'].iloc[-1]:.2f} L={df['Low'].iloc[-1]:.2f} C={df['Close'].iloc[-1]:.2f} V={df['Volume'].iloc[-1]:.0f}")
    print(f"Prev bar OHLCV:    O={df['Open'].iloc[-2]:.2f} H={df['High'].iloc[-2]:.2f} L={df['Low'].iloc[-2]:.2f} C={df['Close'].iloc[-2]:.2f} V={df['Volume'].iloc[-2]:.0f}")
print()

# Compute SMA720
sma_period = 720
if len(df) >= sma_period:
    df[f'SMA_{sma_period}'] = df['Close'].rolling(window=sma_period).mean()
    sma_current = round(float(df[f'SMA_{sma_period}'].iloc[-1]), 2)
    sma_prev = round(float(df[f'SMA_{sma_period}'].iloc[-2]), 2)
    print(f"SMA{sma_period} current bar: {sma_current}")
    print(f"SMA{sma_period} prev bar:    {sma_prev}")
    print()

    # Check exact penny match on current bar
    print("--- CURRENT BAR vs SMA720 ---")
    bar = df.iloc[-1]
    for label in ['Open', 'High', 'Low', 'Close']:
        val = round(float(bar[label]), 2)
        diff = round(abs(val - sma_current), 2)
        match = "EXACT MATCH" if diff == 0.0 else f"off by ${diff:.2f}"
        print(f"  {label}={val:.2f}  SMA={sma_current:.2f}  diff=${diff:.2f}  {match}")

    # Check exact penny match on prev bar
    print("\n--- PREV BAR vs SMA720 ---")
    bar = df.iloc[-2]
    for label in ['Open', 'High', 'Low', 'Close']:
        val = round(float(bar[label]), 2)
        diff = round(abs(val - sma_prev), 2)
        match = "EXACT MATCH" if diff == 0.0 else f"off by ${diff:.2f}"
        print(f"  {label}={val:.2f}  SMA={sma_prev:.2f}  diff=${diff:.2f}  {match}")

    # Check ALL 180 outfit SMAs [30, 60, 90, 180, 360, 720]
    print("\n\n=== ALL 180 OUTFIT SMAs on 30M ===")
    for p in [30, 60, 90, 180, 360, 720]:
        if len(df) >= p:
            df[f'SMA_{p}'] = df['Close'].rolling(window=p).mean()
            sma_val = round(float(df[f'SMA_{p}'].iloc[-1]), 2)
            sma_prev_val = round(float(df[f'SMA_{p}'].iloc[-2]), 2)

            # Current bar
            bar = df.iloc[-1]
            min_diff_cur = 999
            best_cur = ""
            for label in ['Open', 'High', 'Low', 'Close']:
                val = round(float(bar[label]), 2)
                diff = round(abs(val - sma_val), 2)
                if diff < min_diff_cur:
                    min_diff_cur = diff
                    best_cur = f"{label}={val:.2f}"

            # Prev bar
            bar = df.iloc[-2]
            min_diff_prev = 999
            best_prev = ""
            for label in ['Open', 'High', 'Low', 'Close']:
                val = round(float(bar[label]), 2)
                diff = round(abs(val - sma_prev_val), 2)
                if diff < min_diff_prev:
                    min_diff_prev = diff
                    best_prev = f"{label}={val:.2f}"

            match_cur = "EXACT" if min_diff_cur == 0.0 else f"${min_diff_cur:.2f} off"
            match_prev = "EXACT" if min_diff_prev == 0.0 else f"${min_diff_prev:.2f} off"
            print(f"  SMA{p:>4} = {sma_val:.2f} (cur) | closest: {best_cur} [{match_cur}]")
            print(f"  SMA{p:>4} = {sma_prev_val:.2f} (prv) | closest: {best_prev} [{match_prev}]")
            print()
        else:
            print(f"  SMA{p}: NOT ENOUGH BARS ({len(df)} < {p})")
            print()

    # PBA drawdown check context
    print("\n=== PBA DRAWDOWN CHECK (SMA720, current bar) ===")
    sma_val = round(float(df[f'SMA_720'].iloc[-1]), 2)
    c = round(float(df['Close'].iloc[-1]), 2)
    print(f"Close {c:.2f} >= SMA {sma_val:.2f}? {c >= sma_val}")

    pre_start = max(0, len(df) - 1 - 10)
    pre_end = max(0, len(df) - 1 - 2)
    pre_closes = df['Close'].iloc[pre_start:pre_end]
    avg_pre = float(pre_closes.mean())
    print(f"Avg pre-close (8 bars before): {avg_pre:.2f} > SMA {sma_val:.2f}? {avg_pre > sma_val}")

    lookback = min(40, len(df) - 1)
    recent_high = float(df['High'].iloc[-lookback:].max())
    dd_pct = (recent_high - sma_val) / recent_high if recent_high > 0 else 0
    print(f"Recent high (40 bars): {recent_high:.2f}")
    print(f"Drawdown %: {dd_pct*100:.2f}% (need >= 0.5%)")

    # Scan recent bars for any near-miss on SMA720
    print("\n\n=== LAST 20 BARS: CLOSEST APPROACH TO SMA720 ===")
    for i in range(-20, 0):
        idx = len(df) + i
        if idx < 0:
            continue
        bar = df.iloc[idx]
        sma_at = df[f'SMA_720'].iloc[idx]
        if pd.isna(sma_at):
            continue
        sma_at = round(float(sma_at), 2)
        o, h, l, c = round(float(bar['Open']),2), round(float(bar['High']),2), round(float(bar['Low']),2), round(float(bar['Close']),2)
        diffs = {'O': round(abs(o - sma_at),2), 'H': round(abs(h - sma_at),2), 'L': round(abs(l - sma_at),2), 'C': round(abs(c - sma_at),2)}
        min_label = min(diffs, key=diffs.get)
        min_diff = diffs[min_label]
        marker = " <<<< EXACT" if min_diff == 0.0 else (" << NEAR" if min_diff <= 0.05 else "")
        ts = bar.name if hasattr(bar, 'name') else f"bar[{idx}]"
        print(f"  {ts} | O={o:.2f} H={h:.2f} L={l:.2f} C={c:.2f} | SMA720={sma_at:.2f} | closest={min_label} ${min_diff:.2f}{marker}")

else:
    print(f"NOT ENOUGH BARS for SMA{sma_period}: have {len(df)}, need {sma_period}")
    print("This is likely the problem — need more barsback")
    print()
    # Try with more bars
    print("Attempting with barsback=2000...")
    df2 = ts.get_bars(ts_sym, interval, 'Minute', 2000)
    print(f"Bars returned with 2000: {len(df2)}")
    if len(df2) >= sma_period:
        print(f"SUCCESS — {len(df2)} bars is enough for SMA{sma_period}")
    else:
        print(f"STILL NOT ENOUGH — {len(df2)} bars")
