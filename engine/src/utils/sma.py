import pandas as pd
def compute_sma(closes, period):
    return closes.rolling(period).mean() if hasattr(closes, "rolling") else sum(closes[-period:])/period
def compute_all_smas(df):
    # placeholder — real impl in detector.py, keep signature
    return {}
def cleanse_bars(df):
    return df.dropna() if hasattr(df, "dropna") else df
