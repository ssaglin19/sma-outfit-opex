"""Quick API test for all index symbols."""
from ts_client import TradeStationClient
import requests

ts = TradeStationClient()

symbols = ['$SPX.X', '$COMPX.X', '$DJI.X', '$VIX.X', 'SPY', 'SPXU']

for sym in symbols:
    url = f"https://api.tradestation.com/v3/marketdata/barcharts/{sym}"
    params = {'interval': 30, 'unit': 'Minute', 'barsback': 100}
    resp = requests.get(url, headers=ts._get_headers(), params=params)
    if resp.status_code == 200:
        bars = resp.json().get('Bars', [])
        print(f"  {sym:>12}: OK — {len(bars)} bars")
    else:
        print(f"  {sym:>12}: FAIL {resp.status_code} — {resp.text[:200]}")
