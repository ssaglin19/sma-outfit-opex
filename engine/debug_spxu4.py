"""
Debug: Does session template change SMA720?
TradeStation API supports SessionTemplate parameter for extended hours.
"""
from ts_client import TradeStationClient
import requests
import pandas as pd

ts = TradeStationClient()

print("=== Testing different session templates for SPXU 30M ===\n")

# Try different session templates
templates = [
    None,                    # default (no param)
    'Default',
    'USEQPre',               # pre-market
    'USEQPost',              # post-market
    'USEQPreAndPost',        # both
    'USEQ24Hour',            # 24 hour
]

for tmpl in templates:
    url = "https://api.tradestation.com/v3/marketdata/barcharts/SPXU"
    params = {'interval': 30, 'unit': 'Minute', 'barsback': 2000}
    if tmpl:
        params['sessiontemplate'] = tmpl

    resp = requests.get(url, headers=ts._get_headers(), params=params)
    if resp.status_code != 200:
        print(f"  Template '{tmpl}': FAIL {resp.status_code} — {resp.text[:100]}")
        continue

    bars = resp.json().get('Bars', [])
    if not bars:
        print(f"  Template '{tmpl}': OK but 0 bars")
        continue

    df = pd.DataFrame([{
        'Open': float(b['Open']), 'High': float(b['High']),
        'Low': float(b['Low']), 'Close': float(b['Close']),
        'Timestamp': b['TimeStamp']
    } for b in bars])
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df.set_index('Timestamp', inplace=True)
    df.sort_index(inplace=True)

    if len(df) >= 720:
        df['SMA_720'] = df['Close'].rolling(window=720).mean().round(2)
        latest_sma = df['SMA_720'].iloc[-1]

        # Find SMA720 around March 2, 20:00 UTC
        march2_bars = df[(df.index >= '2026-03-02 19:30') & (df.index <= '2026-03-02 20:30')]
        m2_sma = "N/A"
        if not march2_bars.empty:
            m2_sma_vals = march2_bars.get('SMA_720')
            if m2_sma_vals is not None and not m2_sma_vals.isna().all():
                m2_sma = f"{m2_sma_vals.iloc[0]:.2f}"

        # Check first and last bar times to understand session hours
        first_time = df.index[0]
        last_time = df.index[-1]
        # Count bars per day for a sample day
        sample_day = df[df.index.date == df.index[-1].date()]

        print(f"  Template '{tmpl}': {len(df)} bars | SMA720 latest: {latest_sma} | SMA720 @Mar2: {m2_sma} | bars/day sample: {len(sample_day)} | first bar: {first_time}")
    else:
        print(f"  Template '{tmpl}': {len(df)} bars (need 720 for SMA)")
