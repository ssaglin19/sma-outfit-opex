@echo off
echo ============================================
echo   SMA ALERT SYSTEM - MINI PC (AUTONOMOUS)
echo ============================================

echo [1/5] Starting InfluxDB...
start "InfluxDB" cmd /k "cd /d C:\Users\Sean Mini PC\Desktop\influxdb && influxd.exe"
timeout /t 5 /nobreak >nul

echo [2/5] Starting Live Ingest (5 min cycles, market hours only)...
start "LiveIngest" cmd /k "cd /d C:\Users\Sean Mini PC\Documents\sma-alerts && python ingest.py --live"

echo [3/5] Starting Detector (60s cycles, market hours only)...
start "Detector" cmd /k "cd /d C:\Users\Sean Mini PC\Documents\sma-alerts && python detector.py"
timeout /t 2 /nobreak >nul

echo [4/5] Starting Chart Server...
start "ChartServer" cmd /k "cd /d C:\Users\Sean Mini PC\Documents\sma-alerts && python chart_server.py"
timeout /t 1 /nobreak >nul

echo [5/5] Opening Dashboard...
start "" "C:\Users\Sean Mini PC\Documents\sma-alerts\dashboard.html"

echo.
echo ============================================
echo   All services running autonomously.
echo   - InfluxDB: database engine
echo   - Live Ingest: fresh bars every 5 min
echo   - Detector: scans every 60s for alerts
echo   - Chart Server: click alerts to view charts
echo   - Dashboard: auto-refreshes every 60s
echo
echo   Sleeps outside market hours. No touch needed.
echo ============================================
pause
