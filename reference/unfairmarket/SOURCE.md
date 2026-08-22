# Source and attribution

**Origin:** https://github.com/unfairmarket/SMA-outfits
**Commit:** `4f14aa262fcd9524722f5cc1e2b767587327de7b` (branch `main`, sole branch, no tags)
**Commit date:** Wed 20 Aug 2025 07:50:01 -0700 - "Update README.md", Nickolas Raul Diaz
**Mirrored:** 2026-08-21, from a fresh clone into a clean temp dir.

## Completeness

This is a **full mirror**, not a selection. `git ls-files` on the fresh clone returns exactly
**two tracked files**, and both are here:

| file | bytes | sha256 |
|---|---|---|
| `README.md` | 61,832 | `e67ad130a05460bb074b2f658e002a518a196134879d575467091bcf70b122df` |
| `LICENSE`   | 11,558 | `1eb85fc97224598dad1852b5d6483bbcf0aa8608790dcc657a5a2a761ae9c8c6` |

Verified by `diff -r` against the source clone (excluding `.git` and this file): **no differences**.

**The upstream repository contains nothing beyond `LICENSE` and `README.md`** - no subdirectories,
no scripts, no data. Its README *describes* a layout (`SMA_Analysis/`, `Technical_Explanation/`,
`Data_and_Analysis/`, `Visualizations/`, `Documentation/`, `Tools_and_Scripts/`), but **those
directories do not exist in the repository**. The case-study material *is* the README text.

## Case studies

`### Real Time Operations` (README line 345) holds **88 numbered case-study entries / 88 X-thread
links (85 unique URLs; 3 repeat across categories)**, split into four lists that each restart at #1:

| category | case studies |
|---|---|
| Precision Buy Algorithm | **44** |
| Optimized Buying Algorithms | 24 |
| Singular Point Hard Stop Order | 15 |
| Automated Short Orders | 5 |

## Status

Third-party material, vendored **unmodified**, as a case-study catalog only.
**This is NOT my code.** My detector engine is in `engine/`. Keep the two separate.

## Licence

**Apache License 2.0** - full text in `LICENSE` in this directory, copied from source. Respect its
terms, including attribution and notice requirements, in any downstream use or redistribution.

## Upstream org note

`raultrades/SMA-outfits` and `unfairmarket/SMA-outfits` resolve to the **same repository at the
same commit** (`4f14aa26`); GitHub redirects the older org path. The engine's own docs cite the
`raultrades` URL.
