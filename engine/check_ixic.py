from influxdb_client import InfluxDBClient
from dotenv import load_dotenv
import os

load_dotenv()
c = InfluxDBClient(
    url=os.getenv("INFLUXDB_URL", "http://localhost:8086"),
    token=os.getenv("INFLUXDB_TOKEN"),
    org=os.getenv("INFLUXDB_ORG", "sma-alerts"),
)
r = c.query_api().query(
    'from(bucket:"market_data") |> range(start:-90d) |> filter(fn:(r)=>r.ticker=="IXIC") |> count() |> limit(n:1)'
)
if r:
    for table in r:
        for row in table.records:
            print(f"  {row.get_field()}: {row.get_value()} records")
else:
    print("IXIC: NO DATA in market_data bucket")
c.close()
