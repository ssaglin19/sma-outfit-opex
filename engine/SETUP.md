# SMA Alert System — Setup & Architecture

**Last updated:** 2026-04-15

## Architecture

```
TradeStation API (USEQ24Hour session)
    |
    v
ingest.py  -->  InfluxDB (localhost:8086)
                  |-- market_data     (raw OHLCV bars)
                  |-- penny_matches   (exact $0.00 OHLC-to-SMA matches)
                  |-- alerts          (PBA / ASO / OBA / SPHS detections)
                  |-- sma_values
                  |-- scoring
                  |
                  v
detector.py reads market_data --> writes to alerts bucket
                  |
                  v
dashboard.html queries InfluxDB directly from browser (Flux over HTTP)
chart_server.py serves live chart data from TradeStation on port 5555
live_chart.html renders charts (opened from dashboard alert clicks)
```

## Order of Operations (startup)

1. Start InfluxDB (`influxd.exe`)
2. Run ingest (`python ingest.py --quick` for weekly refresh, or `python ingest.py` for full)
3. Start detector (`python detector.py` — loop mode, 60s cycles during market hours)
4. Start chart server (`python chart_server.py` — port 5555)
5. Open `dashboard.html` in browser

One-click launcher: `Desktop\SMA_Dashboard.bat` runs all 5 steps.

## Configuration

Source of truth: `config.py`

- 28 SMA outfits (including 56 Reversal, Tesla Cipher, Apple Cipher added 3/21)
- 77 tickers (indices, ETFs, leveraged/inverse, mega-caps, equities)
- 11 timeframes: 1m, 2m, 3m, 5m, 10m, 15m, 20m, 30m, 1h, 2h, 4h
- 3 systems: S&P 500, NASDAQ, Dow Jones
- 4 alert types: PBA, ASO, SPHS, OBA

## Key Files — Active System

| File | Purpose |
|------|---------|
| `config.py` | 28 outfits, 77 tickers, 11 timeframes, InfluxDB settings |
| `ingest.py` | TradeStation -> InfluxDB pipeline. `--quick` = 2,000 bars/combo (~15 min). Full = 57,600 bars (~9 hrs) |
| `detector.py` | Reads InfluxDB, writes alerts. Loop mode (60s) or `--once`. 4 algorithms: PBA/ASO/SPHS/OBA |
| `chart_server.py` | HTTP server (port 5555). Pulls live from TradeStation for chart rendering |
| `dashboard.html` | THE dashboard. Queries InfluxDB directly via Flux. Outfit/Ticker/Alert panels. Refreshes every 60s |
| `dashboard_LIVE_v1.html` | Backup copy of dashboard.html (safety) |
| `live_chart.html` | Chart popup opened from dashboard alert clicks |
| `scorer.py` | Queries penny_matches, produces outfit + ticker rankings |
| `eod_report.py` | End-of-day HTML report |
| `data_source.py` | TradeStationSource class, symbol mapping (IXIC->$NDX.X, SPX->$SPX.X, etc.) |
| `ts_client.py` | TradeStation API client (USEQ24Hour session) |
| `ts_auth.py` | TradeStation OAuth token management |
| `.env` | API credentials and InfluxDB token |

## Key Files — Old System (NOT in use)

| File | Purpose |
|------|---------|
| `sma_alert_engine.py` | OLD Flask server on port 5050. Pulls directly from TradeStation. DO NOT USE. |
| `sma_alerts.html` | OLD dashboard. Polls sma_alert_engine.py. DO NOT USE. |

## Key Files — Utilities / One-off

| File | Purpose |
|------|---------|
| `influxdb_setup.py` | One-time InfluxDB bucket creation |
| `score_live.py` | Standalone scorer (no InfluxDB, direct TradeStation) |
| `backtest_spxu.py` | SPXU backtesting script |
| `build_ixic_chart.py` | Generates standalone IXIC 56 Reversal chart HTML from InfluxDB |
| `check_data_range.py` | Reports date range of data in each InfluxDB bucket |
| `check_sso_ma500.py` | Quick SSO MA500 lookup |
| `aso_investigate.py` | IXIC/QQQ/TQQQ alert investigation |
| `debug_*.py` | Various debug/investigation scripts |

## InfluxDB

- URL: http://localhost:8086
- Org: `sma-alerts`
- Buckets: `market_data`, `penny_matches`, `alerts`, `sma_values`, `scoring`
- Token: stored in `.env` and hardcoded in `dashboard.html`

## Desktop Launcher

`C:\Users\ssagl\Desktop\SMA_Dashboard.bat` — one-click startup:
1. Starts InfluxDB
2. Runs quick ingest
3. Starts detector (loop mode)
4. Starts chart server
5. Opens dashboard

## Folder Structure

- `C:\Users\ssagl\Documents\sma-alerts\` — all project code
- `C:\Users\ssagl\Desktop\SMA_Dashboard.bat` — launcher shortcut
- `C:\Users\ssagl\Documents\SMA-bat-files\` — individual .bat files (moved off Desktop)
- `C:\Users\ssagl\Downloads\influxdb2-2.7.12-windows\` — InfluxDB binary

## Critical Rules

- The NEW system uses InfluxDB. The OLD system (`sma_alert_engine.py`) used direct TradeStation polling. Do NOT mix them.
- `dashboard.html` queries InfluxDB directly from the browser — no Python backend needed for the dashboard itself.
- `detector.py` is snapshot-only: evaluates last 1-2 bars at runtime. Does NOT backfill historical alerts.
- ASO alerts require ticker mapped to a system AND system state NEGATIVE (23/77 tickers eligible).
- IXIC maps to `$NDX.X` in TradeStation (not $COMPQ or $IXIC).
