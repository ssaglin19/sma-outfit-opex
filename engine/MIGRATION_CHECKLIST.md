# SMA Dashboard — Mini PC Migration Checklist

## Phase 1: Hardware Setup (no software needed yet)

- [ ] Unbox Dell Mini PC
- [ ] Get DisplayPort-to-HDMI cable (the port that looks like HDMI but isn't = DisplayPort)
- [ ] Connect DisplayPort-to-HDMI cable from mini PC to monitor
- [ ] Connect USB keyboard and USB mouse
- [ ] Power on, complete Windows 11 first-boot setup (create user account, connect WiFi)
- [ ] Confirm you're at the Windows desktop and have internet

## Phase 2: Software Install (on the mini PC)

- [ ] Install Python (python.org — match version from laptop: run `python --version` on laptop first)
- [ ] During install: CHECK "Add Python to PATH"
- [ ] Open PowerShell, confirm: `python --version`
- [ ] Install pip packages: `pip install influxdb-client requests python-dotenv`
- [ ] Download InfluxDB 2.7.12 for Windows (influxdata.com) — extract to a known folder
- [ ] Sign into OneDrive on the mini PC (same Microsoft account as laptop)
- [ ] Wait for `Documents\sma-alerts\` folder to sync down

## Phase 3: InfluxDB Setup (on the mini PC)

- [ ] Open PowerShell as Administrator
- [ ] Navigate to InfluxDB folder, run `.\influxd.exe`
- [ ] Open browser, go to `http://localhost:8086`
- [ ] Complete InfluxDB first-time setup: org = `sma-alerts`, bucket = `market_data`
- [ ] Save the new API token
- [ ] Create remaining buckets: `penny_matches`, `alerts`, `sma_values`, `scoring`
- [ ] Update `sma-alerts\.env` with the new InfluxDB token
- [ ] Update the token in `dashboard.html` (hardcoded)

## Phase 4: TradeStation Auth (on the mini PC)

- [ ] Verify TradeStation API credentials in `.env` (client ID, secret, refresh token)
- [ ] These may need to be refreshed — test with a quick API call
- [ ] If refresh token expired: re-auth through TradeStation developer portal

## Phase 5: Quick Ingest (validation run — ~15 min)

- [ ] InfluxDB must be running (Phase 3)
- [ ] Open PowerShell, cd to `sma-alerts` folder
- [ ] Run: `python ingest.py --quick`
- [ ] Confirm no errors, check InfluxDB UI for data in `market_data` bucket
- [ ] Start detector: `python detector.py --once`
- [ ] Start chart server: `python chart_server.py`
- [ ] Open `dashboard.html` in browser — confirm alerts show up
- [ ] If everything works: proceed to Phase 6

## Phase 6: Full Ingest (overnight — ~9 hours)

- [ ] Stop the quick ingest if still running
- [ ] Run: `python ingest.py` (no --quick flag)
- [ ] Let it run overnight
- [ ] Next morning: verify data in InfluxDB, check date ranges
- [ ] Start detector in loop mode: `python detector.py`
- [ ] Start chart server: `python chart_server.py`
- [ ] Open dashboard — full system is live

## Phase 7: Automation (make it always-on)

- [ ] Copy/recreate `SMA_Dashboard.bat` on mini PC Desktop
- [ ] Update all paths in the .bat file to match mini PC folder structure
- [ ] Test the .bat launcher — should start everything in one click
- [ ] Set mini PC power settings: never sleep, never turn off display (or set long timeout)
- [ ] Optional: add SMA_Dashboard.bat to Windows startup folder

## Notes

- The 28 GB InfluxDB database is NOT being transferred — full re-ingest on mini PC instead
- sma-alerts code transfers via OneDrive sync
- New InfluxDB instance = new token — must update .env AND dashboard.html
- TradeStation refresh tokens expire — may need to re-auth on the new machine
