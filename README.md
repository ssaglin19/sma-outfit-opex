# SMA Outfit x OPEX Synthesis (private)

Pairs my SMA-outfit detector engine with the unfairmarket SMA-outfits case studies to backtest an outfit -> catalyst -> OPEX-resolution hypothesis.

## Directory Structure (post-refactor)

```
sma-outfit-opex/
├── engine/
│   ├── src/                 # core pipeline
│   │   ├── detector.py, ingest.py, historical_scan.py, scorer.py, score_live.py
│   │   ├── config.py, data_source.py, ts_client.py, ts_auth.py, influxdb_setup.py
│   │   ├── chart_server.py, eod_report.py, backtest_spxu.py, build_ixic_chart.py
│   │   └── utils/           # shared: influx.py, sma.py (deduped from 4×)
│   ├── public/              # dashboards + calendar UI
│   │   ├── dashboard.html (active), dashboard_LIVE_v1.html
│   │   ├── 56_reversal_activity.html, ixic_56reversal..., live_chart.html, mockup_chart.html, backtest_chart.html
│   │   └── calendar/        # index.html + entries.js, opex_entries.js, etc. (moved from archive/calendar)
│   ├── debug/               # 13 orphaned: debug_spxu*.py (7), debug_ixic.py, find_symbols*.py (2), check_*.py (3), aso_investigate.py
│   ├── archive/
│   │   ├── dashboards/      # 3 redundant backups
│   │   └── old_system/      # sma_alert_engine.py + sma_alerts.html (retired Flask 5050)
│   └── tests/               # test_api.py, test_compx.py
├── archive/
│   ├── catalog.jsonl, enumeration/, threads/, media/ (88 case studies)
│   ├── analysis/            # gap_findings, signature_*
│   └── _*.json              # state (5 files, append-only)
├── reference/unfairmarket/  # third-party case studies, unmodified
├── logs/                    # alerts.log (1.3M, gitignored)
└── refresh_calendar.bat     # nightly refresh (archive/refresh_calendar.py)
```

See `engine/CLAUDE.md` for project rules, `engine/SETUP.md` for startup order.

- `engine/` — my detector codebase (InfluxDB + TradeStation).
- `reference/unfairmarket/` — third-party case-study material, unmodified. See its `SOURCE.md`.
