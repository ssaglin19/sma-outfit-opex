import os
from dotenv import load_dotenv
from influxdb_client import InfluxDBClient
def load_env_config():
    load_dotenv()
    return {
        "url": os.getenv("INFLUXDB_URL", "http://localhost:8086"),
        "org": os.getenv("INFLUXDB_ORG", "sma-alerts"),
        "token": os.getenv("INFLUXDB_TOKEN", ""),
    }
def get_influx_client():
    cfg=load_env_config()
    return InfluxDBClient(url=cfg["url"], org=cfg["org"], token=cfg["token"])
