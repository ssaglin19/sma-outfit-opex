"""Debug: What does detector.py see for IXIC + SMA 888 (closest to MA884)?"""
import pandas as pd
from influxdb_client import InfluxDBClient
from dotenv import load_dotenv
import os

load_dotenv()
client = InfluxDBClient(
    url=os.getenv("INFLUXDB_URL", "http://localhost:8086"),
    token=os.getenv("INFLUXDB_TOKEN"),
    org=os.getenv("INFLUXDB_ORG", "sma-alerts"),
)

# Check what timeframes we have for IXIC
query_api = client.query_api()
print("=== IXIC TIMEFRAMES IN market_data ===")
flux = '''
from(bucket: "market_data")
  |> range(start: -90d)
  |> filter(fn: (r) => r._measurement == "ohlcv")
  |> filter(fn: (r) => r.ticker == "IXIC")
  |> filter(fn: (r) => r._field == "close")
  |> group(columns: ["timeframe"])
  |> count()
  |> group()
'''
tables = query_api.query(flux)
for table in tables:
    for row in table.records:
        print(f"  {row.values.get('timeframe')}: {row.get_value()} bars")

# Now pull bars for common timeframes and check SMA 888
print("\n=== IXIC LATEST BARS + SMA CHECK ===")
for tf in ['5m', '10m', '15m', '20m', '30m', '1h', '4h', '1d']:
    flux = f'''
    from(bucket: "market_data")
      |> range(start: -90d)
      |> filter(fn: (r) => r._measurement == "ohlcv")
      |> filter(fn: (r) => r.ticker == "IXIC")
      |> filter(fn: (r) => r.timeframe == "{tf}")
      |> pivot(rowKey: ["_time"], columnKey: ["_field"], valueColumn: "_value")
      |> sort(columns: ["_time"])
      |> tail(n: 1200)
    '''
    tables = query_api.query(flux)
    rows = []
    for table in tables:
        for row in table.records:
            rows.append({
                'timestamp': row.get_time(),
                'Open': float(row.values.get('open', 0)),
                'High': float(row.values.get('high', 0)),
                'Low': float(row.values.get('low', 0)),
                'Close': float(row.values.get('close', 0)),
            })
    if not rows:
        print(f"  {tf}: NO DATA")
        continue

    df = pd.DataFrame(rows)
    bar_count = len(df)
    last = df.iloc[-1]

    # Check SMA periods from the AN outfit: 11, 44, 88, 111, 444, 888
    # Also check 884 (what the tweet says)
    print(f"\n  {tf}: {bar_count} bars, latest Close={last['Close']:.2f}")
    for sma_p in [11, 44, 88, 111, 444, 888, 884]:
        if bar_count >= sma_p:
            sma_val = round(df['Close'].iloc[-sma_p:].mean(), 2)
            # Check penny match against OHLC
            o, h, l, c = last['Open'], last['High'], last['Low'], last['Close']
            matches = []
            for name, val in [('Open', o), ('High', h), ('Low', l), ('Close', c)]:
                diff = abs(round(val, 2) - sma_val)
                if diff < 0.015:
                    matches.append(f"{name}={val:.2f} diff={diff:.4f}")
            match_str = " *** PENNY MATCH: " + ", ".join(matches) if matches else ""
            print(f"    SMA{sma_p} = {sma_val:.2f}{match_str}")
        else:
            print(f"    SMA{sma_p} = INSUFFICIENT DATA ({bar_count} bars < {sma_p})")

# Also check penny_matches bucket for IXIC
print("\n=== IXIC PENNY MATCHES IN penny_matches BUCKET (last 1 day) ===")
flux = '''
from(bucket: "penny_matches")
  |> range(start: -1d)
  |> filter(fn: (r) => r._measurement == "penny_match")
  |> filter(fn: (r) => r.ticker == "IXIC")
  |> filter(fn: (r) => r._field == "close")
  |> group(columns: ["sma_period", "timeframe", "outfit"])
  |> count()
  |> group()
'''
tables = query_api.query(flux)
if not tables or all(len(t.records) == 0 for t in tables):
    print("  NO penny matches for IXIC in last 1 day")
else:
    for table in tables:
        for row in table.records:
            print(f"  SMA{row.values.get('sma_period')} | {row.values.get('timeframe')} | {row.values.get('outfit')} | {row.get_value()} matches")

client.close()
