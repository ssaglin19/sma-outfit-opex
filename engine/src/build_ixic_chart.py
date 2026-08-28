"""
Build a standalone HTML chart showing IXIC on the 56 Reversal outfit (MA28/55/111/221/442/884)
with buying activity at MA884.

Pulls 2H bars from InfluxDB market_data bucket, computes SMAs, detects penny matches,
scores institutional activity at MA884, and bakes everything into a self-contained HTML file.

Usage:
  python build_ixic_chart.py
"""
import os

import json
import statistics
from datetime import datetime
from influxdb_client import InfluxDBClient

# ── Config ────────────────────────────────────────
INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = os.environ.get("INFLUXDB_TOKEN", "")
INFLUX_ORG = "sma-alerts"
MARKET_BUCKET = "market_data"

TICKER = "IXIC"
TIMEFRAME = "2h"
SMA_PERIOD = 884  # Target SMA for institutional analysis
OUTFIT_NAME = "56 Reversal (28/55/111/221/442/884)"
OUTFIT_PERIODS = [28, 55, 111, 221, 442, 884]
BARS_BACK = 2000  # Need enough for SMA884
PROXIMITY = 0.25
PENNY = 0.01

# All 28 outfits for ranking
SMA_OUTFITS = {
    "S&P (10/50/200)": [10, 50, 200],
    "NAS (20/100/250)": [20, 100, 250],
    "DJI (30/60/90/300/600/900)": [30, 60, 90, 300, 600, 900],
    "AN (33/66/99/333/666/999)": [33, 66, 99, 333, 666, 999],
    "AN (11/44/88/111/444/888)": [11, 44, 88, 111, 444, 888],
    "AN (22/55/77/222/555/777)": [22, 55, 77, 222, 555, 777],
    "Waring's Problem (19/37/73/143/279/548)": [19, 37, 73, 143, 279, 548],
    "Base 2/NVDA (16/32/64/128/256/512)": [16, 32, 64, 128, 256, 512],
    "TSLA (27/53/105/210/420/840)": [27, 53, 105, 210, 420, 840],
    "Time/365 (23/46/91/183/365/730)": [23, 46, 91, 183, 365, 730],
    "Time/366 (23/46/92/183/366/732)": [23, 46, 92, 183, 366, 732],
    "Time/1440 (18/36/72/144/288/576)": [18, 36, 72, 144, 288, 576],
    "Resource Missing/404 (25/51/101/202/404/808)": [25, 51, 101, 202, 404, 808],
    "US President/45 (29/57/114/227/455/911)": [29, 57, 114, 227, 455, 911],
    "US President/46 (23/46/92/184/368/736)": [23, 46, 92, 184, 368, 736],
    "US President/47 (24/47/94/188/376/752)": [24, 47, 94, 188, 376, 752],
    "Speaker House/56 (28/56/112/224/448/896)": [28, 56, 112, 224, 448, 896],
    "WTC/911 (28/57/114/228/456/911)": [28, 57, 114, 228, 456, 911],
    "Russia 2000 (16/31/63/125/250/500)": [16, 31, 63, 125, 250, 500],
    "China Chair (28/56/112/224/448/976)": [28, 56, 112, 224, 448, 976],
    "France President (25/50/100/200/400/600)": [25, 50, 100, 200, 400, 600],
    "SVIX (26/52/106/211/422/844)": [26, 52, 106, 211, 422, 844],
    "Turkey President (24/48/96/192/384/768)": [24, 48, 96, 192, 384, 768],
    "Alphabet (25/50/100/200/400/800)": [25, 50, 100, 200, 400, 800],
    "Regression (27/54/108/216/432/864)": [27, 54, 108, 216, 432, 864],
    "56 Reversal (28/55/111/221/442/884)": [28, 55, 111, 221, 442, 884],
    "Tesla Cipher (39/78/156/311/622/944)": [39, 78, 156, 311, 622, 944],
    "Apple Cipher (31/61/122/244/446/668)": [31, 61, 122, 244, 446, 668],
}


def query_bars(client):
    """Pull IXIC 2H OHLCV bars from InfluxDB."""
    print(f"  Querying {TICKER} {TIMEFRAME} bars from InfluxDB (last {BARS_BACK} days)...")
    query = f'''
from(bucket: "{MARKET_BUCKET}")
  |> range(start: -365d)
  |> filter(fn: (r) => r._measurement == "ohlcv")
  |> filter(fn: (r) => r.ticker == "{TICKER}")
  |> filter(fn: (r) => r.timeframe == "{TIMEFRAME}")
  |> pivot(rowKey: ["_time"], columnKey: ["_field"], valueColumn: "_value")
  |> sort(columns: ["_time"], desc: false)
'''
    tables = client.query_api().query(query, org=INFLUX_ORG)
    rows = []
    for table in tables:
        for rec in table.records:
            vals = rec.values
            rows.append({
                "time": vals["_time"].isoformat(),
                "open": float(vals.get("open", 0)),
                "high": float(vals.get("high", 0)),
                "low": float(vals.get("low", 0)),
                "close": float(vals.get("close", 0)),
                "volume": int(vals.get("volume", 0)),
                "up_volume": int(vals.get("up_volume", 0) or 0),
                "down_volume": int(vals.get("down_volume", 0) or 0),
                "up_ticks": int(vals.get("up_ticks", 0) or 0),
                "down_ticks": int(vals.get("down_ticks", 0) or 0),
                "total_ticks": int(vals.get("total_ticks", 0) or 0),
            })
    print(f"  Got {len(rows)} bars")
    return rows


def compute_sma(closes, period):
    if len(closes) < period:
        return [None] * len(closes)
    result = [None] * (period - 1)
    for i in range(period - 1, len(closes)):
        result.append(sum(closes[i - period + 1:i + 1]) / period)
    return result


def build_chart_data(all_candles, target_date="2026-03-20"):
    """
    Compute SMAs using ALL bars (need 884+ for MA884),
    but only display bars from target_date on the chart.
    """
    from dateutil import parser as dp

    # Add time_et field to all candles
    for c in all_candles:
        try:
            dt = dp.isoparse(c["time"])
            c["time_et"] = dt.strftime("%H:%M")
            c["date_str"] = dt.strftime("%Y-%m-%d")
        except:
            c["time_et"] = c["time"][-8:-3] if len(c["time"]) > 8 else ""
            c["date_str"] = c["time"][:10]

    closes = [c["close"] for c in all_candles]

    # ── Compute SMAs over ALL bars ──
    sma_data = {}
    for period in OUTFIT_PERIODS:
        sma_data[period] = compute_sma(closes, period)

    # ── Find the last 24 bars up to and including target_date ──
    date_indices = [i for i, c in enumerate(all_candles) if c["date_str"] <= target_date]
    if not date_indices:
        print(f"  WARNING: No bars found up to {target_date}")
        print(f"  Available dates: {sorted(set(c['date_str'] for c in all_candles))[-10:]}")
        return None

    # Take last 24 bars
    day_indices = date_indices[-24:]
    print(f"  Chart bars: {len(day_indices)} (last 24 bars ending {target_date})")

    # The chart candles are ONLY the target date bars
    chart_candles = [all_candles[i] for i in day_indices]

    # ── SMA lines for outfit (only for chart bars) ──
    sma_lines = {}
    for period in OUTFIT_PERIODS:
        line_points = []
        for i in day_indices:
            v = sma_data[period][i]
            if v is not None:
                line_points.append({"time": all_candles[i]["time"], "value": round(v, 2)})
        if line_points:
            sma_lines[str(period)] = line_points

    # ── Point interactions (for IXIC: whole dollar match, not penny) ──
    # IXIC protocol is "cut on point break" — match to nearest whole dollar
    interactions = []
    for period, vals in sma_data.items():
        for i in day_indices:
            sma_val = vals[i]
            if sma_val is None:
                continue
            sma_rounded = round(sma_val, 2)
            sma_dollar = round(sma_val, 0)  # Whole dollar for point-level
            c = all_candles[i]
            for field in ["open", "high", "low", "close"]:
                price = round(c[field], 2)
                # Point break: price matches SMA to the nearest whole dollar
                if abs(price - sma_rounded) <= 1.0:
                    interactions.append({
                        "time": c["time"],
                        "price": c[field],
                        "sma_period": period,
                        "ohlc_field": field.capitalize(),
                        "outfit": OUTFIT_NAME,
                    })

    # ── Outfit rankings (point hits per outfit on this day) ──
    all_sma_cache = dict(sma_data)
    outfit_counts = {}
    for name, periods in SMA_OUTFITS.items():
        count = 0
        for period in periods:
            if period not in all_sma_cache:
                all_sma_cache[period] = compute_sma(closes, period)
            vals = all_sma_cache[period]
            for i in day_indices:
                sma_val = vals[i]
                if sma_val is None:
                    continue
                c = all_candles[i]
                for field in ["open", "high", "low", "close"]:
                    if abs(round(c[field], 2) - round(sma_val, 2)) <= 1.0:
                        count += 1
        outfit_counts[name] = count

    ranked = sorted(outfit_counts.items(), key=lambda x: -x[1])
    rankings = [{"outfit": name, "hits": hits, "periods": SMA_OUTFITS[name]}
                for name, hits in ranked if hits > 0]

    # ── MA884 institutional analysis ──
    # For IXIC at ~24000, use wider proximity ($50) to catch activity near the SMA
    proximity = 50.0  # $50 proximity for index-level prices
    target_vals = sma_data.get(SMA_PERIOD, compute_sma(closes, SMA_PERIOD))

    day_total_volume = sum(all_candles[i]["volume"] for i in day_indices) or 1
    day_avg_volume = day_total_volume / max(1, len(day_indices))

    per_bar_trades = []
    for i in day_indices:
        c = all_candles[i]
        if c["total_ticks"] > 0:
            per_bar_trades.append(c["volume"] / c["total_ticks"])
    day_avg_trade = statistics.mean(per_bar_trades) if per_bar_trades else 0
    day_std_trade = statistics.stdev(per_bar_trades) if len(per_bar_trades) > 1 else day_avg_trade * 0.3

    baselines = {
        "day_avg_volume": round(day_avg_volume, 0),
        "day_total_volume": day_total_volume,
        "day_avg_trade_size": round(day_avg_trade, 1),
        "day_std_trade_size": round(day_std_trade, 1),
        "proximity_dollars": proximity,
    }

    analysis = []
    for i in day_indices:
        sma_val = target_vals[i]
        if sma_val is None:
            continue
        c = all_candles[i]
        sma_r = round(sma_val, 2)
        prices = [c["open"], c["high"], c["low"], c["close"]]
        min_dist = min(abs(p - sma_r) for p in prices)
        spans = c["low"] <= sma_r <= c["high"]

        if min_dist > proximity and not spans:
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

        # Absorption score
        absorption_score = 0.0
        absorbed = False
        if delta_pct < -3 and c["close"] >= sma_r - proximity:
            sell_intensity = min(abs(delta_pct) / 15, 1.0)
            vol_factor = min(vol_ratio / 2.0, 1.0)
            absorption_score = sell_intensity * vol_factor
            absorbed = True

        # Rejection wick
        rejection_score = 0.0
        wick_below = c["low"] < sma_r
        closed_above = c["close"] > sma_r
        if wick_below and closed_above:
            wick_depth = sma_r - c["low"]
            body_recovery = c["close"] - sma_r
            rejection_score = min(1.0, (wick_depth / sma_r * 200) + (body_recovery / sma_r * 100))

        # Volume concentration
        vol_conc = vol / max(1, day_total_volume)
        concentration_score = 0.0
        if vol_conc > 0.10:
            concentration_score = 1.0
        elif vol_conc > 0.05:
            concentration_score = vol_conc / 0.10
        elif vol_conc > 0.03:
            concentration_score = vol_conc / 0.15

        # Trade size
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
            f"ma{SMA_PERIOD}": sma_r,
            "ma720": sma_r,
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
        "symbol": TICKER,
        "date": target_date,
        "interval": TIMEFRAME,
        "timezone": "US/Eastern",
        "sma_period": SMA_PERIOD,
        "outfit": OUTFIT_NAME,
        "candles": chart_candles,
        "sma_lines": sma_lines,
        "top_outfit": OUTFIT_NAME,
        "interactions": interactions,
        "rankings": rankings,
        "ma720_analysis": analysis,
        "ma720_baselines": baselines,
    }


def build_html(data):
    """Read live_chart.html template and bake data directly into it."""
    # Read the live_chart.html template
    with open("live_chart.html", "r", encoding="utf-8") as f:
        html = f.read()

    # Replace the loadData function with inline data
    data_json = json.dumps(data, indent=None)

    # We'll replace the entire loadData function with one that uses inline data
    new_script = f"""
const SMA_COLORS = ['#ff6b6b','#ffa06b','#ffd700','#6bffa0','#6bc5ff','#c06bff'];
let DATA = null;
const CHART_PAD = {{ top: 20, right: 70, bottom: 28, left: 12 }};
let chartW, chartH, plotW, plotH, priceMin, priceMax, priceRange, barWidth, barGap;
const canvas = document.getElementById('chart');
const ctx = canvas.getContext('2d');

function parseETTime(iso) {{
    const m = iso.match(/T(\\d{{2}}):(\\d{{2}})/);
    return m ? `${{m[1]}}:${{m[2]}}` : iso;
}}

async function loadData() {{
    // INLINE DATA — no chart_server needed
    DATA = {data_json};

    document.getElementById('headerTitle').innerHTML =
        '{TICKER} — <span>{OUTFIT_NAME} MA{SMA_PERIOD}</span> — PRECISION_BUY_ALGORITHM [{TIMEFRAME}]';
    document.getElementById('headerMeta').textContent =
        `${{DATA.date}} | {TIMEFRAME} | ${{DATA.candles.length}} bars | US/Eastern`;
    document.title = '{TICKER} MA{SMA_PERIOD} {TIMEFRAME} — 56 Reversal';

    if (!DATA.candles || DATA.candles.length === 0) {{
        document.querySelector('.chart-area').innerHTML =
            '<div class="no-data"><div>No bar data found for {TICKER} {TIMEFRAME}</div></div>';
        return;
    }}
    init();
}}
"""

    # Simple string find/replace instead of regex to avoid escape issues
    start_marker = "<script>\nconst SMA_COLORS"
    # Find the start of the script block
    idx = html.find(start_marker)
    if idx == -1:
        start_marker = "<script>\r\nconst SMA_COLORS"
        idx = html.find(start_marker)
    if idx == -1:
        raise ValueError("Could not find script block in live_chart.html")

    # Find the end of the loadData function (the closing brace + newline before init())
    end_marker = "loadData();\n</script>"
    end_idx = html.find(end_marker)
    if end_idx == -1:
        end_marker = "loadData();\r\n</script>"
        end_idx = html.find(end_marker)
    if end_idx == -1:
        raise ValueError("Could not find end of script block")

    # Reconstruct: everything before <script>, new script, then init() onward
    before = html[:idx]
    after = html[end_idx + len(end_marker):]

    # Read everything between loadData() call and </script> — we need init() and draw functions
    # Actually, we need everything AFTER loadData definition up to loadData() call
    # Simpler: grab from after loadData closing brace to the loadData() call
    script_start = idx + len("<script>")
    full_script = html[script_start:end_idx + len(end_marker) - len("</script>")]

    # Find where init() function starts
    init_marker = "\nfunction init()"
    init_idx = full_script.find(init_marker)
    if init_idx == -1:
        raise ValueError("Could not find init() function")

    rest_of_script = full_script[init_idx:]
    # Remove the trailing loadData();\n
    rest_of_script = rest_of_script.replace("loadData();\n", "loadData();\n")

    html_out = before + "<script>\n" + new_script + "\n" + rest_of_script + "</script>" + after
    return html_out


def main():
    print(f"═══════════════════════════════════════════════════════")
    print(f"  IXIC 56 Reversal Chart Builder")
    print(f"  Outfit: {OUTFIT_NAME}")
    print(f"  Target: MA{SMA_PERIOD} on {TIMEFRAME} timeframe")
    print(f"═══════════════════════════════════════════════════════")

    client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)

    # Step 1: Pull bars
    candles = query_bars(client)
    if not candles:
        print("ERROR: No IXIC 2H bars found in InfluxDB.")
        print("  Make sure ingest.py has been run with IXIC on the 2h timeframe.")
        return

    # Step 2: Build chart data (SMAs over all bars, display only 3/20)
    print(f"  Computing SMAs: {OUTFIT_PERIODS}")
    data = build_chart_data(candles, target_date="2026-03-20")
    if data is None:
        print("ERROR: Could not build chart data.")
        return

    print(f"  Interactions (penny matches): {len(data['interactions'])}")
    print(f"  Bars near MA{SMA_PERIOD}: {len(data['ma720_analysis'])}")

    # Show MA884 interactions specifically
    ma884_ix = [ix for ix in data["interactions"] if ix["sma_period"] == 884]
    print(f"  MA884 penny touches: {len(ma884_ix)}")
    for ix in ma884_ix[:10]:
        print(f"    {ix['time'][:16]}  {ix['ohlc_field']}=${ix['price']}")

    # Show top outfit rankings
    print(f"\n  Top outfit rankings (by penny hits):")
    for r in data["rankings"][:5]:
        tag = " ← TARGET" if r["outfit"] == OUTFIT_NAME else ""
        print(f"    {r['outfit']}: {r['hits']} hits{tag}")

    # Step 3: Build standalone HTML
    print(f"\n  Building standalone HTML chart...")
    html = build_html(data)

    outpath = "ixic_56reversal_ma884.html"
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\n  ✓ Chart saved to: {outpath}")
    print(f"  Open it in your browser — no servers needed.")

    client.close()


if __name__ == "__main__":
    main()
