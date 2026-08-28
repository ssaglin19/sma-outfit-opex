"""
SMA Scoring Engine
===================
Queries penny_matches from InfluxDB and produces:
  1. Outfit Ranking — TOTAL / LONG / SHORT / L-S per outfit
  2. Ticker Ranking — TOTAL / LONG / SHORT / L-S per ticker + dominant outfit
  3. System Status — S&P / NASDAQ / Dow positive/negative

Also computes per-row:
  - SLOPE (Rising/Falling) — SMA direction over recent bars
  - STRUCT_BIAS (Bullish/Bearish/Neutral) — based on system status
  - KEY_SMAS — which SMAs in the outfit had matches
  - PRICE_POS (Above/Below/Crossed) — current price vs key SMA
  - BIAS — combined assessment

Usage:
  python scorer.py                    # full scoring, prints tables
  python scorer.py --json             # output as JSON
  python scorer.py --lookback 14      # last 14 days (default)
  python scorer.py --ticker SPXU      # score single ticker
"""

import argparse
import json
import sys
import os
import time
import numpy as np
import pandas as pd
from datetime import datetime, timezone, timedelta

from influxdb_client import InfluxDBClient
from config import (
    INFLUXDB_URL, INFLUXDB_TOKEN, INFLUXDB_ORG,
    SMA_OUTFITS, SYSTEMS, TICKERS, TIMEFRAMES,
)


def load_env_config():
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
    cfg = load_env_config()
    return InfluxDBClient(url=cfg["url"], token=cfg["token"], org=cfg["org"], timeout=120_000)


def query_penny_matches(client, lookback_days=14, ticker=None):
    """
    Query all penny matches from the last N days.
    Returns a list of dicts with: ticker, timeframe, outfit, direction, sma_period, timestamp, etc.
    """
    query_api = client.query_api()

    flux = f'''
    from(bucket: "penny_matches")
      |> range(start: -{lookback_days}d)
      |> filter(fn: (r) => r._measurement == "penny_match")
    '''
    if ticker:
        flux += f'  |> filter(fn: (r) => r.ticker == "{ticker}")\n'

    flux += '''
      |> pivot(rowKey: ["_time"], columnKey: ["_field"], valueColumn: "_value")
    '''

    tables = query_api.query(flux)

    records = []
    for table in tables:
        for row in table.records:
            records.append({
                'timestamp': row.get_time(),
                'ticker': row.values.get('ticker', ''),
                'timeframe': row.values.get('timeframe', ''),
                'outfit': row.values.get('outfit', ''),
                'direction': row.values.get('direction', ''),
                'sma_period': row.values.get('sma_period', ''),
                'ohlc_field': row.values.get('ohlc_field', ''),
                'ohlc_value': row.values.get('ohlc_value', 0),
                'sma_value': row.values.get('sma_value', 0),
                'close': row.values.get('close', 0),
            })

    return records


def score_by_outfit(matches):
    """
    Aggregate matches by outfit.
    Returns sorted list of dicts: outfit, total, long, short, l_minus_s
    """
    outfit_scores = {}
    for m in matches:
        outfit = m['outfit']
        direction = m['direction']
        if outfit not in outfit_scores:
            outfit_scores[outfit] = {'outfit': outfit, 'total': 0, 'long': 0, 'short': 0}
        outfit_scores[outfit]['total'] += 1
        if direction == 'LONG':
            outfit_scores[outfit]['long'] += 1
        else:
            outfit_scores[outfit]['short'] += 1

    results = []
    for o in outfit_scores.values():
        o['l_minus_s'] = o['long'] - o['short']
        results.append(o)

    results.sort(key=lambda x: x['total'], reverse=True)
    return results


def score_by_ticker(matches):
    """
    Aggregate matches by ticker.
    Returns sorted list: ticker, total, long, short, l_minus_s, dominant_outfit
    """
    ticker_scores = {}
    ticker_outfit_counts = {}

    for m in matches:
        ticker = m['ticker']
        direction = m['direction']
        outfit = m['outfit']

        if ticker not in ticker_scores:
            ticker_scores[ticker] = {'ticker': ticker, 'total': 0, 'long': 0, 'short': 0}
            ticker_outfit_counts[ticker] = {}

        ticker_scores[ticker]['total'] += 1
        if direction == 'LONG':
            ticker_scores[ticker]['long'] += 1
        else:
            ticker_scores[ticker]['short'] += 1

        ticker_outfit_counts[ticker][outfit] = ticker_outfit_counts[ticker].get(outfit, 0) + 1

    results = []
    for t in ticker_scores.values():
        t['l_minus_s'] = t['long'] - t['short']
        # Find dominant outfit for this ticker
        ticker = t['ticker']
        if ticker in ticker_outfit_counts and ticker_outfit_counts[ticker]:
            dom = max(ticker_outfit_counts[ticker].items(), key=lambda x: x[1])
            t['dominant_outfit'] = dom[0]
            t['dominant_outfit_count'] = dom[1]
        else:
            t['dominant_outfit'] = 'N/A'
            t['dominant_outfit_count'] = 0
        results.append(t)

    results.sort(key=lambda x: x['total'], reverse=True)
    return results


def query_latest_bars(client, ticker, timeframe, limit=1000):
    """
    Query the most recent OHLCV bars for a ticker/timeframe from market_data.
    Returns a DataFrame with Open, High, Low, Close columns, sorted by time.
    """
    query_api = client.query_api()
    flux = f'''
    from(bucket: "market_data")
      |> range(start: -90d)
      |> filter(fn: (r) => r._measurement == "ohlcv")
      |> filter(fn: (r) => r.ticker == "{ticker}")
      |> filter(fn: (r) => r.timeframe == "{timeframe}")
      |> pivot(rowKey: ["_time"], columnKey: ["_field"], valueColumn: "_value")
      |> sort(columns: ["_time"])
      |> tail(n: {limit})
    '''
    tables = query_api.query(flux)
    rows = []
    for table in tables:
        for row in table.records:
            rows.append({
                'timestamp': row.get_time(),
                'Open': row.values.get('open', 0),
                'High': row.values.get('high', 0),
                'Low': row.values.get('low', 0),
                'Close': row.values.get('close', 0),
            })
    if not rows:
        return pd.DataFrame()
    df = pd.DataFrame(rows)
    df.set_index('timestamp', inplace=True)
    df.sort_index(inplace=True)
    return df


def compute_sma(df, period):
    """Compute SMA of Close for given period. Returns latest value or None."""
    if len(df) < period:
        return None
    return round(float(df['Close'].rolling(window=period).mean().iloc[-1]), 2)


def get_vix_level(client):
    """
    Get latest VIX close from market_data.
    VIX > 20 = high volatility regime.
    """
    # Try multiple timeframes in case some weren't ingested
    for tf in ["30m", "1h", "15m", "5m"]:
        df = query_latest_bars(client, "VIX", tf, limit=10)
        if not df.empty:
            return round(float(df['Close'].iloc[-1]), 2)
    return None


def evaluate_single_system(client, name, config, high_vol):
    """
    Evaluate one system's positive/negative state.

    Normal: short SMA > long SMA = POSITIVE
    High volatility (VIX > 20): price vs long SMA
      - price > long SMA = POSITIVE
      - price < long SMA = NEGATIVE

    Key levels: MA200 (SPX), MA250 (IXIC), MA900 (DJI)
    """
    symbol = config["symbol"]
    # Map TradeStation symbols back to ticker names used in InfluxDB
    influx_ticker_map = {
        "$SPX.X": "SPX",
        "$NDX.X": "IXIC",
        "$DJX.X": "DJI",
    }
    influx_ticker = influx_ticker_map.get(symbol, symbol)

    # Use first timeframe defined for this system
    timeframe = config["timeframes"][0]
    smas = config["smas"]

    # Need enough bars for the largest SMA in this system
    max_sma = max(smas)
    df = query_latest_bars(client, influx_ticker, timeframe, limit=max_sma + 50)

    if df.empty:
        return {"status": "unknown", "detail": f"No data for {influx_ticker}/{timeframe}"}

    # Determine short/long SMA pair for positive/negative rule
    # S&P: MA10 vs MA50, NASDAQ: MA20 vs MA100, Dow: MA90 vs MA300
    if name == "S&P 500":
        short_p, long_p, key_p = 10, 50, 200
    elif name == "NASDAQ":
        short_p, long_p, key_p = 20, 100, 250
    elif name == "Dow Jones":
        short_p, long_p, key_p = 90, 300, 900
    else:
        return {"status": "unknown", "detail": f"Unknown system: {name}"}

    short_val = compute_sma(df, short_p)
    long_val = compute_sma(df, long_p)
    key_val = compute_sma(df, key_p)

    if short_val is None or long_val is None:
        return {"status": "unknown", "detail": f"Not enough bars for SMA{long_p} ({len(df)} bars)"}

    # Latest price (OHLC4 per dashboard logic)
    last = df.iloc[-1]
    price = round((float(last['Open']) + float(last['High']) +
                    float(last['Low']) + float(last['Close'])) / 4, 2)

    if high_vol:
        # Volatility regime: price vs long SMA
        state = "POSITIVE" if price > long_val else "NEGATIVE"
        method = "VOL REGIME"
        detail = f"OHLC4 {price} {'>' if state == 'POSITIVE' else '<'} SMA{long_p} {long_val}"
    else:
        # Normal regime: short SMA vs long SMA
        state = "POSITIVE" if short_val > long_val else "NEGATIVE"
        method = "NORMAL"
        detail = f"SMA{short_p} {short_val} {'>' if state == 'POSITIVE' else '<'} SMA{long_p} {long_val}"

    spread_pct = round(((short_val - long_val) / long_val) * 100, 3)

    # Key level proximity
    key_detail = None
    if key_val is not None:
        distance = abs(price - key_val)
        if distance <= 0.05:  # within 5 cents
            key_detail = f"AT KEY LEVEL SMA{key_p} {key_val} (price {price})"

    return {
        "status": state,
        "method": method,
        "detail": detail,
        "spread_pct": spread_pct,
        "short_sma": f"SMA{short_p}={short_val}",
        "long_sma": f"SMA{long_p}={long_val}",
        "key_sma": f"SMA{key_p}={key_val}" if key_val else None,
        "key_alert": key_detail,
        "price": price,
        "ticker": influx_ticker,
        "timeframe": timeframe,
    }


def get_system_status(client):
    """
    Evaluate all three systems' positive/negative state.
    Uses VIX level to determine volatility regime (VIX > 20 = high vol).

    Ported from sma_alert_engine.py evaluate_system_state().
    """
    # Get VIX level
    vix = get_vix_level(client)
    high_vol = vix is not None and vix > 20

    results = {}
    for name, config in SYSTEMS.items():
        results[name] = evaluate_single_system(client, name, config, high_vol)

    # Add VIX info
    results["_vix"] = {
        "level": vix,
        "regime": "HIGH VOLATILITY" if high_vol else "NORMAL",
        "threshold": 20,
    }

    return results


def score_composite(matches, lookback_days=14):
    """
    Composite hashmap scoring engine.

    Each penny match is keyed by: ticker + timeframe + outfit + sma_period + ohlc_field
    This is the unique fingerprint of a specific SMA interaction.

    For each unique combo, we compute:
      - hit_count: raw frequency of penny matches
      - long_count / short_count: directional breakdown
      - precision: how tight the matches are (avg absolute difference between ohlc and sma)
      - recency_score: exponential decay — recent hits weighted more than old ones
      - time_at_level: how many distinct bars touched this exact SMA (unique timestamps)
      - first_seen / last_seen: when this combo first and last fired
      - avg_gap_hours: average time between consecutive hits

    Ranking uses a composite score:
      composite = (hit_count * 0.3) + (recency_score * 0.3) + (time_at_level * 0.2) + (precision * 0.2)

    All sub-scores are normalized 0-100 before combining.
    """
    from collections import defaultdict
    import math

    now = datetime.now(timezone.utc)
    halflife_days = lookback_days / 3  # recency decay halflife

    # Build the hashmap: composite key -> list of match records
    combos = defaultdict(list)
    for m in matches:
        key = (
            m['ticker'],
            m['timeframe'],
            m['outfit'],
            str(m['sma_period']),
            m.get('ohlc_field', 'close'),
        )
        combos[key].append(m)

    # Score each combo
    scored = []
    for key, hits in combos.items():
        ticker, timeframe, outfit, sma_period, ohlc_field = key
        n = len(hits)

        # Directional counts
        long_count = sum(1 for h in hits if h['direction'] == 'LONG')
        short_count = n - long_count

        # Precision: average |ohlc_value - sma_value| across hits
        diffs = []
        for h in hits:
            ohlc_v = float(h.get('ohlc_value', 0) or 0)
            sma_v = float(h.get('sma_value', 0) or 0)
            if ohlc_v > 0 and sma_v > 0:
                diffs.append(abs(ohlc_v - sma_v))
        avg_diff = sum(diffs) / len(diffs) if diffs else 999
        # Invert: smaller diff = higher precision (scale 0-100)
        # $0.00 diff = 100, $0.01 = ~90, $0.05 = ~50, $0.50+ = ~0
        precision = max(0, 100 * math.exp(-avg_diff * 50)) if avg_diff < 10 else 0

        # Recency: exponential decay weighted sum
        recency_raw = 0
        for h in hits:
            ts = h.get('timestamp')
            if ts:
                if hasattr(ts, 'timestamp'):
                    age_days = (now - ts).total_seconds() / 86400
                else:
                    age_days = lookback_days  # fallback
                weight = math.exp(-0.693 * age_days / halflife_days)  # ln(2) decay
                recency_raw += weight

        # Time at level: count of distinct bar timestamps
        unique_times = set()
        for h in hits:
            ts = h.get('timestamp')
            if ts:
                if hasattr(ts, 'strftime'):
                    unique_times.add(ts.strftime('%Y-%m-%d %H:%M'))
                else:
                    unique_times.add(str(ts))
        time_at_level = len(unique_times)

        # First/last seen
        timestamps = []
        for h in hits:
            ts = h.get('timestamp')
            if ts and hasattr(ts, 'timestamp'):
                timestamps.append(ts)
        timestamps.sort()
        first_seen = timestamps[0] if timestamps else None
        last_seen = timestamps[-1] if timestamps else None

        # Average gap between consecutive hits (hours)
        avg_gap_hours = None
        if len(timestamps) >= 2:
            gaps = [(timestamps[i+1] - timestamps[i]).total_seconds() / 3600
                    for i in range(len(timestamps) - 1)]
            avg_gap_hours = round(sum(gaps) / len(gaps), 1)

        scored.append({
            'ticker': ticker,
            'timeframe': timeframe,
            'outfit': outfit,
            'sma_period': sma_period,
            'ohlc_field': ohlc_field,
            'hit_count': n,
            'long_count': long_count,
            'short_count': short_count,
            'l_minus_s': long_count - short_count,
            'precision': round(precision, 1),
            'recency_raw': round(recency_raw, 2),
            'time_at_level': time_at_level,
            'first_seen': first_seen,
            'last_seen': last_seen,
            'avg_gap_hours': avg_gap_hours,
            'avg_diff': round(avg_diff, 4) if avg_diff < 999 else None,
        })

    if not scored:
        return []

    # Normalize each sub-score to 0-100 for composite ranking
    max_hits = max(s['hit_count'] for s in scored) or 1
    max_recency = max(s['recency_raw'] for s in scored) or 1
    max_tal = max(s['time_at_level'] for s in scored) or 1

    for s in scored:
        norm_hits = (s['hit_count'] / max_hits) * 100
        norm_recency = (s['recency_raw'] / max_recency) * 100
        norm_tal = (s['time_at_level'] / max_tal) * 100
        norm_precision = s['precision']  # already 0-100

        s['composite_score'] = round(
            norm_hits * 0.3 +
            norm_recency * 0.3 +
            norm_tal * 0.2 +
            norm_precision * 0.2,
            1
        )

    scored.sort(key=lambda x: x['composite_score'], reverse=True)
    return scored


def write_composite_to_influx(client, scored, lookback_days):
    """Write composite scores to the scoring bucket in InfluxDB."""
    from influxdb_client import Point
    from influxdb_client.client.write_api import SYNCHRONOUS

    write_api = client.write_api(write_options=SYNCHRONOUS)
    now = datetime.now(timezone.utc)

    points = []
    for s in scored:
        p = (Point("composite_score")
             .tag("ticker", s['ticker'])
             .tag("timeframe", s['timeframe'])
             .tag("outfit", s['outfit'])
             .tag("sma_period", s['sma_period'])
             .tag("ohlc_field", s['ohlc_field'])
             .field("hit_count", s['hit_count'])
             .field("long_count", s['long_count'])
             .field("short_count", s['short_count'])
             .field("l_minus_s", s['l_minus_s'])
             .field("precision", s['precision'])
             .field("recency_raw", s['recency_raw'])
             .field("time_at_level", s['time_at_level'])
             .field("composite_score", s['composite_score'])
             .time(now))
        if s['avg_gap_hours'] is not None:
            p = p.field("avg_gap_hours", s['avg_gap_hours'])
        if s['avg_diff'] is not None:
            p = p.field("avg_diff", s['avg_diff'])
        points.append(p)

    # Write in batches of 5000
    batch_size = 5000
    for i in range(0, len(points), batch_size):
        write_api.write(bucket="scoring", record=points[i:i+batch_size])

    print(f"  Wrote {len(points)} composite scores to 'scoring' bucket")


def print_composite_table(scored, top_n=40):
    """Print top composite-scored combos."""
    print("\n" + "=" * 130)
    print("COMPOSITE SCORING — TOP COMBOS (ticker + timeframe + outfit + sma + ohlc)")
    print("=" * 130)
    print(f"{'#':<4} {'TICKER':<8} {'TF':<5} {'SMA':<6} {'OHLC':<6} {'HITS':>5} {'L':>4} {'S':>4} "
          f"{'PREC':>5} {'RECNCY':>6} {'TAL':>4} {'SCORE':>6}  {'OUTFIT':<35}")
    print("-" * 130)
    for i, s in enumerate(scored[:top_n], 1):
        outfit_short = s['outfit'][:33] if len(s['outfit']) > 33 else s['outfit']
        print(f"{i:<4} {s['ticker']:<8} {s['timeframe']:<5} {s['sma_period']:<6} {s['ohlc_field']:<6} "
              f"{s['hit_count']:>5} {s['long_count']:>4} {s['short_count']:>4} "
              f"{s['precision']:>5.1f} {s['recency_raw']:>6.1f} {s['time_at_level']:>4} "
              f"{s['composite_score']:>6.1f}  {outfit_short:<35}")
    if len(scored) > top_n:
        print(f"  ... and {len(scored) - top_n} more combos")
    print()


def print_outfit_table(outfit_scores):
    """Print outfit ranking as a formatted table."""
    print("\n" + "=" * 80)
    print("OUTFIT RANKING")
    print("=" * 80)
    print(f"{'#':<4} {'Outfit':<45} {'TOTAL':>6} {'LONG':>6} {'SHORT':>6} {'L-S':>6}")
    print("-" * 80)
    for i, o in enumerate(outfit_scores, 1):
        print(f"{i:<4} {o['outfit']:<45} {o['total']:>6} {o['long']:>6} {o['short']:>6} {o['l_minus_s']:>6}")
    print()


def print_ticker_table(ticker_scores, top_n=30):
    """Print ticker ranking as a formatted table."""
    print("\n" + "=" * 100)
    print("TICKER RANKING")
    print("=" * 100)
    print(f"{'#':<4} {'Ticker':<10} {'TOTAL':>6} {'LONG':>6} {'SHORT':>6} {'L-S':>6}  {'DOM_OUTFIT':<40} {'CNT':>4}")
    print("-" * 100)
    for i, t in enumerate(ticker_scores[:top_n], 1):
        print(f"{i:<4} {t['ticker']:<10} {t['total']:>6} {t['long']:>6} {t['short']:>6} {t['l_minus_s']:>6}  {t['dominant_outfit']:<40} {t['dominant_outfit_count']:>4}")
    if len(ticker_scores) > top_n:
        print(f"  ... and {len(ticker_scores) - top_n} more tickers")
    print()


def run_scoring(lookback_days=14, ticker=None, output_json=False, composite_only=False, write_to_influx=False):
    """Run the full scoring pipeline."""
    client = get_influx_client()

    print(f"Querying penny matches (last {lookback_days} days)...")
    matches = query_penny_matches(client, lookback_days=lookback_days, ticker=ticker)
    print(f"Found {len(matches)} penny matches")

    if not matches:
        print("No matches found. Run ingest.py first.")
        client.close()
        return

    # Composite scoring (always runs now)
    print("Computing composite scores...")
    composite_scores = score_composite(matches, lookback_days=lookback_days)
    print(f"Scored {len(composite_scores)} unique combos")

    if write_to_influx:
        write_composite_to_influx(client, composite_scores, lookback_days)

    if composite_only:
        if output_json:
            result = {
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "lookback_days": lookback_days,
                "total_matches": len(matches),
                "unique_combos": len(composite_scores),
                "composite_ranking": composite_scores[:100],
            }
            print(json.dumps(result, indent=2, default=str))
        else:
            print_composite_table(composite_scores)
        client.close()
        return

    # Score by outfit
    outfit_scores = score_by_outfit(matches)

    # Score by ticker
    ticker_scores = score_by_ticker(matches)

    # System status
    system_status = get_system_status(client)

    client.close()

    if output_json:
        result = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "lookback_days": lookback_days,
            "total_matches": len(matches),
            "unique_combos": len(composite_scores),
            "outfit_ranking": outfit_scores,
            "ticker_ranking": ticker_scores,
            "composite_ranking": composite_scores[:100],
            "system_status": system_status,
        }
        print(json.dumps(result, indent=2, default=str))
    else:
        print_outfit_table(outfit_scores)
        print_ticker_table(ticker_scores)
        print_composite_table(composite_scores)

        print("SYSTEM STATUS")
        print("-" * 40)
        vix_info = system_status.get("_vix", {})
        if vix_info:
            print(f"  VIX: {vix_info.get('level', '?')} ({vix_info.get('regime', '?')})")
        for name, s in system_status.items():
            if name.startswith("_"):
                continue
            print(f"  {name}: {s['status']} — {s['detail']}")
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SMA Scoring Engine")
    parser.add_argument("--lookback", type=int, default=14, help="Lookback period in days")
    parser.add_argument("--ticker", help="Score single ticker only")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--composite", action="store_true", help="Show only composite scores")
    parser.add_argument("--write", action="store_true", help="Write composite scores to InfluxDB scoring bucket")
    args = parser.parse_args()

    run_scoring(
        lookback_days=args.lookback,
        ticker=args.ticker,
        output_json=args.json,
        composite_only=args.composite,
        write_to_influx=args.write,
    )
