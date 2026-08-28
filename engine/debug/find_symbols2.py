"""Try more symbol variants and proxies."""
from ts_client import TradeStationClient
import requests

ts = TradeStationClient()

candidates = [
    # Dow alternatives
    '$DJ.X', '$DJIND.X', '$DJX.X', '$DJIA', 'DIA',
    # NASDAQ alternatives
    '$COMPQ.X', '$NCOMP.X', 'QQQ',
    # Verify SPX still works
    '$SPX.X',
]

print("Symbol search:")
for sym in candidates:
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

# Also try symbol search API if available
print("\nTrying symbol lookup API for 'dow jones'...")
url = "https://api.tradestation.com/v3/marketdata/symbollists/dollarone/symbolnames"
resp2 = requests.get(
    "https://api.tradestation.com/v3/marketdata/symbols/suggest/dow",
    headers=ts._get_headers(),
    params={'text': 'dow jones', '$top': 10}
)
if resp2.status_code == 200:
    print(f"  Suggest results: {resp2.text[:500]}")
else:
    # Try the search endpoint
    resp3 = requests.get(
        "https://api.tradestation.com/v3/marketdata/symbols/search/$DJI",
        headers=ts._get_headers(),
        params={'criteria': 'category=Index'}
    )
    if resp3.status_code == 200:
        print(f"  Search results: {resp3.text[:500]}")
    else:
        print(f"  Search FAIL: {resp3.status_code} {resp3.text[:200]}")
