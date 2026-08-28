"""Check which tickers return data from TradeStation on 30m."""
from data_source import get_data_source
import time

MISSING = [
    "WEBS", "UWM", "SDOW", "VXX", "UVXY", "SVXY",
    "SOXS", "SOXL", "ERX", "GUSH", "DRIP", "BOIL", "USO",
    "LABU", "DRN", "REK", "GLD", "TBT", "BITO",
    "COIN", "PYPL", "UPST", "RBLX", "ARM",
    "BRK-B", "GM", "JPM", "V", "UNH",
    "AAPD", "AAPU", "TSLT", "TSLQ",
    "BABA", "TSM",
]

source = get_data_source()
ok = []
fail = []

for t in MISSING:
    df = source.get_bars(t, 30, bars_back=100)
    if df.empty:
        fail.append(t)
        print(f"  FAIL: {t}")
    else:
        ok.append(t)
        print(f"  OK:   {t} ({len(df)} bars)")
    time.sleep(0.5)

print(f"\nWorking: {len(ok)} — {ok}")
print(f"Failed:  {len(fail)} — {fail}")
