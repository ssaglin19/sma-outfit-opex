@echo off
echo ============================================
echo   SMA ALERT SYSTEM - STARTING ALL SERVICES
echo ============================================

echo [1/5] Starting InfluxDB...
start "" "C:\Users\Sean Mini PC\Desktop\influxdb\influxd.exe"
timeout /t 5 /nobreak >nul

echo [2/5] Running Quick Ingest (TradeStation → InfluxDB)...
start "Ingest" cmd /k "cd /d "C:\Users\Sean Mini PC\Documents\sma-alerts" && python ingest.py --quick"

echo [3/5] Starting Detector (loop mode, 60s cycles)...
start "Detector" cmd /k "cd /d "C:\Users\Sean Mini PC\Documents\sma-alerts" && python detector.py"
timeout /t 2 /nobreak >nul

echo [4/5] Starting Chart Server...
start "ChartServer" cmd /k "cd /d "C:\Users\Sean Mini PC\Documents\sma-alerts" && python chart_server.py"
timeout /t 1 /nobreak >nul

echo [5/5] Opening Dashboard...
start "" "C:\Users\Sean Mini PC\Documents\sma-alerts\dashboard.html"

echo.
echo All services started.
echo   - Ingest: pulling fresh bars (~12-15 min)
echo   - Detector: runs every 60s during market hours
echo   - Chart Server: click alerts to view charts
echo   - Dashboard: auto-refreshes every 60s
echo ============================================
pause
