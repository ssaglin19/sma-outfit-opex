"""
Final verification: SPXU scan with USEQ24Hour session (now default in ts_client).
Should detect 180/MA720/30M PBA from March 2.
"""
from ts_client import TradeStationClient
import pandas as pd
import numpy as np

ts = TradeStationClient()

PENNY = 0.01
SMA_OUTFITS = {
    "180": {"smas": [30, 60, 90, 180, 360, 720]},
}
ALL_SMA_PERIODS = [30, 60, 90, 180, 360, 720]

print("=== SPXU — 180 outfit only — 30M — USEQ24Hour ===\n")

df = ts.get_bars('SPXU', 30, 'Minute', 5000)
print(f"Bars: {len(df)} | Range: {df.index[0].date()} to {df.index[-1].date()}")

for p in ALL_SMA_PERIODS:
    df[f'SMA_{p}'] = df['Close'].rolling(window=p).mean().round(2)

# Scan last 2 weeks (~264 bars at 22/day with buffer)
scan_start = max(720 + 10, len(df) - 264)
print(f"Scan window: bars [{scan_start}:{len(df)}] = {len(df) - scan_start} bars\n")

for p in ALL_SMA_PERIODS:
    col = f"SMA_{p}"
    found = False
    for i in range(scan_start, len(df)):
        sma = df[col].iloc[i]
        if pd.isna(sma):
            continue
        sma_r = round(float(sma), 2)
        o = round(float(df['Open'].iloc[i]), 2)
        h = round(float(df['High'].iloc[i]), 2)
        l = round(float(df['Low'].iloc[i]), 2)
        c = round(float(df['Close'].iloc[i]), 2)

        for label, val in [("Open", o), ("High", h), ("Low", l), ("Close", c)]:
            if round(abs(val - sma_r), 2) == 0.0:
                # Check PBA conditions
                if c < sma_r:
                    direction = "ASO candidate (close < SMA)"
                else:
                    direction = "PBA candidate (close >= SMA)"

                # Check drawdown
                lb = min(40, i)
                recent_high = float(df['High'].iloc[max(0,i-lb):i].max())
                dd = (recent_high - sma_r) / recent_high if recent_high > 0 else 0

                # Check pre-close
                pre = df['Close'].iloc[max(0,i-10):max(0,i-2)]
                avg_pre = float(pre.mean()) if len(pre) >= 3 else 0

                # Check if still active (for PBA)
                hard_stop = round(sma_r - PENNY, 2)
                still_active = True
                breach = "N/A"
                for j in range(i+1, len(df)):
                    if round(float(df['Close'].iloc[j]), 2) < hard_stop:
                        still_active = False
                        breach = str(df.index[j])
                        break

                status = "ACTIVE" if still_active else f"STOPPED {breach}"
                print(f"  SMA{p} | {df.index[i]} | {label}={val:.2f} = SMA={sma_r:.2f} | {direction}")
                print(f"         DD={dd*100:.1f}% | AvgPre={avg_pre:.2f} vs SMA={sma_r:.2f} | Stop={hard_stop} | {status}")
                found = True
    if not found:
        # Show how close it got
        min_diff = 999
        for i in range(scan_start, len(df)):
            sma = df[col].iloc[i]
            if pd.isna(sma):
                continue
            sma_r = round(float(sma), 2)
            for val in [df['Open'].iloc[i], df['High'].iloc[i], df['Low'].iloc[i], df['Close'].iloc[i]]:
                diff = round(abs(round(float(val), 2) - sma_r), 2)
                if diff < min_diff:
                    min_diff = diff
        print(f"  SMA{p}: no exact match (closest approach: ${min_diff:.2f})")
