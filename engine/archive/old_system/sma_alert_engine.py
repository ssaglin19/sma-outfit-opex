"""
SMA Alert Engine v3 — TradeStation + Multi-Timeframe
=====================================================
Implements the SMA-outfits framework with strict precision:

TICKERS (32):
  S&P 500: SPX, SPY, UPRO, SPXU, SPXL, SSO, SDS, SPXS, SH
  NASDAQ:  IXIC, QQQ, TQQQ, SQQQ, QLD, QID, PSQ
  Dow Jones: DJI, DIA, UDOW, SDOW, DDM, DXD, DOG
  Russell 2000: IWM, UWM, TNA, RWM (no system state)
  VIX: VIX, VXX, SVIX, UVXY, SVXY (no system state)

SYSTEM STATE (3 systems, evaluated from primary indices only):
- S&P 500: SPX 30M, MA10/MA50 (positive = MA10 > MA50)
- NASDAQ:  IXIC 30M, MA20/MA100 (positive = MA20 > MA100)
- Dow Jones: DJI 15M, MA90/MA300 (positive = MA90 > MA300)
- VIX-based volatility regime shifts
- Key levels: MA200 (SPX), MA250 (IXIC), MA900 (DJI)
- Russell 2000 / VIX groups: NO system state, ASO skipped

DETECTION TYPES (penny-level precision):
1. Precision Buy Algorithm — exact OHLC-to-SMA touch ($0.01) after drawdown
2. Singular Point Hard Stop — one-penny breach below active SMA level + volume spike
3. Automated Short Order — system negative, precise SMA rejection (SKIPPED for no-system groups)
4. Optimized/Magnetized Buying — disproportionate OHLC clustering on singular SMA

OUTFITS (18): ALL applied to ALL tickers
  Systems: SP500, NAS, DJI
  AN: EVIL, ICKY WOODS, LUCKY
  Math: Waring's Problem, Regression 432, 180
  Time: 365, 366, 144
  Political: President 45/46/47, WTC 911, SVIX
  Misc: Resource Missing 404

TIMEFRAMES:
  System state: SPX 30M, IXIC 30M, DJI 15M (fixed per repo)
  SMA Outfit detections (non-index tickers): 1m, 2m, 3m, 5m, 10m, 15m, 20m, 30m, 1h, 2h, 4h

Data: TradeStation API v3
API:  Flask on port 5050
"""

import pandas as pd
import numpy as np
from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
from ts_client import TradeStationClient, yf_to_ts_symbol
import threading
import time
import json
import warnings
import statistics
import os
import logging
warnings.filterwarnings('ignore')

# =============================================================================
# ALERT LOG FILE — persistent append-only log for post-session analysis
# =============================================================================
_ALERT_LOG_DIR = os.path.dirname(os.path.abspath(__file__))
_ALERT_LOG_FILE = os.path.join(_ALERT_LOG_DIR, 'alerts.log')

_alert_logger = logging.getLogger('sma_alert_log')
_alert_logger.setLevel(logging.INFO)
_alert_logger.propagate = False
if not _alert_logger.handlers:
    _fh = logging.FileHandler(_ALERT_LOG_FILE, mode='a', encoding='utf-8')
    _fh.setFormatter(logging.Formatter('%(message)s'))
    _alert_logger.addHandler(_fh)


def _log_alert_to_file(alert):
    """Append a one-line alert record to alerts.log for post-session analysis."""
    try:
        ts_str = alert.get('timestamp', datetime.now().isoformat())
        ticker = alert.get('ticker', '?')
        atype = alert.get('type', '?')
        sma_p = alert.get('sma_period', '')
        outfit = alert.get('outfit', '')
        tf = alert.get('timeframe', '')
        severity = alert.get('severity', '')
        title = alert.get('title', '')
        desc = alert.get('description', '')
        line = f"[{ts_str}] {ticker} | {atype} | SMA{sma_p} | {outfit} | {tf} | {severity} | {title} | {desc}"
        _alert_logger.info(line)
    except Exception:
        pass

# TradeStation client (initialized at startup)
ts = TradeStationClient()

app = Flask(__name__)
CORS(app)

# =============================================================================
# PENNY-LEVEL PRECISION CONSTANT
# =============================================================================
# The repo is explicit: "singular penny or point breach"
# All OHLC-to-SMA matching uses this as the maximum tolerance
PENNY = 0.01

# IQR multiplier for outlier fencing (5x = very permissive, catches only extreme spikes)
_OUTLIER_IQR_MULTIPLIER = 5.0


# =============================================================================
# DATA CLEANSING — applied to every DataFrame from TradeStation before analysis
# =============================================================================
# Adapted from the old Yahoo Finance project's 5-stage pipeline.
# TradeStation data is cleaner, but defensive cleansing costs nothing.

def cleanse_bars(df):
    """
    Clean raw OHLCV bars from TradeStation.

    Stages:
      1. Drop rows with NaT timestamps
      2. Remove duplicate timestamps (keep last)
      3. Drop rows where any OHLC value is NaN or non-positive
      4. Drop structurally invalid bars (High < Low)
      5. IQR-fenced outlier correction per OHLC column:
         Values outside Q1 - 5*IQR / Q3 + 5*IQR are replaced with
         linear interpolation from surrounding clean bars.

    Returns cleaned DataFrame (may be empty).
    """
    if df is None or df.empty:
        return df

    # 1. NaT timestamps
    df = df[df.index.notna()]

    # 2. Duplicate timestamps — keep last occurrence
    if df.index.duplicated().any():
        df = df[~df.index.duplicated(keep='last')]

    # 3. NaN / non-positive OHLC
    price_cols = [c for c in ['Open', 'High', 'Low', 'Close'] if c in df.columns]
    if price_cols:
        df = df.dropna(subset=price_cols)
        df = df[(df[price_cols] > 0).all(axis=1)]

    # 4. Structural consistency: High >= Low
    if 'High' in df.columns and 'Low' in df.columns:
        df = df[df['High'] >= df['Low']]

    if df.empty:
        return df

    # 5. IQR-fenced outlier correction
    result = df.copy()
    for col in price_cols:
        series = result[col]
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1
        if iqr == 0:
            continue
        lower_fence = q1 - _OUTLIER_IQR_MULTIPLIER * iqr
        upper_fence = q3 + _OUTLIER_IQR_MULTIPLIER * iqr
        mask = (series < lower_fence) | (series > upper_fence)
        if mask.any():
            result.loc[mask, col] = float('nan')
            result[col] = result[col].interpolate(method='linear').ffill().bfill()

    return result


# =============================================================================
# SMA OUTFIT CONFIGURATIONS (18 outfits)
# =============================================================================
# ALL outfits apply to ALL 32 tickers. System protocols are flagged separately.

SMA_OUTFITS = {
    # --- THE THREE SYSTEMS (state evaluation protocols) ---
    "S&P 500 System": {
        "smas": [10, 50, 200],
        "description": "The System — SPX 30M midterm",
        "is_system": True,
        "positive_rule": {"short": 10, "long": 50},
        "vol_shift_level": 50,
        "key_level": 200,
    },
    "NASDAQ System": {
        "smas": [20, 100, 250],
        "description": "NASDAQ — IXIC 30M midterm",
        "is_system": True,
        "positive_rule": {"short": 20, "long": 100},
        "vol_shift_level": 100,
        "key_level": 250,
    },
    "Dow Jones System": {
        "smas": [30, 60, 90, 300, 600, 900],
        "description": "DJI — 15M/1H midterm",
        "is_system": True,
        "positive_rule": {"short": 90, "long": 300},
        "vol_shift_level": 300,
        "key_level": 900,
    },
    # --- AN ---
    "EVIL (666)": {
        "smas": [33, 66, 99, 333, 666, 999],
        "description": "Alphanumeric — EVIL 666",
    },
    "ICKY WOODS (888)": {
        "smas": [11, 44, 88, 111, 444, 888],
        "description": "Alphanumeric — ICKY WOODS 888",
    },
    "LUCKY (777)": {
        "smas": [22, 55, 77, 222, 555, 777],
        "description": "Alphanumeric — LUCKY 777",
    },
    # --- MATH ---
    "Waring's Problem": {
        "smas": [19, 37, 73, 143, 279, 548],
        "description": "Hilbert integers — 19/37/73/143/279/548",
    },
    "Regression (432)": {
        "smas": [27, 54, 108, 216, 432, 864],
        "description": "Regression — 432",
    },
    "180": {
        "smas": [30, 60, 90, 180, 360, 720],
        "description": "180 — 30/60/90/180/360/720",
    },
    # --- TIME ---
    "Time (365)": {
        "smas": [23, 46, 91, 183, 365, 730],
        "description": "Calendar year",
    },
    "Time (366)": {
        "smas": [23, 46, 92, 183, 366, 732],
        "description": "Leap year",
    },
    "Time (144)": {
        "smas": [18, 36, 72, 144, 288, 576],
        "description": "Minutes in a day",
    },
    # --- POLITICAL ---
    "President 45": {
        "smas": [29, 57, 114, 227, 455, 911],
        "description": "U.S. president seat 45",
    },
    "President 46": {
        "smas": [23, 46, 92, 184, 368, 736],
        "description": "U.S. president seat 46",
    },
    "President 47": {
        "smas": [24, 47, 94, 188, 376, 752],
        "description": "U.S. president seat 47",
    },
    "WTC (911)": {
        "smas": [28, 57, 114, 228, 456, 911],
        "description": "World Trade Center homage",
    },
    "SVIX (211)": {
        "smas": [26, 52, 106, 211, 422, 844],
        "description": "SVIX — 211",
    },
    # --- MISC ---
    "Resource Missing (404)": {
        "smas": [25, 51, 101, 202, 404, 808],
        "description": "404 reference",
    },
}

# =============================================================================
# TICKERS (31) — grouped by index
# =============================================================================

TICKER_GROUPS = {
    "S&P 500": ["^GSPC", "SPY", "UPRO", "SPXU", "SPXL", "SSO", "SDS", "SPXS", "SH"],
    "NASDAQ": ["^IXIC", "QQQ", "TQQQ", "SQQQ", "QLD", "QID", "PSQ"],
    "Dow Jones": ["^DJI", "DIA", "UDOW", "SDOW", "DDM", "DXD", "DOG"],
    "Russell 2000": ["IWM", "UWM", "TNA", "RWM"],
    "VIX": ["^VIX", "VXX", "SVIX", "UVXY", "SVXY"],
}

# Flat list of all tickers
TICKERS = [t for group in TICKER_GROUPS.values() for t in group]

# Display names — indices get human-readable names, ETFs use ticker as-is
TICKER_DISPLAY = {
    "^GSPC": "SPX",
    "^IXIC": "IXIC",
    "^DJI": "DJI",
    "^VIX": "VIX",
}

# Which group each ticker belongs to (for UI and interval lookup)
TICKER_TO_GROUP = {}
for _grp, _tickers in TICKER_GROUPS.items():
    for _t in _tickers:
        TICKER_TO_GROUP[_t] = _grp

# =============================================================================
# TIMEFRAME CONFIGURATION
# =============================================================================
# System state evaluation: fixed timeframes per repo
#   SPX 30M, IXIC 30M, DJI 15M
# SMA Outfit detection on non-index tickers: ALL timeframes per repo
#   1m, 2m, 3m, 5m, 10m, 15m, 20m, 30m, 1h, 2h, 4h

SYSTEM_TIMEFRAMES = {
    "^GSPC": 30,   # SPX 30M
    "^IXIC": 30,   # IXIC 30M (can alternate 20M/30M per repo, using 30M)
    "^DJI": 15,    # DJI 15M
}

# All SMA outfit timeframes (interval in minutes for TradeStation unit=Minute)
# Repo: 1m, 2m, 3m, 5m, 10m, 15m, 20m, 30m, 1h, 2h, 4h
OUTFIT_TIMEFRAMES = [1, 2, 3, 5, 10, 15, 20, 30, 60, 120, 240]

# VIX fetch uses daily bars
VIX_SYMBOL = '$VIX.X'

# Ticker → system mapping (for READING system state in detections)
# Russell 2000 and VIX have no system — ASO skipped for those
TICKER_SYSTEM_MAP = {}
for _t in TICKER_GROUPS["S&P 500"]:
    TICKER_SYSTEM_MAP[_t] = "S&P 500 System"
for _t in TICKER_GROUPS["NASDAQ"]:
    TICKER_SYSTEM_MAP[_t] = "NASDAQ System"
for _t in TICKER_GROUPS["Dow Jones"]:
    TICKER_SYSTEM_MAP[_t] = "Dow Jones System"
# Russell 2000: not in map → None
# VIX: not in map → None

# Only the PRIMARY INDEX ticker evaluates and SETS system state
# (inverse/leveraged ETFs would produce wrong state)
SYSTEM_PRIMARY_TICKERS = {
    "S&P 500 System": "^GSPC",
    "NASDAQ System": "^IXIC",
    "Dow Jones System": "^DJI",
}


# =============================================================================
# DATA STORE
# =============================================================================

class DataStore:
    """Thread-safe store for market data, system states, and alerts."""

    def __init__(self):
        self.lock = threading.Lock()
        self.price_data = {}
        self.sma_values = {}
        self.alerts = []
        self.system_states = {}
        self.last_update = None
        self.outfit_detections = {}
        self.vix_level = None
        self.high_volatility = False
        # Track active precision buy levels for hard stop detection
        self.active_precision_levels = {}  # ticker -> [(sma_period, sma_value, outfit_name)]
        # Deduplication: track what was alerted last cycle to avoid spam
        self._last_cycle_keys = set()
        # OHLC interaction counts: ticker -> outfit_name -> count
        # Accumulates across the session (not reset per cycle)
        self.ohlc_interaction_counts = {}
        # Dominant outfit per ticker (computed after each full scan)
        self.dominant_outfits = {}  # ticker -> {outfit, count, runner_up, runner_up_count, ratio}
        # Institutional activity bubbles: ticker -> list of bubble dicts
        # Each bubble: {sma_value, detection_type, confidence, signals, outfit, timeframe, bar_range}
        self.bubbles = {}
        # --- STATE MACHINE (per-interaction lifecycle tracking) ---
        # Key: (ticker, tf_label, sma_period)
        # Values: None | "pba" | "aso" | "sphs_pba" | "sphs_aso"
        self.near_state = {}
        # OBA consecutive magnetized bar count per (ticker, tf_label, sma_period)
        self.oba_consec = {}
        # OBA already fired this cluster per (ticker, tf_label, sma_period)
        self.oba_fired = set()
        # Cold-start guard: last bar timestamp per (ticker, tf_label)
        self.last_bar_ts = {}

    def update(self, ticker, df, sma_vals, detections):
        with self.lock:
            self.price_data[ticker] = df
            self.sma_values[ticker] = sma_vals
            self.outfit_detections[ticker] = detections
            self.last_update = datetime.now().isoformat()

    def add_alert(self, alert):
        """Add alert with deduplication. Returns True if new, False if duplicate.
        Dedup key intentionally EXCLUDES outfit so that the same (ticker, type, sma_period)
        fires only once per cycle regardless of which outfit detected it first.
        Cross-outfit dedup mirrors the old project's approach; dominant outfit filtering
        is a separate, additive suppression layer."""
        # Build dedup key — no outfit: same SMA period across outfits dedupes
        dedup_key = f"{alert.get('ticker')}|{alert.get('type')}|{alert.get('sma_period','')}"
        with self.lock:
            if dedup_key in self._last_cycle_keys:
                return False
            self._last_cycle_keys.add(dedup_key)
            alert['id'] = len(self.alerts)
            alert['timestamp'] = datetime.now().isoformat()
            self.alerts.append(alert)
            if len(self.alerts) > 1000:
                self.alerts = self.alerts[-1000:]
            # Persist to disk for post-session analysis
            _log_alert_to_file(alert)
            return True

    def clear_cycle_dedup(self):
        with self.lock:
            self._last_cycle_keys.clear()

    def set_system_state(self, name, state_info):
        with self.lock:
            old = self.system_states.get(name, {})
            state_info["prev_state"] = old.get("state")
            state_info["changed"] = (
                old.get("state") is not None and
                old.get("state") != state_info.get("state")
            )
            self.system_states[name] = state_info

    def get_system_state(self, name):
        with self.lock:
            return self.system_states.get(name, {})

    def get_all_system_states(self):
        with self.lock:
            return dict(self.system_states)

    def is_any_system_negative(self):
        with self.lock:
            return any(s.get("state") == "NEGATIVE" for s in self.system_states.values())

    def is_system_negative(self, system_name):
        with self.lock:
            return self.system_states.get(system_name, {}).get("state") == "NEGATIVE"

    def register_precision_level(self, ticker, sma_period, sma_value, outfit_name):
        with self.lock:
            if ticker not in self.active_precision_levels:
                self.active_precision_levels[ticker] = []
            self.active_precision_levels[ticker].append((sma_period, sma_value, outfit_name))
            # Keep only last 50 levels per ticker
            self.active_precision_levels[ticker] = self.active_precision_levels[ticker][-50:]

    def get_precision_levels(self, ticker):
        with self.lock:
            return list(self.active_precision_levels.get(ticker, []))

    def record_interactions(self, ticker, outfit_name, count):
        """Record OHLC interaction hits for a ticker/outfit. Accumulates across session."""
        with self.lock:
            if ticker not in self.ohlc_interaction_counts:
                self.ohlc_interaction_counts[ticker] = {}
            if outfit_name not in self.ohlc_interaction_counts[ticker]:
                self.ohlc_interaction_counts[ticker][outfit_name] = 0
            self.ohlc_interaction_counts[ticker][outfit_name] += count

    def compute_dominant_outfit(self, ticker):
        """
        Determine the dominant outfit for a ticker based on accumulated hit counts.

        Dominant = the outfit with the most OHLC interactions, provided it has:
        - At least 2x the hits of the runner-up (clear separation)
        - At least 3 total hits (not just noise)

        Returns the dominant outfit info dict, or None.
        """
        with self.lock:
            counts = self.ohlc_interaction_counts.get(ticker, {})
            if not counts:
                return None

            # Sort outfits by count descending
            ranked = sorted(counts.items(), key=lambda x: x[1], reverse=True)
            if len(ranked) == 0:
                return None

            top_outfit, top_count = ranked[0]
            runner_up = ranked[1][0] if len(ranked) > 1 else None
            runner_up_count = ranked[1][1] if len(ranked) > 1 else 0

            # Minimum absolute hits
            if top_count < 3:
                return None

            # Must have clear dominance: at least 1.5x the runner-up
            # (If there's no runner-up, any count >= 3 qualifies)
            ratio = top_count / max(1, runner_up_count)
            if runner_up_count > 0 and ratio < 1.5:
                return None

            result = {
                "outfit": top_outfit,
                "count": top_count,
                "runner_up": runner_up,
                "runner_up_count": runner_up_count,
                "ratio": round(ratio, 2),
                "all_counts": dict(ranked[:5]),  # top 5 for display
            }
            self.dominant_outfits[ticker] = result
            return result

    def get_dominant_outfit(self, ticker):
        with self.lock:
            return self.dominant_outfits.get(ticker)

    def get_all_dominant_outfits(self):
        with self.lock:
            return dict(self.dominant_outfits)

    def get_all_interaction_counts(self):
        with self.lock:
            return {t: dict(c) for t, c in self.ohlc_interaction_counts.items()}

    def set_bubbles(self, ticker, bubble_list):
        """Store institutional activity bubbles for a ticker."""
        with self.lock:
            self.bubbles[ticker] = bubble_list

    def get_bubbles(self, ticker):
        with self.lock:
            return list(self.bubbles.get(ticker, []))

    def get_all_bubbles(self):
        with self.lock:
            return {t: list(b) for t, b in self.bubbles.items() if b}

    # --- STATE MACHINE METHODS ---

    def get_near_state(self, key):
        """Get interaction state for (ticker, tf_label, sma_period)."""
        with self.lock:
            return self.near_state.get(key)

    def set_near_state(self, key, state):
        """Set or clear interaction state."""
        with self.lock:
            if state is None:
                self.near_state.pop(key, None)
                self.oba_consec.pop(key, None)
                self.oba_fired.discard(key)
            else:
                self.near_state[key] = state

    def reset_oba(self, key):
        """Reset OBA tracking for a key (SPHS breach or clear)."""
        with self.lock:
            self.oba_consec.pop(key, None)
            self.oba_fired.discard(key)

    def increment_oba_consec(self, key):
        """Increment OBA consecutive magnetized bar count. Returns new count."""
        with self.lock:
            self.oba_consec[key] = self.oba_consec.get(key, 0) + 1
            return self.oba_consec[key]

    def reset_oba_consec(self, key):
        """Reset OBA consecutive count (gap in magnetization)."""
        with self.lock:
            self.oba_consec[key] = 0

    def is_oba_fired(self, key):
        with self.lock:
            return key in self.oba_fired

    def mark_oba_fired(self, key):
        with self.lock:
            self.oba_fired.add(key)

    def check_cold_start(self, tf_key, bar_ts):
        """Cold-start guard. Returns True if this is the first bar (skip detection).
        tf_key = (ticker, tf_label). bar_ts = current bar timestamp."""
        with self.lock:
            if tf_key not in self.last_bar_ts:
                self.last_bar_ts[tf_key] = bar_ts
                return True  # first bar ever — skip
            if bar_ts == self.last_bar_ts[tf_key]:
                return True  # same bar — skip
            self.last_bar_ts[tf_key] = bar_ts
            return False

    def get_snapshot(self):
        with self.lock:
            return {
                "last_update": self.last_update,
                "system_states": dict(self.system_states),
                "alerts": list(self.alerts[-100:]),
                "tickers": list(self.price_data.keys()),
                "vix": self.vix_level,
                "high_volatility": self.high_volatility,
                "dominant_outfits": dict(self.dominant_outfits),
                "bubbles": {t: list(b) for t, b in self.bubbles.items() if b},
            }

    def get_chart_data(self, ticker):
        with self.lock:
            if ticker not in self.price_data:
                return None
            df = self.price_data[ticker].copy()
            sma_vals = self.sma_values.get(ticker, {})
            return df, sma_vals

    def get_detections(self):
        with self.lock:
            return dict(self.outfit_detections)


store = DataStore()


# =============================================================================
# VIX / VOLATILITY REGIME
# =============================================================================

def fetch_vix():
    """Fetch VIX level to determine volatility regime."""
    try:
        df = ts.get_bars(VIX_SYMBOL, 1, 'Daily', 5)
        if not df.empty:
            level = float(df['Close'].iloc[-1])
            store.vix_level = level
            store.high_volatility = level > 20
            return level
    except Exception as e:
        print(f"[WARN] VIX fetch failed: {e}")
    return None


# =============================================================================
# SMA COMPUTATION
# =============================================================================

def compute_all_smas(df):
    """Compute every unique SMA period across all outfits on the dataframe.

    SMA source: OHLC4 = (Open + High + Low + Close) / 4
    Per the SMA-outfits framework specification.
    """
    all_periods = set()
    for outfit in SMA_OUTFITS.values():
        all_periods.update(outfit["smas"])

    # Compute OHLC4 series once, reuse for all SMAs
    ohlc4 = (df['Open'] + df['High'] + df['Low'] + df['Close']) / 4

    computed = {}
    for p in sorted(all_periods):
        col = f"SMA_{p}"
        if len(df) >= p:
            df[col] = ohlc4.rolling(window=p).mean()
            last_val = df[col].iloc[-1]
            computed[p] = round(float(last_val), 2) if not pd.isna(last_val) else None
        else:
            computed[p] = None

    return computed


def get_sma_value(df, period):
    """Get the current SMA value for a period. Returns None if unavailable."""
    col = f"SMA_{period}"
    if col in df.columns and len(df) > 0:
        val = df[col].iloc[-1]
        if not pd.isna(val):
            return float(val)
    return None


# =============================================================================
# SYSTEM STATE EVALUATION
# =============================================================================

def evaluate_system_state(df, system_config, high_vol):
    """
    Evaluate system positive/negative state.

    Normal: short SMA > long SMA = POSITIVE
    High volatility (rising VIX): candle close above long SMA = POSITIVE
                                   candle close below long SMA = NEGATIVE
    """
    rule = system_config.get("positive_rule")
    if not rule:
        return None

    short_p = rule["short"]
    long_p = rule["long"]
    short_val = get_sma_value(df, short_p)
    long_val = get_sma_value(df, long_p)

    if short_val is None or long_val is None:
        return None

    # Use OHLC4 for price (per spec)
    last = df.iloc[-1]
    price = (float(last['Open']) + float(last['High']) +
             float(last['Low']) + float(last['Close'])) / 4

    if high_vol:
        # Volatility regime: candle close vs long SMA
        vol_level = system_config.get("vol_shift_level", long_p)
        vol_sma = get_sma_value(df, vol_level)
        if vol_sma is None:
            vol_sma = long_val
        state = "POSITIVE" if price > vol_sma else "NEGATIVE"
        eval_method = "volatility_regime"
        eval_detail = f"OHLC4 {price:.2f} {'>' if state == 'POSITIVE' else '<'} SMA{vol_level} {vol_sma:.2f}"
    else:
        # Normal regime: short SMA vs long SMA
        state = "POSITIVE" if short_val > long_val else "NEGATIVE"
        eval_method = "normal"
        eval_detail = f"SMA{short_p} {short_val:.2f} {'>' if state == 'POSITIVE' else '<'} SMA{long_p} {long_val:.2f}"

    spread = ((short_val - long_val) / long_val) * 100

    # Key level check (MA200/MA250/MA900)
    key_level = system_config.get("key_level")
    key_sma_val = None
    at_key_level = False
    key_breach = None
    if key_level:
        key_sma_val = get_sma_value(df, key_level)
        if key_sma_val is not None:
            distance = abs(price - key_sma_val)
            at_key_level = distance <= PENNY * 5  # within 5 cents
            if at_key_level:
                key_breach = "above" if price >= key_sma_val else "below"

    return {
        "state": state,
        "eval_method": eval_method,
        "eval_detail": eval_detail,
        "short_sma": short_p,
        "short_value": round(short_val, 2),
        "long_sma": long_p,
        "long_value": round(long_val, 2),
        "price": round(price, 2),
        "spread_pct": round(spread, 3),
        "key_level_sma": key_level,
        "key_level_value": round(key_sma_val, 2) if key_sma_val else None,
        "at_key_level": at_key_level,
        "key_breach": key_breach,
        "high_volatility": high_vol,
    }


# =============================================================================
# DETECTION TYPE 1: PRECISION BUYING ALGORITHM
# =============================================================================
# README: "activates when an arbitrage detection system identifies a precision
#  OHLC relationship within a SINGULAR timeframe, SINGULAR equity, and SINGULAR
#  SMA Outfit that has been historically or statistically significant following
#  an SMA-induced drawdown"
#
# Case study evidence (exact language from @unfairmarket threads):
# - SCO at 18.21, MA448 at 18.20 → "Hard stop order at MA448 18.20"
# - SQQQ at 22.36, MA50 at 22.36 → "singular penny break of that buying protocol"
# - SOXL at 21.93, MA224 at 21.92 → "hard stop order at the [2M MA224 at 21.92]"
# - SVIX at 13.55, MA376 at 13.55 → "high frequency program at precisely 13.55"
# - XLE at 81.85, 404 outfit → "breaches 81.85 by a singular penny"
# - RWM at 18.21, [2000] outfit → "banks have an established risk parameter"
#
# Pattern from case studies:
# 1. Price draws DOWN to a DISTINCT SMA level (the SMA was below recent price)
# 2. OHLC matches SMA to the exact cent ($0.00 variance)
# 3. Close >= SMA (support held, buying off the level)
# 4. The SMA is the "selection" — entry point AND risk level
# 5. Hard stop = SMA value minus 1 penny ("cut on singular penny break")
# 6. {candle close below PARM:MA___, ignore +SMA Outfit} = invalidation

def detect_precision_buy(df, sma_period, system_context, outfit_sma_periods=None):
    """
    Detect Precision Buy Algorithm for a single SMA period.

    A PBA triggers when price pulls back DOWN to a specific SMA level after a
    drawdown and that SMA acts as DISTINCT SUPPORT. Key validations:

    1. Exact penny match: an OHLC value = SMA value to the cent
    2. Close >= SMA on the touch bar (support held, buying off the level)
    3. The SMA is a DISTINCT level — not just tracking price. Verified by
       checking that the SMA is meaningfully separated from recent price
       action before the touch.
    4. Price is NOT below ALL SMAs in the outfit. If it is, this SMA isn't
       support — price has crashed through everything.
    5. Meaningful drawdown: recent high to SMA must show a real pullback.
    6. Current close still at/above the SMA (invalidation check).
    """
    if len(df) < max(20, sma_period + 5):
        return None

    col = f"SMA_{sma_period}"
    if col not in df.columns:
        return None

    sma_val = get_sma_value(df, sma_period)
    if sma_val is None:
        return None

    # OUTFIT CONTEXT CHECK: if ALL other SMAs in the outfit are above price,
    # then price has crashed through every level — the matched SMA isn't
    # acting as support, it's just a short-period SMA tracking price downward.
    if outfit_sma_periods:
        current_close = float(df['Close'].iloc[-1])
        other_smas_above = 0
        other_smas_computed = 0
        for other_p in outfit_sma_periods:
            if other_p == sma_period:
                continue
            other_val = get_sma_value(df, other_p)
            if other_val is not None:
                other_smas_computed += 1
                if other_val > current_close + PENNY:
                    other_smas_above += 1
        # If we have at least 2 other computable SMAs and ALL are above price,
        # reject — price is below everything in the outfit
        if other_smas_computed >= 2 and other_smas_above == other_smas_computed:
            return None

    # Check both current bar and previous bar for the selection
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

        # 1. OHLC4 TOUCH: bar's OHLC4 within $0.01 of SMA (per spec)
        if abs(round(ohlc4, 2) - sma_rounded) > PENNY:
            continue

        # 2. Close must be AT or ABOVE the SMA (buying off the level)
        if round(c, 2) < sma_rounded:
            continue

        # 3. APPROACH FROM ABOVE: previous bar's OHLC4 was above the SMA
        #    Plus SMA distinctness checks to filter tracking SMAs.
        if abs(bar_offset) + 1 >= len(df):
            continue
        prev_bar = df.iloc[bar_offset - 1]
        prev_ohlc4 = (float(prev_bar['Open']) + float(prev_bar['High']) +
                       float(prev_bar['Low']) + float(prev_bar['Close'])) / 4
        if prev_ohlc4 <= sma_rounded:
            continue  # was not above SMA — not approaching from above

        # 3b. DRAWDOWN CHECK: OHLC4 from 3 bars back must be > prev OHLC4
        #     (price was declining into the MA, not flat/rising)
        if abs(bar_offset) + 2 < len(df):
            bar_3back = df.iloc[bar_offset - 2]
            ohlc4_3back = (float(bar_3back['Open']) + float(bar_3back['High']) +
                           float(bar_3back['Low']) + float(bar_3back['Close'])) / 4
            if ohlc4_3back <= prev_ohlc4:
                continue  # price was not declining into MA

        # 3c. SMA DISTINCTNESS: avg OHLC4 of bars 3-12 before touch must be
        #     meaningfully ABOVE the SMA (SMA is distinct support, not tracking)
        pre_touch_start = max(0, len(df) + bar_offset - 12)
        pre_touch_end = max(0, len(df) + bar_offset - 2)
        if pre_touch_end <= pre_touch_start:
            continue
        pre_slice = df.iloc[pre_touch_start:pre_touch_end]
        if len(pre_slice) < 3:
            continue
        pre_ohlc4_vals = (pre_slice['Open'] + pre_slice['High'] +
                          pre_slice['Low'] + pre_slice['Close']) / 4
        avg_pre_ohlc4 = float(pre_ohlc4_vals.mean())

        if avg_pre_ohlc4 <= sma_rounded:
            continue

        gap_pct = (avg_pre_ohlc4 - sma_rounded) / sma_rounded if sma_rounded > 0 else 0
        if gap_pct < 0.003:  # 0.3% minimum gap
            continue

        # 4. Drawdown magnitude: drop from recent high to this SMA level
        lookback = min(40, len(df) - 1)
        start_idx = max(0, len(df) + bar_offset - lookback)
        end_idx = len(df) + bar_offset
        if end_idx <= start_idx:
            continue
        recent_high = float(df['High'].iloc[start_idx:end_idx].max())
        drawdown_to_sma = recent_high - sma_rounded
        drawdown_pct = drawdown_to_sma / recent_high if recent_high > 0 else 0

        if drawdown_pct < 0.01:  # 1% minimum drawdown
            continue

        # 5. Current OHLC4 must still be at/above the SMA (invalidation check)
        cur_bar = df.iloc[-1]
        cur_ohlc4 = (float(cur_bar['Open']) + float(cur_bar['High']) +
                      float(cur_bar['Low']) + float(cur_bar['Close'])) / 4
        current_sma = get_sma_value(df, sma_period)
        if current_sma is not None and round(cur_ohlc4, 2) < round(current_sma, 2):
            continue

        bar_label = "current" if bar_offset == -1 else "prev"

        return {
            "type": "precision_buy_algorithm",
            "sma_period": sma_period,
            "sma_value": sma_rounded,
            "ohlc4": round(ohlc4, 2),
            "drawdown_pct": round(drawdown_pct * 100, 2),
            "avg_pre_ohlc4": round(avg_pre_ohlc4, 2),
            "gap_pct": round(gap_pct * 100, 3),
            "close": round(c, 2),
            "bar": bar_label,
            "hard_stop_level": round(sma_rounded - PENNY, 2),
            "system_context": system_context,
            "description": (
                f"PRECISION BUY — SMA {sma_period} at {sma_rounded:.2f} | "
                f"OHLC4 {ohlc4:.2f} ({bar_label} bar) | Close {c:.2f} | "
                f"Hard stop: {sma_rounded - PENNY:.2f} | "
                f"Drawdown {drawdown_pct*100:.1f}% from {recent_high:.2f}"
            ),
        }

    return None


    # NOTE: SPHS detection is now handled entirely by the state machine in
    # run_detections_on_df(). It fires when an active "pba" or "aso" state
    # experiences a singular penny breach (any OHLC value exactly $0.01 past
    # the SMA). The standalone detect_hard_stop() has been removed.


# =============================================================================
# DETECTION TYPE 3: AUTOMATED SHORT ORDER
# =============================================================================
# README: "hinges on the anticipation of a price decline, which is facilitated
#  by the SMA outfits designed to analyze specific OHLC patterns"
# README: "critically dependent on systems interpreting market data, more
#  specifically the SMA outfits"
# README: "when any of these systems are negative, the largest wealth firms
#  are reaping profits, and some are shorting the market"
#
# Case study evidence:
# - SVXY at [2H][420][MA420 at 43.15] → "conditional sell program"
# - GME at 3m MA72 → "secure profit orders there"
#
# Pattern: system negative + price rallies UP to SMA resistance + rejects
# The SMA must be ABOVE recent price (acting as resistance/ceiling)

def detect_auto_short(df, sma_period, system_context, ticker_system_name=None, outfit_sma_periods=None):
    """
    Detect Automated Short Order for a single SMA period.

    The SMA must be acting as RESISTANCE above recent price — price rallied
    UP to it and rejected. Mirrors PBA logic but inverted: SMA is ceiling.

    The ticker's OWN system must be negative (not just any system).
    """
    # Hard gate: the ticker's OWN system must be negative
    # The README is specific: each system governs its own tickers
    if ticker_system_name:
        system_key = f"{ticker_system_name.split()[0].lower()}_state"
        # Map system name to context key
        state_map = {
            "S&P 500 System": "sp500_state",
            "NASDAQ System": "nasdaq_state",
            "Dow Jones System": "dji_state",
        }
        state_key = state_map.get(ticker_system_name)
        if state_key and system_context.get(state_key) != "NEGATIVE":
            return None
    else:
        # No system for this ticker (Russell/VIX) — ASO should not fire
        return None

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

        # 1. OHLC4 TOUCH: bar's OHLC4 within $0.01 of SMA (per spec)
        if abs(round(ohlc4, 2) - sma_rounded) > PENNY:
            continue

        # 2. Close must be AT or BELOW the SMA (rejection — failed to break above)
        if round(c, 2) > sma_rounded:
            continue

        # 3. APPROACH FROM BELOW: previous bar's OHLC4 was below the SMA
        if abs(bar_offset) + 1 >= len(df):
            continue
        prev_bar = df.iloc[bar_offset - 1]
        prev_ohlc4 = (float(prev_bar['Open']) + float(prev_bar['High']) +
                       float(prev_bar['Low']) + float(prev_bar['Close'])) / 4
        if prev_ohlc4 >= sma_rounded:
            continue  # was not below SMA — not approaching from below

        # 3b. RALLY CHECK: OHLC4 from 3 bars back must be < prev OHLC4
        #     (price was rising into the MA)
        if abs(bar_offset) + 2 < len(df):
            bar_3back = df.iloc[bar_offset - 2]
            ohlc4_3back = (float(bar_3back['Open']) + float(bar_3back['High']) +
                           float(bar_3back['Low']) + float(bar_3back['Close'])) / 4
            if ohlc4_3back >= prev_ohlc4:
                continue  # price was not rising into MA

        # 4. Current OHLC4 confirmation: still at or below SMA
        cur_bar = df.iloc[-1]
        cur_ohlc4 = (float(cur_bar['Open']) + float(cur_bar['High']) +
                      float(cur_bar['Low']) + float(cur_bar['Close'])) / 4
        current_sma = get_sma_value(df, sma_period)
        if current_sma and round(cur_ohlc4, 2) > round(current_sma, 2):
            continue  # price broke above since — invalidated

        bar_label = "current" if bar_offset == -1 else "prev"

        return {
            "type": "automated_short_order",
            "sma_period": sma_period,
            "sma_value": sma_rounded,
            "ohlc4": round(ohlc4, 2),
            "close": round(c, 2),
            "bar": bar_label,
            "hard_stop_level": round(sma_rounded + PENNY, 2),
            "system_context": system_context,
            "description": (
                f"AUTO SHORT — SMA {sma_period} at {sma_rounded:.2f} | "
                f"OHLC4 {ohlc4:.2f} ({bar_label} bar) | Close {c:.2f} | "
                f"Hard stop: {sma_rounded + PENNY:.2f} (penny above) | "
                f"SYSTEM NEGATIVE"
            ),
        }

    return None


# =============================================================================
# DETECTION TYPE 4: OPTIMIZED / MAGNETIZED BUYING ALGORITHM
# =============================================================================
# README: "disproportionate tabulation of OHLC entries that reflect a
#  relationship to a singular SMA outfit"
# README: "operate during periods of heightened volatility"
# README: "strategically attract buy orders to a specific price level on a
#  SMA outfit"
# README: "ensure minimal slippage and an optimal execution"
# README: "more adaptive [than precision buy]... operate during periods of
#  heightened volatility that advanced trading divisions use to gamify equities"
#
# Case study evidence:
# - RWM 30M SVIX Outfit → "magnetized buying algorithm"
# - QQQ 1m MA444 → "magnetized orders on that parameter"
# - MA404 → "the selection of the MA404, where they knew to bid long"
#
# Pattern: "disproportionate" = far more OHLC-SMA matches than random chance.
# For a $500 stock, even 2-3 exact cent matches is extraordinary.
# For a $7 stock, you'd expect ~5 matches per 10 bars by pure probability.
# Thresholds MUST be price-adjusted to be statistically meaningful.

def detect_optimized_buy(df, sma_period, high_vol, system_context):
    """
    Detect Optimized/Magnetized Buying Algorithm for a single SMA period.

    The "disproportionate tabulation" must be STATISTICALLY disproportionate
    relative to what random chance would produce at this price level.
    Thresholds are price-adjusted: cheap stocks need far more touches to be
    significant because random matches are more probable.
    """
    if len(df) < 15:
        return None

    col = f"SMA_{sma_period}"
    if col not in df.columns:
        return None

    # Scan last 10 bars for OHLC clustering on this SMA
    window_size = min(10, len(df) - 1)
    window = df.iloc[-window_size:]

    penny_touches = 0   # exact cent match ($0.00)
    near_touches = 0    # within $0.01
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

    # PRICE-ADJUSTED SIGNIFICANCE:
    # For a bar on a $P stock with typical range R cents:
    #   prob(any single OHLC matches SMA to cent) ≈ 1/R
    #   prob(at least one of 4 OHLC matches) ≈ 4/R (for large R)
    #   Expected touches over 10 bars ≈ 40/R
    #
    # We need actual touches to be at least 3x expected to be "disproportionate"
    cur = df.iloc[-1]
    current_price = (float(cur['Open']) + float(cur['High']) +
                     float(cur['Low']) + float(cur['Close'])) / 4
    if current_price <= 0:
        return None

    # Estimate typical bar range in cents (use actual data)
    bar_ranges = (window['High'] - window['Low']).dropna()
    if len(bar_ranges) == 0:
        return None
    avg_range_cents = float(bar_ranges.mean()) / 0.01  # convert to cent count
    if avg_range_cents < 1:
        avg_range_cents = 1

    # Expected random penny-exact touches: 4 OHLC checks per bar, 10 bars
    # Each check has ~1/avg_range_cents chance of exact cent match
    expected_penny = (4.0 * window_size) / avg_range_cents
    # Expected near ($0.01) touches: ~2x the penny chance (two extra cents)
    expected_near = expected_penny * 2
    expected_total = expected_penny + expected_near

    # "Disproportionate" = at least 3x expected AND minimum absolute counts
    # This scales naturally: $500 stock needs ~3 touches, $7 stock needs ~20+
    min_penny = max(3, int(expected_penny * 3))
    min_total = max(6, int(expected_total * 3))
    min_bars = max(3, int(window_size * 0.4))  # touches must span 40%+ of bars

    is_magnetized = (
        (penny_touches >= min_penny or total_touches >= min_total)
        and bars_with_touch >= min_bars
    )

    if not is_magnetized:
        return None

    current_sma = get_sma_value(df, sma_period)
    if current_sma is None:
        return None

    # Capitular low = risk level (deepest point of the drawdown)
    capitular_low = float(window['Low'].min())
    density = total_touches / max(1, window_size)

    return {
        "type": "optimized_buying_algorithm",
        "sma_period": sma_period,
        "sma_value": round(current_sma, 2),
        "penny_touches": penny_touches,
        "near_touches": near_touches,
        "total_touches": total_touches,
        "bars_with_touch": bars_with_touch,
        "window_size": window_size,
        "density": round(density, 2),
        "capitular_low": round(capitular_low, 2),
        "high_volatility": high_vol,
        "expected_penny": round(expected_penny, 2),
        "significance_ratio": round(penny_touches / max(0.01, expected_penny), 2),
        "system_context": system_context,
        "description": (
            f"MAGNETIZED BUY — SMA {sma_period} at {current_sma:.2f} | "
            f"{penny_touches} penny + {near_touches} near touches "
            f"across {bars_with_touch}/{window_size} bars | "
            f"{penny_touches / max(0.01, expected_penny):.1f}x expected | "
            f"Capitular low: {capitular_low:.2f}"
            f"{' | HIGH VOL' if high_vol else ''}"
        ),
    }


# =============================================================================
# SILENT OHLC INTERACTION COUNTING
# =============================================================================
# Counts every OHLC-to-SMA penny match across all outfits on a dataframe.
# This runs BEFORE detection logic and feeds the dominant outfit ranking.
# Only counts on the last N bars (scan window), not the entire history.

def count_ohlc_interactions(df, scan_bars=20):
    """
    Count OHLC-to-SMA exact penny matches per outfit on the last scan_bars bars.

    Returns dict: outfit_name -> hit_count
    Each hit = one OHLC field matching one SMA to the exact cent ($0.00).
    """
    if len(df) < 2:
        return {}

    window = df.iloc[-min(scan_bars, len(df)):]
    outfit_counts = {}

    for outfit_name, outfit in SMA_OUTFITS.items():
        hits = 0
        for sma_p in outfit["smas"]:
            col = f"SMA_{sma_p}"
            if col not in df.columns:
                continue

            for i in range(len(window)):
                row = window.iloc[i]
                if pd.isna(row.get(col)):
                    continue
                sma_at_bar = round(float(row[col]), 2)

                for field in ['Open', 'High', 'Low', 'Close']:
                    val = round(float(row[field]), 2)
                    if val == sma_at_bar:
                        hits += 1

        if hits > 0:
            outfit_counts[outfit_name] = hits

    return outfit_counts


# =============================================================================
# INSTITUTIONAL ACTIVITY DETECTION — OUTFIT-AGNOSTIC BASE LAYER
# =============================================================================
# Scans ALL bars near ANY SMA level (from any outfit) for abnormal activity:
#   - Volume ratio vs day average (elevated volume at level)
#   - Trade size sigma vs day average (large block orders)
#   - Delta (UpVolume - DownVolume) direction and magnitude
#   - Volume concentration (% of day's volume at this level)
#
# Bubbles are rendered whenever abnormal institutional activity is detected.
# Green = buy-side abnormality (net buying pressure), Red = sell-side.
# Direction is INFERRED from data, not assumed from detection type.

# Proximity band: bar is "near" an SMA if any OHLC field is within this %
PROXIMITY_PCT = 0.003   # 0.3%
PROXIMITY_MIN = 0.25    # or within $0.25, whichever is larger


def _bar_near_sma(row, sma_val):
    """Check if any OHLC field on this bar is within proximity of sma_val."""
    if sma_val is None or pd.isna(sma_val) or sma_val <= 0:
        return False
    band = max(PROXIMITY_MIN, sma_val * PROXIMITY_PCT)
    for field in ('Open', 'High', 'Low', 'Close'):
        if abs(float(row[field]) - sma_val) <= band:
            return True
    return False


def compute_institutional_signals(df, scan_bars=20):
    """
    Outfit-agnostic institutional activity detection.

    Scans the last `scan_bars` bars of `df` for abnormal institutional
    activity at ANY SMA level. For each SMA column present on the DataFrame,
    finds bars where OHLC is within the proximity band of the per-bar SMA
    value, then measures raw metrics on those bars.

    Args:
        df: DataFrame with OHLCV + UpVolume/DownVolume/TotalTicks columns
            and SMA_* columns already computed by compute_all_smas().
        scan_bars: Number of recent bars to scan.

    Returns:
        list of bubble dicts, one per SMA level with abnormal activity.
        Each dict contains raw metrics and inferred direction.
        Empty list if nothing abnormal found.
    """
    if len(df) < max(scan_bars, 5):
        return []

    window = df.iloc[-scan_bars:]

    has_tick_data = 'TotalTicks' in df.columns and window['TotalTicks'].sum() > 0
    has_delta_data = 'UpVolume' in df.columns and window['UpVolume'].sum() > 0

    if not has_delta_data and not has_tick_data:
        return []

    # Day baselines from full window
    day_total_vol = int(window['Volume'].sum())
    if day_total_vol == 0:
        return []

    day_avg_vol = day_total_vol / max(1, len(window))

    # Per-bar avg trade sizes for sigma baseline
    per_bar_trade_sizes = []
    if has_tick_data:
        for i in range(len(window)):
            r = window.iloc[i]
            t = int(r.get('TotalTicks', 0))
            v = int(r.get('Volume', 0))
            if t > 0:
                per_bar_trade_sizes.append(v / t)

    trade_size_mean = statistics.mean(per_bar_trade_sizes) if len(per_bar_trade_sizes) >= 3 else 0
    trade_size_std = statistics.stdev(per_bar_trade_sizes) if len(per_bar_trade_sizes) >= 3 else 0

    # Find all SMA columns on the df
    sma_cols = [c for c in df.columns if c.startswith('SMA_')]

    bubbles = []

    for sma_col in sma_cols:
        sma_period = int(sma_col.split('_')[1])

        # Collect bars near this SMA (using per-bar SMA value)
        near_indices = []
        for i in range(len(window)):
            row = window.iloc[i]
            sma_val = row.get(sma_col)
            if pd.isna(sma_val):
                continue
            if _bar_near_sma(row, float(sma_val)):
                near_indices.append(i)

        if not near_indices:
            continue

        near_rows = window.iloc[near_indices]
        near_vol = int(near_rows['Volume'].sum())
        near_bar_count = len(near_indices)

        # Use the SMA value from the most recent near-bar for display
        last_near_row = window.iloc[near_indices[-1]]
        sma_display_val = round(float(last_near_row[sma_col]), 2)

        # --- METRIC 1: Volume ratio vs day average ---
        avg_vol_at_level = near_vol / max(1, near_bar_count)
        vol_ratio = avg_vol_at_level / max(1, day_avg_vol)

        # --- METRIC 2: Trade size sigma ---
        trade_size_sigma = 0.0
        avg_trade_at_level = 0.0
        if has_tick_data:
            near_ticks = int(near_rows['TotalTicks'].sum())
            avg_trade_at_level = near_vol / max(1, near_ticks)
            if trade_size_std > 0:
                trade_size_sigma = (avg_trade_at_level - trade_size_mean) / trade_size_std

        # --- METRIC 3: Delta (direction inferred from data) ---
        net_delta = 0
        delta_pct = 0.0
        total_up = 0
        total_down = 0
        if has_delta_data:
            total_up = int(near_rows['UpVolume'].sum())
            total_down = int(near_rows['DownVolume'].sum())
            net_delta = total_up - total_down
            delta_total = total_up + total_down
            delta_pct = (net_delta / max(1, delta_total)) * 100  # -100 to +100

        # --- METRIC 4: Volume concentration (% of scanned volume at this level) ---
        vol_concentration = (near_vol / max(1, day_total_vol)) * 100

        # --- ABNORMALITY CHECK ---
        # Thresholds set high to surface only genuine institutional footprints,
        # not normal market noise. Must hit 2+ flags to qualify.
        flags = []

        if vol_ratio >= 3.0:
            flags.append(f"HIGH VOL {vol_ratio:.1f}x")

        if trade_size_sigma >= 2.5:
            flags.append(f"LARGE TRADES {trade_size_sigma:.1f}σ")

        if abs(delta_pct) >= 30:
            flags.append(f"DELTA {delta_pct:+.1f}%")

        if vol_concentration >= 25:
            flags.append(f"VOL CONC {vol_concentration:.1f}%")

        if len(flags) < 2:
            continue

        # Infer direction from delta
        if delta_pct > 5:
            direction = 'buy'
        elif delta_pct < -5:
            direction = 'sell'
        else:
            direction = 'neutral'

        # Which outfits contain this SMA period?
        matching_outfits = []
        for oname, odata in SMA_OUTFITS.items():
            if sma_period in odata["smas"]:
                matching_outfits.append(oname)

        bubbles.append({
            'sma_period': sma_period,
            'sma_value': sma_display_val,
            'direction': direction,  # 'buy', 'sell', or 'neutral'
            'flags': flags,
            'metrics': {
                'vol_ratio': round(vol_ratio, 2),
                'trade_size_sigma': round(trade_size_sigma, 2),
                'avg_trade_size': round(avg_trade_at_level, 1),
                'delta_pct': round(delta_pct, 1),
                'up_volume': total_up,
                'down_volume': total_down,
                'net_delta': net_delta,
                'vol_concentration': round(vol_concentration, 1),
                'near_bar_count': near_bar_count,
                'near_volume': near_vol,
            },
            'outfits': matching_outfits,
        })

    return bubbles


def should_bubble(bubble):
    """
    Determine if a bubble dict should be rendered. With the new outfit-agnostic
    detection, any bubble that made it through the abnormality check should render.

    Returns:
        (should_render, confidence) tuple.
    """
    if not bubble:
        return False, None

    flags = bubble.get('flags', [])
    if len(flags) >= 3:
        return True, 'high'
    elif len(flags) >= 2:
        return True, 'medium'
    return False, None


# =============================================================================
# MAIN ANALYSIS PIPELINE
# =============================================================================

OBA_CONSECUTIVE = 3  # minimum consecutive magnetized bars to fire OBA


def run_detections_on_df(df, ticker, display, sys_name, high_vol, timeframe_label):
    """
    Run all 4 detection types on a single dataframe (one ticker, one timeframe).

    Uses a per-(ticker, tf, sma_period) state machine that persists across cycles:
      None       → PBA/ASO entry conditions met → "pba"/"aso"
      "pba"      → blast-through (close < SMA) → None
                 → SPHS breach (OHLC ≤ SMA - $0.01) → "sphs_pba"
                 → bar clears above SMA (Low > SMA) → None
                 → magnetized 3+ bars → OBA fires (once per cluster)
      "aso"      → blast-through (close > SMA) → None
                 → SPHS breach (OHLC ≥ SMA + $0.01) → "sphs_aso"
                 → bar clears below SMA (High < SMA) → None
                 → magnetized 3+ bars → OBA fires (once per cluster)
      "sphs_pba" → bar clears above SMA → None
      "sphs_aso" → bar clears below SMA → None

    Returns dict: outfit_name -> list of detection dicts.
    """
    if df is None or len(df) < 2:
        return {}

    # --- Cold-start guard: skip first bar per (ticker, tf) ---
    tf_key = (display, timeframe_label)
    bar_ts = df.index[-1]
    if store.check_cold_start(tf_key, bar_ts):
        return {}

    system_context = {
        "sp500_state": store.get_system_state("S&P 500 System").get("state"),
        "nasdaq_state": store.get_system_state("NASDAQ System").get("state"),
        "dji_state": store.get_system_state("Dow Jones System").get("state"),
        "any_negative": store.is_any_system_negative(),
        "sp500_negative": store.is_system_negative("S&P 500 System"),
        "high_volatility": high_vol,
        "vix": store.vix_level,
    }

    all_detections = {}

    # Current bar OHLC + OHLC4
    bar = df.iloc[-1]
    o, h, l, c = float(bar['Open']), float(bar['High']), float(bar['Low']), float(bar['Close'])
    ohlc4 = (o + h + l + c) / 4
    ohlc = (o, h, l, c)

    for outfit_name, outfit in SMA_OUTFITS.items():
        outfit_dets = []
        outfit_sma_periods = outfit["smas"]

        for sma_p in outfit["smas"]:
            col = f"SMA_{sma_p}"
            if col not in df.columns:
                continue
            sma_val = df[col].iloc[-1]
            if pd.isna(sma_val):
                continue
            sma_val = float(sma_val)

            state_key = (display, timeframe_label, sma_p)
            cur_state = store.get_near_state(state_key)

            # Derived flags
            ohlc4_touches_ma = abs(round(ohlc4, 2) - round(sma_val, 2)) <= PENNY
            # SPHS: "singular penny breach" — any OHLC value breaches by EXACTLY
            # $0.01 (not $0.02+, which would be a blast-through, not a stop)
            sphs_breach_below = any(
                round(sma_val - v, 2) == PENNY for v in ohlc
                if v < sma_val
            )
            sphs_breach_above = any(
                round(v - sma_val, 2) == PENNY for v in ohlc
                if v > sma_val
            )
            bar_above_ma = l > sma_val    # entire bar above SMA
            bar_below_ma = h < sma_val    # entire bar below SMA
            bar_interacts = l <= sma_val <= h  # bar range straddles SMA

            # =============================================================
            # STATE: None — check for new PBA or ASO entry
            # =============================================================
            if cur_state is None:
                # Try PBA entry
                pba = detect_precision_buy(df, sma_p, system_context,
                                           outfit_sma_periods=outfit_sma_periods)
                if pba:
                    pba["timeframe"] = timeframe_label
                    store.set_near_state(state_key, "pba")
                    store.register_precision_level(display, sma_p, pba["sma_value"], outfit_name)
                    store.add_alert({
                        "ticker": display,
                        "severity": "critical",
                        "type": "precision_buy_algorithm",
                        "sma_period": sma_p,
                        "timeframe": timeframe_label,
                        "title": f"{display} PRECISION BUY SMA{sma_p} [{outfit_name}] {timeframe_label}",
                        "description": pba["description"] + f" | TF: {timeframe_label}",
                        "outfit": outfit_name,
                    })
                    outfit_dets.append(pba)
                    continue  # PBA fired, don't also check ASO on same bar

                # Try ASO entry (only if system-gated ticker)
                if sys_name:
                    aso = detect_auto_short(df, sma_p, system_context,
                                            ticker_system_name=sys_name,
                                            outfit_sma_periods=outfit_sma_periods)
                    if aso:
                        aso["timeframe"] = timeframe_label
                        store.set_near_state(state_key, "aso")
                        severity = "critical" if system_context.get("any_negative") else "high"
                        store.add_alert({
                            "ticker": display,
                            "severity": severity,
                            "type": "automated_short_order",
                            "sma_period": sma_p,
                            "timeframe": timeframe_label,
                            "title": f"{display} AUTO SHORT SMA{sma_p} [{outfit_name}] {timeframe_label}",
                            "description": aso["description"] + f" | TF: {timeframe_label}",
                            "outfit": outfit_name,
                        })
                        outfit_dets.append(aso)
                        continue

                # Also check OBA standalone (statistical clustering) even without active PBA/ASO
                oba = detect_optimized_buy(df, sma_p, high_vol, system_context)
                if oba:
                    oba["timeframe"] = timeframe_label
                    store.add_alert({
                        "ticker": display,
                        "severity": "high",
                        "type": "optimized_buying_algorithm",
                        "sma_period": sma_p,
                        "timeframe": timeframe_label,
                        "title": f"{display} MAGNETIZED BUY SMA{sma_p} [{outfit_name}] {timeframe_label}",
                        "description": oba["description"] + f" | TF: {timeframe_label}",
                        "outfit": outfit_name,
                    })
                    outfit_dets.append(oba)

            # =============================================================
            # STATE: "pba" — active PBA, monitor for SPHS/blast-through/OBA
            # =============================================================
            elif cur_state == "pba":
                if c < sma_val:
                    # Blast-through: close dropped below SMA → invalidate
                    store.set_near_state(state_key, None)  # also resets OBA
                elif sphs_breach_below:
                    # SPHS breach while PBA active
                    store.set_near_state(state_key, "sphs_pba")
                    store.reset_oba(state_key)
                    sma_rounded = round(sma_val, 2)
                    breach = round(sma_val - c, 2)
                    vol_avg = float(df['Volume'].iloc[max(0, len(df)-20):len(df)-1].mean()) if len(df) > 2 else 0
                    vol_ratio = float(bar['Volume']) / max(1, vol_avg)
                    sphs_det = {
                        "type": "singular_point_hard_stop",
                        "sma_period": sma_p,
                        "sma_value": sma_rounded,
                        "breach_amount": round(breach, 2),
                        "close": round(c, 2),
                        "low": round(l, 2),
                        "volume_ratio": round(vol_ratio, 2),
                        "timeframe": timeframe_label,
                        "system_context": system_context,
                        "description": (
                            f"HARD STOP — SMA {sma_p} at {sma_rounded:.2f} | "
                            f"Breach ${breach:.2f} | Close {c:.2f}, Low {l:.2f} | "
                            f"Vol {vol_ratio:.1f}x avg | STATE: pba→sphs_pba"
                        ),
                    }
                    store.add_alert({
                        "ticker": display,
                        "severity": "critical",
                        "type": "singular_point_hard_stop",
                        "sma_period": sma_p,
                        "timeframe": timeframe_label,
                        "title": f"{display} HARD STOP SMA{sma_p} [{outfit_name}] {timeframe_label}",
                        "description": sphs_det["description"] + f" | TF: {timeframe_label}",
                        "outfit": outfit_name,
                    })
                    outfit_dets.append(sphs_det)
                elif bar_above_ma:
                    # Bar entirely above SMA → interaction over, reset
                    store.set_near_state(state_key, None)
                else:
                    # Still interacting — check magnetization for OBA
                    if bar_interacts:
                        consec = store.increment_oba_consec(state_key)
                        if consec >= OBA_CONSECUTIVE and not store.is_oba_fired(state_key):
                            store.mark_oba_fired(state_key)
                            sma_rounded = round(sma_val, 2)
                            oba_det = {
                                "type": "optimized_buying_algorithm",
                                "sma_period": sma_p,
                                "sma_value": sma_rounded,
                                "consecutive_bars": consec,
                                "timeframe": timeframe_label,
                                "system_context": system_context,
                                "description": (
                                    f"MAGNETIZED BUY — SMA {sma_p} at {sma_rounded:.2f} | "
                                    f"{consec} consecutive magnetized bars | "
                                    f"STATE: active PBA cluster"
                                ),
                            }
                            store.add_alert({
                                "ticker": display,
                                "severity": "high",
                                "type": "optimized_buying_algorithm",
                                "sma_period": sma_p,
                                "timeframe": timeframe_label,
                                "title": f"{display} MAGNETIZED BUY SMA{sma_p} [{outfit_name}] {timeframe_label}",
                                "description": oba_det["description"] + f" | TF: {timeframe_label}",
                                "outfit": outfit_name,
                            })
                            outfit_dets.append(oba_det)
                    else:
                        store.reset_oba_consec(state_key)

            # =============================================================
            # STATE: "aso" — active ASO, mirror of PBA monitoring
            # =============================================================
            elif cur_state == "aso":
                if c > sma_val:
                    # Blast-through: close rose above SMA → invalidate
                    store.set_near_state(state_key, None)
                elif sphs_breach_above:
                    # SPHS breach while ASO active
                    store.set_near_state(state_key, "sphs_aso")
                    store.reset_oba(state_key)
                    sma_rounded = round(sma_val, 2)
                    breach = round(c - sma_val, 2)
                    sphs_det = {
                        "type": "singular_point_hard_stop",
                        "sma_period": sma_p,
                        "sma_value": sma_rounded,
                        "breach_amount": round(breach, 2),
                        "close": round(c, 2),
                        "high": round(h, 2),
                        "timeframe": timeframe_label,
                        "system_context": system_context,
                        "description": (
                            f"HARD STOP — SMA {sma_p} at {sma_rounded:.2f} | "
                            f"Breach above ${breach:.2f} | Close {c:.2f}, High {h:.2f} | "
                            f"STATE: aso→sphs_aso"
                        ),
                    }
                    store.add_alert({
                        "ticker": display,
                        "severity": "critical",
                        "type": "singular_point_hard_stop",
                        "sma_period": sma_p,
                        "timeframe": timeframe_label,
                        "title": f"{display} HARD STOP SMA{sma_p} [{outfit_name}] {timeframe_label}",
                        "description": sphs_det["description"] + f" | TF: {timeframe_label}",
                        "outfit": outfit_name,
                    })
                    outfit_dets.append(sphs_det)
                elif bar_below_ma:
                    # Bar entirely below SMA → interaction over, reset
                    store.set_near_state(state_key, None)
                else:
                    # Still interacting — check magnetization for OBA
                    if bar_interacts:
                        consec = store.increment_oba_consec(state_key)
                        if consec >= OBA_CONSECUTIVE and not store.is_oba_fired(state_key):
                            store.mark_oba_fired(state_key)
                            sma_rounded = round(sma_val, 2)
                            oba_det = {
                                "type": "optimized_buying_algorithm",
                                "sma_period": sma_p,
                                "sma_value": sma_rounded,
                                "consecutive_bars": consec,
                                "timeframe": timeframe_label,
                                "system_context": system_context,
                                "description": (
                                    f"MAGNETIZED — SMA {sma_p} at {sma_rounded:.2f} | "
                                    f"{consec} consecutive magnetized bars | "
                                    f"STATE: active ASO cluster"
                                ),
                            }
                            store.add_alert({
                                "ticker": display,
                                "severity": "high",
                                "type": "optimized_buying_algorithm",
                                "sma_period": sma_p,
                                "timeframe": timeframe_label,
                                "title": f"{display} MAGNETIZED SMA{sma_p} [{outfit_name}] {timeframe_label}",
                                "description": oba_det["description"] + f" | TF: {timeframe_label}",
                                "outfit": outfit_name,
                            })
                            outfit_dets.append(oba_det)
                    else:
                        store.reset_oba_consec(state_key)

            # =============================================================
            # STATE: "sphs_pba" — waiting for bar to clear above SMA
            # =============================================================
            elif cur_state == "sphs_pba":
                if bar_above_ma:
                    store.set_near_state(state_key, None)

            # =============================================================
            # STATE: "sphs_aso" — waiting for bar to clear below SMA
            # =============================================================
            elif cur_state == "sphs_aso":
                if bar_below_ma:
                    store.set_near_state(state_key, None)

        if outfit_dets:
            if outfit_name not in all_detections:
                all_detections[outfit_name] = []
            all_detections[outfit_name].extend(outfit_dets)

    return all_detections


def analyze_ticker(ticker, high_vol):
    """
    Full analysis pipeline for one ticker:

    INDEX TICKERS (^GSPC, ^IXIC, ^DJI):
      - Fetch at their system timeframe (30m, 30m, 15m)
      - Evaluate system state
      - Run detections on that single timeframe

    NON-INDEX TICKERS (ETFs):
      - Fetch at ALL 11 outfit timeframes (1m thru 4h)
      - Run detections on EACH timeframe
      - No system state evaluation
    """
    try:
        display = TICKER_DISPLAY.get(ticker, ticker)
        sys_name = TICKER_SYSTEM_MAP.get(ticker)
        is_primary = sys_name and SYSTEM_PRIMARY_TICKERS.get(sys_name) == ticker
        ts_symbol = yf_to_ts_symbol(ticker)

        combined_detections = {}
        chart_df = None
        chart_sma_vals = {}
        total_det_count = 0
        best_df = None  # full df for institutional signal computation

        # Determine timeframes to scan
        if ticker in SYSTEM_TIMEFRAMES:
            # INDEX TICKER: single system timeframe
            tf_minutes = SYSTEM_TIMEFRAMES[ticker]
            timeframes = [tf_minutes]
        else:
            # NON-INDEX TICKER: all outfit timeframes
            timeframes = OUTFIT_TIMEFRAMES

        for tf in timeframes:
            # Compute barsback: need enough bars for longest SMA (999) + buffer
            barsback = min(1200, 57600)

            # Timeframe label for display
            if tf >= 60:
                tf_label = f"{tf // 60}H"
            else:
                tf_label = f"{tf}M"

            df = ts.get_bars(ts_symbol, tf, 'Minute', barsback)
            if df.empty:
                continue

            # Cleanse raw bars (outlier correction, structural validation)
            df = cleanse_bars(df)
            if df.empty:
                continue

            # Compute SMAs
            all_sma_values = compute_all_smas(df)

            # Silent OHLC interaction counting (feeds dominant outfit ranking)
            interaction_counts = count_ohlc_interactions(df, scan_bars=20)
            for outfit_name_ic, hit_count in interaction_counts.items():
                store.record_interactions(display, outfit_name_ic, hit_count)

            # System state evaluation (index tickers only)
            if is_primary:
                config = SMA_OUTFITS[sys_name]
                state = evaluate_system_state(df, config, high_vol)
                if state:
                    state["ticker"] = display
                    store.set_system_state(sys_name, state)

                    if state.get("changed"):
                        store.add_alert({
                            "ticker": display,
                            "severity": "critical",
                            "type": "system_state_change",
                            "title": f"{sys_name} → {state['state']}",
                            "description": (
                                f"{sys_name} FLIPPED to {state['state']}. "
                                f"{state['eval_detail']} "
                                f"({'VOL REGIME' if state['eval_method'] == 'volatility_regime' else 'NORMAL'})"
                            ),
                            "outfit": sys_name,
                        })

                    if state.get("at_key_level"):
                        store.add_alert({
                            "ticker": display,
                            "severity": "critical",
                            "type": "key_level",
                            "title": f"{display} AT KEY LEVEL SMA{state['key_level_sma']}",
                            "description": (
                                f"Price {state['price']} at SMA{state['key_level_sma']} "
                                f"({state['key_level_value']}) — "
                                f"recovery/downturn determinant | Breach: {state['key_breach']}"
                            ),
                            "outfit": sys_name,
                        })

            # Run detections
            tf_detections = run_detections_on_df(df, ticker, display, sys_name, high_vol, tf_label)
            for outfit_name, dets in tf_detections.items():
                if outfit_name not in combined_detections:
                    combined_detections[outfit_name] = []
                combined_detections[outfit_name].extend(dets)
                total_det_count += len(dets)

            # Use 30m data for chart display (or whatever the first timeframe is)
            if chart_df is None or tf == 30:
                chart_df = df.tail(200).copy()
                best_df = df.copy()  # keep full df for institutional signals
                chart_sma_vals = {}
                for outfit_name, outfit in SMA_OUTFITS.items():
                    outfit_vals = {}
                    for p in outfit["smas"]:
                        outfit_vals[p] = all_sma_values.get(p)
                    chart_sma_vals[outfit_name] = outfit_vals

        # Compute dominant outfit for this ticker after all timeframes scanned
        dominant = store.compute_dominant_outfit(display)

        # Filter detections: only keep those from the dominant outfit
        # Non-dominant detections were counted but their alerts are suppressed
        if dominant:
            dominant_name = dominant["outfit"]
            filtered_detections = {}
            filtered_count = 0
            for outfit_name_f, dets in combined_detections.items():
                if outfit_name_f == dominant_name:
                    filtered_detections[outfit_name_f] = dets
                    filtered_count += len(dets)
            combined_detections = filtered_detections
            total_det_count = filtered_count

            # Also filter alerts: remove any alerts from this cycle for
            # non-dominant outfits on this ticker
            with store.lock:
                store.alerts = [
                    a for a in store.alerts
                    if a.get('ticker') != display
                    or a.get('outfit') == dominant_name
                    or a.get('type') in ('system_state_change', 'key_level')
                ]

        # =====================================================================
        # INSTITUTIONAL ACTIVITY — BUBBLE COMPUTATION (OUTFIT-AGNOSTIC)
        # =====================================================================
        # Scan ALL SMA levels on best_df for abnormal institutional activity.
        # Decoupled from dominant outfit — any SMA where OHLC interacts and
        # metrics are abnormal gets a bubble. Green=buy, Red=sell.
        ticker_bubbles = []
        if best_df is not None and len(best_df) > 20:
            raw_bubbles = compute_institutional_signals(best_df, scan_bars=20)
            for bub in raw_bubbles:
                render, confidence = should_bubble(bub)
                if render:
                    bub['confidence'] = confidence
                    ticker_bubbles.append(bub)

        store.set_bubbles(display, ticker_bubbles)

        # Store chart data
        if chart_df is not None:
            chart_df.index = chart_df.index.strftime('%Y-%m-%d %H:%M')
            store.update(display, chart_df, chart_sma_vals, combined_detections)

        price_str = ""
        if chart_df is not None and len(chart_df) > 0:
            price_str = f" @ {float(chart_df['Close'].iloc[-1]):.2f}"

        tf_str = ", ".join(f"{t}m" if t < 60 else f"{t//60}h" for t in timeframes)
        dom_str = f" | DOM: {dominant['outfit']} ({dominant['count']} hits, {dominant['ratio']}x)" if dominant else " | no dominant outfit"
        bubble_str = f" | BUBBLES: {len(ticker_bubbles)}" if ticker_bubbles else ""
        print(f"  [OK] {display}{price_str} -- {total_det_count} detections [{tf_str}]{dom_str}{bubble_str}")

    except Exception as e:
        print(f"  [ERR] {TICKER_DISPLAY.get(ticker, ticker)}: {e}")
        import traceback
        traceback.print_exc()


# =============================================================================
# ANALYSIS LOOP
# =============================================================================

def analysis_loop():
    """Background loop: fetch VIX, then analyze all tickers. Repeat every 60s."""
    while True:
        ts = datetime.now().strftime('%H:%M:%S')
        print(f"\n{'='*60}")
        print(f"  [{ts}] Analysis cycle starting")
        print(f"{'='*60}")

        # Clear dedup keys for new cycle
        store.clear_cycle_dedup()

        # Fetch VIX for volatility regime
        vix = fetch_vix()
        high_vol = store.high_volatility
        if vix is not None:
            regime = "HIGH VOLATILITY" if high_vol else "NORMAL"
            print(f"  VIX: {vix:.2f} — {regime}")
        else:
            print(f"  VIX: unavailable — defaulting to normal regime")

        # Analyze each ticker
        for ticker in TICKERS:
            analyze_ticker(ticker, high_vol)

        # Print system states summary
        states = store.get_all_system_states()
        if states:
            print(f"\n  SYSTEM STATES:")
            for name, s in states.items():
                print(f"    {name}: {s.get('state', '?')} ({s.get('eval_detail', '')})")

        ts2 = datetime.now().strftime('%H:%M:%S')
        print(f"\n  [{ts2}] Cycle complete. Next in 60s.")
        time.sleep(60)


# =============================================================================
# FLASK API
# =============================================================================

@app.route('/api/snapshot')
def api_snapshot():
    return jsonify(store.get_snapshot())

@app.route('/api/alerts')
def api_alerts():
    with store.lock:
        return jsonify({"alerts": list(store.alerts[-200:])})

@app.route('/api/chart/<ticker>')
def api_chart(ticker):
    result = store.get_chart_data(ticker.upper())
    if result is None:
        return jsonify({"error": "No data"}), 404
    df, sma_vals = result
    records = []
    for idx, row in df.iterrows():
        record = {
            "time": idx,
            "open": round(row['Open'], 2),
            "high": round(row['High'], 2),
            "low": round(row['Low'], 2),
            "close": round(row['Close'], 2),
            "volume": int(row['Volume']),
        }
        for col in df.columns:
            if col.startswith('SMA_'):
                val = row[col]
                if not pd.isna(val):
                    record[col] = round(val, 2)
        records.append(record)
    return jsonify({"ticker": ticker.upper(), "bars": records, "sma_outfits": sma_vals})

@app.route('/api/detections')
def api_detections():
    return jsonify(store.get_detections())

@app.route('/api/outfits')
def api_outfits():
    return jsonify({
        name: {"smas": cfg["smas"], "description": cfg["description"]}
        for name, cfg in SMA_OUTFITS.items()
    })

@app.route('/api/dominant')
def api_dominant():
    """Dominant outfit per ticker + all interaction counts."""
    return jsonify({
        "dominant_outfits": store.get_all_dominant_outfits(),
        "interaction_counts": store.get_all_interaction_counts(),
    })

@app.route('/api/bubbles')
def api_bubbles():
    """Institutional activity bubbles for all tickers."""
    return jsonify({"bubbles": store.get_all_bubbles()})

@app.route('/api/bubbles/<ticker>')
def api_bubbles_ticker(ticker):
    """Institutional activity bubbles for a specific ticker."""
    return jsonify({"ticker": ticker.upper(), "bubbles": store.get_bubbles(ticker.upper())})

@app.route('/api/groups')
def api_groups():
    return jsonify({
        group: [TICKER_DISPLAY.get(t, t) for t in tickers]
        for group, tickers in TICKER_GROUPS.items()
    })

@app.route('/')
def index():
    return "SMA Alert Engine v2 running. Dashboard at sma_alerts.html"


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("  SMA ALERT ENGINE v3 — TradeStation + Multi-Timeframe")
    print(f"  Tickers: {len(TICKERS)} across {len(TICKER_GROUPS)} groups")
    for grp, tickers_list in TICKER_GROUPS.items():
        names = [TICKER_DISPLAY.get(t, t) for t in tickers_list]
        print(f"    {grp}: {', '.join(names)}")
    print(f"  SMA Outfits: {len(SMA_OUTFITS)} (ALL applied to ALL tickers)")
    print(f"  Systems: S&P [10/50/200] 30M, NASDAQ [20/100/250] 30M, DJI [30/60/90/300/600/900] 15M")
    print(f"  Detection timeframes: {', '.join(str(t)+'m' if t < 60 else str(t//60)+'h' for t in OUTFIT_TIMEFRAMES)}")
    print(f"  No system: Russell 2000, VIX (ASO skipped)")
    print(f"  Precision: ${PENNY} (penny-level)")
    print(f"  Alert Types: Precision Buy | Hard Stop | Auto Short | Optimized Buy")
    print(f"  Data: TradeStation API v3")
    print("=" * 60)

    thread = threading.Thread(target=analysis_loop, daemon=True)
    thread.start()

    app.run(host='0.0.0.0', port=5050, debug=False)
