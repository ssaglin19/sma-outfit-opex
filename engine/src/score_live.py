"""
Live SMA Scorer — No InfluxDB Required
========================================
Fetches data via configured data source (TradeStation interim / Lightspeed target),
computes all outfit SMAs, finds penny matches, and outputs scoring tables.

Use this to validate scoring logic before InfluxDB is set up.

Usage:
  python score_live.py                         # all tickers, 30m only
  python score_live.py --ticker SPXU           # single ticker, all timeframes
  python score_live.py --timeframe 30m         # all tickers, single timeframe
  python score_live.py --ticker SPXU --timeframe 30m
  python score_live.py --quick                 # fast mode: fewer tickers, 30m only
"""

import argparse
import time
import sys
import json
import numpy as np
import pandas as pd
from datetime import datetime

from config import (
    TICKERS, TIMEFRAMES, SMA_OUTFITS, ALL_OUTFIT_SMAS,
)
from data_source import get_data_source


# Quick-test ticker subset
QUICK_TICKERS = [
    "SPY", "QQQ", "DIA", "SPXU", "TQQQ", "SQQQ",
    "SVIX", "UVXY", "SOXS", "SOXL", "NVDA", "TSLA",
    "AAPL", "MSFT", "META", "AMD", "BITO",
]


def compute_smas(df, periods):
    """Compute SMA values. Returns dict: {period: rounded Series}."""
    smas = {}
    for p in periods:
        if len(df) >= p:
            smas[p] = df['Close'].rolling(window=p).mean().round(2)
    return smas


def find_penny_matches(df, smas, ticker, tf_label):
    """
    Find exact penny matches ($0.00) between OHLC and SMA values.
    Returns list of match dicts.
    """
    matches = []
    ohlc_fields = ['Open', 'High', 'Low', 'Close']

    for period, sma_series in smas.items():
        for field in ohlc_fields:
            ohlc_rounded = df[field].round(2)
            match_mask = (ohlc_rounded == sma_series) & sma_series.notna()
            match_indices = df.index[match_mask]

            for ts in match_indices:
                close_val = round(float(df.loc[ts, 'Close']), 2)
                sma_val = round(float(sma_series.loc[ts]), 2)
                direction = "LONG" if close_val >= sma_val else "SHORT"

                matches.append({
                    'timestamp': ts,
                    'ticker': ticker,
                    'timeframe': tf_label,
                    'ohlc_field': field,
                    'ohlc_value': round(float(df.loc[ts, field]), 2),
                    'sma_period': period,
                    'sma_value': sma_val,
                    'direction': direction,
                    'close': close_val,
                })

    return matches


def classify_by_outfit(matches):
    """Tag each match with its outfit(s)."""
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


def score_outfits(classified):
    """Aggregate by outfit → TOTAL/LONG/SHORT/L-S."""
    scores = {}
    for m in classified:
        o = m['outfit']
        if o not in scores:
            scores[o] = {'outfit': o, 'total': 0, 'long': 0, 'short': 0}
        scores[o]['total'] += 1
        if m['direction'] == 'LONG':
            scores[o]['long'] += 1
        else:
            scores[o]['short'] += 1

    for s in scores.values():
        s['l_minus_s'] = s['long'] - s['short']

    return sorted(scores.values(), key=lambda x: x['total'], reverse=True)


def score_tickers(classified):
    """Aggregate by ticker → TOTAL/LONG/SHORT/L-S + dominant outfit."""
    scores = {}
    outfit_counts = {}

    for m in classified:
        t = m['ticker']
        if t not in scores:
            scores[t] = {'ticker': t, 'total': 0, 'long': 0, 'short': 0}
            outfit_counts[t] = {}
        scores[t]['total'] += 1
        if m['direction'] == 'LONG':
            scores[t]['long'] += 1
        else:
            scores[t]['short'] += 1
        o = m['outfit']
        outfit_counts[t][o] = outfit_counts[t].get(o, 0) + 1

    for t in scores.values():
        t['l_minus_s'] = t['long'] - t['short']
        ticker = t['ticker']
        if outfit_counts.get(ticker):
            dom = max(outfit_counts[ticker].items(), key=lambda x: x[1])
            t['dominant_outfit'] = dom[0]
            t['dom_count'] = dom[1]
        else:
            t['dominant_outfit'] = 'N/A'
            t['dom_count'] = 0

    return sorted(scores.values(), key=lambda x: x['total'], reverse=True)


def print_outfit_table(outfit_scores):
    print("\n" + "=" * 80)
    print("OUTFIT RANKING")
    print("=" * 80)
    print(f"{'#':<4} {'Outfit':<45} {'TOTAL':>6} {'LONG':>6} {'SHORT':>6} {'L-S':>6}")
    print("-" * 80)
    for i, o in enumerate(outfit_scores, 1):
        print(f"{i:<4} {o['outfit']:<45} {o['total']:>6} {o['long']:>6} {o['short']:>6} {o['l_minus_s']:>6}")


def print_ticker_table(ticker_scores, top_n=30):
    print("\n" + "=" * 100)
    print("TICKER RANKING")
    print("=" * 100)
    print(f"{'#':<4} {'Ticker':<10} {'TOTAL':>6} {'LONG':>6} {'SHORT':>6} {'L-S':>6}  {'DOM_OUTFIT':<40} {'CNT':>4}")
    print("-" * 100)
    for i, t in enumerate(ticker_scores[:top_n], 1):
        print(f"{i:<4} {t['ticker']:<10} {t['total']:>6} {t['long']:>6} {t['short']:>6} {t['l_minus_s']:>6}  {t['dominant_outfit']:<40} {t['dom_count']:>4}")
    if len(ticker_scores) > top_n:
        print(f"  ... and {len(ticker_scores) - top_n} more tickers")


def run(ticker_filter=None, timeframe_filter=None, quick=False, output_json=False):
    source = get_data_source()
    source_name = type(source).__name__

    tickers = QUICK_TICKERS if quick else TICKERS
    if ticker_filter:
        tickers = [ticker_filter]

    timeframes = TIMEFRAMES
    if timeframe_filter:
        timeframes = [tf for tf in TIMEFRAMES if tf['label'] == timeframe_filter]
    elif quick:
        timeframes = [tf for tf in TIMEFRAMES if tf['label'] == '30m']

    all_classified = []
    total_bars = 0
    combos = len(tickers) * len(timeframes)

    print(f"Data source: {source_name}")
    print(f"Scanning {len(tickers)} tickers × {len(timeframes)} timeframes = {combos} combos")
    print(f"Computing SMAs for {len(ALL_OUTFIT_SMAS)} outfit periods: {ALL_OUTFIT_SMAS[:5]}...{ALL_OUTFIT_SMAS[-3:]}")
    print()

    start = time.time()

    for ticker in tickers:
        for tf in timeframes:
            try:
                df = source.get_bars(ticker, tf['interval'], bars_back=57600)
                if df.empty:
                    print(f"  {ticker}/{tf['label']}: no data")
                    continue

                smas = compute_smas(df, ALL_OUTFIT_SMAS)
                matches = find_penny_matches(df, smas, ticker, tf['label'])
                classified = classify_by_outfit(matches)
                all_classified.extend(classified)
                total_bars += len(df)

                print(f"  {ticker}/{tf['label']}: {len(df)} bars, {len(matches)} raw matches, {len(classified)} classified")

            except Exception as e:
                print(f"  {ticker}/{tf['label']}: ERROR — {e}")

            time.sleep(0.6)  # rate limit

    elapsed = time.time() - start
    print(f"\nProcessed {total_bars:,} bars in {elapsed:.0f}s")
    print(f"Total classified matches: {len(all_classified):,}")

    if not all_classified:
        print("No matches found.")
        return

    outfit_scores = score_outfits(all_classified)
    ticker_scores = score_tickers(all_classified)

    if output_json:
        result = {
            "generated_at": datetime.now().isoformat(),
            "total_matches": len(all_classified),
            "total_bars": total_bars,
            "outfit_ranking": outfit_scores,
            "ticker_ranking": ticker_scores,
        }
        print(json.dumps(result, indent=2, default=str))
    else:
        print_outfit_table(outfit_scores)
        print_ticker_table(ticker_scores)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Live SMA Scorer (no InfluxDB)")
    parser.add_argument("--ticker", help="Single ticker")
    parser.add_argument("--timeframe", help="Single timeframe (e.g. 30m)")
    parser.add_argument("--quick", action="store_true", help="Quick mode: fewer tickers, 30m only")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    run(
        ticker_filter=args.ticker,
        timeframe_filter=args.timeframe,
        quick=args.quick,
        output_json=args.json,
    )
