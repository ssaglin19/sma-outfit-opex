"""
End-of-Day SMA Report Generator
=================================
Generates an HTML + JSON report of the day's SMA penny matches.
Only counts matches during institutional hours (0930-1600 EST).

Usage:
  python eod_report.py                    # generate report for today
  python eod_report.py --date 2026-03-18  # generate report for specific date
  python eod_report.py --lookback 7       # last 7 days
  python eod_report.py --output-dir ./reports
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone, timedelta

from influxdb_client import InfluxDBClient
from config import SMA_OUTFITS, SYSTEMS, TICKERS, TIMEFRAMES


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
    from config import INFLUXDB_URL, INFLUXDB_TOKEN, INFLUXDB_ORG
    return {
        "url": env.get("INFLUXDB_URL", INFLUXDB_URL),
        "token": env.get("INFLUXDB_TOKEN", INFLUXDB_TOKEN),
        "org": env.get("INFLUXDB_ORG", INFLUXDB_ORG),
    }


def get_influx_client():
    cfg = load_env_config()
    return InfluxDBClient(url=cfg["url"], token=cfg["token"], org=cfg["org"], timeout=120_000)


def query_penny_matches(client, lookback_days=1):
    """Query penny matches from InfluxDB for the given lookback period."""
    query_api = client.query_api()
    flux = f'''
    from(bucket: "penny_matches")
      |> range(start: -{lookback_days}d)
      |> filter(fn: (r) => r._measurement == "penny_match")
      |> pivot(rowKey: ["_time"], columnKey: ["_field"], valueColumn: "_value")
    '''
    tables = query_api.query(flux)
    records = []
    for table in tables:
        for row in table.records:
            ts = row.get_time()
            # Filter to institutional hours only (0930-1600 EST)
            # Convert UTC to EST (UTC-5, ignoring DST for simplicity — EST is UTC-5, EDT is UTC-4)
            est_hour = (ts.hour - 5) % 24 if ts.tzinfo else ts.hour
            est_min = ts.minute
            est_mins = est_hour * 60 + est_min
            # 0930 = 570 mins, 1600 = 960 mins
            if est_mins < 570 or est_mins > 960:
                continue
            records.append({
                'timestamp': ts.isoformat(),
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
    scores = {}
    for m in matches:
        outfit = m['outfit']
        direction = m['direction']
        if outfit not in scores:
            scores[outfit] = {'outfit': outfit, 'total': 0, 'long': 0, 'short': 0}
        scores[outfit]['total'] += 1
        if direction == 'LONG':
            scores[outfit]['long'] += 1
        else:
            scores[outfit]['short'] += 1
    results = []
    for o in scores.values():
        o['l_minus_s'] = o['long'] - o['short']
        results.append(o)
    results.sort(key=lambda x: x['total'], reverse=True)
    return results


def score_by_ticker(matches):
    scores = {}
    ticker_outfit_counts = {}
    for m in matches:
        ticker = m['ticker']
        direction = m['direction']
        outfit = m['outfit']
        if ticker not in scores:
            scores[ticker] = {'ticker': ticker, 'total': 0, 'long': 0, 'short': 0}
            ticker_outfit_counts[ticker] = {}
        scores[ticker]['total'] += 1
        if direction == 'LONG':
            scores[ticker]['long'] += 1
        else:
            scores[ticker]['short'] += 1
        ticker_outfit_counts[ticker][outfit] = ticker_outfit_counts[ticker].get(outfit, 0) + 1

    results = []
    for t in scores.values():
        t['l_minus_s'] = t['long'] - t['short']
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


def get_system_status(client):
    """Get system status (reuses scorer.py logic inline)."""
    from scorer import get_system_status as _get_status
    return _get_status(client)


def generate_json_report(matches, outfit_scores, ticker_scores, system_status, lookback_days):
    return {
        "report_type": "eod_sma_report",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "lookback_days": lookback_days,
        "institutional_hours_only": True,
        "total_matches": len(matches),
        "outfit_ranking": outfit_scores,
        "ticker_ranking": ticker_scores,
        "system_status": system_status,
    }


def generate_html_report(matches, outfit_scores, ticker_scores, system_status, lookback_days):
    total = len(matches)
    gen_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # VIX info
    vix_info = system_status.get('_vix', {})
    vix_level = vix_info.get('level', '?')
    vix_regime = vix_info.get('regime', '?')

    # System rows
    sys_rows = ''
    for name, s in system_status.items():
        if name.startswith('_'):
            continue
        status = s.get('status', 'unknown')
        detail = s.get('detail', '')
        color = '#22c55e' if status == 'POSITIVE' else '#ef4444' if status == 'NEGATIVE' else '#64748b'
        sys_rows += f'''
        <tr>
          <td style="font-weight:700;">{name}</td>
          <td style="color:{color}; font-weight:700;">{status}</td>
          <td style="color:#64748b; font-size:11px;">{detail}</td>
        </tr>'''

    # Outfit rows
    outfit_rows = ''
    for i, o in enumerate(outfit_scores, 1):
        ls_color = '#22c55e' if o['l_minus_s'] >= 0 else '#ef4444'
        outfit_rows += f'''
        <tr>
          <td style="color:#64748b;">{i}</td>
          <td style="font-weight:600;">{o['outfit']}</td>
          <td class="num">{o['total']:,}</td>
          <td class="num" style="color:#22c55e;">{o['long']:,}</td>
          <td class="num" style="color:#ef4444;">{o['short']:,}</td>
          <td class="num" style="color:{ls_color}; font-weight:700;">{'+' if o['l_minus_s'] >= 0 else ''}{o['l_minus_s']:,}</td>
        </tr>'''

    # Ticker rows (top 50)
    ticker_rows = ''
    for i, t in enumerate(ticker_scores[:50], 1):
        ls_color = '#22c55e' if t['l_minus_s'] >= 0 else '#ef4444'
        ticker_rows += f'''
        <tr>
          <td style="color:#64748b;">{i}</td>
          <td style="font-weight:600;">{t['ticker']}</td>
          <td class="num">{t['total']:,}</td>
          <td class="num" style="color:#22c55e;">{t['long']:,}</td>
          <td class="num" style="color:#ef4444;">{t['short']:,}</td>
          <td class="num" style="color:{ls_color}; font-weight:700;">{'+' if t['l_minus_s'] >= 0 else ''}{t['l_minus_s']:,}</td>
          <td style="color:#06b6d4; font-size:10px;">{t['dominant_outfit']}</td>
          <td class="num" style="color:#22c55e;">{t['dominant_outfit_count']:,}</td>
        </tr>'''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>SMA EOD Report — {gen_time}</title>
<style>
  :root {{ --bg:#0a0e17; --surface:#111827; --border:#1e2d45; --text:#e2e8f0; --muted:#64748b; }}
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ font-family:'SF Mono','Fira Code',monospace; background:var(--bg); color:var(--text); padding:24px; }}
  h1 {{ font-size:18px; letter-spacing:2px; text-transform:uppercase;
       background:linear-gradient(90deg,#06b6d4,#a855f7); -webkit-background-clip:text; -webkit-text-fill-color:transparent;
       margin-bottom:4px; }}
  .meta {{ font-size:11px; color:var(--muted); margin-bottom:20px; }}
  .section {{ background:var(--surface); border:1px solid var(--border); border-radius:6px; padding:16px; margin-bottom:16px; }}
  .section h2 {{ font-size:12px; color:var(--muted); text-transform:uppercase; letter-spacing:1px; margin-bottom:10px; }}
  table {{ width:100%; border-collapse:collapse; font-size:11px; }}
  th {{ padding:5px 6px; text-align:left; font-size:9px; text-transform:uppercase; letter-spacing:0.5px;
       color:var(--muted); border-bottom:1px solid var(--border); }}
  td {{ padding:4px 6px; border-bottom:1px solid rgba(30,45,69,0.4); }}
  .num {{ text-align:right; font-variant-numeric:tabular-nums; }}
  .summary-grid {{ display:grid; grid-template-columns:repeat(4,1fr); gap:12px; margin-bottom:16px; }}
  .summary-card {{ background:var(--surface); border:1px solid var(--border); border-radius:6px; padding:14px; text-align:center; }}
  .summary-card .value {{ font-size:24px; font-weight:700; color:#06b6d4; }}
  .summary-card .label {{ font-size:10px; color:var(--muted); margin-top:4px; }}
  .vix-info {{ display:inline-block; padding:4px 10px; border-radius:4px; font-weight:700; font-size:12px; }}
  .vix-high {{ background:rgba(239,68,68,0.2); color:#ef4444; }}
  .vix-elevated {{ background:rgba(245,158,11,0.2); color:#f59e0b; }}
  .vix-normal {{ background:rgba(34,197,94,0.1); color:#22c55e; }}
</style>
</head>
<body>
<h1>SMA Outfit Scoring — EOD Report</h1>
<div class="meta">
  Generated: {gen_time} &middot; Lookback: {lookback_days} day(s) &middot; Institutional Hours Only (0930-1600 EST)
</div>

<div class="summary-grid">
  <div class="summary-card">
    <div class="value">{total:,}</div>
    <div class="label">Total SMA Hits</div>
  </div>
  <div class="summary-card">
    <div class="value">{len(outfit_scores)}</div>
    <div class="label">Outfits Scored</div>
  </div>
  <div class="summary-card">
    <div class="value">{len(ticker_scores)}</div>
    <div class="label">Tickers Active</div>
  </div>
  <div class="summary-card">
    <div class="value"><span class="vix-info {'vix-high' if vix_level != '?' and float(str(vix_level)) >= 30 else 'vix-elevated' if vix_level != '?' and float(str(vix_level)) >= 20 else 'vix-normal'}">VIX {vix_level}</span></div>
    <div class="label">{vix_regime}</div>
  </div>
</div>

<div class="section">
  <h2>System Status</h2>
  <table>
    <thead><tr><th>System</th><th>Status</th><th>Detail</th></tr></thead>
    <tbody>{sys_rows}</tbody>
  </table>
</div>

<div class="section">
  <h2>Outfit Ranking — Top {len(outfit_scores)}</h2>
  <table>
    <thead><tr><th>#</th><th>Outfit</th><th class="num">Total</th><th class="num">Long</th><th class="num">Short</th><th class="num">L-S</th></tr></thead>
    <tbody>{outfit_rows}</tbody>
  </table>
</div>

<div class="section">
  <h2>Ticker Ranking — Top {min(50, len(ticker_scores))}</h2>
  <table>
    <thead><tr><th>#</th><th>Ticker</th><th class="num">Total</th><th class="num">Long</th><th class="num">Short</th><th class="num">L-S</th><th>Dom. Outfit</th><th class="num">Cnt</th></tr></thead>
    <tbody>{ticker_rows}</tbody>
  </table>
</div>

</body>
</html>'''
    return html


def run_eod_report(lookback_days=1, output_dir=None):
    """Generate EOD report as both HTML and JSON."""
    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reports')
    os.makedirs(output_dir, exist_ok=True)

    client = get_influx_client()

    print(f"Querying penny matches (last {lookback_days} day(s), institutional hours only)...")
    matches = query_penny_matches(client, lookback_days=lookback_days)
    print(f"Found {len(matches)} matches during institutional hours")

    if not matches:
        print("No matches found.")
        client.close()
        return

    outfit_scores = score_by_outfit(matches)
    ticker_scores = score_by_ticker(matches)
    system_status = get_system_status(client)
    client.close()

    # Generate filenames with date
    date_str = datetime.now().strftime('%Y-%m-%d')
    json_path = os.path.join(output_dir, f'eod_report_{date_str}.json')
    html_path = os.path.join(output_dir, f'eod_report_{date_str}.html')

    # JSON
    report_data = generate_json_report(matches, outfit_scores, ticker_scores, system_status, lookback_days)
    with open(json_path, 'w') as f:
        json.dump(report_data, f, indent=2, default=str)
    print(f"JSON report: {json_path}")

    # HTML
    html = generate_html_report(matches, outfit_scores, ticker_scores, system_status, lookback_days)
    with open(html_path, 'w') as f:
        f.write(html)
    print(f"HTML report: {html_path}")

    print(f"\nReport summary:")
    print(f"  Total SMA hits: {len(matches):,}")
    print(f"  Outfits scored: {len(outfit_scores)}")
    print(f"  Tickers active: {len(ticker_scores)}")
    print(f"  Top outfit: {outfit_scores[0]['outfit']} ({outfit_scores[0]['total']:,} hits)")
    print(f"  Top ticker: {ticker_scores[0]['ticker']} ({ticker_scores[0]['total']:,} hits)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate EOD SMA Report")
    parser.add_argument("--lookback", type=int, default=1, help="Lookback period in days (default: 1)")
    parser.add_argument("--output-dir", help="Output directory for reports")
    args = parser.parse_args()

    run_eod_report(
        lookback_days=args.lookback,
        output_dir=args.output_dir,
    )
