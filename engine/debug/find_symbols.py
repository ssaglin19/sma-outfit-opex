"""Try common TradeStation symbol variants for NASDAQ Composite and Dow Jones."""
from ts_client import TradeStationClient
import requests

ts = TradeStationClient()

nasdaq_candidates = ['$COMP.X', '$COMPX.X', '$COMP', '$IXIC.X', '$NDX.X', '$NASX.X']
dow_candidates = ['$DJI.X', '$INDU.X', '$DJI', '$DOWI.X', '$DJIA.X', '$DJT.X']

print("NASDAQ Composite candidates:")
for sym in nasdaq_candidates:
    url = f"https://api.tradestation.com/v3/marketdata/barcharts/{sym}"
    params = {'interval': 30, 'unit': 'Minute', 'barsback': 5}
    resp = requests.get(url, headers=ts._get_headers(), params=params)
    if resp.status_code == 200:
        bars = resp.json().get('Bars', [])
        if bars:
            last_close = bars[-1].get('Close', '?')
            print(f"  {sym:>12}: OK — last close: {last_close}")
        else:
            print(f"  {sym:>12}: OK but 0 bars")
    else:
        print(f"  {sym:>12}: FAIL {resp.status_code}")

print("\nDow Jones candidates:")
for sym in dow_candidates:
    url = f"https://api.tradestation.com/v3/marketdata/barcharts/{sym}"
    params = {'interval': 30, 'unit': 'Minute', 'barsback': 5}
    resp = requests.get(url, headers=ts._get_headers(), params=params)
    if resp.status_code == 200:
        bars = resp.json().get('Bars', [])
        if bars:
            last_close = bars[-1].get('Close', '?')
            print(f"  {sym:>12}: OK — last close: {last_close}")
        else:
            print(f"  {sym:>12}: OK but 0 bars")
    else:
        print(f"  {sym:>12}: FAIL {resp.status_code}")
