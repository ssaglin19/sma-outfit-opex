# SMA Alert System — Project Instructions

## What This Is

A real-time SMA (Simple Moving Average) outfit detection system that monitors 77 equity tickers across 28 SMA outfits and 11 timeframes. It detects when price touches an SMA to the exact penny and generates alerts categorized as PBA (Precision Buy Algorithm), ASO (Automated Short Order), SPHS (Singular Point Hard Stop), or OBA (Optimized Buying Algorithm).

Based on: https://github.com/raultrades/SMA-outfits

## System Architecture

```
TradeStation API --> ingest.py --> InfluxDB --> detector.py --> alerts bucket
                                                    |
                                    dashboard.html (queries InfluxDB directly from browser)
                                    chart_server.py (port 5555, serves chart data from TradeStation)
                                    live_chart.html (chart popup from dashboard)
```

TWO SYSTEMS EXIST — ONLY USE THE NEW ONE:
- NEW (active): InfluxDB-based. `detector.py` + `dashboard.html` + `ingest.py`
- OLD (retired): `sma_alert_engine.py` (Flask on port 5050) + `sma_alerts.html`. DO NOT MODIFY OR USE.

## Critical Rules

1. **Never mix old and new systems.** The old system (`sma_alert_engine.py`) pulls directly from TradeStation. The new system uses InfluxDB as the data store. They are completely separate architectures.

2. **`dashboard.html` queries InfluxDB directly from the browser** via Flux over HTTP. There is no Python backend serving the dashboard. The InfluxDB token is hardcoded in the HTML.

3. **`detector.py` reads from InfluxDB only.** It does NOT pull from TradeStation. Do not add TradeStation imports or calls to detector.py.

4. **`detector.py` is snapshot-only.** It evaluates the last 1-2 bars at runtime. It does NOT backfill historical alerts. If it wasn't running when activity happened, those alerts don't exist.

5. **ASO gate:** Only 23/77 tickers are mapped to systems (S&P, NASDAQ, Dow) in detector.py. Unmapped tickers CANNOT generate ASO alerts. This is by design, not a bug.

6. **IXIC symbol mapping:** IXIC maps to `$NDX.X` in TradeStation (data_source.py line 61). Not $COMPQ, not $IXIC.

7. **Do not modify `dashboard.html` without backing it up first.** Current backup: `dashboard_LIVE_v1.html`.

8. **Penny match = exact $0.00 difference** between OHLC price and SMA value, rounded to the cent. For indices (IXIC/SPX/DJI), the protocol is "point break" (whole dollar) not "penny break."

## File Reference

Read `SETUP.md` for full file listing, startup order, and InfluxDB configuration.

## Config (config.py)

- 28 SMA outfits (including 56 Reversal, Tesla Cipher, Apple Cipher)
- 77 tickers (indices, ETFs, leveraged/inverse, mega-caps)
- 11 timeframes: 1m through 4h
- 3 systems: S&P 500, NASDAQ, Dow Jones
- InfluxDB: localhost:8086, org `sma-alerts`

## InfluxDB Buckets

- `market_data` — raw OHLCV bars (measurement: `ohlcv`)
- `penny_matches` — exact penny touches (measurement: `penny_match`)
- `alerts` — detection alerts from detector.py (measurement: `alert`)
- `sma_values` — computed SMA values
- `scoring` — outfit/ticker scores

## User Preferences

- Keep explanations concise
- Make no assumptions
- Every feature must trace back to the GitHub repo or case study evidence
- Do not freestyle or add features without explicit approval

## Pending Work

See the todo list in the current session, and `POTENTIAL_BUILD_IDEAS.md` for future features.

## Mini PC Migration

A Dell Mini Desktop (i5 8th gen, Windows 11) is being set up as a dedicated always-on machine for this system. Setup workflow is documented in session context.
