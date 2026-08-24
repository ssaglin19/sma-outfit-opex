# Gap extraction - summary

**Text only. No vision, no images downloaded, no new network beyond caption text already collected.**
Output: `gap_findings.jsonl` (2,211 rows).

## Step 1 - the boundary

| | date |
|---|---|
| reference repo `unfairmarket/SMA-outfits`, last of 43 commits (`4f14aa26`) | **2025-08-20** |
| newest case study linked in its README (#15, Hard Stop, RWM) | 2025-08-15 |

**GAP_START = 2025-08-20**, set by the **repo's last commit**, which is the later of the two by five
days. Everything after it is undocumented by the reference repo.

The repo was actively maintained - 43 commits from 2024-06 through 2025-08 - and then stopped. The
account did not.

## Step 2 - the gap

**2,211 posts, 2025-08-21 -> 2026-08-21** - almost exactly one year of undocumented activity.
661 carry media (29.9%); 1,366 are replies (61.8%).

By month: 2025-08 29 | 09 144 | 10 73 | 11 134 | 12 178 | 2026-01 117 | 02 112 | 03 335 | 04 396 |
05 220 | 06 237 | 07 154 | 08 82

## Step 3 - what the captions actually yield

**The gap era's format is not the case-study era's format.** Probed before extracting:

| marker | share of gap posts |
|---|---|
| price `d.dd` | 25.5% |
| purchased / bought | 14.2% |
| "<Name> Outfit" | 7.9% |
| bare `MA###` | 6.7% |
| "program" | 4.8% |
| "penny break" | 4.1% |
| bracketed MA ladder | 1.2% |
| **`PARM:MA###`** | **0.4%** |
| **cashtag `$TICK`** | **0.0%** |

Two expectations did not survive contact: **cashtags are entirely absent** from this era, and
**`PARM:MA###` appears in nine posts out of 2,211**. He writes tickers bare or in quotes - `'SQQQ'`,
`the SQQQ` - so extraction matches against a ticker vocabulary rather than a `$` prefix.

### Extraction result

| | count | share |
|---|---|---|
| **fully extractable** (ticker + price + outfit + action) | **108** | **4.9%** |
| at least one field recovered | 1,091 | 49.3% |
| **needs a targeted vision pass** (>=1 field missing) | **2,103** | **95.1%** |

Field presence: ticker 43.1% | price 25.5% | action 19.8% | co-executed ticker 10.0% |
timeframe 7.2% | named outfit 7.1% | MA designation 6.7%.

Missing by field: outfit 1,955 | action 1,774 | price 1,647 | ticker 1,258.

**The outfit is the field the captions almost never carry** - 1,955 of 2,211 lack it. That is the
same wall the case-study catalog hit: the author records the outfit on the chart, not in the text.

## Ticker distribution (79 distinct, first ticker per post)

SPXU 63 | SVIX 49 | RWM 44 | GUSH 38 | UCO 37 | DOG 33 | SQQQ 32 | XLF 30 | VIXY 24 | JPM 23 |
SCO 22 | DUST 21 | MUU 21 | SOXS 21 | UVIX 20 | SSO 20 | ERX 20 | MSTX 19

Noticeably broader and more commodity/sector-weighted than the case-study era, which was dominated
by QQQ-complex instruments.

## Where this leaves the gap

A year of activity is now indexed with dates, tickers and prices where stated - but only **108 rows
are complete from text**. The realistic target for a targeted vision pass is the **661 gap posts that
carry a chart**, not all 2,211: that is where the outfit actually lives, and it is a small enough set
to be practical.

Standing caveat: ~30% of this account's enumerated posts are tombstoned at source and unrecoverable,
so the gap as measured is what survived, not everything posted.
