"""
Debug: Why does our SMA720 ($49.05) differ from the chart ($48.78)?
Check SMA720 values around March 2nd, and test with different barsback.
"""
from ts_client import TradeStationClient
import pandas as pd

ts = TradeStationClient()

print("=== SPXU 30M — SMA720 Investigation ===\n")

# Test 1: Fetch with different barsback amounts and compare SMA720
for barsback in [1200, 2000, 3000, 5000]:
    df = ts.get_bars('SPXU', 30, 'Minute', barsback)
    if df.empty:
        print(f"  barsback={barsback}: no data")
        continue
    if len(df) < 720:
        print(f"  barsback={barsback}: only {len(df)} bars, need 720 for SMA")
        continue
    df['SMA_720'] = df['Close'].rolling(window=720).mean().round(2)
    latest_sma = df['SMA_720'].iloc[-1]
    print(f"  barsback={barsback}: {len(df)} bars | date range: {df.index[0].date()} to {df.index[-1].date()} | SMA720 latest: {latest_sma}")

# Test 2: With 5000 bars, show SMA720 values around March 2-3
print(f"\n=== SMA720 values around March 1-5 ===")
df = ts.get_bars('SPXU', 30, 'Minute', 5000)
if not df.empty and len(df) >= 720:
    df['SMA_720'] = df['Close'].rolling(window=720).mean().round(2)

    # Filter to March 1-5
    march_bars = df[(df.index >= '2026-03-01') & (df.index <= '2026-03-06')]
    if not march_bars.empty:
        print(f"  Bars in Mar 1-5: {len(march_bars)}")
        for idx, row in march_bars.iterrows():
            sma = row.get('SMA_720')
            if pd.isna(sma):
                continue
            o = round(float(row['Open']), 2)
            h = round(float(row['High']), 2)
            l = round(float(row['Low']), 2)
            c = round(float(row['Close']), 2)
            sma = round(float(sma), 2)
            # Check for penny match
            diffs = {'O': round(abs(o - sma), 2), 'H': round(abs(h - sma), 2),
                     'L': round(abs(l - sma), 2), 'C': round(abs(c - sma), 2)}
            min_field = min(diffs, key=diffs.get)
            min_diff = diffs[min_field]
            marker = " <<<< EXACT MATCH" if min_diff == 0.0 else (" << NEAR" if min_diff <= 0.05 else "")
            print(f"  {idx} | O={o:.2f} H={h:.2f} L={l:.2f} C={c:.2f} | SMA720={sma:.2f} | closest={min_field} ${min_diff:.2f}{marker}")
    else:
        print("  No bars found in Mar 1-5 range")

    # Also check: what's SMA720 at the bar closest to $48.78?
    print(f"\n=== Bars where SMA720 was near $48.78 ===")
    valid = df.dropna(subset=['SMA_720'])
    near_target = valid[abs(valid['SMA_720'] - 48.78) <= 0.10]
    if not near_target.empty:
        print(f"  Found {len(near_target)} bars where SMA720 was within $0.10 of $48.78:")
        for idx, row in near_target.head(20).iterrows():
            sma = round(float(row['SMA_720']), 2)
            o = round(float(row['Open']), 2)
            h = round(float(row['High']), 2)
            l = round(float(row['Low']), 2)
            c = round(float(row['Close']), 2)
            diffs = {'O': round(abs(o - sma), 2), 'H': round(abs(h - sma), 2),
                     'L': round(abs(l - sma), 2), 'C': round(abs(c - sma), 2)}
            min_field = min(diffs, key=diffs.get)
            min_diff = diffs[min_field]
            marker = " <<<< EXACT" if min_diff == 0.0 else ""
            print(f"  {idx} | O={o:.2f} H={h:.2f} L={l:.2f} C={c:.2f} | SMA720={sma:.2f} | closest={min_field} ${min_diff:.2f}{marker}")
    else:
        print("  SMA720 never reached $48.78 in available data")
        # Show where SMA720 was in the data
        print(f"  SMA720 range: {valid['SMA_720'].min():.2f} to {valid['SMA_720'].max():.2f}")
