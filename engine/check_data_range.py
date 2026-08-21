"""Check how far back our InfluxDB data goes for each bucket."""
import os
from influxdb_client import InfluxDBClient

INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = os.environ.get("INFLUXDB_TOKEN", "")
INFLUX_ORG = "sma-alerts"

client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
qa = client.query_api()

for bucket in ["market_data", "penny_matches", "alerts", "sma_values", "scoring"]:
    print(f"\n{'='*50}")
    print(f"  BUCKET: {bucket}")
    print(f"{'='*50}")

    # Earliest record
    try:
        q = f'''
from(bucket: "{bucket}")
  |> range(start: -10y)
  |> first()
  |> keep(columns: ["_time"])
  |> sort(columns: ["_time"])
  |> limit(n: 1)
'''
        tables = qa.query(q, org=INFLUX_ORG)
        earliest = None
        for t in tables:
            for r in t.records:
                ts = r.get_time()
                if earliest is None or ts < earliest:
                    earliest = ts
        if earliest:
            print(f"  Earliest: {earliest.strftime('%Y-%m-%d %H:%M')}")
        else:
            print(f"  Earliest: (empty bucket)")
    except Exception as e:
        print(f"  Earliest: ERROR - {e}")

    # Latest record
    try:
        q = f'''
from(bucket: "{bucket}")
  |> range(start: -10y)
  |> last()
  |> keep(columns: ["_time"])
  |> sort(columns: ["_time"], desc: true)
  |> limit(n: 1)
'''
        tables = qa.query(q, org=INFLUX_ORG)
        latest = None
        for t in tables:
            for r in t.records:
                ts = r.get_time()
                if latest is None or ts > latest:
                    latest = ts
        if latest:
            print(f"  Latest:   {latest.strftime('%Y-%m-%d %H:%M')}")
        else:
            print(f"  Latest:   (empty bucket)")
    except Exception as e:
        print(f"  Latest:   ERROR - {e}")

# Also check a few specific tickers in market_data
print(f"\n{'='*50}")
print(f"  SAMPLE TICKERS — date range in market_data")
print(f"{'='*50}")
for ticker in ["TQQQ", "SPXU", "SPY", "IXIC", "AAPL", "SSO"]:
    try:
        q = f'''
from(bucket: "market_data")
  |> range(start: -10y)
  |> filter(fn: (r) => r._measurement == "ohlcv")
  |> filter(fn: (r) => r.ticker == "{ticker}")
  |> filter(fn: (r) => r._field == "close")
  |> first()
  |> keep(columns: ["_time"])
'''
        tables = qa.query(q, org=INFLUX_ORG)
        earliest = None
        for t in tables:
            for r in t.records:
                earliest = r.get_time()

        q2 = f'''
from(bucket: "market_data")
  |> range(start: -10y)
  |> filter(fn: (r) => r._measurement == "ohlcv")
  |> filter(fn: (r) => r.ticker == "{ticker}")
  |> filter(fn: (r) => r._field == "close")
  |> last()
  |> keep(columns: ["_time"])
'''
        tables2 = qa.query(q2, org=INFLUX_ORG)
        latest = None
        for t in tables2:
            for r in t.records:
                ts = r.get_time()
                if latest is None or ts > latest:
                    latest = ts

        if earliest and latest:
            print(f"  {ticker:6s}: {earliest.strftime('%Y-%m-%d')} → {latest.strftime('%Y-%m-%d')}")
        else:
            print(f"  {ticker:6s}: (no data)")
    except Exception as e:
        print(f"  {ticker:6s}: ERROR - {e}")

client.close()
