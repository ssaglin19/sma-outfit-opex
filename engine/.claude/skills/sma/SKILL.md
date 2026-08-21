---
name: sma
description: "SMA Alert System — real-time penny-match detection across 77 tickers, 28 outfits, 11 timeframes using InfluxDB + TradeStation. Use this skill whenever working on the sma-alerts project, including: querying InfluxDB data, modifying detector/ingest/dashboard code, adding outfits or tickers, debugging alert logic, building charts, or discussing system architecture. Trigger on any mention of SMA outfits, penny matches, PBA/ASO/SPHS/OBA alerts, detector.py, ingest.py, dashboard.html, or the sma-alerts project."
---

# SMA Alert System — Skill Reference

## What This System Does

Monitors 77 equity tickers across 28 SMA outfits and 11 timeframes. Detects when price touches an SMA to the exact penny ($0.00 difference between OHLC and SMA value). Generates alerts categorized as PBA, ASO, SPHS, or OBA.

Based on: https://github.com/raultrades/SMA-outfits

## Architecture (memorize this)

```
TradeStation API --> ingest.py --> InfluxDB --> detector.py --> alerts bucket
                                                    |
                                    dashboard.html (queries InfluxDB directly from browser)
                                    chart_server.py (port 5555, serves chart data)
                                    live_chart.html (chart popup from dashboard)
```

There are TWO systems in the codebase. **Only use the NEW one:**

| System | Files | Status |
|--------|-------|--------|
| NEW (active) | `detector.py`, `dashboard.html`, `ingest.py` | InfluxDB-based. USE THIS. |
| OLD (retired) | `sma_alert_engine.py`, `sma_alerts.html` | Flask on port 5050. DO NOT TOUCH. |

## Non-Negotiable Rules

1. **Never mix old and new systems.** They are completely separate architectures.
2. **`dashboard.html` queries InfluxDB directly from the browser** via Flux over HTTP. No Python backend serves it. The InfluxDB token is hardcoded in the HTML.
3. **`detector.py` reads from InfluxDB only.** It does NOT call TradeStation. Never add TradeStation imports to detector.py.
4. **`detector.py` is snapshot-only.** Evaluates last 1-2 bars at runtime. Does NOT backfill. If it wasn't running when activity happened, those alerts don't exist.
5. **ASO gate:** Only 23/77 tickers are mapped to systems (S&P, NASDAQ, Dow). Unmapped tickers CANNOT generate ASO alerts. This is by design.
6. **IXIC symbol mapping:** IXIC maps to `$NDX.X` in TradeStation. Not $COMPQ, not $IXIC.
7. **Back up `dashboard.html` before modifying it.** Current backup: `dashboard_LIVE_v1.html`.
8. **Penny match = exact $0.00 difference** between OHLC price and SMA value, rounded to cent. For indices (IXIC/SPX/DJI), the protocol is "point break" (whole dollar) not "penny break."
9. **Do not add features without explicit approval.** Every feature must trace back to the GitHub repo or case study evidence.

## Config Quick Reference (config.py)

- **28 SMA outfits** including 56 Reversal (MA28/55/111/221/442/884), Tesla Cipher, Apple Cipher
- **77 tickers:** indices, ETFs, leveraged/inverse, mega-caps
- **11 timeframes:** 1m, 2m, 3m, 5m, 10m, 15m, 20m, 30m, 1h, 2h, 4h
- **3 systems:** S&P 500, NASDAQ, Dow Jones
- **4 alert types:** PBA (Precision Buy Algorithm), ASO (Automated Short Order), SPHS (Singular Point Hard Stop), OBA (Optimized Buying Algorithm)

## InfluxDB

- URL: `http://localhost:8086`
- Org: `sma-alerts`
- Buckets: `market_data`, `penny_matches`, `alerts`, `sma_values`, `scoring`
- Token: in `.env` file and hardcoded in `dashboard.html`

## Key Files

| File | What It Does |
|------|-------------|
| `config.py` | 28 outfits, 77 tickers, 11 timeframes, InfluxDB settings |
| `ingest.py` | TradeStation → InfluxDB. `--quick` ~15 min, full ~9 hrs |
| `detector.py` | Reads InfluxDB → writes alerts. Loop mode (60s) or `--once` |
| `chart_server.py` | HTTP on port 5555, pulls live from TradeStation for charts |
| `dashboard.html` | THE dashboard. Queries InfluxDB via Flux. Auto-refreshes 60s |
| `live_chart.html` | Chart popup from dashboard alert clicks |
| `scorer.py` | Queries penny_matches, produces outfit + ticker rankings |
| `eod_report.py` | End-of-day HTML report |
| `data_source.py` | TradeStationSource class, symbol mapping |
| `ts_client.py` | TradeStation API client (USEQ24Hour session) |
| `ts_auth.py` | OAuth token management |

## ASO Detection Deep Dive

The ASO algorithm has a hard gate at detector.py line 338: if a ticker isn't in `TICKER_SYSTEM_MAP`, it immediately returns None. Only 23 tickers qualify:

- **S&P 500 (9):** SPX, SPY, UPRO, SPXU, SPXL, SSO, SDS, SPXS, SH
- **NASDAQ (7):** IXIC, QQQ, TQQQ, SQQQ, QLD, QID, PSQ
- **Dow Jones (7):** DJI, DIA, UDOW, SDOW, DDM, DXD, DOG

Even for mapped tickers, ASO requires: system NEGATIVE state + exact penny match + close ≤ SMA (rejection) + multi-bar rally pattern + current bar confirmation.

## Startup Order

1. Start InfluxDB (`influxd.exe`)
2. Run ingest (`python ingest.py --quick`)
3. Start detector (`python detector.py` — loop mode)
4. Start chart server (`python chart_server.py` — port 5555)
5. Open `dashboard.html` in browser

One-click: `Desktop\SMA_Dashboard.bat`

## User Preferences

- Keep explanations concise
- Make no assumptions
- Treat like an expert — no hand-holding
- Every feature must trace back to the GitHub repo or case study evidence
- Do not freestyle or add features without explicit approval

## Reference Documents

- `CLAUDE.md` — Project instructions (read first)
- `SETUP.md` — Full architecture and file listing
- `INVESTIGATION_ASO_SPARSE_ALERTS.md` — ASO gate analysis
- `POTENTIAL_BUILD_IDEAS.md` — Approved future feature ideas
