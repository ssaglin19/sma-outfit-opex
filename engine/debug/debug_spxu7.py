"""
Pinpoint: Compare SMA720 at March 2 20:00 between ts.get_bars() and direct API call.
"""
from ts_client import TradeStationClient
import requests
import pandas as pd

ts = TradeStationClient()

# Method 1: via ts.get_bars() (what the scanner uses)
print("=== Method 1: ts.get_bars() ===")
df1 = ts.get_bars('SPXU', 30, 'Minute', 5000)
df1['SMA_720'] = df1['Close'].rolling(window=720).mean()
m2_bars = df1[(df1.index >= '2026-03-02 19:30') & (df1.index <= '2026-03-02 20:30')]
print(f"Bars: {len(df1)} | Range: {df1.index[0]} to {df1.index[-1]}")
print(f"Bars/day (Mar 13): {len(df1[df1.index.date == df1.index[-1].date()])}")
for idx, row in m2_bars.iterrows():
    sma_raw = row['SMA_720']
    sma_r = round(sma_raw, 2) if not pd.isna(sma_raw) else None
    l = round(float(row['Low']), 2)
    print(f"  {idx} | Low={l} | SMA720 raw={sma_raw:.6f} rounded={sma_r} | diff={round(abs(l - sma_r), 2) if sma_r else 'N/A'}")

# Method 2: direct API call with explicit sessiontemplate (what debug_spxu5 used)
print("\n=== Method 2: direct requests.get() ===")
url = "https://api.tradestation.com/v3/marketdata/barcharts/SPXU"
params = {'interval': 30, 'unit': 'Minute', 'barsback': 5000, 'sessiontemplate': 'USEQ24Hour'}
resp = requests.get(url, headers=ts._get_headers(), params=params)
bars = resp.json().get('Bars', [])
df2 = pd.DataFrame([{
    'Open': float(b['Open']), 'High': float(b['High']),
    'Low': float(b['Low']), 'Close': float(b['Close']),
    'Timestamp': b['TimeStamp']
} for b in bars])
df2['Timestamp'] = pd.to_datetime(df2['Timestamp'])
df2.set_index('Timestamp', inplace=True)
df2.sort_index(inplace=True)
df2['SMA_720'] = df2['Close'].rolling(window=720).mean()
m2_bars2 = df2[(df2.index >= '2026-03-02 19:30') & (df2.index <= '2026-03-02 20:30')]
print(f"Bars: {len(df2)} | Range: {df2.index[0]} to {df2.index[-1]}")
print(f"Bars/day (Mar 13): {len(df2[df2.index.date == df2.index[-1].date()])}")
for idx, row in m2_bars2.iterrows():
    sma_raw = row['SMA_720']
    sma_r = round(sma_raw, 2) if not pd.isna(sma_raw) else None
    l = round(float(row['Low']), 2)
    print(f"  {idx} | Low={l} | SMA720 raw={sma_raw:.6f} rounded={sma_r} | diff={round(abs(l - sma_r), 2) if sma_r else 'N/A'}")

# Compare bar counts and first/last bars
print(f"\n=== Comparison ===")
print(f"Method 1 total bars: {len(df1)}, Method 2 total bars: {len(df2)}")
print(f"Method 1 first bar: {df1.index[0]}")
print(f"Method 2 first bar: {df2.index[0]}")
print(f"Method 1 last bar: {df1.index[-1]}")
print(f"Method 2 last bar: {df2.index[-1]}")

# Check if the bar data at March 2 20:00 is identical
if not m2_bars.empty and not m2_bars2.empty:
    b1 = m2_bars.iloc[0] if '2026-03-02 20:00' in str(m2_bars.index[0]) else None
    b2 = m2_bars2.iloc[0] if '2026-03-02 20:00' in str(m2_bars2.index[0]) else None
    if b1 is not None and b2 is not None:
        print(f"\nBar at Mar 2 20:00:")
        print(f"  M1: O={b1['Open']} H={b1['High']} L={b1['Low']} C={b1['Close']}")
        print(f"  M2: O={b2['Open']} H={b2['High']} L={b2['Low']} C={b2['Close']}")
