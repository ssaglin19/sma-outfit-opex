"""Test if $COMPX.X returns NASDAQ Composite (IXIC) data from TradeStation."""
from ts_client import TradeStationClient
import os
from dotenv import load_dotenv

load_dotenv()
ts = TradeStationClient()

# Try candidate symbols for NASDAQ Composite
candidates = ['$COMPX.X', '$COMP.X', '$IXIC.X', '$COMPQ.X']

for sym in candidates:
    print(f"\n--- {sym} ---")
    try:
        df = ts.get_bars(sym, 30, 'Minute', barsback=5)
        if df is not None and not df.empty:
            last = df.iloc[-1]
            print(f"  Close: {last['Close']:.2f}")
            print(f"  Time:  {df.index[-1]}")
            print(f"  Bars:  {len(df)}")
        else:
            print("  NO DATA")
    except Exception as e:
        print(f"  ERROR: {e}")

# Also show what $NDX.X returns for comparison
print(f"\n--- $NDX.X (current IXIC mapping) ---")
try:
    df = ts.get_bars('$NDX.X', 30, 'Minute', barsback=5)
    if df is not None and not df.empty:
        last = df.iloc[-1]
        print(f"  Close: {last['Close']:.2f}")
except Exception as e:
    print(f"  ERROR: {e}")
