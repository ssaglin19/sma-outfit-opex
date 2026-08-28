"""
Gap Index — bridges the 2,211 undocumented posts (2025-08-21 → 2026-08-21) to the engine.

Miner found:
- 2,211 gap rows, 2,103 needs_vision, 1,955 missing outfit, 36 MAs not in engine (21,41,42…)
- 79 tickers in gap, 37 not in engine (UCO 31 media, VIXY 21, DUST 17, MSTX 16…)
- 138 named_outfit variants, 81 MA ladders, 16 catalog timeframes empty, 500s/9m/8m missing from engine
- Temporal burst: 2026-04 396 posts, 2026-03 335 posts — March-April 2026 is the event-horizon cluster

This module gives the bridge a way to query gap without vision: it indexes gap_findings.jsonl
and joins each row to its OPEX horizon (via opex.py) and to its inverse pair (via inverse_map.py).

No pandas, no network — stdlib only, reads the JSONL already on disk.
"""
from __future__ import annotations
import json
import pathlib
from collections import Counter
from typing import List, Dict, Optional
from .opex import OPEXCalendar
from .inverse_map import get_inverse_pair

_GAP_PATH = pathlib.Path(__file__).resolve().parents[3] / "archive" / "analysis" / "gap_findings.jsonl"
# fallback for repo root when running from engine/src
if not _GAP_PATH.exists():
    _GAP_PATH = pathlib.Path("/mnt/c/Users/ssagl/sma-outfit-opex/archive/analysis/gap_findings.jsonl")

def _load_gap() -> List[Dict]:
    if not _GAP_PATH.exists():
        return []
    with open(_GAP_PATH, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]

_GAP = _load_gap()
_CAL = OPEXCalendar()

def gap_stats() -> Dict:
    """Quick profiling for the miner report."""
    if not _GAP:
        return {"gap_rows": 0}
    return {
        "gap_rows": len(_GAP),
        "needs_vision": sum(1 for g in _GAP if g.get("needs_vision")),
        "missing_outfit": sum(1 for g in _GAP if "outfit" in g.get("missing", [])),
        "has_media": sum(1 for g in _GAP if g.get("has_media")),
        "unique_tickers": len(set(g.get("ticker") for g in _GAP if g.get("ticker"))),
        "unique_ma": len(set(g.get("ma_designation") for g in _GAP if g.get("ma_designation"))),
        "by_month": dict(Counter(g.get("date","")[:7] for g in _GAP).most_common(6)),
        "top_tickers": Counter(g.get("ticker") for g in _GAP if g.get("ticker")).most_common(6),
    }

def query_gap(ticker: Optional[str] = None, has_media: Optional[bool] = None, limit: int = 100) -> List[Dict]:
    """Filter gap rows and attach horizon + inverse metadata."""
    out=[]
    for g in _GAP:
        if ticker and g.get("ticker") != ticker.upper():
            continue
        if has_media is not None and g.get("has_media") != has_media:
            continue
        # attach horizon
        date = g.get("date","")
        horizon = None
        try:
            if date:
                horizon = _CAL.resolve_event_horizon(date)
        except: pass
        pair = get_inverse_pair(g.get("ticker","")) if g.get("ticker") else None
        out.append({**g, "_horizon": horizon, "_inverse": pair.__dict__ if pair else None})
        if len(out) >= limit:
            break
    return out

def cluster_months() -> Dict[str, int]:
    """Temporal clustering — March-April 2026 burst is the anomaly."""
    return dict(Counter(g.get("date","")[:7] for g in _GAP))

def tickers_not_in_engine(engine_tickers: List[str]) -> List[Dict]:
    """Anomaly: tickers in gap but not in engine TICKERS."""
    eng=set(t.upper() for t in engine_tickers)
    cnt=Counter(g.get("ticker") for g in _GAP if g.get("ticker"))
    return [{"ticker": t, "gap_count": c, "media": sum(1 for g in _GAP if g.get("ticker")==t and g.get("has_media"))} for t,c in cnt.items() if t not in eng]

def mas_not_in_engine(engine_mas: List[int]) -> List[int]:
    """Anomaly: MA periods mentioned in gap but not in engine ALL_SMA."""
    import re
    eng=set(engine_mas)
    mas=[]
    for g in _GAP:
        ma=g.get("ma_designation")
        if ma: mas.extend(int(x) for x in re.findall(r"MA(\d+)", ma) if x.isdigit())
    return sorted(set(mas) - eng)
