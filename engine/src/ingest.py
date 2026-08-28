"""
Data Ingestion Pipeline: Data Source → InfluxDB
=================================================
Fetches OHLCV bars via the configured data source (TradeStation interim,
Lightspeed target per repo), computes outfit SMAs, detects exact penny
matches, and writes everything into InfluxDB.

Data source is controlled by DATA_SOURCE in .env:
  tradestation  (default, interim)
  lightspeed    (target, per repo)
  csv           (manual file import)

Buckets:
  market_data   — raw OHLCV bars
  penny_matches — exact $0.00 OHLC-to-SMA matches with LONG/SHORT classification

Usage:
  python ingest.py                   # full ingest (all tickers, all timeframes)
  python ingest.py --ticker SPXU     # single ticker
  python ingest.py --timeframe 30m   # single timeframe
  python ingest.py --ticker SPXU --timeframe 30m
  python ingest.py --dry-run         # compute without writing to InfluxDB
"""

import argparse
import time
import sys
import os
import numpy as np
import pandas as pd
from datetime import datetime, timezone

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

from config import (
    INFLUXDB_URL, INFLUXDB_TOKEN, INFLUXDB_ORG, INFLUXDB_BUCKET,
    TICKERS, TIMEFRAMES, SMA_OUTFITS, ALL_OUTFIT_SMAS,
    SMA_MIN, SMA_MAX,
)
from data_source import get_data_source


def load_env_config():
    """Load InfluxDB config from .env, falling back to config.py defaults."""
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    env = {}
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if '=' in line and not line.startswith('#'):
                    k, v = line.split('=', 1)
                    env[k.strip()] = v.strip()

    return {
        "url": env.get("INFLUXDB_URL", INFLUXDB_URL),
        "token": env.get("INFLUXDB_TOKEN", INFLUXDB_TOKEN),
        "org": env.get("INFLUXDB_ORG", INFLUXDB_ORG),
    }


def get_influx_client():
    """Create InfluxDB client from env/config."""
    cfg = load_env_config()
    return InfluxDBClient(url=cfg["url"], token=cfg["token"], org=cfg["org"], timeout=120_000)


def compute_smas(df, sma_periods):
    """
    Compute SMA values for given periods.
    Returns dict: {period: Series of SMA values}.
    Only computes SMAs where we have enough data.
    """
    smas = {}
    for p in sma_periods:
        if len(df) >= p:
            smas[p] = df['Close'].rolling(window=p).mean()
    return smas


def find_penny_matches(df, smas):
    """
    Find all exact penny matches ($0.00 difference) between OHLC and SMA values.

    Returns list of dicts:
      {timestamp, ohlc_field, ohlc_value, sma_period, sma_value,
       direction (LONG/SHORT), close}

    Direction:
      LONG = Close >= SMA at the match bar (price above or at SMA)
      SHORT = Close < SMA at the match bar (price below SMA)
    """
    matches = []
    ohlc_fields = ['Open', 'High', 'Low', 'Close']

    for period, sma_series in smas.items():
        sma_rounded = sma_series.round(2)

        for field in ohlc_fields:
            ohlc_rounded = df[field].round(2)
            match_mask = (ohlc_rounded == sma_rounded) & sma_rounded.notna()
            match_indices = df.index[match_mask]

            for ts in match_indices:
                close_val = round(float(df.loc[ts, 'Close']), 2)
                sma_val = round(float(sma_rounded.loc[ts]), 2)
                direction = "LONG" if close_val >= sma_val else "SHORT"

                matches.append({
                    'timestamp': ts,
                    'ohlc_field': field,
                    'ohlc_value': round(float(df.loc[ts, field]), 2),
                    'sma_period': period,
                    'sma_value': sma_val,
                    'direction': direction,
                    'close': close_val,
                })

    return matches


def classify_matches_by_outfit(matches):
    """
    For each match, determine which outfit(s) it belongs to.
    A match belongs to an outfit if its SMA period is in that outfit's period list.
    """
    classified = []
    for m in matches:
        period = m['sma_period']
        matched_outfits = []
        for outfit_name, outfit_periods in SMA_OUTFITS.items():
            if period in outfit_periods:
                matched_outfits.append(outfit_name)
        if not matched_outfits:
            matched_outfits = ["_unaffiliated"]
        for outfit in matched_outfits:
            classified.append({**m, 'outfit': outfit})
    return classified


def write_ohlcv_to_influx(write_api, df, ticker, timeframe_label):
    """Write raw OHLCV bars to market_data bucket in small batches."""
    BATCH = 1000
    points = []
    for ts, row in df.iterrows():
        p = (Point("ohlcv")
             .tag("ticker", ticker)
             .tag("timeframe", timeframe_label)
             .field("open", float(row['Open']))
             .field("high", float(row['High']))
             .field("low", float(row['Low']))
             .field("close", float(row['Close']))
             .field("volume", int(row.get('Volume', 0)))
             .time(ts, WritePrecision.S))
        points.append(p)
        if len(points) >= BATCH:
            write_api.write(bucket="market_data", record=points)
            points = []
    if points:
        write_api.write(bucket="market_data", record=points)


def write_penny_matches_to_influx(write_api, matches, ticker, timeframe_label):
    """Write penny match events to penny_matches bucket in small batches."""
    BATCH = 1000
    points = []
    for m in matches:
        p = (Point("penny_match")
             .tag("ticker", ticker)
             .tag("timeframe", timeframe_label)
             .tag("ohlc_field", m['ohlc_field'])
             .tag("direction", m['direction'])
             .tag("outfit", m['outfit'])
             .tag("sma_period", str(m['sma_period']))
             .field("ohlc_value", m['ohlc_value'])
             .field("sma_value", m['sma_value'])
             .field("close", m['close'])
             .field("sma_period_int", m['sma_period'])
             .time(m['timestamp'], WritePrecision.S))
        points.append(p)
        if len(points) >= BATCH:
            write_api.write(bucket="penny_matches", record=points)
            points = []
    if points:
        write_api.write(bucket="penny_matches", record=points)


def ingest_ticker_timeframe(source, write_api, ticker, tf, dry_run=False, bars_back=57600):
    """
    Ingest one ticker × one timeframe:
      1. Fetch bars from data source
      2. Compute all outfit SMAs
      3. Find penny matches
      4. Classify by outfit
      5. Write to InfluxDB

    Returns (bar_count, match_count).
    """
    label = tf['label']
    interval = tf['interval']

    df = source.get_bars(ticker, interval, bars_back=bars_back)
    if df.empty:
        return 0, 0

    # Compute SMAs for all outfit periods
    smas = compute_smas(df, ALL_OUTFIT_SMAS)

    # Find penny matches
    matches = find_penny_matches(df, smas)

    # Classify by outfit
    classified = classify_matches_by_outfit(matches)

    if dry_run:
        print(f"    {ticker}/{label}: {len(df)} bars, {len(matches)} raw matches, {len(classified)} classified")
        return len(df), len(classified)

    # Write to InfluxDB
    write_ohlcv_to_influx(write_api, df, ticker, label)
    write_penny_matches_to_influx(write_api, classified, ticker, label)

    return len(df), len(classified)


def run_ingest(ticker_filter=None, timeframe_filter=None, dry_run=False, quick=False, bars_back_override=None):
    """
    Run full ingestion pipeline.

    Args:
        ticker_filter: Optional single ticker to process
        timeframe_filter: Optional single timeframe label (e.g. "30m")
        dry_run: If True, compute but don't write to InfluxDB
        quick: If True, only pull last 2000 bars (weekly refresh ~12-15 min)
    """
    source = get_data_source()
    source_name = type(source).__name__
    bars_back = bars_back_override if bars_back_override else (2000 if quick else 57600)

    if not dry_run:
        client = get_influx_client()
        write_api = client.write_api(write_options=SYNCHRONOUS)
    else:
        write_api = None

    tickers = [ticker_filter] if ticker_filter else TICKERS
    timeframes = TIMEFRAMES
    if timeframe_filter:
        timeframes = [tf for tf in TIMEFRAMES if tf['label'] == timeframe_filter]
        if not timeframes:
            print(f"Unknown timeframe: {timeframe_filter}")
            return

    total_bars = 0
    total_matches = 0
    total_combos = len(tickers) * len(timeframes)
    done = 0

    mode = "QUICK (2,000 bars/combo)" if quick else "FULL (57,600 bars/combo)"
    print(f"Data source: {source_name}")
    print(f"Mode: {mode}")
    print(f"Ingesting {len(tickers)} tickers × {len(timeframes)} timeframes = {total_combos} combos")
    print(f"Computing SMAs for {len(ALL_OUTFIT_SMAS)} outfit periods per combo")
    if dry_run:
        print("DRY RUN — no writes to InfluxDB")
    print()

    start = time.time()

    for ticker in tickers:
        print(f"  [{ticker}]")
        for tf in timeframes:
            done += 1
            try:
                bars, matches = ingest_ticker_timeframe(
                    source, write_api, ticker, tf, dry_run=dry_run, bars_back=bars_back
                )
                total_bars += bars
                total_matches += matches
                print(f"    {tf['label']}: {bars} bars, {matches} matches")
            except Exception as e:
                print(f"    {tf['label']}: ERROR — {e}")

            # Rate limit for API sources
            time.sleep(0.6)

        print()

    elapsed = time.time() - start
    print(f"Done in {elapsed:.0f}s")
    print(f"Total: {total_bars:,} bars, {total_matches:,} penny matches across {done} combos")

    if not dry_run:
        client.close()


def is_market_open():
    """Check if US market is open (0930-1600 EST, weekdays)."""
    from zoneinfo import ZoneInfo
    from datetime import datetime
    now = datetime.now(ZoneInfo("America/New_York"))
    if now.weekday() >= 5:
        return False
    mins = now.hour * 60 + now.minute
    return 570 <= mins <= 960  # 0930-1600


def run_live(ticker_filter=None, timeframe_filter=None, interval_sec=300):
    """
    Live mode: lightweight ingest every N seconds during market hours.
    Pulls 1100 bars/combo (enough for SMA 999 + buffer) to keep data fresh.
    Sleeps outside market hours, auto-resumes at open.
    """
    from datetime import datetime
    print("=" * 60)
    print("  SMA INGEST — LIVE MODE")
    print(f"  Interval: {interval_sec}s ({interval_sec // 60} min)")
    print(f"  Bars per combo: 1100 (SMA 999 + buffer)")
    print("  Runs during market hours, sleeps outside")
    print("=" * 60)

    while True:
        if is_market_open():
            ts = datetime.now().strftime('%H:%M:%S')
            print(f"\n[{ts}] Live ingest cycle starting...")
            try:
                run_ingest(
                    ticker_filter=ticker_filter,
                    timeframe_filter=timeframe_filter,
                    dry_run=False,
                    quick=False,
                    bars_back_override=1100,
                )
            except Exception as e:
                print(f"  ERROR: {e}")
            print(f"  [{datetime.now().strftime('%H:%M:%S')}] Cycle done. Next in {interval_sec}s.")
        else:
            ts = datetime.now().strftime('%H:%M:%S')
            print(f"  [{ts}] Market closed. Waiting...")
        time.sleep(interval_sec)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest market data into InfluxDB")
    parser.add_argument("--ticker", help="Single ticker to process")
    parser.add_argument("--timeframe", help="Single timeframe label (e.g. 30m)")
    parser.add_argument("--dry-run", action="store_true", help="Compute but don't write to InfluxDB")
    parser.add_argument("--quick", action="store_true", help="Weekly refresh: 2,000 bars/combo (~12-15 min)")
    parser.add_argument("--live", action="store_true", help="Continuous ingest every 5 min during market hours")
    parser.add_argument("--live-interval", type=int, default=300, help="Live mode interval in seconds (default: 300)")
    args = parser.parse_args()

    if args.live:
        run_live(
            ticker_filter=args.ticker,
            timeframe_filter=args.timeframe,
            interval_sec=args.live_interval,
        )
    else:
        run_ingest(
            ticker_filter=args.ticker,
            timeframe_filter=args.timeframe,
            dry_run=args.dry_run,
            quick=args.quick,
        )
