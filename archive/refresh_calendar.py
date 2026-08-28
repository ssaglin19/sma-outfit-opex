r"""Daily incremental refresh: discover new @UnfairMarket posts, extract, append.

RUN:  py -3 archive\refresh_calendar.py        (or via refresh_calendar.bat)

HOW IT FINDS NEW POSTS
  Wayback's CDX index. Measured 2026-08-26: every one of 3,000 sampled posts was
  archived the SAME DAY it was posted (median lag 0). CDX *indexing* trails a few
  hours, so a post made today lands here tomorrow -- T+1, by design, not a bug.
  No X API, no key, no login, no scraping of x.com.

HOW IT READS THEM
  cdn.syndication.twimg.com/tweet-result -- X's own public embed backend. It now
  requires a derived `token` param; without it the endpoint returns a bare {} and
  looks broken. See _token(). Older scripts in this repo predate that change.

NON-DESTRUCTIVE, APPEND-ONLY
  Writes ONLY calendar/auto_entries.js. It never touches the curated layers
  (entries.js, gap_entries.js, finding_entries.js) and never renumbers or
  rewrites an entry it already emitted -- overlay notes and hides are keyed to
  post_id, so re-running must only ever add.

Every emitted entry carries provenance:"auto". Extraction is text-only and
unreviewed; keeping it in its own layer means a bad extraction stays visible and
toggleable rather than blending into curated data.
"""
import datetime
import json
import math
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CAL = os.path.join(HERE, "calendar")
OUT = os.path.join(CAL, "auto_entries.js")
STATE = os.path.join(HERE, "_auto_state.json")

HANDLE = "UnfairMarket"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
CDX = ("https://web.archive.org/cdx/search/cdx?url=twitter.com/{h}/status/*"
       "&output=json&fl=timestamp,original&collapse=urlkey&limit=-{n}")
SYND = "https://cdn.syndication.twimg.com/tweet-result?id={i}&lang=en&token={t}"

CDX_ROWS = 3000          # newest N unique post URLs to consider per run
FETCH_PAUSE = 1.0        # seconds between syndication calls -- do not hammer
CTX = ssl.create_default_context()


# --------------------------------------------------------------------------- net
def _get(url, timeout=60, tries=3):
    """Return (status, body). Never raises -- callers treat failure as 'skip'."""
    for attempt in range(tries):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            if e.code in (404, 403):        # gone / protected -- not retryable
                return e.code, b""
            if attempt == tries - 1:
                return e.code, b""
        except Exception:
            if attempt == tries - 1:
                return "ERR", b""
        time.sleep(2 * (attempt + 1))       # archive.org throttles; back off
    return "ERR", b""


def _b36(n):
    d = "0123456789abcdefghijklmnopqrstuvwxyz"
    i, frac = int(n), n - int(n)
    s = ""
    while i:
        s = d[i % 36] + s
        i //= 36
    s = s or "0"
    f = ""
    for _ in range(20):
        frac *= 36
        k = int(frac)
        f += d[k]
        frac -= k
    return s + "." + f


def _token(tid):
    """X's syndication token. Omit it and tweet-result returns a bare {}."""
    return _b36((int(tid) / 1e15) * math.pi).replace("0", "").replace(".", "")


def snowflake_date(tid):
    ms = (int(tid) >> 22) + 1288834974657
    return datetime.datetime.fromtimestamp(ms / 1000.0, datetime.timezone.utc).date()


# ------------------------------------------------------------------- vocabulary
def load_vocab():
    """Ticker vocabulary: the calendar's own direction map, plus engine config."""
    vocab = set()
    td = os.path.join(CAL, "ticker_direction.js")
    if os.path.exists(td):
        vocab |= set(re.findall(r'"([A-Z][A-Z0-9]{0,6})"\s*:',
                                open(td, encoding="utf-8", errors="replace").read()))
    cfg = os.path.join(os.path.dirname(HERE), "engine", "config.py")
    if os.path.exists(cfg):
        s = open(cfg, encoding="utf-8", errors="replace").read()
        m = re.search(r"TICKERS\s*=\s*\[(.*?)\n\]", s, re.S)
        if m:
            vocab |= set(re.findall(r'"([A-Z][A-Z0-9]{0,6})"', m.group(1)))
    return vocab


STOP = {"MA", "SMA", "ER", "US", "OHLC", "IRL", "ETF", "AM", "PM", "EOD", "CPI",
        "FOMC", "GDP", "PPI", "ATH", "OK", "AI", "THE", "AND", "OR", "IF", "ALL",
        "NEW", "BUY", "SELL", "LONG", "SHORT", "HIGH", "LOW", "PRC", "XI"}

ACTION_PATTERNS = [                       # order matters: first match wins
    ("purchased", r"\b(purchas\w+|bought|picked up|i'?m long|went long|accumulat\w+)\b"),
    ("cut",       r"\b(cut the trade|cutting|i cut|stopped out|hard stop)\b"),
    ("sold",      r"\b(sold|selling|exited|closed the)\b"),
    ("hold",      r"\b(holding|i am holding|i'?m holding|still hold|continue to hold)\b"),
]
RE_PRICE = re.compile(r"\b(\d{1,6}\.\d{2})\b")
RE_TF = re.compile(r"\b(\d{1,3})\s?(s|sec|m|min|M|h|hr|H|d|D)\b")
RE_MA = re.compile(r"\bMA\s?(\d{1,4})\b", re.I)      # he writes "ma100" lowercase
RE_BRACKET = re.compile(r"\[(\d{2,4})\]")
RE_RATIO = re.compile(r"\b\d{2,3}/\d{2,3}(?:/\d{2,3})*\b")   # "[20/100]", "33/66/99"
RE_NAMED = re.compile(r"([A-Z0-9][\w'&/.\- ]{1,38}?)\s+(?:SMA\s+)?[Oo]utfit\b")


def extract(text, vocab):
    """Literal text extraction only. Anything not clearly stated stays empty."""
    t = re.sub(r"\s+", " ", text or "").strip()
    low = t.lower()

    tickers = []
    for cand in re.findall(r"\$([A-Z]{1,6})\b", t):          # explicit $TICKER wins
        if cand not in STOP and cand not in tickers:
            tickers.append(cand)
    for cand in re.findall(r"\b([A-Z]{2,6})\b", t):          # bare, must be known
        if cand in vocab and cand not in STOP and cand not in tickers:
            tickers.append(cand)

    action = ""
    for name, pat in ACTION_PATTERNS:
        if re.search(pat, low):
            action = name
            break

    prices = []
    for p in RE_PRICE.findall(t):
        if p not in prices:
            prices.append(p)

    tf = ""
    mt = RE_TF.search(t)
    if mt:
        unit = {"sec": "s", "min": "m", "hr": "h"}.get(mt.group(2).lower(), mt.group(2).lower())
        tf = mt.group(1) + unit

    named = ""
    nm = RE_NAMED.search(t)
    if nm:
        cand = re.sub(r"^(the|its|it'?s|a|an|my)\s+", "", nm.group(1).strip(" ,.;:"), flags=re.I)
        if cand and len(cand) <= 40:
            named = cand + " outfit"

    # ma_designation is ANY moving-average reference: a single "ma100" counts.
    # Kept separate from a full named ladder because one MA reference is enough
    # to make a post a finding, which is how he actually writes in replies.
    desig = []
    for b in dict.fromkeys(RE_RATIO.findall(t)):
        desig.append(b)
    for b in dict.fromkeys(RE_BRACKET.findall(t)):
        if b not in desig:
            desig.append("[" + b + "]")
    mas = list(dict.fromkeys(x for x in RE_MA.findall(t)))
    if mas:
        desig.append(" ".join("MA" + x for x in mas))
    ma_designation = " / ".join(dict.fromkeys(desig))

    outfit = " / ".join(x for x in (named, ma_designation) if x)
    return {"tickers": tickers, "action": action, "prices": prices,
            "timeframe": tf, "outfit": outfit,
            "named_outfit": named, "ma_designation": ma_designation}


# ------------------------------------------------------------------------ state
def load_state():
    if os.path.exists(STATE):
        try:
            return json.load(open(STATE, encoding="utf-8"))
        except Exception:
            pass
    return {}


def seed_watermark():
    """First run: start after the newest post_id the calendar already carries."""
    best = 0
    for name in ("gap_entries.js", "finding_entries.js", "auto_entries.js"):
        p = os.path.join(CAL, name)
        if not os.path.exists(p):
            continue
        for m in re.finditer(r'"post_id"\s*:\s*"(\d{15,25})"',
                             open(p, encoding="utf-8", errors="replace").read()):
            best = max(best, int(m.group(1)))
    return best


def curated_ids():
    """post_ids already carried by the CURATED layers. Never emit a duplicate of
    one -- that would put the same post on the calendar twice under two types."""
    ids = set()
    for name in ("entries.js", "gap_entries.js", "finding_entries.js"):
        p = os.path.join(CAL, name)
        if os.path.exists(p):
            ids |= set(re.findall(r'"post_id"\s*:\s*"(\d{15,25})"',
                                  open(p, encoding="utf-8", errors="replace").read()))
    return ids


def existing_ids():
    """Every post_id auto_entries.js already holds -- we never re-emit one."""
    if not os.path.exists(OUT):
        return set()
    return set(re.findall(r'"post_id"\s*:\s*"(\d{15,25})"',
                          open(OUT, encoding="utf-8", errors="replace").read()))


# ------------------------------------------------------------------------- main
def main():
    vocab = load_vocab()
    state = load_state()
    have = existing_ids() | curated_ids()
    # FLOOR, not a moving watermark. CDX backfills: it indexes captures days
    # late and out of order, so a "max id seen" watermark silently skips any
    # post indexed after it advanced past that id. The floor is fixed at the
    # newest curated post and never moves; `processed` records every id we have
    # already fetched, whatever the outcome, so nothing is fetched twice and
    # nothing is missed.
    floor = int(state.get("floor_id") or 0) or seed_watermark()
    processed = set(state.get("processed") or [])
    print("floor (fixed): %d" % floor)
    print("already processed: %d ids" % len(processed))
    print("already on the calendar (auto + curated): %d posts" % len(have))
    print("ticker vocabulary: %d symbols" % len(vocab))

    st, body = _get(CDX.format(h=HANDLE, n=CDX_ROWS), timeout=120)
    if st != 200 or not body:
        print("CDX unavailable (%s) -- nothing written, watermark untouched" % st)
        return 1
    rows = [r for r in json.loads(body) if r and r[0] != "timestamp"]

    found = {}
    for ts, orig in rows:
        m = re.search(r"/status/(\d{15,25})", orig)
        if not m:
            continue
        pid = m.group(1)
        if int(pid) > floor and pid not in have and pid not in processed:
            found.setdefault(pid, ts)
    new_ids = sorted(found, key=int)
    print("CDX rows: %d  ->  new post IDs: %d" % (len(rows), len(new_ids)))
    if not new_ids:
        state.update(last_run=datetime.datetime.now().isoformat(timespec="seconds"),
                     floor_id=floor)
        json.dump(state, open(STATE, "w", encoding="utf-8"), indent=1)
        print("nothing new -- auto_entries.js untouched")
        return 0

    kept, skipped = [], 0
    tombstoned = []          # deleted by the author -- recorded, never silently lost
    for n, pid in enumerate(new_ids, 1):
        st, b = _get(SYND.format(i=pid, t=_token(pid)), timeout=30)
        time.sleep(FETCH_PAUSE)
        if st != 200 or len(b) < 10:
            tombstoned.append(pid)
            continue
        try:
            j = json.loads(b)
        except Exception:
            tombstoned.append(pid)
            continue
        if not j or not j.get("user"):
            # TweetTombstone: "This Post was deleted by the Post author."
            # He deletes a lot -- 14 of 27 in the 2026-08-20..25 window. Recorded
            # so a later pass can try to recover them from Wayback's own snapshot
            # (the JSON capture is indexed; replay was 503 when last attempted).
            tombstoned.append(pid)
            continue
        if (j.get("user", {}).get("screen_name") or "").lower() != HANDLE.lower():
            skipped += 1                  # someone else's post in the reply chain
            continue

        text = j.get("text") or ""
        media = j.get("mediaDetails") or []
        e = extract(text, vocab)

        # Selection: media, OR ticker+action, OR ticker+MA-designation.
        # That third clause matters -- he analyses outfits in plain replies with
        # no chart and no purchase verb ("Consider IXIC's ma100! ... the HIBL
        # short at [2H MA83]"), which a media-or-action rule throws away.
        # Ticker alone is NOT enough: that would sweep in ordinary chatter.
        interesting = bool(media) or bool(
            e["tickers"] and (e["action"] or e["ma_designation"] or e["named_outfit"]))
        if not interesting:
            skipped += 1
            continue

        created = (j.get("created_at") or "")[:10] or str(snowflake_date(pid))
        kept.append({
            "date": created,
            "type": "auto_finding",
            "label": "Auto Finding",
            "category": "Auto Finding",
            "fields": {
                "post_id": pid,
                "ticker": e["tickers"][0] if e["tickers"] else None,
                "price": e["prices"][0] if e["prices"] else None,
                "action": e["action"] or None,
                "co_executed": " ".join(e["tickers"][1:4]) or None,
                "outfit": e["outfit"] or None,
                "ma_designation": e["ma_designation"] or None,
                "timeframe": e["timeframe"] or None,
                "has_media": bool(media),
                "provenance": "auto",
                "ingested": datetime.date.today().isoformat(),
                "note": "auto-ingested from text; UNREVIEWED",
            },
        })
        if n % 25 == 0:
            print("   fetched %d/%d ..." % (n, len(new_ids)))

    print("kept: %d   deleted-by-author: %d   not-a-finding: %d"
          % (len(kept), len(tombstoned), skipped))

    if kept:
        prior = []
        if os.path.exists(OUT):
            src = open(OUT, encoding="utf-8", errors="replace").read()
            m = re.search(r"push\.apply\([^,]+,\s*(\[.*\])\s*\);\s*$", src, re.S)
            if m:
                prior = json.loads(m.group(1))
        merged = prior + kept                       # APPEND ONLY -- never rewrite
        merged.sort(key=lambda r: (r["date"], r["fields"]["post_id"]))
        with open(OUT, "w", encoding="utf-8", newline="\n") as f:
            f.write("/* ---------------------------------------------------------------------------\n"
                    " * AUTO-INGESTED FINDINGS  --  GENERATED by refresh_calendar.py. Do not hand-edit.\n"
                    " *\n"
                    " * Discovered via Wayback CDX, read via X's public syndication endpoint, fields\n"
                    " * extracted from caption TEXT ONLY. Every entry carries provenance:\"auto\" and\n"
                    " * is UNREVIEWED -- it is a separate layer so a bad extraction stays visible and\n"
                    " * toggleable instead of blending into the curated layers.\n"
                    " *\n"
                    " * Append-only. Re-running never rewrites or renumbers an existing entry, so\n"
                    " * user_overlay notes and hides (keyed to post_id) survive every refresh.\n"
                    " * --------------------------------------------------------------------------- */\n\n"
                    "window.CALENDAR_ENTRIES = window.CALENDAR_ENTRIES || [];\n"
                    # push.apply, NOT push(array) -- a plain push appends the
                    # array itself as one phantom entry with no .type, which
                    # shows up in the calendar as an "undefined" layer toggle.
                    "window.CALENDAR_ENTRIES.push.apply(window.CALENDAR_ENTRIES, ")
            f.write(json.dumps(merged, indent=1, ensure_ascii=False))
            f.write(");\n")
        print("auto_entries.js: %d total (%d new)  %d bytes"
              % (len(merged), len(kept), os.path.getsize(OUT)))

    prior_tomb = state.get("tombstoned") or []
    state.update(last_run=datetime.datetime.now().isoformat(timespec="seconds"),
                 floor_id=floor,
                 last_cdx_rows=len(rows),
                 newest_cdx_capture=max((ts for ts, _ in rows), default=None),
                 processed=sorted(processed | set(new_ids), key=int),
                 tombstoned=sorted(set(prior_tomb) | set(tombstoned), key=int))
    json.dump(state, open(STATE, "w", encoding="utf-8"), indent=1)
    print("processed set now %d ids" % (len(processed) + len(new_ids)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
