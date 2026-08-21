"""
Data Source Abstraction Layer
==============================
Provides a common interface for fetching OHLCV bar data.
Swap implementations without changing downstream code.

Current: TradeStation (interim)
Target:  Lightspeed (per repo spec)

To add a new data source:
  1. Subclass DataSource
  2. Implement get_bars()
  3. Update get_data_source() factory
"""

import os
import pandas as pd
from abc import ABC, abstractmethod


class DataSource(ABC):
    """Abstract base for market data providers."""

    @abstractmethod
    def get_bars(self, symbol, interval_minutes, bars_back=5000):
        """
        Fetch OHLCV bars for a symbol at a given interval.

        Args:
            symbol: Ticker symbol (standard form, e.g. 'SPY', 'SPXU', 'SPX')
            interval_minutes: Bar interval in minutes (1, 2, 3, 5, 10, 15, 20, 30, 60, 120, 240)
            bars_back: Number of historical bars to fetch

        Returns:
            pd.DataFrame with columns: Open, High, Low, Close, Volume
            Index: DatetimeIndex (UTC)
            Empty DataFrame on error.
        """
        pass

    @abstractmethod
    def translate_symbol(self, ticker):
        """
        Convert a standard ticker name to this source's symbol format.
        E.g. 'SPX' → '$SPX.X' for TradeStation
        """
        pass


class TradeStationSource(DataSource):
    """
    TradeStation API v3 — interim data source.
    Uses USEQ24Hour session template for correct SMA values.
    """

    def __init__(self):
        from ts_client import TradeStationClient
        self.client = TradeStationClient()
        self.symbol_map = {
            "SPX":   "$SPX.X",
            "IXIC":  "$NDX.X",
            "DJI":   "$DJX.X",
            "VIX":   "$VIX.X",
            "TNX":   "$TNX.X",
            "DXY":   "$DXY.X",
            "BRK-B": "BRK.B",
        }

    def translate_symbol(self, ticker):
        return self.symbol_map.get(ticker, ticker)

    def get_bars(self, symbol, interval_minutes, bars_back=57600):
        ts_symbol = self.translate_symbol(symbol)

        # TradeStation limit: 500,000 intraday minutes per request
        max_bars = min(bars_back, 500_000 // interval_minutes)

        # TradeStation uses 'Minute' unit for all intraday
        df = self.client.get_bars(
            ts_symbol,
            interval=interval_minutes,
            unit='Minute',
            barsback=max_bars,
        )

        if df.empty:
            return df

        # Normalize columns to standard names
        cols = {'Open': 'Open', 'High': 'High', 'Low': 'Low', 'Close': 'Close', 'Volume': 'Volume'}
        df = df[list(cols.keys())].rename(columns=cols)
        return df


class LightspeedSource(DataSource):
    """
    Lightspeed data source — placeholder for future implementation.
    When Lightspeed is set up, implement get_bars() to pull from
    Lightspeed's data feed or exported files.
    """

    def __init__(self):
        raise NotImplementedError(
            "Lightspeed data source not yet configured. "
            "Use TradeStation as interim: DATA_SOURCE=tradestation in .env"
        )

    def translate_symbol(self, ticker):
        # Lightspeed uses standard ticker symbols
        return ticker

    def get_bars(self, symbol, interval_minutes, bars_back=5000):
        raise NotImplementedError("Lightspeed integration pending")


class CSVSource(DataSource):
    """
    CSV file data source — for manual imports.
    Reads OHLCV data from CSV files in a specified directory.

    Expected directory structure:
      csv_data/
        {ticker}/
          {ticker}_{interval}m.csv

    CSV format:
      Timestamp,Open,High,Low,Close,Volume
      2026-03-01 09:30:00,50.00,50.50,49.80,50.25,100000
    """

    def __init__(self, data_dir=None):
        if data_dir is None:
            data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'csv_data')
        self.data_dir = data_dir

    def translate_symbol(self, ticker):
        return ticker

    def get_bars(self, symbol, interval_minutes, bars_back=5000):
        filepath = os.path.join(self.data_dir, symbol, f"{symbol}_{interval_minutes}m.csv")
        if not os.path.exists(filepath):
            return pd.DataFrame()

        df = pd.read_csv(filepath, parse_dates=['Timestamp'], index_col='Timestamp')
        df = df.sort_index()

        # Return last N bars
        if bars_back and len(df) > bars_back:
            df = df.iloc[-bars_back:]

        return df[['Open', 'High', 'Low', 'Close', 'Volume']]


def get_data_source(source_name=None):
    """
    Factory: return the configured data source.
    Reads DATA_SOURCE from .env if source_name not specified.

    Options: 'tradestation' (default), 'lightspeed', 'csv'
    """
    if source_name is None:
        env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
        if os.path.exists(env_path):
            with open(env_path) as f:
                for line in f:
                    if line.strip().startswith('DATA_SOURCE='):
                        source_name = line.strip().split('=', 1)[1].strip().lower()
                        break
        if source_name is None:
            source_name = 'tradestation'

    if source_name == 'tradestation':
        return TradeStationSource()
    elif source_name == 'lightspeed':
        return LightspeedSource()
    elif source_name == 'csv':
        return CSVSource()
    else:
        raise ValueError(f"Unknown data source: {source_name}. Use 'tradestation', 'lightspeed', or 'csv'.")
