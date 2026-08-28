"""
Chart Data Server
=================
Thin HTTP server that serves TradeStation bar data (with institutional columns)
to the live chart on demand. Only called when user clicks an alert.

Serves data in the same JSON format as backtest_spxu.py exports, so
live_chart.html (a copy of backtest_chart.html) can render it directly.

Usage:
  python chart_server.py              # runs on port 5555
  python chart_server.py --port 8888  # custom port

Endpoints:
  GET /chart?ticker=SPXU&timeframe=30m&sma=720&outfit=Speaker+House/56&bars=300
  GET /health
"""

import json
import sys
import os
import argparse
import statistics
import numpy as np
import pandas as pd
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ts_client import TradeStationClient
from config import SMA_OUTFITS
try:
    from bridge import bridge_outfit_to_horizon
    from adapters.opex import OPEXCalendar
    from adapters.gap_index import query_gap, gap_stats, cluster_months
    BRIDGE_AVAILABLE = True
except ImportError:
    BRIDGE_AVAILABLE = False
    bridge_outfit_to_horizon = None

# Symbol mapping (same as data_source.py)
SYMBOL_MAP = {
    "SPX":  "$SPX.X",
    "IXIC": "$NDX.X",
    "DJI":  "$DJX.X",
    "VIX":  "$VIX.X",
    "TNX":  "$TNX.X",
}

# Timeframe string -> (interval_minutes, unit)
TIMEFRAME_MAP = {
    "1m":  (1, "Minute"),
    "2m":  (2, "Minute"),
    "3m":  (3, "Minute"),
    "5m":  (5, "Minute"),
    "10m": (10, "Minute"),
    "15m": (15, "Minute"),
    "20m": (20, "Minute"),
    "30m": (30, "Minute"),
    "1h":  (60, "Minute"),
    "2h":  (120, "Minute"),
    "4h":  (240, "Minute"),
    "1d":  (1, "Daily"),
}

PENNY = 0.01
PROXIMITY_DOLLARS = 0.25

ts_client = TradeStationClient()


def compute_sma(closes, period):
    """Compute SMA for a given period over a list of closes."""
    if len(closes) < period:
        return [None] * len(closes)
    result = [None] * (period - 1)
    for i in range(period - 1, len(closes)):
        result.append(sum(closes[i - period + 1:i + 1]) / period)
    return result


def build_chart_data(df, ticker, timeframe, sma_period, outfit_name):
    """
    Build the JSON payload in the same format as backtest_spxu.py exports.
    """
    sma_period = int(sma_period)

    # --- Candles ---
    candles = []
    for ts_idx, row in df.iterrows():
        candles.append({
            "time": ts_idx.isoformat(),
            "time_et": ts_idx.strftime("%H:%M") if hasattr(ts_idx, "strftime") else "",
            "open": round(float(row["Open"]), 2),
            "high": round(float(row["High"]), 2),
            "low": round(float(row["Low"]), 2),
            "close": round(float(row["Close"]), 2),
            "volume": int(row.get("Volume", 0)),
            "up_volume": int(row.get("UpVolume", 0)),
            "down_volume": int(row.get("DownVolume", 0)),
            "up_ticks": int(row.get("UpTicks", 0)),
            "down_ticks": int(row.get("DownTicks", 0)),
            "total_ticks": int(row.get("TotalTicks", 0)),
        })

    closes = [c["close"] for c in candles]

    # --- Determine outfit periods ---
    outfit_periods = SMA_OUTFITS.get(outfit_name, [])
    if not outfit_periods:
        # Fallback: find outfit containing the alert SMA period
        for name, periods in SMA_OUTFITS.items():
            if sma_period in periods:
                outfit_name = name
                outfit_periods = periods
                break
    if not outfit_periods:
        outfit_periods = [sma_period]

    # --- Compute SMA lines for the outfit ---
    sma_lines = {}
    sma_data = {}  # period -> list of values (for interaction detection)
    for period in outfit_periods:
        vals = compute_sma(closes, period)
        sma_data[period] = vals
        line_points = []
        for i, v in enumerate(vals):
            if v is not None:
                line_points.append({
                    "time": candles[i]["time"],
                    "value": round(v, 2),
                })
        if line_points:
            sma_lines[str(period)] = line_points

    # --- Penny interactions (price == SMA to the penny) ---
    interactions = []
    for period, vals in sma_data.items():
        for i, sma_val in enumerate(vals):
            if sma_val is None:
                continue
            sma_rounded = round(sma_val, 2)
            c = candles[i]
            for field in ["open", "high", "low", "close"]:
                if round(c[field], 2) == sma_rounded:
                    interactions.append({
                        "time": c["time"],
                        "price": c[field],
                        "sma_period": period,
                        "ohlc_field": field.capitalize(),
                        "outfit": outfit_name,
                    })

    # --- Outfit rankings (count interactions per outfit) ---
    outfit_counts = {}
    for name, periods in SMA_OUTFITS.items():
        count = 0
        for period in periods:
            vals = compute_sma(closes, period) if period not in sma_data else sma_data[period]
            if period not in sma_data:
                sma_data[period] = vals
            for i, sma_val in enumerate(vals):
                if sma_val is None:
                    continue
                sma_rounded = round(sma_val, 2)
                c = candles[i]
                for field in ["open", "high", "low", "close"]:
                    if round(c[field], 2) == sma_rounded:
                        count += 1
        outfit_counts[name] = count

    ranked = sorted(outfit_counts.items(), key=lambda x: -x[1])
    rankings = [{"outfit": name, "hits": hits, "periods": SMA_OUTFITS[name]}
                for name, hits in ranked if hits > 0]

    # --- Bar analysis at target SMA level ---
    target_sma_vals = sma_data.get(sma_period, compute_sma(closes, sma_period))
    day_total_volume = sum(c["volume"] for c in candles) or 1
    day_avg_volume = day_total_volume / max(1, len(candles))

    # Compute day avg trade size
    per_bar_trades = []
    for c in candles:
        if c["total_ticks"] > 0:
            per_bar_trades.append(c["volume"] / c["total_ticks"])
    day_avg_trade = statistics.mean(per_bar_trades) if per_bar_trades else 0
    day_std_trade = statistics.stdev(per_bar_trades) if len(per_bar_trades) > 1 else day_avg_trade * 0.3

    baselines = {
        "day_avg_volume": round(day_avg_volume, 0),
        "day_total_volume": day_total_volume,
        "day_avg_trade_size": round(day_avg_trade, 1),
        "day_std_trade_size": round(day_std_trade, 1),
        "proximity_dollars": PROXIMITY_DOLLARS,
    }

    analysis = []
    for i, sma_val in enumerate(target_sma_vals):
        if sma_val is None:
            continue
        c = candles[i]
        sma_r = round(sma_val, 2)
        prices = [c["open"], c["high"], c["low"], c["close"]]
        min_dist = min(abs(p - sma_r) for p in prices)
        spans = c["low"] <= sma_r <= c["high"]

        if min_dist > PROXIMITY_DOLLARS and not spans:
            continue

        vol = c["volume"]
        up_vol = c["up_volume"]
        down_vol = c["down_volume"]
        ticks = c["total_ticks"]
        avg_trade = vol / max(1, ticks) if ticks > 0 else 0
        vol_ratio = vol / max(1, day_avg_volume)
        sigma = (avg_trade - day_avg_trade) / max(0.01, day_std_trade) if day_std_trade > 0 else 0
        net_delta = up_vol - down_vol
        delta_pct = net_delta / max(1, vol) * 100

        # Score: absorption
        absorption_score = 0.0
        absorbed = False
        if delta_pct < -3 and c["close"] >= sma_r - 0.05:
            sell_intensity = min(abs(delta_pct) / 15, 1.0)
            vol_factor = min(vol_ratio / 2.0, 1.0)
            absorption_score = sell_intensity * vol_factor
            absorbed = True

        # Score: rejection wick
        rejection_score = 0.0
        wick_below = c["low"] < sma_r
        closed_above = c["close"] > sma_r
        if wick_below and closed_above:
            wick_depth = sma_r - c["low"]
            body_recovery = c["close"] - sma_r
            rejection_score = min(1.0, (wick_depth / sma_r * 200) + (body_recovery / sma_r * 100))

        # Score: volume concentration
        vol_conc = vol / max(1, day_total_volume)
        concentration_score = 0.0
        if vol_conc > 0.10:
            concentration_score = 1.0
        elif vol_conc > 0.05:
            concentration_score = vol_conc / 0.10
        elif vol_conc > 0.03:
            concentration_score = vol_conc / 0.15

        # Score: trade size
        trade_score = 0.0
        if sigma >= 2.0: trade_score = 1.0
        elif sigma >= 1.5: trade_score = 0.7
        elif sigma >= 1.0: trade_score = 0.4
        elif sigma >= 0.5: trade_score = 0.15

        composite = (absorption_score * 0.35 + rejection_score * 0.30 +
                     concentration_score * 0.20 + trade_score * 0.15)

        entry = {
            "time": c["time"],
            "time_et": c["time_et"],
            "open": c["open"], "high": c["high"], "low": c["low"], "close": c["close"],
            f"ma{sma_period}": sma_r,
            "ma720": sma_r,  # backtest_chart.html expects this key
            "min_distance": round(min_dist, 4),
            "spans_ma": spans,
            "volume": vol,
            "vol_ratio": round(vol_ratio, 2),
            "avg_trade_size": round(avg_trade, 1),
            "trade_size_sigma": round(sigma, 2),
            "up_volume": up_vol,
            "down_volume": down_vol,
            "net_delta": net_delta,
            "delta_pct": round(delta_pct, 1),
            "up_ticks": c["up_ticks"],
            "down_ticks": c["down_ticks"],
            "ticks_total": ticks,
            "scores": {
                "absorption": {"score": round(absorption_score, 3), "absorbed": absorbed,
                               "delta_pct": round(delta_pct, 1), "vol_ratio": round(vol_ratio, 2)},
                "rejection_wick": {"score": round(rejection_score, 3), "wick_below": wick_below,
                                   "closed_above": closed_above},
                "volume_concentration": {"score": round(concentration_score, 3),
                                         "pct_of_day": round(vol_conc * 100, 2)},
                "trade_size": {"score": round(trade_score, 3), "sigma": round(sigma, 2),
                               "avg_trade": round(avg_trade, 1), "day_avg": round(day_avg_trade, 1)},
                "_composite": round(composite, 3),
                "_max": 1.0,
            },
        }
        analysis.append(entry)

    return {
        "symbol": ticker,
        "date": candles[-1]["time"][:10] if candles else "",
        "interval": timeframe,
        "timezone": "US/Eastern",
        "sma_period": sma_period,
        "outfit": outfit_name,
        "candles": candles,
        "sma_lines": sma_lines,
        "top_outfit": outfit_name,
        "interactions": interactions,
        "rankings": rankings,
        "ma720_analysis": analysis,
        "ma720_baselines": baselines,
    }


class ChartHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == '/chart':
            self.handle_chart(parse_qs(parsed.query))
        elif parsed.path == '/bridge':
            self.handle_bridge(parse_qs(parsed.query))
        elif parsed.path == '/gap':
            self.handle_gap(parse_qs(parsed.query))
        elif parsed.path == '/opex':
            self.handle_opex(parse_qs(parsed.query))
        elif parsed.path == '/health':
            self.send_json({"status": "ok", "bridge": BRIDGE_AVAILABLE})
        else:
            self.send_error_json(404, "Not found")

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def handle_chart(self, params):
        ticker = params.get('ticker', [None])[0]
        timeframe = params.get('timeframe', ['5m'])[0]
        sma_period = params.get('sma', ['200'])[0]
        outfit = params.get('outfit', [''])[0]
        bars_back = int(params.get('bars', ['300'])[0])

        if not ticker:
            self.send_error_json(400, "Missing 'ticker' parameter")
            return

        tf = TIMEFRAME_MAP.get(timeframe)
        if not tf:
            self.send_error_json(400, f"Unknown timeframe: {timeframe}")
            return

        interval, unit = tf
        ts_symbol = SYMBOL_MAP.get(ticker, ticker)
        bars_back = min(bars_back, 5000)

        print(f"  [chart] {ticker} ({ts_symbol}) {timeframe} SMA{sma_period} {outfit}")

        try:
            df = ts_client.get_bars(ts_symbol, interval, unit, barsback=bars_back)
        except Exception as e:
            self.send_error_json(500, f"TradeStation error: {e}")
            return

        if df.empty:
            self.send_json({"symbol": ticker, "candles": [], "error": "No data"})
            return

        data = build_chart_data(df, ticker, timeframe, sma_period, outfit)
        self.send_json(data)

    def handle_bridge(self, params):
        """GET /bridge?ticker=DOG&date=2026-03-05&outfit=56+Reversal&sma=28&target=IXIC
        Returns unified {ok, ...} from bridge_outfit_to_horizon. No Influx/TS needed for horizon-only.
        If bars are requested via &bars=1, caller should fetch /chart separately and post to /bridge POST.
        """
        if not BRIDGE_AVAILABLE:
            self.send_error_json(500, "Bridge not available — check adapters/")
            return
        ticker = params.get('ticker', [None])[0]
        date = params.get('date', [None])[0]
        outfit = params.get('outfit', [''])[0]
        sma = params.get('sma', [None])[0]
        target = params.get('target', ['IXIC'])[0]
        # date may be passed as 'time' from alert (_time) — accept both
        if not date:
            date = params.get('time', [None])[0]
        if date and 'T' in date:
            date = date.split('T')[0]
        if not ticker or not date:
            self.send_error_json(400, "Missing ticker or date (YYYY-MM-DD). Use /bridge?ticker=DOG&date=2026-03-05")
            return
        try:
            sma_int = int(sma) if sma and str(sma).isdigit() else None
        except:
            sma_int = None
        result = bridge_outfit_to_horizon(ticker, date, outfit or None, sma_int, accumulation_index=target)
        self.send_json(result)

    def handle_opex(self, params):
        """GET /opex?date=2026-03-05  → next OPEX events"""
        if not BRIDGE_AVAILABLE:
            self.send_error_json(500, "Bridge not available")
            return
        date = params.get('date', [None])[0]
        if not date:
            self.send_error_json(400, "Missing date")
            return
        if 'T' in date:
            date = date.split('T')[0]
        try:
            cal = OPEXCalendar()
            # next events after date
            import datetime
            d = datetime.date.fromisoformat(date)
            nxt = cal.next_opex(d)
            triple = cal.next_opex(d, kind="Triple Witching")
            horizon = cal.resolve_event_horizon(d)
            def _ser(e):
                if e is None: return None
                d = dict(e.__dict__); d["date"] = d["date"].isoformat() if hasattr(d["date"], "isoformat") else d["date"]
                return d
            self.send_json({"date": date, "next": _ser(nxt), "triple": _ser(triple), "horizon": horizon, "all_next_5": [_ser(e) for e in cal.events if e.date > d][:5]})
        except Exception as e:
            self.send_error_json(400, str(e))

    def handle_gap(self, params):
        """GET /gap?ticker=DOG&has_media=true&limit=20  → gap rows + horizon+inverse"""
        if not BRIDGE_AVAILABLE:
            self.send_error_json(500, "Bridge not available")
            return
        ticker = params.get('ticker', [None])[0]
        has_media = params.get('has_media', [None])[0]
        limit = int(params.get('limit', ['20'])[0])
        if has_media is not None:
            has_media = has_media.lower() in ('true','1','yes')
        else:
            has_media = None
        try:
            rows = query_gap(ticker=ticker, has_media=has_media, limit=limit)
            stats = gap_stats()
            self.send_json({"count": len(rows), "stats": stats, "rows": rows})
        except Exception as e:
            self.send_error_json(500, str(e))

    def send_json(self, data):
        body = json.dumps(data).encode()
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-Length', len(body))
        self.end_headers()
        self.wfile.write(body)

    def send_error_json(self, code, msg):
        body = json.dumps({"ok": False, "error": msg, "code": "ERROR"}).encode()
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-Length', len(body))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass  # Handled by print in handle_chart


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chart data server")
    parser.add_argument("--port", type=int, default=5555)
    args = parser.parse_args()

    print(f"Chart server running on http://localhost:{args.port}")
    print(f"  Endpoint: /chart?ticker=SPXU&timeframe=30m&sma=720&outfit=Speaker+House/56")
    print(f"  Health:   /health")
    server = HTTPServer(('127.0.0.1', args.port), ChartHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nChart server stopped.")
