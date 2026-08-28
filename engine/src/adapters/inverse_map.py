"""
Inverse / Leveraged → Underlying → Index map

Thesis: sma outfit is the catalyst that triggers trend shift; the vehicle
is often a leveraged/inverse ETF that inversely correlates with the
accumulation target. Bearish vehicles (SQQQ, DOG, SPXU, SDS, SDOW) spike
as the market is shocked lower → capitulation → OPEX pin → accumulation
in the index (IXIC/SPX/DJI) marks the bottom.

Example from user: Mar 4-5 2026 DOG bought = bearish DOG vehicle shocks
Dow lower into March Triple Witching, while banks silently accumulate IXIC.
DOG is short Dow (1× inverse), so DOG ↑ = DJI ↓, and DJI ↓ in that window
was capitulation that resolved with IXIC bottom.

This module is the Rosetta stone so the engine can join a firing in DOG
to what happened in IXIC/SPX on the same clock without manual lookup.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class InversePair:
    vehicle: str       # what the outfit fires on (e.g. DOG)
    underlying: str    # ETF it tracks inversely (e.g. DIA)
    index: str         # index it ultimately shorts (e.g. DJI / $DJX.X)
    leverage: str      # e.g. "-1×", "-2×", "2×", "3×"
    direction: str     # "inverse" or "leveraged"
    # For correlation: vehicle ↑ when index ↓
    index_symbol_ts: str  # TradeStation symbol for the index

# Master map — extend as new vehicles appear in case studies
# Keep canonical uppercase; lookup is case-insensitive.
_INVERSE_MAP_RAW = {
    # Dow family
    "DOG":  InversePair("DOG",  "DIA",  "DJI",  "-1×", "inverse", "$DJX.X"),
    "DDM":  InversePair("DDM",  "DIA",  "DJI",  "2×",  "leveraged", "$DJX.X"),
    "UDOW": InversePair("UDOW", "DIA",  "DJI",  "3×",  "leveraged", "$DJX.X"),
    "SDOW": InversePair("SDOW", "DIA",  "DJI",  "-2×", "inverse", "$DJX.X"),
    # S&P family
    "SH":   InversePair("SH",   "SPY",  "SPX",  "-1×", "inverse", "$SPX.X"),
    "SDS":  InversePair("SDS",  "SPY",  "SPX",  "-2×", "inverse", "$SPX.X"),
    "SPXU": InversePair("SPXU", "SPY",  "SPX",  "-3×", "inverse", "$SPX.X"),
    "SPXS": InversePair("SPXS", "SPY",  "SPX",  "-3×", "inverse", "$SPX.X"),
    "SSO":  InversePair("SSO",  "SPY",  "SPX",  "2×",  "leveraged", "$SPX.X"),
    "SPXL": InversePair("SPXL", "SPY",  "SPX",  "3×",  "leveraged", "$SPX.X"),
    "UPRO": InversePair("UPRO", "SPY",  "SPX",  "3×",  "leveraged", "$SPX.X"),
    # Nasdaq family
    "PSQ":  InversePair("PSQ",  "QQQ",  "IXIC", "-1×", "inverse", "$NDX.X"),
    "QID":  InversePair("QID",  "QQQ",  "IXIC", "-2×", "inverse", "$NDX.X"),
    "SQQQ": InversePair("SQQQ", "QQQ",  "IXIC", "-3×", "inverse", "$NDX.X"),
    "QLD":  InversePair("QLD",  "QQQ",  "IXIC", "2×",  "leveraged", "$NDX.X"),
    "TQQQ": InversePair("TQQQ", "QQQ",  "IXIC", "3×",  "leveraged", "$NDX.X"),
    # Small-cap
    "RWM":  InversePair("RWM",  "IWM",  "RUT",  "-1×", "inverse", "$RUT.X"),
    "TZA":  InversePair("TZA",  "IWM",  "RUT",  "-3×", "inverse", "$RUT.X"),
    "TNA":  InversePair("TNA",  "IWM",  "RUT",  "3×",  "leveraged", "$RUT.X"),
    "UWM":  InversePair("UWM",  "IWM",  "RUT",  "2×",  "leveraged", "$RUT.X"),
    # Volatility (special: SVIX/SQQQ vol vehicles)
    "SVIX": InversePair("SVIX", "VIX",  "VIX",  "-1×", "inverse", "$VIX.X"),
    "VIXY": InversePair("VIXY", "VIX",  "VIX",  "1×",  "leveraged", "$VIX.X"),
    "UVIX": InversePair("UVIX", "VIX",  "VIX",  "1×",  "leveraged", "$VIX.X"),
    # Gold inverse (from gap findings: GLL)
    "GLL":  InversePair("GLL",  "GLD",  "GOLD", "-2×", "inverse", "GLD"),
    # --- Gap-anomaly vehicles (high media in 2025-08 → 2026-08 gap, not in engine) ---
    # Discovered by Miner: UCO 31, VIXY 21, DUST 17, MSTX 16, SCO 13, UVIX 14, TZA 10, GLL 7, SOXS/SOXS etc already covered
    # Energy / Oil
    "UCO":  InversePair("UCO",  "OIL",  "OIL",  "2×",  "leveraged", "USO"),
    "SCO":  InversePair("SCO",  "OIL",  "OIL",  "-2×", "inverse", "USO"),
    # VIX family extension
    "VIXY": InversePair("VIXY", "VIX",  "VIX",  "1×",  "leveraged", "$VIX.X"),
    # Gold miners inverse
    "DUST": InversePair("DUST", "GDX",  "GOLD", "-2×", "inverse", "GDX"),
    # MicroStrategy leveraged (MSTX 16 media, MSTU, MSTX, MSTR)
    "MSTX": InversePair("MSTX", "MSTR", "MSTR", "2×",  "leveraged", "MSTR"),
    "MSTU": InversePair("MSTU", "MSTR", "MSTR", "2×",  "leveraged", "MSTR"),
    "MSTR": InversePair("MSTR", "MSTR", "MSTR", "1×",  "underlying", "MSTR"),
    # Small-cap / Russell extended
    "TZA":  InversePair("TZA",  "IWM",  "RUT",  "-3×", "inverse", "$RUT.X"),
    "UVIX": InversePair("UVIX", "VIX",  "VIX",  "2×",  "leveraged", "$VIX.X"),
    # Tech / Semi already have SOXS/SOXL, add YANG, FAS etc.
    "YANG": InversePair("YANG", "FXI",  "FXI",  "-3×", "inverse", "FXI"),
    "FAS":  InversePair("FAS",  "XLF",  "XLF",  "3×",  "leveraged", "XLF"),
    "XLF":  InversePair("XLF",  "XLF",  "XLF",  "1×",  "underlying", "XLF"),

    # Keep DIA/QQQ/SPY themselves as "underlying" self-maps for convenience
    "DIA":  InversePair("DIA",  "DIA",  "DJI",  "1×",  "underlying", "$DJX.X"),
    "QQQ":  InversePair("QQQ",  "QQQ",  "IXIC", "1×",  "underlying", "$NDX.X"),
    "SPY":  InversePair("SPY",  "SPY",  "SPX",  "1×",  "underlying", "$SPX.X"),
    "IWM":  InversePair("IWM",  "IWM",  "RUT",  "1×",  "underlying", "$RUT.X"),
    "IXIC": InversePair("IXIC", "QQQ",  "IXIC", "1×",  "index", "$NDX.X"),
    "SPX":  InversePair("SPX",  "SPY",  "SPX",  "1×",  "index", "$SPX.X"),
    "DJI":  InversePair("DJI",  "DIA",  "DJI",  "1×",  "index", "$DJX.X"),
}

INVERSE_MAP = {k.upper(): v for k, v in _INVERSE_MAP_RAW.items()}

def get_inverse_pair(ticker: str) -> Optional[InversePair]:
    """Case-insensitive lookup. Returns None if ticker is not a known vehicle/underlying."""
    return INVERSE_MAP.get(ticker.strip().upper()) if ticker else None

def underlying_for(ticker: str) -> Optional[str]:
    p = get_inverse_pair(ticker)
    return p.underlying if p else None

def index_for(ticker: str) -> Optional[str]:
    p = get_inverse_pair(ticker)
    return p.index if p else None

def accumulation_target_for(vehicle_ticker: str) -> Optional[str]:
    """
    For a bearish vehicle bought (e.g. DOG), what index is being capitulated
    and then accumulated? DOG → DJI (but user's Mar 2026 example: DOG shock
    → IXIC accumulation, so cross-index capitulation is allowed — this returns
    the vehicle's own index; the bridge layer will broaden to SPX/IXIC/DJI).
    """
    p = get_inverse_pair(vehicle_ticker)
    return p.index if p else None

# Convenience: the three major indexes for bottom detection
MAJOR_INDEXES = {
    "SPX": "$SPX.X",
    "IXIC": "$NDX.X",
    "DJI": "$DJX.X",
    "RUT": "$RUT.X",
    "VIX": "$VIX.X",
}
