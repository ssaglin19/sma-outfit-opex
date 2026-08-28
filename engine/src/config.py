"""
SMA Alert System — Configuration
==================================
All 26 outfits, full ticker list, timeframes, and InfluxDB settings.
Source of truth: https://github.com/raultrades/SMA-outfits/README.md
"""

# ──────────────────────────────────────────────
# InfluxDB Connection
# ──────────────────────────────────────────────
INFLUXDB_URL = "http://localhost:8086"
INFLUXDB_TOKEN = "sma-alerts-token"       # set after influx setup
INFLUXDB_ORG = "sma-alerts"
INFLUXDB_BUCKET = "market_data"

# ──────────────────────────────────────────────
# SMA Parameter Range (per repo: 1–999)
# ──────────────────────────────────────────────
SMA_MIN = 1
SMA_MAX = 999

# ──────────────────────────────────────────────
# 25 SMA Outfits — from repo README raw data table
# ──────────────────────────────────────────────
SMA_OUTFITS = {
    "S&P (10/50/200)":                  [10, 50, 200],
    "NAS (20/100/250)":                 [20, 100, 250],
    "DJI (30/60/90/300/600/900)":       [30, 60, 90, 300, 600, 900],
    "AN (33/66/99/333/666/999)":        [33, 66, 99, 333, 666, 999],
    "AN (11/44/88/111/444/888)":        [11, 44, 88, 111, 444, 888],
    "AN (22/55/77/222/555/777)":        [22, 55, 77, 222, 555, 777],
    "Waring's Problem (19/37/73/143/279/548)": [19, 37, 73, 143, 279, 548],
    "Base 2/NVDA (16/32/64/128/256/512)": [16, 32, 64, 128, 256, 512],
    "TSLA (27/53/105/210/420/840)":     [27, 53, 105, 210, 420, 840],
    "Time/365 (23/46/91/183/365/730)":  [23, 46, 91, 183, 365, 730],
    "Time/366 (23/46/92/183/366/732)":  [23, 46, 92, 183, 366, 732],
    "Time/1440 (18/36/72/144/288/576)": [18, 36, 72, 144, 288, 576],
    "Resource Missing/404 (25/51/101/202/404/808)": [25, 51, 101, 202, 404, 808],
    "US President/45 (29/57/114/227/455/911)": [29, 57, 114, 227, 455, 911],
    "US President/46 (23/46/92/184/368/736)": [23, 46, 92, 184, 368, 736],
    "US President/47 (24/47/94/188/376/752)": [24, 47, 94, 188, 376, 752],
    "Speaker House/56 (28/56/112/224/448/896)": [28, 56, 112, 224, 448, 896],
    "WTC/911 (28/57/114/228/456/911)":  [28, 57, 114, 228, 456, 911],
    "Russia 2000 (16/31/63/125/250/500)": [16, 31, 63, 125, 250, 500],
    "China Chair (28/56/112/224/448/976)": [28, 56, 112, 224, 448, 976],
    "France President (25/50/100/200/400/600)": [25, 50, 100, 200, 400, 600],
    "SVIX (26/52/106/211/422/844)":     [26, 52, 106, 211, 422, 844],
    "Turkey President (24/48/96/192/384/768)": [24, 48, 96, 192, 384, 768],
    "Alphabet (25/50/100/200/400/800)": [25, 50, 100, 200, 400, 800],
    "Regression (27/54/108/216/432/864)": [27, 54, 108, 216, 432, 864],
    "56 Reversal (28/55/111/221/442/884)":   [28, 55, 111, 221, 442, 884],
    "Tesla Cipher (39/78/156/311/622/944)":  [39, 78, 156, 311, 622, 944],
    "Apple Cipher (31/61/122/244/446/668)":  [31, 61, 122, 244, 446, 668],
    "BIT1 (16/31/62/124/248/746)":           [16, 31, 62, 124, 248, 746],
    "BIT2 (16/31/62/124/246/748)":           [16, 31, 62, 124, 246, 748],
    "GOOG (50/100/200/400/800)":             [50, 100, 200, 400, 800],
    "OIL (29/58/116/232/464/898)":           [29, 58, 116, 232, 464, 898],
    "SOXS (26/51/102/204/408/816)":          [26, 51, 102, 204, 408, 816],
}

# Collect all unique SMA periods referenced by outfits
ALL_OUTFIT_SMAS = sorted(set(p for smas in SMA_OUTFITS.values() for p in smas))

# ──────────────────────────────────────────────
# The Three Systems (midterm trend protocols)
# ──────────────────────────────────────────────
SYSTEMS = {
    "S&P 500": {
        "symbol": "$SPX.X",
        "timeframes": ["30m"],
        "smas": [10, 50, 200],
        "positive": "MA10 > MA50",
        "negative": "MA10 < MA50",
        "volatile_pivot": "MA50",
    },
    "NASDAQ": {
        "symbol": "$NDX.X",
        "timeframes": ["20m", "30m"],
        "smas": [20, 100, 250],
        "positive": "MA20 > MA100",
        "negative": "MA20 < MA100",
        "volatile_pivot": "MA100",
    },
    "Dow Jones": {
        "symbol": "$DJX.X",
        "timeframes": ["15m", "1h"],
        "smas": [30, 60, 90, 300, 600, 900],
        "positive": "MA90 > MA300",
        "negative": "MA90 < MA300",
        "volatile_pivot": "MA300",
    },
}

# ──────────────────────────────────────────────
# Timeframes (from repo: minute to 4h for intraday)
# ──────────────────────────────────────────────
TIMEFRAMES = [
    {"label": "1m",  "interval": 1,  "unit": "Minute"},
    {"label": "2m",  "interval": 2,  "unit": "Minute"},
    {"label": "3m",  "interval": 3,  "unit": "Minute"},
    {"label": "5m",  "interval": 5,  "unit": "Minute"},
    {"label": "10m", "interval": 10, "unit": "Minute"},
    {"label": "15m", "interval": 15, "unit": "Minute"},
    {"label": "20m", "interval": 20, "unit": "Minute"},
    {"label": "30m", "interval": 30, "unit": "Minute"},
    {"label": "1h",  "interval": 60, "unit": "Minute"},
    {"label": "2h",  "interval": 120, "unit": "Minute"},
    {"label": "4h",  "interval": 240, "unit": "Minute"},
]

# ──────────────────────────────────────────────
# Data Source (set DATA_SOURCE in .env)
# ──────────────────────────────────────────────
# Target: Lightspeed (per repo spec)
# Interim: TradeStation (until Lightspeed is configured)
# Options: 'tradestation', 'lightspeed', 'csv'
DATA_SOURCE = "tradestation"

# ──────────────────────────────────────────────
# Full Ticker List — from repo README
# ──────────────────────────────────────────────
TICKERS = [
    # Indices
    "SPX", "IXIC", "DJI", "VIX",
    # S&P 500 ETFs (leveraged/inverse)
    "SPY", "UPRO", "SPXU", "SPXL", "SSO", "SDS", "SPXS", "SH",
    # NASDAQ ETFs (leveraged/inverse)
    "QQQ", "TQQQ", "SQQQ", "QLD", "QID", "PSQ",
    # Dow ETFs (leveraged/inverse)
    "DIA", "UDOW", "SDOW", "DDM", "DXD", "DOG",
    # Russell ETFs
    "IWM", "UWM", "TNA", "RWM",
    # Volatility ETFs
    "VXX", "SVIX", "UVXY", "SVXY",
    # Semiconductor ETFs
    "SOXS", "SOXL",
    # Energy / Commodity ETFs
    "ERX", "GUSH", "DRIP", "BOIL", "USO",
    # Other ETFs
    "WEBS", "LABU", "DRN", "REK", "GLD", "TLT", "TBT", "BITO",
    # Mega-cap equities
    "AAPL", "MSFT", "AMZN", "GOOG", "NVDA", "META", "TSLA",
    # Other equities
    "AMD", "NFLX", "INTC", "COIN", "QCOM", "PYPL",
    "UPST", "RBLX", "AI", "ARM",
    "BRK-B", "GM", "JPM", "V", "UNH", "ENPH",
    # Leveraged single-stock
    "AAPD", "AAPU", "TSLT", "TSLQ",
    # Additional equities
    "ORCX",
    # International
    "BABA", "TSM",
]

# ──────────────────────────────────────────────
# Data Source API config
# ──────────────────────────────────────────────
# TradeStation (interim) settings
TS_SESSION_TEMPLATE = "USEQ24Hour"
TS_MAX_BARS_BACK = 57600   # API max for Minute bars

# How many bars we need for SMA 999 + buffer
# On USEQ24Hour (~22 bars/day for 30m), 999 SMA needs ~999 bars minimum
# For 1m bars, 999 SMA needs 999 bars = ~45 days of 1m data
# We fetch max available and compute what we can

# Lightspeed (target) settings — configure when ready
# LIGHTSPEED_HOST = "localhost"
# LIGHTSPEED_PORT = 8000
