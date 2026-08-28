"""
TradeStation API Client
========================
Handles authentication (token refresh), bar data fetching, quote snapshots,
and options chain data.

Endpoints used:
  GET /v3/marketdata/barcharts/{symbol}   — OHLCV + volume delta + tick data
  GET /v3/marketdata/quotes/{symbols}     — real-time quote snapshot (bid/ask/VWAP)
  GET /v3/marketdata/options/expirations/{underlying} — option expirations
  GET /v3/marketdata/options/strikes/{underlying}     — option strikes
  Stream endpoints (future): market depth, option chains

Auth: OAuth 2.0 Bearer token, refreshed from refresh_token.
"""

import requests
import os
import time
import pandas as pd
from datetime import datetime

TOKEN_URL = 'https://signin.tradestation.com/oauth/token'
API_BASE = 'https://api.tradestation.com/v3'


def load_env(env_path=None):
    """Load .env file from same directory as this module."""
    if env_path is None:
        env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    env = {}
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if '=' in line and not line.startswith('#'):
                    k, v = line.split('=', 1)
                    env[k.strip()] = v.strip()
    return env


class TradeStationClient:
    """Handles token refresh and market data requests."""

    def __init__(self):
        env = load_env()
        self.client_id = env.get('TS_CLIENT_ID', '')
        self.client_secret = env.get('TS_CLIENT_SECRET', '')
        self.refresh_token = env.get('TS_REFRESH_TOKEN', '')
        self.access_token = None
        self.token_expiry = 0  # epoch time

        if not self.client_id or not self.refresh_token:
            raise ValueError("TS_CLIENT_ID and TS_REFRESH_TOKEN must be set in .env. Run ts_auth.py first.")

    def _refresh_access_token(self):
        """Exchange refresh_token for a new access_token."""
        resp = requests.post(TOKEN_URL, data={
            'grant_type': 'refresh_token',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': self.refresh_token,
        })
        if resp.status_code != 200:
            raise Exception(f"Token refresh failed ({resp.status_code}): {resp.text}")

        tokens = resp.json()
        self.access_token = tokens['access_token']
        # Token expires in ~1200 seconds (20 min), refresh a bit early
        self.token_expiry = time.time() + tokens.get('expires_in', 1200) - 60

        # If a new refresh_token was issued, update it
        new_refresh = tokens.get('refresh_token')
        if new_refresh and new_refresh != self.refresh_token:
            self.refresh_token = new_refresh
            self._save_refresh_token(new_refresh)

    def _save_refresh_token(self, token):
        """Update refresh token in .env file."""
        env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
        if not os.path.exists(env_path):
            return
        with open(env_path, 'r') as f:
            content = f.read()
        lines = content.split('\n')
        new_lines = []
        found = False
        for line in lines:
            if line.startswith('TS_REFRESH_TOKEN'):
                new_lines.append(f'TS_REFRESH_TOKEN={token}')
                found = True
            else:
                new_lines.append(line)
        if not found:
            new_lines.append(f'TS_REFRESH_TOKEN={token}')
        with open(env_path, 'w') as f:
            f.write('\n'.join(new_lines))

    def _get_headers(self):
        """Get auth headers, refreshing token if needed."""
        if self.access_token is None or time.time() >= self.token_expiry:
            self._refresh_access_token()
        return {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json',
        }

    def get_bars(self, symbol, interval, unit='Minute', barsback=5000,
                 firstdate=None, lastdate=None):
        """
        Fetch historical OHLCV bars.

        Args:
            symbol: Ticker symbol (e.g., 'SPY', '$SPX.X')
            interval: Bar interval integer (e.g., 1, 3, 5, 10, 15, 20, 30)
            unit: 'Minute', 'Daily', 'Weekly', 'Monthly'
            barsback: Number of bars to fetch (max 57600 for Minute).
                      Ignored if firstdate is provided.
            firstdate: ISO date string (e.g., '2025-06-01') — start of range
            lastdate: ISO date string (e.g., '2026-03-03') — end of range

        Returns:
            pandas DataFrame with columns: Open, High, Low, Close, Volume,
            UpVolume, DownVolume, UpTicks, DownTicks, UnchangedVolume,
            UnchangedTicks, TotalTicks.
            Index is datetime. Returns empty DataFrame on error.
        """
        url = f"{API_BASE}/marketdata/barcharts/{symbol}"
        params = {
            'interval': interval,
            'unit': unit,
            # No sessiontemplate = default regular session (0930-1600 EST)
        }
        if firstdate:
            params['firstdate'] = firstdate
            if lastdate:
                params['lastdate'] = lastdate
        else:
            params['barsback'] = barsback

        try:
            resp = requests.get(url, headers=self._get_headers(), params=params)

            # Token expired mid-request — retry once
            if resp.status_code == 401:
                self.access_token = None
                resp = requests.get(url, headers=self._get_headers(), params=params)

            if resp.status_code != 200:
                print(f"  [API ERR] {symbol} {interval}{unit[0]}: {resp.status_code}")
                try:
                    print(f"  [API BODY] {resp.text[:500]}")
                except Exception:
                    pass
                return pd.DataFrame()

            data = resp.json()
            bars = data.get('Bars', [])
            if not bars:
                return pd.DataFrame()

            records = []
            for bar in bars:
                records.append({
                    'Open': float(bar.get('Open', 0)),
                    'High': float(bar.get('High', 0)),
                    'Low': float(bar.get('Low', 0)),
                    'Close': float(bar.get('Close', 0)),
                    'Volume': int(bar.get('TotalVolume', 0)),
                    'UpVolume': int(bar.get('UpVolume', 0)),
                    'DownVolume': int(bar.get('DownVolume', 0)),
                    'UpTicks': int(bar.get('UpTicks', 0)),
                    'DownTicks': int(bar.get('DownTicks', 0)),
                    'UnchangedVolume': int(bar.get('UnchangedVolume', 0)),
                    'UnchangedTicks': int(bar.get('UnchangedTicks', 0)),
                    'TotalTicks': int(bar.get('TotalTicks', 0)),
                    'Timestamp': bar.get('TimeStamp', ''),
                })

            df = pd.DataFrame(records)
            df['Timestamp'] = pd.to_datetime(df['Timestamp'])
            df.set_index('Timestamp', inplace=True)
            df.sort_index(inplace=True)
            return df

        except Exception as e:
            print(f"  [ERR] {symbol} {interval}{unit[0]}: {e}")
            return pd.DataFrame()


    def get_quote_snapshot(self, symbols):
        """
        Fetch real-time quote snapshot for one or more symbols.

        Args:
            symbols: Single symbol string or list of symbols (max ~50)

        Returns:
            dict: symbol -> {Bid, Ask, BidSize, AskSize, Last, Volume, VWAP, ...}
            Returns empty dict on error.
        """
        if isinstance(symbols, list):
            symbols_str = ','.join(symbols)
        else:
            symbols_str = symbols

        url = f"{API_BASE}/marketdata/quotes/{symbols_str}"

        try:
            resp = requests.get(url, headers=self._get_headers())

            if resp.status_code == 401:
                self.access_token = None
                resp = requests.get(url, headers=self._get_headers())

            if resp.status_code != 200:
                print(f"  [API ERR] Quote snapshot: {resp.status_code}")
                return {}

            data = resp.json()
            quotes = data.get('Quotes', [])
            result = {}
            for q in quotes:
                sym = q.get('Symbol', '')
                result[sym] = {
                    'Bid': float(q.get('Bid', 0)),
                    'Ask': float(q.get('Ask', 0)),
                    'BidSize': int(q.get('BidSize', 0)),
                    'AskSize': int(q.get('AskSize', 0)),
                    'Last': float(q.get('Last', 0)),
                    'Volume': int(q.get('Volume', 0)),
                    'VWAP': float(q.get('VWAP', 0)),
                    'High52Week': float(q.get('High52Week', 0)),
                    'Low52Week': float(q.get('Low52Week', 0)),
                    'NetChange': float(q.get('NetChange', 0)),
                    'PreviousClose': float(q.get('PreviousClose', 0)),
                }
            return result

        except Exception as e:
            print(f"  [ERR] Quote snapshot: {e}")
            return {}

    def get_option_expirations(self, underlying):
        """
        Fetch available option expiration dates for an underlying symbol.

        Returns:
            list of expiration date strings, or empty list on error.
        """
        url = f"{API_BASE}/marketdata/options/expirations/{underlying}"
        try:
            resp = requests.get(url, headers=self._get_headers())
            if resp.status_code == 401:
                self.access_token = None
                resp = requests.get(url, headers=self._get_headers())
            if resp.status_code != 200:
                return []
            data = resp.json()
            return data.get('Expirations', [])
        except Exception as e:
            print(f"  [ERR] Option expirations {underlying}: {e}")
            return []

    def get_option_strikes(self, underlying, expiration=None):
        """
        Fetch option chain strikes with volume, OI, and Greeks.

        Args:
            underlying: e.g. 'SPXU'
            expiration: specific expiration date string, or None for nearest

        Returns:
            list of option dicts with Strike, Type, Volume, OpenInterest,
            Bid, Ask, Delta, Gamma, IV, etc. Empty list on error.
        """
        url = f"{API_BASE}/marketdata/options/strikes/{underlying}"
        params = {}
        if expiration:
            params['expiration'] = expiration

        try:
            resp = requests.get(url, headers=self._get_headers(), params=params)
            if resp.status_code == 401:
                self.access_token = None
                resp = requests.get(url, headers=self._get_headers(), params=params)
            if resp.status_code != 200:
                return []
            data = resp.json()
            return data.get('Strikes', data.get('Options', []))
        except Exception as e:
            print(f"  [ERR] Option strikes {underlying}: {e}")
            return []


# Mapping from yfinance-style symbols to TradeStation symbols
YF_TO_TS = {
    '^GSPC': '$SPX.X',
    '^IXIC': '$NDX.X',      # NASDAQ 100 — closest available (NASDAQ Composite not available intraday)
    '^DJI': '$DJX.X',       # Dow Jones 1/100 scale — SMA crossovers identical to full index
    '^VIX': '$VIX.X',
}


def yf_to_ts_symbol(yf_symbol):
    """Convert yfinance symbol to TradeStation symbol. ETFs unchanged."""
    return YF_TO_TS.get(yf_symbol, yf_symbol)
