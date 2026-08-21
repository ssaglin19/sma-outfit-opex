"""
SMA Detection Engine (InfluxDB-Aware)
======================================
Reads OHLCV bars from InfluxDB market_data bucket, computes SMAs,
and runs the 4 detection algorithms:

  1. Precision Buy Algorithm (PBA)
  2. Automated Short Order (ASO)
  3. Singular Point Hard Stop (SPHS)
  4. Optimized/Magnetized Buying Algorithm (OBA)

Writes fired alerts to InfluxDB 'alerts' bucket.
Runs as a loop during market hours (0930-1600 EST), 60s cycles.

Ported from sma_alert_engine.py — same logic, InfluxDB data source.

Usage:
  python detector.py              # run detection loop
  python detector.py --once       # single cycle then exit
  python detector.py --ticker SPY # single ticker, single cycle
"""

import argparse
import json
import os
import sys
import time
import warnings
import numpy as np
import pandas as pd
from datetime import datetime, timezone, timedelta
from collections import defaultdict

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

from config import (
    INFLUXDB_URL, INFLUXDB_TOKEN, INFLUXDB_ORG,
    SMA_OUTFITS, SYSTEMS, TICKERS, TIMEFRAMES,
)

warnings.filterwarnings('ignore')

# =============================================================================
# CONSTANTS
# =============================================================================
PENNY = 0.01
OBA_CONSECUTIVE = 3  # minimum consecutive magnetized bars to fire OBA
IQR_MULTIPLIER = 5.0

# Ticker → system mapping
TICKER_SYSTEM_MAP = {}
SP500_TICKERS = ["SPX", "SPY", "UPRO", "SPXU", "SPXL", "SSO", "SDS", "SPXS", "SH"]
NASDAQ_TICKERS = ["IXIC", "QQQ", "TQQQ", "SQQQ", "QLD", "QID", "PSQ"]
DOW_TICKERS = ["DJI", "DIA", "UDOW", "SDOW", "DDM", "DXD", "DOG"]
for t in SP500_TICKERS:
    TICKER_SYSTEM_MAP[t] = "S&P 500"
for t in NASDAQ_TICKERS:
    TICKER_SYSTEM_MAP[t] = "NASDAQ"
for t in DOW_TICKERS:
    TICKER_SYSTEM_MAP[t] = "Dow Jones"

# All unique SMA periods from all outfits
ALL_SMA_PERIODS = sorted(set(p for smas in SMA_OUTFITS.values() for p in smas))

# Timeframe labels
TF_LABELS = [tf['label'] for tf in TIMEFRAMES]


# =============================================================================
# ENV / INFLUX
# =============================================================================
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


def ensure_alerts_bucket(client):
    """Create alerts bucket if it doesn't exist."""
    buckets_api = client.buckets_api()
    existing = buckets_api.find_buckets().buckets
    names = [b.name for b in existing]
    if "alerts" not in names:
        org = client.organizations_api().find_organizations(org="sma-alerts")[0]
        from influxdb_client.domain.bucket_retention_rules import BucketRetentionRules
        buckets_api.create_bucket(
            bucket_name="alerts",
            org_id=org.id,
            retention_rules=[BucketRetentionRules(type="expire", every_seconds=0)]
        )
        print("Created 'alerts' bucket")


# =============================================================================
# DATA FETCHING FROM INFLUXDB
# =============================================================================
def query_bars(client, ticker, timeframe, limit=1200):
    """Fetch OHLCV bars from market_data bucket. Returns DataFrame."""
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
                'Open': float(row.values.get('open', 0)),
                'High': float(row.values.get('high', 0)),
                'Low': float(row.values.get('low', 0)),
                'Close': float(row.values.get('close', 0)),
                'Volume': int(row.values.get('volume', 0)),
            })
    if not rows:
        return pd.DataFrame()
    df = pd.DataFrame(rows)
    df.set_index('timestamp', inplace=True)
    df.sort_index(inplace=True)
    return df


# =============================================================================
# DATA CLEANSING (ported from sma_alert_engine.py)
# =============================================================================
def cleanse_bars(df):
    if df is None or df.empty:
        return df
    df = df[df.index.notna()]
    if df.index.duplicated().any():
        df = df[~df.index.duplicated(keep='last')]
    price_cols = [c for c in ['Open', 'High', 'Low', 'Close'] if c in df.columns]
    if price_cols:
        df = df.dropna(subset=price_cols)
        df = df[(df[price_cols] > 0).all(axis=1)]
    if 'High' in df.columns and 'Low' in df.columns:
        df = df[df['High'] >= df['Low']]
    if df.empty:
        return df
    result = df.copy()
    for col in price_cols:
        series = result[col]
        q1, q3 = series.quantile(0.25), series.quantile(0.75)
        iqr = q3 - q1
        if iqr == 0:
            continue
        mask = (series < q1 - IQR_MULTIPLIER * iqr) | (series > q3 + IQR_MULTIPLIER * iqr)
        if mask.any():
            result.loc[mask, col] = float('nan')
            result[col] = result[col].interpolate(method='linear').ffill().bfill()
    return result


# =============================================================================
# SMA COMPUTATION
# =============================================================================
def compute_all_smas(df):
    """Compute all outfit SMA columns on the DataFrame. Modifies df in place."""
    for period in ALL_SMA_PERIODS:
        col = f"SMA_{period}"
        if len(df) >= period:
            df[col] = df['Close'].rolling(window=period).mean()
        else:
            df[col] = float('nan')
    return df


def get_sma_value(df, period):
    col = f"SMA_{period}"
    if col in df.columns and not pd.isna(df[col].iloc[-1]):
        return round(float(df[col].iloc[-1]), 2)
    return None


# =============================================================================
# SYSTEM STATUS (reuse from scorer.py)
# =============================================================================
def get_system_status(client):
    """Get system status. Returns dict with system states + VIX info."""
    from scorer import get_system_status as _get
    return _get(client)


# =============================================================================
# DETECTION: PRECISION BUY ALGORITHM
# =============================================================================
def detect_precision_buy(df, sma_period, system_context, outfit_sma_periods=None):
    """Detect PBA — price pullback to SMA support with exact penny touch."""
    if len(df) < max(20, sma_period + 5):
        return None
    col = f"SMA_{sma_period}"
    if col not in df.columns:
        return None
    sma_val = get_sma_value(df, sma_period)
    if sma_val is None:
        return None

    # Outfit context: reject if all other SMAs are above price
    if outfit_sma_periods:
        current_close = float(df['Close'].iloc[-1])
        other_above = 0
        other_computed = 0
        for other_p in outfit_sma_periods:
            if other_p == sma_period:
                continue
            other_val = get_sma_value(df, other_p)
            if other_val is not None:
                other_computed += 1
                if other_val > current_close + PENNY:
                    other_above += 1
        if other_computed >= 2 and other_above == other_computed:
            return None

    for bar_offset in [-1, -2]:
        if abs(bar_offset) >= len(df):
            continue
        bar = df.iloc[bar_offset]
        o, h, l, c = float(bar['Open']), float(bar['High']), float(bar['Low']), float(bar['Close'])
        ohlc4 = (o + h + l + c) / 4
        bar_sma = float(df[col].iloc[bar_offset]) if not pd.isna(df[col].iloc[bar_offset]) else None
        if bar_sma is None:
            continue
        sma_rounded = round(bar_sma, 2)

        # 1. OHLC4 touch within $0.01
        if abs(round(ohlc4, 2) - sma_rounded) > PENNY:
            continue
        # 2. Close >= SMA (support held)
        if round(c, 2) < sma_rounded:
            continue
        # 3. Approach from above
        if abs(bar_offset) + 1 >= len(df):
            continue
        prev_bar = df.iloc[bar_offset - 1]
        prev_ohlc4 = (float(prev_bar['Open']) + float(prev_bar['High']) +
                       float(prev_bar['Low']) + float(prev_bar['Close'])) / 4
        if prev_ohlc4 <= sma_rounded:
            continue
        # 3b. Drawdown check
        if abs(bar_offset) + 2 < len(df):
            bar_3back = df.iloc[bar_offset - 2]
            ohlc4_3back = (float(bar_3back['Open']) + float(bar_3back['High']) +
                           float(bar_3back['Low']) + float(bar_3back['Close'])) / 4
            if ohlc4_3back <= prev_ohlc4:
                continue
        # 3c. SMA distinctness
        pre_start = max(0, len(df) + bar_offset - 12)
        pre_end = max(0, len(df) + bar_offset - 2)
        if pre_end <= pre_start:
            continue
        pre_slice = df.iloc[pre_start:pre_end]
        if len(pre_slice) < 3:
            continue
        pre_ohlc4_vals = (pre_slice['Open'] + pre_slice['High'] + pre_slice['Low'] + pre_slice['Close']) / 4
        avg_pre_ohlc4 = float(pre_ohlc4_vals.mean())
        if avg_pre_ohlc4 <= sma_rounded:
            continue
        gap_pct = (avg_pre_ohlc4 - sma_rounded) / sma_rounded if sma_rounded > 0 else 0
        if gap_pct < 0.003:
            continue
        # 4. Drawdown magnitude
        lookback = min(40, len(df) - 1)
        start_idx = max(0, len(df) + bar_offset - lookback)
        end_idx = len(df) + bar_offset
        if end_idx <= start_idx:
            continue
        recent_high = float(df['High'].iloc[start_idx:end_idx].max())
        drawdown_pct = (recent_high - sma_rounded) / recent_high if recent_high > 0 else 0
        if drawdown_pct < 0.01:
            continue
        # 5. Current OHLC4 still at/above SMA
        cur_bar = df.iloc[-1]
        cur_ohlc4 = (float(cur_bar['Open']) + float(cur_bar['High']) +
                      float(cur_bar['Low']) + float(cur_bar['Close'])) / 4
        current_sma = get_sma_value(df, sma_period)
        if current_sma is not None and round(cur_ohlc4, 2) < round(current_sma, 2):
            continue

        return {
            "type": "precision_buy_algorithm",
            "sma_period": sma_period,
            "sma_value": sma_rounded,
            "ohlc4": round(ohlc4, 2),
            "drawdown_pct": round(drawdown_pct * 100, 2),
            "close": round(c, 2),
            "bar": "current" if bar_offset == -1 else "prev",
            "hard_stop_level": round(sma_rounded - PENNY, 2),
            "description": (
                f"PRECISION BUY — SMA {sma_period} at {sma_rounded:.2f} | "
                f"OHLC4 {ohlc4:.2f} | Close {c:.2f} | "
                f"Hard stop: {sma_rounded - PENNY:.2f} | "
                f"Drawdown {drawdown_pct*100:.1f}% from {recent_high:.2f}"
            ),
        }
    return None


# =============================================================================
# DETECTION: AUTOMATED SHORT ORDER
# =============================================================================
def detect_auto_short(df, sma_period, system_context, ticker_system_name=None):
    """Detect ASO — price rallies to SMA resistance and rejects.
    System negative = CRITICAL severity. System positive = HIGH severity.
    No longer hard-gated on system state."""
    # Determine system alignment for severity
    system_negative = False
    if ticker_system_name:
        state_map = {
            "S&P 500": "sp500_state",
            "NASDAQ": "nasdaq_state",
            "Dow Jones": "dji_state",
        }
        state_key = state_map.get(ticker_system_name)
        if state_key and system_context.get(state_key) == "NEGATIVE":
            system_negative = True

    if len(df) < max(20, sma_period + 5):
        return None
    col = f"SMA_{sma_period}"
    if col not in df.columns:
        return None
    sma_val = get_sma_value(df, sma_period)
    if sma_val is None:
        return None

    for bar_offset in [-1, -2]:
        if abs(bar_offset) >= len(df):
            continue
        bar = df.iloc[bar_offset]
        o, h, l, c = float(bar['Open']), float(bar['High']), float(bar['Low']), float(bar['Close'])
        ohlc4 = (o + h + l + c) / 4
        bar_sma = float(df[col].iloc[bar_offset]) if not pd.isna(df[col].iloc[bar_offset]) else None
        if bar_sma is None:
            continue
        sma_rounded = round(bar_sma, 2)

        # 1. OHLC4 touch
        if abs(round(ohlc4, 2) - sma_rounded) > PENNY:
            continue
        # 2. Close <= SMA (rejection)
        if round(c, 2) > sma_rounded:
            continue
        # 3. Approach from below
        if abs(bar_offset) + 1 >= len(df):
            continue
        prev_bar = df.iloc[bar_offset - 1]
        prev_ohlc4 = (float(prev_bar['Open']) + float(prev_bar['High']) +
                       float(prev_bar['Low']) + float(prev_bar['Close'])) / 4
        if prev_ohlc4 >= sma_rounded:
            continue
        # 3b. Rally check
        if abs(bar_offset) + 2 < len(df):
            bar_3back = df.iloc[bar_offset - 2]
            ohlc4_3back = (float(bar_3back['Open']) + float(bar_3back['High']) +
                           float(bar_3back['Low']) + float(bar_3back['Close'])) / 4
            if ohlc4_3back >= prev_ohlc4:
                continue
        # 4. Current confirmation
        cur_bar = df.iloc[-1]
        cur_ohlc4 = (float(cur_bar['Open']) + float(cur_bar['High']) +
                      float(cur_bar['Low']) + float(cur_bar['Close'])) / 4
        current_sma = get_sma_value(df, sma_period)
        if current_sma and round(cur_ohlc4, 2) > round(current_sma, 2):
            continue

        sys_label = "SYSTEM NEGATIVE" if system_negative else "COUNTER-TREND"
        return {
            "type": "automated_short_order",
            "sma_period": sma_period,
            "sma_value": sma_rounded,
            "ohlc4": round(ohlc4, 2),
            "close": round(c, 2),
            "bar": "current" if bar_offset == -1 else "prev",
            "hard_stop_level": round(sma_rounded + PENNY, 2),
            "system_negative": system_negative,
            "description": (
                f"AUTO SHORT — SMA {sma_period} at {sma_rounded:.2f} | "
                f"OHLC4 {ohlc4:.2f} | Close {c:.2f} | "
                f"Hard stop: {sma_rounded + PENNY:.2f} | {sys_label}"
            ),
        }
    return None


# =============================================================================
# DETECTION: OPTIMIZED / MAGNETIZED BUYING
# =============================================================================
def detect_optimized_buy(df, sma_period, high_vol, system_context):
    """Detect OBA — disproportionate OHLC clustering on a single SMA.
    Now direction-aware: determines LONG vs SHORT based on price action."""
    if len(df) < 15:
        return None
    col = f"SMA_{sma_period}"
    if col not in df.columns:
        return None

    window_size = min(10, len(df) - 1)
    window = df.iloc[-window_size:]
    penny_touches = 0
    near_touches = 0
    bars_with_touch = 0

    for i in range(len(window)):
        row = window.iloc[i]
        if pd.isna(row.get(col)):
            continue
        sma_at_bar = round(float(row[col]), 2)
        bar_has_touch = False
        for field in ['Open', 'High', 'Low', 'Close']:
            val = round(float(row[field]), 2)
            dist = round(abs(val - sma_at_bar), 2)
            if dist == 0.0:
                penny_touches += 1
                bar_has_touch = True
            elif dist <= PENNY:
                near_touches += 1
                bar_has_touch = True
        if bar_has_touch:
            bars_with_touch += 1

    total_touches = penny_touches + near_touches

    # Price-adjusted significance
    cur = df.iloc[-1]
    current_price = (float(cur['Open']) + float(cur['High']) +
                     float(cur['Low']) + float(cur['Close'])) / 4
    if current_price <= 0:
        return None

    bar_ranges = (window['High'] - window['Low']).dropna()
    if len(bar_ranges) == 0:
        return None
    avg_range_cents = float(bar_ranges.mean()) / 0.01
    if avg_range_cents < 1:
        avg_range_cents = 1

    expected_penny = (4.0 * window_size) / avg_range_cents
    expected_near = expected_penny * 2
    expected_total = expected_penny + expected_near

    min_penny = max(3, int(expected_penny * 3))
    min_total = max(6, int(expected_total * 3))
    min_bars = max(3, int(window_size * 0.4))

    is_magnetized = (
        (penny_touches >= min_penny or total_touches >= min_total)
        and bars_with_touch >= min_bars
    )
    if not is_magnetized:
        return None

    current_sma = get_sma_value(df, sma_period)
    if current_sma is None:
        return None

    # ── DIRECTIONAL AWARENESS ──
    # Determine if this is support (LONG) or resistance (SHORT)
    current_close = round(float(cur['Close']), 2)
    sma_rounded = round(current_sma, 2)

    # Check where price came from (pre-window) vs where it is now
    pre_window_idx = max(0, len(df) - window_size - 5)
    pre_window_end = max(0, len(df) - window_size)
    if pre_window_end > pre_window_idx:
        pre_slice = df.iloc[pre_window_idx:pre_window_end]
        pre_ohlc4 = float(((pre_slice['Open'] + pre_slice['High'] +
                            pre_slice['Low'] + pre_slice['Close']) / 4).mean())
    else:
        pre_ohlc4 = current_price

    approached_from_above = pre_ohlc4 > sma_rounded
    approached_from_below = pre_ohlc4 < sma_rounded
    closed_above = current_close >= sma_rounded
    closed_below = current_close < sma_rounded

    # Determine direction
    if approached_from_above and closed_above:
        # Pullback to support, held = LONG (OBA buy)
        direction = "LONG"
    elif approached_from_below and closed_below:
        # Rally to resistance, rejected = SHORT (OBA sell)
        direction = "SHORT"
    elif approached_from_above and closed_below:
        # Broke through support = SHORT
        direction = "SHORT"
    elif approached_from_below and closed_above:
        # Broke through resistance = LONG
        direction = "LONG"
    else:
        # Indeterminate — use close vs SMA
        direction = "LONG" if closed_above else "SHORT"

    capitular_low = float(window['Low'].min())
    density = total_touches / max(1, window_size)
    sig_ratio = penny_touches / max(0.01, expected_penny)

    if direction == "LONG":
        alert_type = "optimized_buying_algorithm"
        label = "MAGNETIZED BUY"
    else:
        alert_type = "optimized_short_algorithm"
        label = "MAGNETIZED SHORT"

    return {
        "type": alert_type,
        "sma_period": sma_period,
        "sma_value": sma_rounded,
        "direction": direction,
        "penny_touches": penny_touches,
        "near_touches": near_touches,
        "total_touches": total_touches,
        "bars_with_touch": bars_with_touch,
        "window_size": window_size,
        "density": round(density, 2),
        "capitular_low": round(capitular_low, 2),
        "significance_ratio": round(sig_ratio, 2),
        "description": (
            f"{label} — SMA {sma_period} at {current_sma:.2f} | "
            f"{penny_touches} penny + {near_touches} near touches "
            f"across {bars_with_touch}/{window_size} bars | "
            f"{sig_ratio:.1f}x expected | "
            f"Close {current_close:.2f} {'above' if closed_above else 'below'} SMA"
            f"{' | HIGH VOL' if high_vol else ''}"
        ),
    }


# =============================================================================
# STATE MACHINE + DETECTION PIPELINE
# =============================================================================
class DetectionState:
    """Persistent state machine for detection lifecycle tracking."""

    def __init__(self):
        # Key: (ticker, tf_label, sma_period)
        self.near_state = {}        # None | "pba" | "aso" | "sphs_pba" | "sphs_aso"
        self.oba_consec = {}        # consecutive magnetized bar count
        self.oba_fired = set()      # OBA already fired this cluster
        self.last_bar_ts = {}       # bar timestamp tracking
        self.cycle_dedup = set()    # dedup within a cycle
        self._first_cycle = True    # skip only the very first cycle
        self.fired_alerts = set()   # cross-cycle dedup: (ticker, type, sma_period, bar_ts)

    def get_state(self, key):
        return self.near_state.get(key)

    def set_state(self, key, state):
        if state is None:
            self.near_state.pop(key, None)
            self.oba_consec.pop(key, None)
            self.oba_fired.discard(key)
        else:
            self.near_state[key] = state

    def increment_oba(self, key):
        self.oba_consec[key] = self.oba_consec.get(key, 0) + 1
        return self.oba_consec[key]

    def reset_oba_consec(self, key):
        self.oba_consec[key] = 0

    def is_oba_fired(self, key):
        return key in self.oba_fired

    def mark_oba_fired(self, key):
        self.oba_fired.add(key)

    def check_cold_start(self, tf_key, bar_ts):
        """Track bar timestamps. Returns True only on the very first startup cycle."""
        if tf_key not in self.last_bar_ts:
            self.last_bar_ts[tf_key] = bar_ts
            return self._first_cycle
        self.last_bar_ts[tf_key] = bar_ts
        return False

    def is_dedup(self, key):
        if key in self.cycle_dedup:
            return True
        self.cycle_dedup.add(key)
        return False

    def clear_cycle_dedup(self):
        self.cycle_dedup.clear()

    def mark_first_cycle_done(self):
        self._first_cycle = False

    def is_alert_fired(self, ticker, alert_type, sma_period, bar_ts):
        """Cross-cycle dedup — don't re-fire same alert on same bar."""
        key = (ticker, alert_type, sma_period, bar_ts)
        return key in self.fired_alerts

    def record_alert_fired(self, ticker, alert_type, sma_period, bar_ts):
        self.fired_alerts.add((ticker, alert_type, sma_period, bar_ts))

    def prune_fired_alerts(self, max_size=50000):
        """Prevent memory bloat — keep only recent fired alerts."""
        if len(self.fired_alerts) > max_size:
            self.fired_alerts.clear()


# Global state persists across cycles
state = DetectionState()


def run_detections_on_df(df, ticker, sys_name, high_vol, timeframe_label, system_context, skip_cold_start=False):
    """
    Run all 4 detection types on a single dataframe.
    Returns list of alert dicts.
    """
    if df is None or len(df) < 2:
        return []

    tf_key = (ticker, timeframe_label)
    bar_ts = df.index[-1]
    if not skip_cold_start and state.check_cold_start(tf_key, bar_ts):
        return []

    alerts = []
    bar = df.iloc[-1]
    o, h, l, c = float(bar['Open']), float(bar['High']), float(bar['Low']), float(bar['Close'])
    ohlc = (o, h, l, c)

    for outfit_name, outfit_periods in SMA_OUTFITS.items():
        for sma_p in outfit_periods:
            col = f"SMA_{sma_p}"
            if col not in df.columns:
                continue
            sma_val = df[col].iloc[-1]
            if pd.isna(sma_val):
                continue
            sma_val = float(sma_val)

            state_key = (ticker, timeframe_label, sma_p)
            cur_state = state.get_state(state_key)

            # Derived flags
            ohlc4 = (o + h + l + c) / 4
            ohlc4_touches = abs(round(ohlc4, 2) - round(sma_val, 2)) <= PENNY
            sphs_breach_below = any(round(sma_val - v, 2) == PENNY for v in ohlc if v < sma_val)
            sphs_breach_above = any(round(v - sma_val, 2) == PENNY for v in ohlc if v > sma_val)
            bar_above = l > sma_val
            bar_below = h < sma_val
            bar_interacts = l <= sma_val <= h

            # =========================================================
            # STATE: None — check for new PBA or ASO entry
            # =========================================================
            if cur_state is None:
                # PBA
                pba = detect_precision_buy(df, sma_p, system_context, outfit_sma_periods=outfit_periods)
                if pba:
                    dedup_key = f"{ticker}|precision_buy_algorithm|{sma_p}"
                    if not state.is_dedup(dedup_key):
                        state.set_state(state_key, "pba")
                        pba["ticker"] = ticker
                        pba["outfit"] = outfit_name
                        pba["timeframe"] = timeframe_label
                        pba["severity"] = "critical"
                        pba["title"] = f"{ticker} PRECISION BUY SMA{sma_p} [{outfit_name}] {timeframe_label}"
                        alerts.append(pba)
                    continue

                # ASO — now fires regardless of system state
                aso = detect_auto_short(df, sma_p, system_context, ticker_system_name=sys_name)
                if aso:
                    dedup_key = f"{ticker}|automated_short_order|{sma_p}"
                    if not state.is_dedup(dedup_key):
                        state.set_state(state_key, "aso")
                        aso["ticker"] = ticker
                        aso["outfit"] = outfit_name
                        aso["timeframe"] = timeframe_label
                        aso["severity"] = "critical" if aso.get("system_negative") else "high"
                        aso["title"] = f"{ticker} AUTO SHORT SMA{sma_p} [{outfit_name}] {timeframe_label}"
                        alerts.append(aso)
                    continue

                # OBA standalone
                oba = detect_optimized_buy(df, sma_p, high_vol, system_context)
                if oba:
                    dedup_key = f"{ticker}|optimized_buying_algorithm|{sma_p}"
                    if not state.is_dedup(dedup_key):
                        oba["ticker"] = ticker
                        oba["outfit"] = outfit_name
                        oba["timeframe"] = timeframe_label
                        oba["severity"] = "high"
                        oba["title"] = f"{ticker} MAGNETIZED BUY SMA{sma_p} [{outfit_name}] {timeframe_label}"
                        alerts.append(oba)

            # =========================================================
            # STATE: "pba" — active PBA
            # =========================================================
            elif cur_state == "pba":
                if c < sma_val:
                    state.set_state(state_key, None)
                elif sphs_breach_below:
                    state.set_state(state_key, "sphs_pba")
                    sma_rounded = round(sma_val, 2)
                    breach = round(sma_val - c, 2)
                    vol_avg = float(df['Volume'].iloc[max(0, len(df)-20):len(df)-1].mean()) if len(df) > 2 else 0
                    vol_ratio = float(bar['Volume']) / max(1, vol_avg)
                    sphs = {
                        "type": "singular_point_hard_stop",
                        "ticker": ticker,
                        "outfit": outfit_name,
                        "timeframe": timeframe_label,
                        "severity": "critical",
                        "sma_period": sma_p,
                        "sma_value": sma_rounded,
                        "breach_amount": round(breach, 2),
                        "close": round(c, 2),
                        "volume_ratio": round(vol_ratio, 2),
                        "title": f"{ticker} HARD STOP SMA{sma_p} [{outfit_name}] {timeframe_label}",
                        "description": (
                            f"HARD STOP — SMA {sma_p} at {sma_rounded:.2f} | "
                            f"Breach ${breach:.2f} | Close {c:.2f} | Vol {vol_ratio:.1f}x avg"
                        ),
                    }
                    dedup_key = f"{ticker}|singular_point_hard_stop|{sma_p}"
                    if not state.is_dedup(dedup_key):
                        alerts.append(sphs)
                elif bar_above:
                    state.set_state(state_key, None)
                else:
                    if bar_interacts:
                        consec = state.increment_oba(state_key)
                        if consec >= OBA_CONSECUTIVE and not state.is_oba_fired(state_key):
                            state.mark_oba_fired(state_key)
                            sma_rounded = round(sma_val, 2)
                            oba = {
                                "type": "optimized_buying_algorithm",
                                "ticker": ticker,
                                "outfit": outfit_name,
                                "timeframe": timeframe_label,
                                "severity": "high",
                                "sma_period": sma_p,
                                "sma_value": sma_rounded,
                                "consecutive_bars": consec,
                                "title": f"{ticker} MAGNETIZED BUY SMA{sma_p} [{outfit_name}] {timeframe_label}",
                                "description": (
                                    f"MAGNETIZED BUY — SMA {sma_p} at {sma_rounded:.2f} | "
                                    f"{consec} consecutive bars | active PBA cluster"
                                ),
                            }
                            dedup_key = f"{ticker}|optimized_buying_algorithm|{sma_p}"
                            if not state.is_dedup(dedup_key):
                                alerts.append(oba)
                    else:
                        state.reset_oba_consec(state_key)

            # =========================================================
            # STATE: "aso" — active ASO
            # =========================================================
            elif cur_state == "aso":
                if c > sma_val:
                    state.set_state(state_key, None)
                elif sphs_breach_above:
                    state.set_state(state_key, "sphs_aso")
                    sma_rounded = round(sma_val, 2)
                    breach = round(c - sma_val, 2)
                    sphs = {
                        "type": "singular_point_hard_stop",
                        "ticker": ticker,
                        "outfit": outfit_name,
                        "timeframe": timeframe_label,
                        "severity": "critical",
                        "sma_period": sma_p,
                        "sma_value": sma_rounded,
                        "breach_amount": round(breach, 2),
                        "close": round(c, 2),
                        "title": f"{ticker} HARD STOP SMA{sma_p} [{outfit_name}] {timeframe_label}",
                        "description": (
                            f"HARD STOP — SMA {sma_p} at {sma_rounded:.2f} | "
                            f"Breach above ${breach:.2f} | Close {c:.2f}"
                        ),
                    }
                    dedup_key = f"{ticker}|singular_point_hard_stop|{sma_p}"
                    if not state.is_dedup(dedup_key):
                        alerts.append(sphs)
                elif bar_below:
                    state.set_state(state_key, None)
                else:
                    if bar_interacts:
                        consec = state.increment_oba(state_key)
                        if consec >= OBA_CONSECUTIVE and not state.is_oba_fired(state_key):
                            state.mark_oba_fired(state_key)
                            sma_rounded = round(sma_val, 2)
                            oba = {
                                "type": "optimized_buying_algorithm",
                                "ticker": ticker,
                                "outfit": outfit_name,
                                "timeframe": timeframe_label,
                                "severity": "high",
                                "sma_period": sma_p,
                                "sma_value": sma_rounded,
                                "consecutive_bars": consec,
                                "title": f"{ticker} MAGNETIZED SMA{sma_p} [{outfit_name}] {timeframe_label}",
                                "description": (
                                    f"MAGNETIZED — SMA {sma_p} at {sma_rounded:.2f} | "
                                    f"{consec} consecutive bars | active ASO cluster"
                                ),
                            }
                            dedup_key = f"{ticker}|optimized_buying_algorithm|{sma_p}"
                            if not state.is_dedup(dedup_key):
                                alerts.append(oba)
                    else:
                        state.reset_oba_consec(state_key)

            # =========================================================
            # STATE: "sphs_pba" / "sphs_aso" — waiting for clear
            # =========================================================
            elif cur_state == "sphs_pba":
                if bar_above:
                    state.set_state(state_key, None)
            elif cur_state == "sphs_aso":
                if bar_below:
                    state.set_state(state_key, None)

    return alerts


# =============================================================================
# ALERT WRITING TO INFLUXDB
# =============================================================================
def write_alerts_to_influx(write_api, alerts):
    """Write alert events to the alerts bucket."""
    points = []
    for a in alerts:
        p = (Point("alert")
             .tag("ticker", a.get("ticker", ""))
             .tag("type", a.get("type", ""))
             .tag("severity", a.get("severity", ""))
             .tag("outfit", a.get("outfit", ""))
             .tag("timeframe", a.get("timeframe", ""))
             .field("sma_period", int(a.get("sma_period", 0)))
             .field("sma_value", float(a.get("sma_value", 0)))
             .field("close", float(a.get("close", 0)))
             .field("title", a.get("title", ""))
             .field("description", a.get("description", ""))
             .field("hard_stop_level", float(a.get("hard_stop_level", 0)))
             .time(datetime.now(timezone.utc), WritePrecision.MS))
        points.append(p)
    if points:
        write_api.write(bucket="alerts", record=points)


# =============================================================================
# MARKET HOURS CHECK
# =============================================================================
def is_market_open():
    from zoneinfo import ZoneInfo
    now = datetime.now(ZoneInfo("America/New_York"))
    if now.weekday() >= 5:
        return False
    mins = now.hour * 60 + now.minute
    return 570 <= mins <= 960  # 0930-1600


# =============================================================================
# MAIN DETECTION CYCLE
# =============================================================================
def run_cycle(client, write_api, ticker_filter=None, skip_cold_start=False):
    """Run one full detection cycle across all tickers and timeframes."""
    state.clear_cycle_dedup()

    # Get system status
    sys_status = get_system_status(client)
    vix_info = sys_status.get("_vix", {})
    vix_level = vix_info.get("level")
    high_vol = vix_level is not None and vix_level > 20

    # Build system context
    system_context = {
        "sp500_state": sys_status.get("S&P 500", {}).get("status"),
        "nasdaq_state": sys_status.get("NASDAQ", {}).get("status"),
        "dji_state": sys_status.get("Dow Jones", {}).get("status"),
        "any_negative": any(
            sys_status.get(s, {}).get("status") == "NEGATIVE"
            for s in ["S&P 500", "NASDAQ", "Dow Jones"]
        ),
        "high_volatility": high_vol,
        "vix": vix_level,
    }

    regime = "HIGH VOL" if high_vol else "NORMAL"
    print(f"  VIX: {vix_level} ({regime})")
    for name in ["S&P 500", "NASDAQ", "Dow Jones"]:
        s = sys_status.get(name, {})
        print(f"  {name}: {s.get('status', '?')} — {s.get('detail', '?')}")

    tickers = [ticker_filter] if ticker_filter else TICKERS
    all_alerts = []
    total_detections = 0

    for ticker in tickers:
        sys_name = TICKER_SYSTEM_MAP.get(ticker)
        ticker_alerts = []

        for tf in TIMEFRAMES:
            tf_label = tf['label']
            df = query_bars(client, ticker, tf_label, limit=1200)
            if df.empty:
                continue
            df = cleanse_bars(df)
            if df.empty or len(df) < 20:
                continue
            df = compute_all_smas(df)

            alerts = run_detections_on_df(df, ticker, sys_name, high_vol, tf_label, system_context, skip_cold_start=skip_cold_start)
            ticker_alerts.extend(alerts)

        if ticker_alerts:
            total_detections += len(ticker_alerts)
            all_alerts.extend(ticker_alerts)
            types = defaultdict(int)
            for a in ticker_alerts:
                types[a['type']] += 1
            type_str = ", ".join(f"{k.replace('_', ' ').title()}: {v}" for k, v in types.items())
            print(f"  [{ticker}] {len(ticker_alerts)} alerts — {type_str}")

    # Cross-cycle dedup: filter out alerts already fired on same bar
    new_alerts = []
    for a in all_alerts:
        bar_ts = None
        # Get the bar timestamp for dedup
        ticker = a.get("ticker", "")
        tf_label = a.get("timeframe", "")
        tf_key = (ticker, tf_label)
        bar_ts = state.last_bar_ts.get(tf_key)
        if bar_ts and state.is_alert_fired(ticker, a.get("type", ""), a.get("sma_period", 0), bar_ts):
            continue
        if bar_ts:
            state.record_alert_fired(ticker, a.get("type", ""), a.get("sma_period", 0), bar_ts)
        new_alerts.append(a)

    # Write new alerts to InfluxDB
    if new_alerts:
        write_alerts_to_influx(write_api, new_alerts)
        print(f"\n  TOTAL: {len(new_alerts)} alerts written to InfluxDB")
    else:
        print(f"\n  No alerts this cycle")

    state.mark_first_cycle_done()
    state.prune_fired_alerts()
    return new_alerts


def run_detector(once=False, ticker_filter=None):
    """Main entry point. Runs detection cycles."""
    client = get_influx_client()
    ensure_alerts_bucket(client)
    write_api = client.write_api(write_options=SYNCHRONOUS)

    print("=" * 60)
    print("  SMA DETECTION ENGINE (InfluxDB)")
    active_count = 1 if ticker_filter else len(TICKERS)
    print(f"  Tickers: {active_count}" + (f" ({ticker_filter})" if ticker_filter else ""))
    print(f"  Outfits: {len(SMA_OUTFITS)}")
    print(f"  Timeframes: {len(TIMEFRAMES)}")
    print(f"  Detection types: PBA | ASO | SPHS | OBA")
    print("=" * 60)

    if once:
        ts = datetime.now().strftime('%H:%M:%S')
        print(f"\n[{ts}] Single detection cycle")
        run_cycle(client, write_api, ticker_filter=ticker_filter, skip_cold_start=True)
        client.close()
        return

    while True:
        ts = datetime.now().strftime('%H:%M:%S')
        if is_market_open():
            print(f"\n{'='*60}")
            print(f"  [{ts}] Detection cycle starting")
            print(f"{'='*60}")
            run_cycle(client, write_api, ticker_filter=ticker_filter)
            print(f"  [{datetime.now().strftime('%H:%M:%S')}] Cycle complete. Next in 60s.")
        else:
            print(f"  [{ts}] Market closed. Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SMA Detection Engine")
    parser.add_argument("--once", action="store_true", help="Single cycle then exit")
    parser.add_argument("--ticker", help="Single ticker only")
    args = parser.parse_args()

    run_detector(once=args.once, ticker_filter=args.ticker)
