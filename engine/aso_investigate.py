"""Check IXIC/NDX alerts and all NASDAQ-related tickers"""
from influxdb_client import InfluxDBClient

client = InfluxDBClient(
    url="http://localhost:8086",
    token="__INFLUXDB_TOKEN__",
    org="sma-alerts",
    timeout=30_000
)
api = client.query_api()

# Check all NASDAQ-related tickers for alerts
for ticker in ["IXIC", "NDX", "$NDX.X", "COMPX", "QQQ", "TQQQ", "SQQQ"]:
    try:
        q = f'''from(bucket: "alerts")
  |> range(start: 2026-03-20T00:00:00Z, stop: 2026-03-21T00:00:00Z)
  |> filter(fn: (r) => r._measurement == "alert")
  |> filter(fn: (r) => r.ticker == "{ticker}")
  |> pivot(rowKey: ["_time"], columnKey: ["_field"], valueColumn: "_value")
  |> sort(columns: ["_time"])'''
        tables = api.query(q)
        count = 0
        for t in tables:
            for r in t.records:
                count += 1
                vals = r.values
                print(f"  [{r.get_time()}] {ticker} | {vals.get('type','?')} | {vals.get('outfit','?')} | SMA{vals.get('sma_period','?')} @ ${vals.get('sma_value','?')} | {vals.get('timeframe','?')}")
        if count == 0:
            print(f"  {ticker}: no alerts on 3/20")
        else:
            print(f"  {ticker}: {count} alerts on 3/20\n")
    except Exception as e:
        print(f"  {ticker}: error - {e}")

# Also check all distinct tickers in alerts bucket
print("\n=== ALL TICKERS WITH ALERTS ON 3/20 ===")
try:
    q = '''from(bucket: "alerts")
  |> range(start: 2026-03-20T00:00:00Z, stop: 2026-03-21T00:00:00Z)
  |> filter(fn: (r) => r._measurement == "alert")
  |> group(columns: ["ticker", "type"])
  |> count()
  |> sort(columns: ["_value"], desc: true)'''
    tables = api.query(q)
    for t in tables:
        for r in t.records:
            print(f"  {r.values.get('ticker','?')} | {r.values.get('type','?')}: {r.get_value()}")
except Exception as e:
    print(f"  Failed: {e}")

client.close()
print("\nDone.")
