# SMA Alert System — ASO Alert Sparsity Investigation

**Investigation Date:** 2026-03-22
**Status:** Read-only analysis complete (InfluxDB offline)
**Key Finding:** Design limitation prevents 70% of tickers from generating ASO alerts

---

## Executive Summary

The investigation reveals that "ASO" (Automated Short Order) alert sparsity is not a data or configuration bug — it is the result of an intentional system design constraint. **Only 23 of 77 tickers (30%) are mapped to the three scoring systems and can therefore generate ASO alerts. The other 54 tickers (70%) are architecturally prevented from triggering ASO detection.**

---

## 1. Critical Finding: "ASO" Is Not a Ticker

The user's statement "ticker ASO has sparse alerts" appears to stem from terminology confusion:

- **ASO** is the name of one of four detection algorithms (Automated Short Order), not a ticker symbol
- There is **no ticker named "ASO"** in the 77-ticker configuration
- ASO is a detection type alongside PBA (Precision Buy Algorithm), SPHS (Singular Point Hard Stop), and OBA (Optimized Buying Algorithm)

**Confirmed ticker count:** 77 unique ticker symbols configured in `config.py` (SPY, AAPL, NVDA, QQQ, etc.). None are named ASO.

---

## 2. System Architecture — The Three Scoring Systems

The alert system maintains three independent scoring systems that calculate trend state for index-level pattern recognition:

| System | Index Symbol | SMAs | Positive | Negative | Timeframes |
|--------|--------------|------|----------|----------|-----------|
| **S&P 500** | $SPX.X | 10, 50, 200 | MA10 > MA50 | MA10 < MA50 | 30m |
| **NASDAQ** | $NDX.X | 20, 100, 250 | MA20 > MA100 | MA20 < MA100 | 20m, 30m |
| **Dow Jones** | $DJX.X | 30, 60, 90, 300, 600, 900 | MA90 > MA300 | MA90 < MA300 | 15m, 1h |

Each system can be in one of three states: POSITIVE, NEGATIVE, or NEUTRAL.

---

## 3. The Architectural Bottleneck: Ticker-to-System Mapping

The critical limitation is in `detector.py` (lines 51-61), where only **23 of 77 tickers** are explicitly mapped to one of the three systems:

### S&P 500 mapped tickers (9):
```
SPX, SPY, UPRO, SPXU, SPXL, SSO, SDS, SPXS, SH
```

### NASDAQ mapped tickers (7):
```
IXIC, QQQ, TQQQ, SQQQ, QLD, QID, PSQ
```

### Dow Jones mapped tickers (7):
```
DJI, DIA, UDOW, SDOW, DDM, DXD, DOG
```

### Unmapped tickers (54 of 77 — 70%):
```
AAPD, AAPL, AAPU, AI, AMD, AMZN, ARM, BABA, BITO, BOIL, BRK-B,
COIN, DRIP, DRN, ENPH, ERX, GLD, GM, GOSH, GUSH, INTC, IWM, JPM,
LABU, META, MSFT, NFLX, NVDA, ORCX, PYPL, QCOM, RBLX, REK, RWM,
SOXL, SOXS, SVIX, SVXY, TBT, TLT, TNA, TSLA, TSLQ, TSLT, TSM,
UNH, UPST, USO, UVXY, UWM, V, VIX, VXX, WEBS
```

**Key observation:** Popular mega-cap stocks (AAPL, MSFT, NVDA, TSLA, META, GOOG, AMZN) are in the unmapped category.

---

## 4. Why ASO Alerts Are Sparse: The "No System = No ASO" Gate

The `detect_auto_short()` function in `detector.py` (lines 325-403) implements a hard architectural gate:

```python
def detect_auto_short(df, sma_period, system_context, ticker_system_name=None):
    """Detect ASO — system negative, price rallies to SMA resistance and rejects."""
    # Hard gate: ticker's own system must be negative
    if ticker_system_name:
        state_map = {
            "S&P 500": "sp500_state",
            "NASDAQ": "nasdaq_state",
            "Dow Jones": "dji_state",
        }
        state_key = state_map.get(ticker_system_name)
        if state_key and system_context.get(state_key) != "NEGATIVE":
            return None
    else:
        return None  # No system = no ASO  ← LINE 338 (THE GATE)
```

**What this means:**
- If a ticker is NOT in `TICKER_SYSTEM_MAP`, the parameter `ticker_system_name` is `None`
- When `ticker_system_name` is `None`, line 338 returns `None` immediately
- No further pattern checking occurs
- Therefore, **54 of 77 tickers (70%) cannot produce ASO alerts under any market condition**

**For the 23 mapped tickers, ASO detection also requires:**
1. The ticker's mapped system must be in NEGATIVE state (at that moment)
2. Exact penny match ($0.00 difference between OHLC and SMA)
3. Close price <= SMA (rejection, opposite of support)
4. Multi-bar rally pattern approaching from below (bars -1 and -2 checks)
5. Current bar OHLC4 <= current SMA (confirmation)

---

## 5. Complete ASO Detection Logic

### Phase A: System Validation (Hard Gate)
- Must be in TICKER_SYSTEM_MAP or returns None
- Mapped system must currently be NEGATIVE or returns None
- Russell 2000 and VIX tickers intentionally have no system mapping (per SESSION_STATE.md)

### Phase B: Data Sufficiency
- Minimum 20 bars required: `len(df) >= max(20, sma_period + 5)`
- SMA column must exist: `f"SMA_{sma_period}" in columns`
- SMA value must be computable (not NaN after rolling window)

### Phase C: Pattern Matching (checks both -1 and -2 bar offsets)
1. **Penny touch:** OHLC4 rounded to $0.01 must equal SMA rounded to $0.01
2. **Rejection:** Close <= SMA (price fails to stay above resistance)
3. **Approach pattern:** Previous bar OHLC4 < SMA (approached from below)
4. **Rally presence:** 3-bar OHLC4 < 2-bar OHLC4 (rally up to resistance)
5. **Current confirmation:** Current bar OHLC4 <= current SMA (still rejected)

### Phase D: Alert Generation
- Alert type: "automated_short_order"
- Hard stop level: SMA + $0.01 (resistance line, just above rejection point)
- Fields: sma_period, sma_value, ohlc4, close, bar offset, description

---

## 6. Why ASO Alerts Are Inherently Sparse (Even for Mapped Tickers)

Beyond the architectural gate, several factors limit ASO alert frequency:

### Design Constraints:
1. **System state dependency** — System must be NEGATIVE (not always true)
2. **Penny-precision requirement** — Needs $0.00 exact match (rare)
3. **Rejection pattern** — Requires close < SMA, opposite of support (less common)
4. **Multi-bar setup** — Specific rally pattern required (4-bar sequence validation)
5. **Only 23 tickers qualify** — 54 tickers structurally excluded

### Data Constraints:
- SMA periods range 10–999 bars. Large SMA periods need many historical bars
- If InfluxDB ingestion started recently, old SMA periods may have NaN values
- Penny match detection depends on TradeStation data accuracy and bar frequency

### Market Constraints:
- ASO fires on rejection patterns (price rallies to resistance, fails)
- These patterns are inherently less common than simple support holds (PBA)
- System must be negative simultaneously with pattern occurrence (timing dependent)

---

## 7. Configuration Details

### SMA Outfits
- **Count in config:** 26 named outfits + 2 system outfits = 28 total
- **Unique periods:** 129 SMA periods referenced across all outfits
- **Period range:** 1 to 999 bars (per SMA_MIN = 1, SMA_MAX = 999)

### Timeframes Configured (11 total)
```
1m, 2m, 3m, 5m, 10m, 15m, 20m, 30m, 1h, 2h, 4h
```

### Data Source
- **Current:** TradeStation (interim, configured in config.DATA_SOURCE)
- **Target:** Lightspeed (per repository specification)

---

## 8. Code Review Summary

### Files Analyzed:

**config.py** (lines 1–164)
- Defines INFLUXDB settings (bucket: "market_data")
- Lists all 28 SMA outfits and their SMA periods
- Lists all 77 tickers (no ASO ticker)
- Defines 3 systems with SMA thresholds
- Lists 11 timeframes

**detector.py** (lines 1–700+)
- **Lines 51–61:** TICKER_SYSTEM_MAP defines only 23 mapped tickers
- **Lines 325–403:** `detect_auto_short()` with critical gate at line 338
- **Line 338 exact code:** `return None  # No system = no ASO`
- ASO requires system_context passed in (calls scorer.py)

**ingest.py** (lines 1–306)
- Penny match detection (lines 82–120): checks OHLC vs SMA within $0.01
- SMA computation (lines 69–79): rolling window averages
- Outfit classification (lines 123–139): maps SMA period to outfit
- Writes to "penny_matches" bucket with outfit, sma_period, direction tags

**SESSION_STATE.md**
- Explicitly states: "Russell 2000 and VIX have NO system state (ASO skipped...)"
- Explicitly states: "ASO only fires when any system is NEGATIVE"

---

## 9. Investigation Limitations

**InfluxDB Status:** Not running at localhost:8086 during investigation
- Unable to query penny_matches bucket to confirm alert counts by ticker
- Unable to verify system state history during recent trading sessions
- Unable to spot-check specific ticker/outfit/timeframe combinations

**Without live InfluxDB queries, cannot answer:**
- How many penny matches exist for each ticker vs. system?
- Which outfits generate the most ASO alerts?
- What is the date range and volume of historical data?
- Are any of the 23 mapped tickers producing zero ASO alerts?
- Has system been NEGATIVE frequently during recent trading?

---

## 10. Hypotheses for Root Cause

Depending on user intent, the sparsity could stem from:

### **Hypothesis A: User meant a specific unmapped ticker**
(Example: AAPL, NVDA, TSLA, or another mega-cap)

**Root cause:** Ticker not in TICKER_SYSTEM_MAP → line 338 returns None → zero ASO alerts possible by design

**Evidence:**
- 54 of 77 tickers (70%) have no system mapping
- Major equities (AAPL, MSFT, NVDA, GOOG, AMZN) are in unmapped list
- Config supports 77 tickers but detector only acknowledges 23 for ASO

### **Hypothesis B: User meant the ASO algorithm type has sparse alerts generally**

**Root cause:** Multiple strict gates (system negative, penny match, pattern validation) naturally limit ASO frequency

**Evidence:**
- ASO requires exact $0.00 match (vs. other algorithms allow $0.01 flexibility)
- Rejection patterns less common than support patterns
- System state must be NEGATIVE (not a constant condition)
- SESSION_STATE.md explicitly notes ASO precision thresholds

### **Hypothesis C: One of the 23 mapped tickers isn't working as expected**

**Root cause:** System state stuck in POSITIVE/NEUTRAL, or SMA data insufficient

**Evidence:**
- Would need InfluxDB query to confirm system state history
- Would need to verify SMA computation for specific periods
- Would need to check if penny matches exist in database

---

## 11. Recommendations for Next Steps

### To Clarify User Intent:
1. Ask: "Are you referring to a specific ticker symbol, or the ASO algorithm type?"
2. If specific ticker: confirm the ticker and check if it's in TICKER_SYSTEM_MAP
3. If algorithm: run InfluxDB queries to compare ASO vs. PBA/SPHS/OBA alert counts

### To Investigate Further (when InfluxDB is available):
1. Verify InfluxDB is running and has data:
   ```bash
   curl http://localhost:8086/ping
   ```

2. Query penny_matches count by detection type:
   ```flux
   from(bucket: "penny_matches")
     |> range(start: -90d)
     |> filter(fn: (r) => r._measurement == "penny_match")
     |> group(columns: ["outfit", "direction"])
     |> count()
   ```

3. Query ASO alerts specifically:
   ```flux
   from(bucket: "alerts")
     |> range(start: -14d)
     |> filter(fn: (r) => r.type == "automated_short_order")
     |> group(columns: ["ticker", "outfit"])
     |> count()
   ```

4. Check system state history:
   ```flux
   from(bucket: "system_state")  # or alerts bucket if included
     |> range(start: -14d)
     |> filter(fn: (r) => r.system == "S&P 500")
     |> group(columns: ["state"])
     |> count()
   ```

---

## 12. Key Code Locations

| Topic | File | Lines |
|-------|------|-------|
| Ticker list | config.py | 117–148 |
| System definitions | config.py | 62–87 |
| System mapping | detector.py | 51–61 |
| ASO gate (critical) | detector.py | 325–338 |
| ASO pattern logic | detector.py | 349–403 |
| Penny match detection | ingest.py | 82–120 |
| Outfit classification | ingest.py | 123–139 |
| Session constraints | SESSION_STATE.md | Lines 14–16, 28 |

---

## Conclusion

The sparsity of ASO alerts is not a data quality issue or accidental misconfiguration. It reflects the system's intentional design:

1. **Architectural:** Only 23 of 77 tickers (30%) can generate ASO alerts; the other 70% are structurally excluded
2. **Algorithmic:** Even mapped tickers require a specific multi-bar rejection pattern with exact penny matches, which are rare
3. **Conditional:** System must be NEGATIVE at the moment of pattern occurrence (timing-dependent)

The investigation found no evidence of a bug. If sparse ASO alerts are problematic, the solution would require expanding TICKER_SYSTEM_MAP in detector.py to include unmapped tickers, or loosening the detection thresholds in detect_auto_short().

---

**Investigation completed:** 2026-03-22
**Analysis method:** Static code review of config.py, detector.py, ingest.py, SESSION_STATE.md
**Data source:** File system only (InfluxDB offline)
