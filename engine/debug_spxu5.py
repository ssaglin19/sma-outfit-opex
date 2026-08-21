"""
Confirm: With USEQ24Hour, does SPXU Low=$48.78 match SMA720 at exact penny on March 2?
"""
from ts_client import TradeStationClient
import requests
import pandas as pd

ts = TradeStationClient()

print("=== SPXU 30M with USEQ24Hour session ===\n")

url = "https://api.tradestation.com/v3/marketdata/barcharts/SPXU"
params = {'interval': 30, 'unit': 'Minute', 'barsback': 5000, 'sessiontemplate': 'USEQ24Hour'}

resp = requests.get(url, headers=ts._get_headers(), params=params)
bars = resp.json().get('Bars', [])
print(f"Bars fetched: {len(bars)}")

df = pd.DataFrame([{
    'Open': float(b['Open']), 'High': float(b['High']),
    'Low': float(b['Low']), 'Close': float(b['Close']),
    'Timestamp': b['TimeStamp']
} for b in bars])
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.set_index('Timestamp', inplace=True)
df.sort_index(inplace=True)

# Compute SMA720 WITHOUT rounding during computation (round only for display)
df['SMA_720_raw'] = df['Close'].rolling(window=720).mean()
df['SMA_720'] = df['SMA_720_raw'].round(2)

print(f"Date range: {df.index[0]} to {df.index[-1]}")
print(f"Bars/day sample (latest day): {len(df[df.index.date == df.index[-1].date()])}")

# Show March 2 bars with exact SMA720 values
print(f"\n=== March 2 bars — exact SMA720 values ===")
march2 = df[df.index.date == pd.Timestamp('2026-03-02').date()]
for idx, row in march2.iterrows():
    sma_raw = row['SMA_720_raw']
    if pd.isna(sma_raw):
        continue
    sma_rounded = round(sma_raw, 2)
    o = round(float(row['Open']), 2)
    h = round(float(row['High']), 2)
    l = round(float(row['Low']), 2)
    c = round(float(row['Close']), 2)

    # Check all OHLC
    for label, val in [("O", o), ("H", h), ("L", l), ("C", c)]:
        diff = round(abs(val - sma_rounded), 2)
        if diff <= 0.02:
            marker = "EXACT PENNY MATCH!" if diff == 0.0 else f"off by ${diff:.2f}"
            print(f"  {idx} | {label}={val:.2f} vs SMA720={sma_rounded:.2f} (raw={sma_raw:.6f}) | {marker}")

# Also check a wider window
print(f"\n=== All bars where OHLC is within $0.05 of SMA720 (Feb 28 - Mar 5) ===")
window = df[(df.index >= '2026-02-28') & (df.index <= '2026-03-05')]
for idx, row in window.iterrows():
    sma_raw = row['SMA_720_raw']
    if pd.isna(sma_raw):
        continue
    sma_rounded = round(sma_raw, 2)
    o = round(float(row['Open']), 2)
    h = round(float(row['High']), 2)
    l = round(float(row['Low']), 2)
    c = round(float(row['Close']), 2)
    for label, val in [("O", o), ("H", h), ("L", l), ("C", c)]:
        diff = round(abs(val - sma_rounded), 2)
        if diff == 0.0:
            print(f"  >>> {idx} | {label}={val:.2f} = SMA720={sma_rounded:.2f} (raw={sma_raw:.6f}) | EXACT MATCH")
        elif diff <= 0.05:
            print(f"      {idx} | {label}={val:.2f} ~ SMA720={sma_rounded:.2f} (raw={sma_raw:.6f}) | ${diff:.2f} off")
