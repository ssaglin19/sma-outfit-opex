# Run log

- case studies: **88** (85 unique post IDs; 3 IDs appear twice in the source README)
- posts captured: **228** (case-study posts plus their ancestor chains)
- catalog records: **234**
- media downloaded: **234** files, 9,363,607 bytes (8.9 MB), failures: 0
- posts enriched with Wayback metrics: **174**

## Sources

1. **syndication** - `cdn.syndication.twimg.com/tweet-result` - X's public embed backend.
   No auth, no API key, no login, no headless browser. Works by tweet ID at any age.
   This reached **all 85** unique case-study posts, including the 2023 cohort that has
   zero Wayback coverage.
2. **wayback** - archived X-API-v2 JSON (`mimetype application/json`). Used only to add
   `public_metrics`, `context_annotations` and `conversation_id`, which the embed payload lacks.

Sources 2 and 3 of the original brief (paid X API, Playwright/headless) were **not needed
and not used**. No account was logged into; nothing was posted, liked or followed.

## Handle note

The README links use `rauItrades` (capital i). The account now presents as **@UnfairMarket**
(user id `1442931286365007872`) - the same account, renamed. `raultrades` (lowercase L) is a
*different* account and is not the source of these posts.

## Status meaning

- **COMPLETE** - the conversation reports no further replies; root plus ancestor chain archived.
- **PARTIAL** - the conversation reports additional replies. The public embed endpoint exposes a
  post's *ancestors* but not its *descendants*, so the author's forward reply chain is not
  retrievable this way. What is archived is complete as far as it goes, and is flagged here
  rather than silently truncated.

## Per case study

| # | case | date | posts | media | wayback metrics | status |
|---|---|---|---|---|---|---|
| 01 | #8 Precision Buy Algorithm | 2023-03-22 | 3 | 4 | no | COMPLETE |
| 02 | #17 Precision Buy Algorithm | 2023-06-05 | 3 | 1 | no | COMPLETE |
| 03 | #9 Precision Buy Algorithm | 2023-07-17 | 1 | 1 | no | COMPLETE |
| 04 | #18 Precision Buy Algorithm | 2023-09-12 | 2 | 2 | no | COMPLETE |
| 05 | #6 Precision Buy Algorithm | 2023-09-21 | 1 | 1 | no | PARTIAL (3 replies indicated) |
| 06 | #7 Precision Buy Algorithm | 2023-10-06 | 1 | 1 | no | COMPLETE |
| 07 | #16 Precision Buy Algorithm | 2023-10-31 | 1 | 1 | no | PARTIAL (3 replies indicated) |
| 08 | #5 Precision Buy Algorithm | 2023-11-08 | 3 | 3 | no | COMPLETE |
| 09 | #4 Precision Buy Algorithm | 2023-11-09 | 1 | 1 | no | PARTIAL (3 replies indicated) |
| 10 | #3 Precision Buy Algorithm | 2023-11-21 | 1 | 1 | no | PARTIAL (3 replies indicated) |
| 11 | #2 Precision Buy Algorithm | 2023-11-22 | 1 | 1 | no | COMPLETE |
| 12 | #1 Precision Buy Algorithm | 2023-12-05 | 1 | 1 | no | PARTIAL (2 replies indicated) |
| 13 | #1 Optimized Buying Algorithms | 2023-12-14 | 4 | 4 | no | COMPLETE |
| 14 | #14 Precision Buy Algorithm | 2024-01-08 | 1 | 1 | no | PARTIAL (6 replies indicated) |
| 15 | #15 Precision Buy Algorithm | 2024-02-06 | 1 | 1 | no | PARTIAL (7 replies indicated) |
| 16 | #13 Precision Buy Algorithm | 2024-03-18 | 1 | 1 | no | COMPLETE |
| 17 | #12 Precision Buy Algorithm | 2024-03-28 | 1 | 1 | no | PARTIAL (4 replies indicated) |
| 18 | #11 Precision Buy Algorithm | 2024-04-18 | 1 | 1 | no | PARTIAL (4 replies indicated) |
| 19 | #10 Precision Buy Algorithm | 2024-04-19 | 1 | 1 | no | PARTIAL (3 replies indicated) |
| 20 | #19 Precision Buy Algorithm | 2024-05-14 | 1 | 1 | yes | COMPLETE |
| 21 | #20 Precision Buy Algorithm | 2024-06-04 | 11 | 12 | yes | COMPLETE |
| 22 | #21 Precision Buy Algorithm | 2024-06-12 | 1 | 1 | yes | PARTIAL (7 replies indicated) |
| 23 | #22 Precision Buy Algorithm | 2024-06-27 | 1 | 1 | yes | PARTIAL (2 replies indicated) |
| 24 | #1 Singular Point Hard Stop Order | 2024-06-28 | 1 | 1 | yes | PARTIAL (4 replies indicated) |
| 25 | #1 Automated Short Orders | 2024-06-28 | 74 | 80 | yes | COMPLETE |
| 26 | #23 Precision Buy Algorithm | 2024-07-01 | 1 | 1 | yes | PARTIAL (2 replies indicated) |
| 27 | #24 Precision Buy Algorithm | 2024-07-08 | 3 | 3 | no | PARTIAL (2 replies indicated) |
| 28 | #2 Singular Point Hard Stop Order | 2024-07-10 | 1 | 1 | yes | PARTIAL (3 replies indicated) |
| 29 | #2 Automated Short Orders | 2024-07-10 | 16 | 16 | yes | COMPLETE |
| 30 | #25 Precision Buy Algorithm | 2024-07-19 | 1 | 1 | yes | COMPLETE |
| 31 | #26 Precision Buy Algorithm | 2024-07-22 | 1 | 1 | yes | PARTIAL (2 replies indicated) |
| 32 | #2 Optimized Buying Algorithms | 2024-08-09 | 1 | 1 | yes | PARTIAL (2 replies indicated) |
| 33 | #27 Precision Buy Algorithm | 2024-08-16 | 1 | 1 | yes | PARTIAL (4 replies indicated) |
| 34 | #3 Optimized Buying Algorithms | 2024-08-22 | 1 | 1 | yes | PARTIAL (7 replies indicated) |
| 35 | #28 Precision Buy Algorithm | 2024-08-27 | 3 | 1 | yes | COMPLETE |
| 36 | #3 Automated Short Orders | 2024-08-27 | 1 | 1 | yes | PARTIAL (4 replies indicated) |
| 37 | #4 Optimized Buying Algorithms | 2024-08-28 | 1 | 1 | yes | PARTIAL (4 replies indicated) |
| 38 | #29 Precision Buy Algorithm | 2024-08-28 | 3 | 3 | yes | PARTIAL (2 replies indicated) |
| 39 | #5 Optimized Buying Algorithms | 2024-09-06 | 1 | 1 | yes | PARTIAL (4 replies indicated) |
| 40 | #6 Optimized Buying Algorithms | 2024-09-11 | 1 | 1 | yes | PARTIAL (3 replies indicated) |
| 41 | #30 Precision Buy Algorithm | 2024-09-17 | 1 | 1 | yes | PARTIAL (3 replies indicated) |
| 42 | #7 Optimized Buying Algorithms | 2024-09-20 | 1 | 1 | yes | PARTIAL (3 replies indicated) |
| 43 | #31 Precision Buy Algorithm | 2024-10-01 | 1 | 1 | yes | PARTIAL (5 replies indicated) |
| 44 | #32 Precision Buy Algorithm | 2024-10-04 | 1 | 1 | yes | PARTIAL (2 replies indicated) |
| 45 | #34 Precision Buy Algorithm | 2025-01-07 | 1 | 1 | yes | PARTIAL (2 replies indicated) |
| 46 | #33 Precision Buy Algorithm | 2025-01-08 | 1 | 1 | yes | PARTIAL (2 replies indicated) |
| 47 | #35 Precision Buy Algorithm | 2025-01-08 | 1 | 1 | yes | PARTIAL (2 replies indicated) |
| 48 | #11 Optimized Buying Algorithms | 2025-01-10 | 1 | 1 | yes | COMPLETE |
| 49 | #8 Optimized Buying Algorithms | 2025-01-13 | 33 | 35 | yes | PARTIAL (2 replies indicated) |
| 50 | #9 Optimized Buying Algorithms | 2025-01-30 | 1 | 1 | yes | PARTIAL (5 replies indicated) |
| 51 | #12 Optimized Buying Algorithms | 2025-01-30 | 1 | 1 | yes | PARTIAL (5 replies indicated) |
| 52 | #10 Optimized Buying Algorithms | 2025-02-06 | 1 | 1 | yes | PARTIAL (6 replies indicated) |
| 53 | #13 Optimized Buying Algorithms | 2025-02-06 | 1 | 1 | yes | PARTIAL (6 replies indicated) |
| 54 | #3 Singular Point Hard Stop Order | 2025-03-28 | 1 | 1 | yes | PARTIAL (5 replies indicated) |
| 55 | #4 Singular Point Hard Stop Order | 2025-05-22 | 1 | 1 | yes | PARTIAL (5 replies indicated) |
| 56 | #36 Precision Buy Algorithm | 2025-05-22 | 1 | 1 | no | PARTIAL (4 replies indicated) |
| 57 | #5 Singular Point Hard Stop Order | 2025-06-02 | 1 | 1 | yes | PARTIAL (9 replies indicated) |
| 58 | #6 Singular Point Hard Stop Order | 2025-06-05 | 1 | 1 | yes | PARTIAL (3 replies indicated) |
| 59 | #7 Singular Point Hard Stop Order | 2025-06-10 | 1 | 1 | yes | PARTIAL (7 replies indicated) |
| 60 | #8 Singular Point Hard Stop Order | 2025-06-11 | 1 | 1 | yes | PARTIAL (2 replies indicated) |
| 61 | #14 Optimized Buying Algorithms | 2025-06-11 | 1 | 1 | yes | PARTIAL (7 replies indicated) |
| 62 | #9 Singular Point Hard Stop Order | 2025-06-11 | 1 | 1 | yes | PARTIAL (3 replies indicated) |
| 63 | #37 Precision Buy Algorithm | 2025-06-11 | 1 | 1 | yes | PARTIAL (10 replies indicated) |
| 64 | #38 Precision Buy Algorithm | 2025-06-12 | 1 | 1 | yes | PARTIAL (6 replies indicated) |
| 65 | #10 Singular Point Hard Stop Order | 2025-06-13 | 1 | 1 | yes | COMPLETE |
| 66 | #11 Singular Point Hard Stop Order | 2025-06-13 | 1 | 1 | yes | PARTIAL (3 replies indicated) |
| 67 | #39 Precision Buy Algorithm | 2025-06-13 | 1 | 1 | yes | PARTIAL (3 replies indicated) |
| 68 | #12 Singular Point Hard Stop Order | 2025-06-13 | 1 | 1 | yes | PARTIAL (8 replies indicated) |
| 69 | #40 Precision Buy Algorithm | 2025-06-23 | 1 | 1 | yes | PARTIAL (7 replies indicated) |
| 70 | #13 Singular Point Hard Stop Order | 2025-06-24 | 1 | 1 | yes | PARTIAL (6 replies indicated) |
| 71 | #14 Singular Point Hard Stop Order | 2025-06-25 | 1 | 1 | yes | PARTIAL (2 replies indicated) |
| 72 | #16 Optimized Buying Algorithms | 2025-06-26 | 1 | 1 | yes | PARTIAL (3 replies indicated) |
| 73 | #15 Optimized Buying Algorithms | 2025-06-30 | 1 | 1 | yes | PARTIAL (5 replies indicated) |
| 74 | #41 Precision Buy Algorithm | 2025-07-01 | 1 | 1 | yes | PARTIAL (3 replies indicated) |
| 75 | #17 Optimized Buying Algorithms | 2025-07-03 | 1 | 1 | yes | PARTIAL (4 replies indicated) |
| 76 | #4 Automated Short Orders | 2025-07-07 | 1 | 1 | yes | PARTIAL (2 replies indicated) |
| 77 | #42 Precision Buy Algorithm | 2025-07-07 | 1 | 1 | yes | PARTIAL (24 replies indicated) |
| 78 | #18 Optimized Buying Algorithms | 2025-07-09 | 1 | 1 | yes | PARTIAL (10 replies indicated) |
| 79 | #43 Precision Buy Algorithm | 2025-07-09 | 1 | 1 | yes | PARTIAL (6 replies indicated) |
| 80 | #44 Precision Buy Algorithm | 2025-07-11 | 1 | 1 | yes | PARTIAL (4 replies indicated) |
| 81 | #19 Optimized Buying Algorithms | 2025-07-21 | 1 | 1 | yes | PARTIAL (5 replies indicated) |
| 82 | #5 Automated Short Orders | 2025-07-21 | 1 | 1 | yes | PARTIAL (6 replies indicated) |
| 83 | #20 Optimized Buying Algorithms | 2025-07-23 | 1 | 1 | yes | PARTIAL (3 replies indicated) |
| 84 | #21 Optimized Buying Algorithms | 2025-07-23 | 1 | 1 | yes | PARTIAL (4 replies indicated) |
| 85 | #23 Optimized Buying Algorithms | 2025-07-24 | 1 | 1 | yes | PARTIAL (3 replies indicated) |
| 86 | #24 Optimized Buying Algorithms | 2025-07-25 | 1 | 1 | yes | PARTIAL (2 replies indicated) |
| 87 | #22 Optimized Buying Algorithms | 2025-07-28 | 1 | 1 | yes | PARTIAL (6 replies indicated) |
| 88 | #15 Singular Point Hard Stop Order | 2025-08-15 | 1 | 1 | yes | PARTIAL (7 replies indicated) |
