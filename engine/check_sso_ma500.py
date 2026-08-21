"""Quick check: SSO at MA500 (Russia 2000 outfit)"""
import os
from influxdb_client import InfluxDBClient

INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = os.environ.get("INFLUXDB_TOKEN", "")
INFLUX_ORG = "sma-alerts"

client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)

# Pull SSO bars - check all timeframes available
for tf in ["1m", "3m", "5m", "15m", "30m", "1h", "2h"]:
    query = f'''
from(bucket: "market_data")
  |> range(start: -30d)
  |> filter(fn: (r) => r._measurement == "ohlcv")
  |> filter(fn: (r) => r.ticker == "SSO")
  |> filter(fn: (r) => r.timeframe == "{tf}")
  |> filter(fn: (r) => r._field == "close")
  |> sort(columns: ["_time"], desc: true)
  |> limit(n: 600)
'''
    tables = client.query_api().query(query, org=INFLUX_ORG)
    bars = []
    for table in tables:
        for rec in table.records:
            bars.append({"time": rec.get_time().isoformat(), "close": float(rec.get_value())})

    if not bars:
        continue

    bars.reverse()  # chronological
    closes = [b["close"] for b in bars]

    # Compute MA500 if we have enough bars
    if len(closes) >= 500:
        ma500 = sum(closes[-500:]) / 500
        current = closes[-1]
        diff = current - ma500
        print(f"  {tf}: {len(bars)} bars | Last: ${current:.2f} | MA500: ${ma500:.2f} | Diff: ${diff:.2f}")
    else:
        print(f"  {tf}: {len(bars)} bars (need 500 for MA500) | Last: ${closes[-1]:.2f}")

# Also check penny_matches for SSO + SMA 500
print(f"\n  Penny matches for SSO at SMA 500:")
query = '''
from(bucket: "penny_matches")
  |> range(start: -30d)
  |> filter(fn: (r) => r._measurement == "penny_match")
  |> filter(fn: (r) => r.ticker == "SSO")
  |> filter(fn: (r) => r.sma_period == "500")
  |> pivot(rowKey: ["_time"], columnKey: ["_field"], valueColumn: "_value")
  |> sort(columns: ["_time"], desc: true)
  |> limit(n: 20)
'''
tables = client.query_api().query(query, org=INFLUX_ORG)
count = 0
for table in tables:
    for rec in table.records:
        v = rec.values
        print(f"    {v['_time'].strftime('%Y-%m-%d %H:%M')} | SMA500=${v.get('sma_value','')} | {v.get('price_field','')}=${v.get('close','')}")
        count += 1
if count == 0:
    print("    (none found)")

# Check alerts for SSO
print(f"\n  Recent alerts for SSO:")
query = '''
from(bucket: "alerts")
  |> range(start: -30d)
  |> filter(fn: (r) => r._measurement == "alert")
  |> filter(fn: (r) => r.ticker == "SSO")
  |> pivot(rowKey: ["_time"], columnKey: ["_field"], valueColumn: "_value")
  |> sort(columns: ["_time"], desc: true)
  |> limit(n: 10)
'''
tables = client.query_api().query(query, org=INFLUX_ORG)
count = 0
for table in tables:
    for rec in table.records:
        v = rec.values
        print(f"    {v['_time'].strftime('%Y-%m-%d %H:%M')} | {v.get('type','')} | {v.get('outfit','')} | MA{v.get('sma_period','')} | ${v.get('price','')}")
        count += 1
if count == 0:
    print("    (none found)")

client.close()
