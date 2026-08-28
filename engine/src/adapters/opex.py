"""
OPEX Calendar — Python port of engine/public/calendar/opex_entries.js

Rules (2023-01-01 .. 2026-12-31, plus any future range):
  Monthly OPEX     3rd Friday of every month.
  Triple Witching  3rd Friday of Mar/Jun/Sep/Dec emits Triple Witching INSTEAD of Monthly.
  VIX Expiration   3rd-Friday(next month) minus 30 days (normally Wed). If that lands on
                   weekend/holiday, roll back to preceding business day.

Holiday handling: NYSE closures hardcoded in JS; we port the same set.

This gives the event-horizon anchor: any SMA outfit firing resolves into the
next OPEX (or VIX) window. Example: DOG bought Mar 4-5 2026 → Triple Witching
Mar 20 2026 → IXIC bottom.
"""
from __future__ import annotations
import calendar
import datetime
from dataclasses import dataclass
from typing import List, Optional

# NYSE holidays that affect 2023-2027 3rd Fridays / VIX Wednesdays
# Sourced from NYSE calendar; same set as opex_entries.js generator.
NYSE_HOLIDAYS = {
    # 2023
    "2023-01-02", "2023-01-16", "2023-02-20", "2023-04-07", "2023-05-29", "2023-06-19", "2023-07-04", "2023-09-04", "2023-11-23", "2023-12-25",
    # 2024
    "2024-01-01", "2024-01-15", "2024-02-19", "2024-03-29", "2024-05-27", "2024-06-19", "2024-07-04", "2024-09-02", "2024-11-28", "2024-12-25",
    # 2025
    "2025-01-01", "2025-01-20", "2025-02-17", "2025-04-18", "2025-05-26", "2025-06-19", "2025-07-04", "2025-09-01", "2025-11-27", "2025-12-25",
    # 2026
    "2026-01-01", "2026-01-19", "2026-02-16", "2026-04-03", "2026-05-25", "2026-06-19", "2026-07-03", "2026-09-07", "2026-11-26", "2026-12-25",
    # 2027
    "2027-01-01", "2027-01-18", "2027-02-15", "2027-03-26", "2027-05-31", "2027-06-19", "2027-07-05", "2027-09-06", "2027-11-25", "2027-12-24",
}

TRIPLE_MONTHS = {3, 6, 9, 12}

@dataclass(frozen=True)
class OPEXEvent:
    date: datetime.date
    kind: str  # "Monthly OPEX" | "Triple Witching" | "VIX Expiration"
    label: str
    category: str
    weekday: str
    holiday_adjusted: bool

def _third_friday(year: int, month: int) -> datetime.date:
    """Return 3rd Friday of month."""
    c = calendar.monthcalendar(year, month)
    fridays = [week[calendar.FRIDAY] for week in c if week[calendar.FRIDAY] != 0]
    return datetime.date(year, month, fridays[2])

def _is_business_day(d: datetime.date) -> bool:
    return d.weekday() < 5 and d.isoformat() not in NYSE_HOLIDAYS

def _roll_back_to_business_day(d: datetime.date) -> tuple[datetime.date, bool]:
    """Roll back to preceding business day if d is weekend/holiday."""
    orig = d
    while not _is_business_day(d):
        d -= datetime.timedelta(days=1)
    return d, (d != orig)

def _vix_expiration_for_month(year: int, month: int) -> OPEXEvent:
    """VIX expiration for given month = 3rd Friday of NEXT month minus 30 days."""
    # next month
    ny, nm = (year, month + 1) if month < 12 else (year + 1, 1)
    third_fri_next = _third_friday(ny, nm)
    raw = third_fri_next - datetime.timedelta(days=30)
    adj, holiday_adjusted = _roll_back_to_business_day(raw)
    return OPEXEvent(
        date=adj,
        kind="VIX Expiration",
        label="VIX Expiration",
        category="VIX Expiration",
        weekday=adj.strftime("%a"),
        holiday_adjusted=holiday_adjusted,
    )

def _monthly_or_triple(year: int, month: int) -> OPEXEvent:
    raw = _third_friday(year, month)
    adj, holiday_adjusted = _roll_back_to_business_day(raw)
    is_triple = month in TRIPLE_MONTHS
    kind = "Triple Witching" if is_triple else "Monthly OPEX"
    return OPEXEvent(
        date=adj,
        kind=kind,
        label=kind,
        category=kind,
        weekday=adj.strftime("%a"),
        holiday_adjusted=holiday_adjusted,
    )

class OPEXCalendar:
    """Deterministic OPEX calendar. No network, no Influx."""
    def __init__(self, start: str = "2023-01-01", end: str = "2026-12-31"):
        self.start = datetime.date.fromisoformat(start)
        self.end = datetime.date.fromisoformat(end)
        self.events: List[OPEXEvent] = self._build()

    def _build(self) -> List[OPEXEvent]:
        evs: List[OPEXEvent] = []
        y, m = self.start.year, self.start.month
        while True:
            cur = datetime.date(y, m, 1)
            if cur > self.end:
                break
            # VIX for this month
            vix = _vix_expiration_for_month(y, m)
            if self.start <= vix.date <= self.end:
                evs.append(vix)
            # Monthly / Triple
            mt = _monthly_or_triple(y, m)
            if self.start <= mt.date <= self.end:
                evs.append(mt)
            # next month
            m += 1
            if m > 12:
                m = 1
                y += 1
        evs.sort(key=lambda e: e.date)
        return evs

    def next_opex(self, after: datetime.date | str, kind: Optional[str] = None) -> Optional[OPEXEvent]:
        """Next event strictly after `after`. If kind given, filter to that kind."""
        if isinstance(after, str):
            after = datetime.date.fromisoformat(after)
        for e in self.events:
            if e.date > after and (kind is None or e.kind == kind):
                return e
        return None

    def resolve_event_horizon(self, firing_date: datetime.date | str, window_days: int = 25) -> dict:
        """
        For a SMA outfit firing date, find the next Triple Witching within window,
        else next Monthly OPEX. This is the 'event horizon' the thesis refers to:
        DOG Mar 4-5 → Triple Mar 20 (within 15d) = valid horizon.
        """
        if isinstance(firing_date, str):
            firing_date = datetime.date.fromisoformat(firing_date)
        triple = self.next_opex(firing_date, kind="Triple Witching")
        monthly = self.next_opex(firing_date, kind="Monthly OPEX")
        # Prefer triple if within window
        chosen = None
        if triple and (triple.date - firing_date).days <= window_days:
            chosen = triple
        elif monthly and (monthly.date - firing_date).days <= window_days:
            chosen = monthly
        elif triple:
            chosen = triple
        else:
            chosen = monthly
        vix = self.next_opex(firing_date, kind="VIX Expiration")
        return {
            "firing_date": firing_date.isoformat(),
            "triple_witching": triple.date.isoformat() if triple else None,
            "monthly_opex": monthly.date.isoformat() if monthly else None,
            "vix_expiration": vix.date.isoformat() if vix else None,
            "event_horizon": chosen.date.isoformat() if chosen else None,
            "event_horizon_kind": chosen.kind if chosen else None,
            "days_to_horizon": (chosen.date - firing_date).days if chosen else None,
        }

# Module-level helpers for glue code
_DEFAULT_CAL = OPEXCalendar()

def next_opex(after: str | datetime.date, kind: Optional[str] = None) -> Optional[OPEXEvent]:
    return _DEFAULT_CAL.next_opex(after, kind)

def resolve_event_horizon(firing_date: str | datetime.date, window_days: int = 25) -> dict:
    return _DEFAULT_CAL.resolve_event_horizon(firing_date, window_days)
