# Text-signature search - summary

**No vision, no images, no network beyond caption text.** Source: `archive/enumeration/timeline_meta.jsonl`
plus caption text fetched for his 9,543 live posts. Output: `signature_matches.jsonl` (2,975 rows).

## Headline: the caption signature does not find findings reliably

Measured against the **4,645 charted posts**, not against the 88:

| signature | matches | % with media | recall of charted | false pos |
|---|---|---|---|---|
| A  penny-break / program | 556 | 71.6% | 8.6% | 158 |
| B  A + bracketed MA ladder | 718 | 72.7% | 11.2% | 196 |
| C  B + bare `MA###` | 1,264 | 76.3% | 20.8% | 299 |
| D  C + outfit / operat* | 2,423 | 63.7% | 33.2% | 879 |
| E  D + action verbs (used) | 2,990 | 64.5% | **41.6%** | 1,060 |

Baseline: 48.7% of his captions have media. **The loosest signature reaches only 41.6% of charted
posts at 64.5% precision** - a 16pp lift over guessing. Tightening the signature raises precision to
76% but collapses recall to 21%. There is no setting that is both clean and complete.

Why the 88 misled us: the same signature scores **95.5% recall on the case studies**. Those 88 were
hand-picked by the author *because* they were written up in prose. The wider timeline is terse -
most charted posts say little or nothing about the outfit.

## What the signature harvested (fraction of the 88 containing each)

price `d.dd` 76.1% | bare `MA###` 61.4% | purchased/bought/picked up 51.1% | "outfit" 40.9% |
operat* 28.4% | "program" 22.7% | "penny break" 22.7% | bracketed ladder 21.6% | cashtag 12.5% |
sold/short 5.7%

The two phrases proposed as the signature - penny-break and program - are in under a quarter of
the 88 each, and 34.1% combined.

## Matches

**2,975** captions matched (E). 1,921 have media, 1,054 do not. 64 are existing case studies.

Tightest tier: D 1,173 | E 567 | A 556 | C 517 | B 162

**Text-extractability is the second negative:**

| | count | share |
|---|---|---|
| fully extractable (ticker + outfit + price + action) | **219** | **7.4%** |
| missing at least one field | 2,756 | 92.6% |

Missing by field: action 1,812 | price 1,665 | outfit 1,601 | ticker 1,277.

So even among matched captions, **fewer than one in thirteen** yields a complete row from text alone.
Every other row is flagged `needs_vision: true`.

## By year

| year | matches | of which charted |
|---|---|---|
| 2021 | 1 | 0 |
| 2022 | 10 | 6 |
| 2023 | 26 | 18 |
| 2024 | 1,624 | 1,141 |
| 2025 | 846 | 493 |
| 2026 | 468 | 263 |

## Tickers (first per post, 94 distinct)

SQQQ 202 | SVIX 162 | TQQQ 159 | SPXU 125 | QQQ 100 | RWM 82 | SPX 76 | SOXS 72 | DJI 65 |
JPM 62 | IWM 54 | IXIC 52 | VXX 38 | GUSH 27 | NVDA 20

## Verdict

Text signature is a **filter, not a solution**. It narrows 9,543 posts to 2,975 worth looking at, and
delivers 219 complete rows for free - but it cannot substitute for the chart image, because the
author records the outfit *on the chart*, not in the caption.

Recommended use: treat the 1,921 matched-and-charted posts as a **priority queue** for any future
targeted vision pass, ordered by tier (B and C are the highest-precision). That is roughly 40% of the
charted corpus at ~76% precision, versus 4,645 images for full coverage.

Standing caveat, unchanged: ~30% of enumerated posts are tombstoned at source and unrecoverable, so
all counts here describe what survived, not what was posted.
