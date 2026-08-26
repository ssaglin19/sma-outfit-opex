@echo off
REM ============================================================
REM   SMA CALENDAR - DAILY REFRESH
REM   1. new @UnfairMarket posts (Wayback -> syndication -> extract)
REM   2. SPX daily OHLC (TradeStation)
REM   3. commit + push
REM Schedule this once a day AFTER the US close (e.g. 18:00 ET).
REM Wayback indexes T+1, so a post made today arrives tomorrow -- by design.
REM ============================================================
cd /d "%~dp0"

echo.
echo ================= %DATE% %TIME% =================

echo [1/3] Scanning for new posts...
py -3 archive\refresh_calendar.py
if errorlevel 1 echo   (post scan reported a problem - continuing to prices)

echo.
echo [2/3] Refreshing SPX daily OHLC...
py -3 archive\calendar\build_prices.py
if errorlevel 1 echo   (price bake reported a problem - continuing to commit)

echo.
echo [3/3] Committing...
REM Stage CONTENT only. _auto_state.json bumps last_run every single night, so
REM staging it up front would commit a timestamp diff daily and say nothing.
REM It rides along only when there is real content to commit.
git add archive/calendar/auto_entries.js archive/calendar/prices.js
git diff --cached --quiet && (echo   nothing changed today - no commit. && goto :done)
git add archive/_auto_state.json
git commit -q -m "calendar: daily refresh %DATE%"
git push -q origin main && echo   pushed.

:done
echo.
echo Done.
