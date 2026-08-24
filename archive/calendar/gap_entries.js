/* ---------------------------------------------------------------------------
 * GAP FINDINGS LAYER  --  the undocumented year, enriched from caption TEXT.
 *
 * Appends to the shared global, so include order does not matter:
 *     window.CALENDAR_ENTRIES = window.CALENDAR_ENTRIES || [];
 *     window.CALENDAR_ENTRIES.push(...);
 *
 * WHAT THIS IS
 *   Posts made AFTER the reference repo stopped. GAP_START = 2025-08-20, the
 *   last of that repo's 43 commits (later than the newest case study,
 *   2025-08-15). Selection: a gap post with media, OR with both a ticker and an
 *   action recoverable from its caption.
 *
 * *** THIS LAYER OVERLAPS THE PLAIN "finding" LAYER ***
 *   Every charted gap post also appears in finding_entries.js, which covers all
 *   charted posts regardless of era. From 2025-08-21 onward the two layers mark
 *   THE SAME POSTS -- this one simply carries the enriched fields. Viewing both
 *   at once double-marks those days.
 *   To read the gap cleanly: toggle the plain "finding" layer OFF.
 *
 * FIELDS
 *   ticker / price / action / co_executed come from the caption text.
 *   `outfit` is deliberately null: the author records the outfit on the CHART,
 *   and only ~7% of gap captions name it. Where the text DOES name one, the
 *   value is preserved in `outfit_text` and the note says so -- nothing measured
 *   was thrown away to satisfy the schema.
 *
 * REGENERATE from archive/analysis/gap_findings.jsonl. Do not hand-edit.
 * entries.js, opex_entries.js and finding_entries.js are separate and untouched.
 * --------------------------------------------------------------------------- */

window.CALENDAR_ENTRIES = window.CALENDAR_ENTRIES || [];
window.CALENDAR_ENTRIES.push.apply(window.CALENDAR_ENTRIES, [
 {
  "date": "2025-08-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1959102701213466710",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-08-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1961093841605546367",
   "ticker": "SQQQ",
   "price": "17.25",
   "action": "purchased",
   "co_executed": "NVDA",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-08-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1961094588015501816",
   "ticker": "SQQQ",
   "price": "17.25",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA33"
  }
 },
 {
  "date": "2025-08-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1961100804015927602",
   "ticker": "SQQQ",
   "price": "17.25",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-08-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1961122723423556092",
   "ticker": "VIXY",
   "price": "34.46",
   "action": "purchased",
   "co_executed": "SQQQ",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-08-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1961123434102231133",
   "ticker": "VIXY",
   "price": "34.46",
   "action": null,
   "co_executed": "SQQQ",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-08-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1961128440427577806",
   "ticker": "VIXY",
   "price": "34.46",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-08-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1961140960311824480",
   "ticker": "VIXY",
   "price": "34.46",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-08-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1961142198042595795",
   "ticker": "VIX",
   "price": "34.46",
   "action": "cut",
   "co_executed": "SQQQ, SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-08-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1961143275970334729",
   "ticker": "VIXY",
   "price": "34.46",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-08-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1961143896135930065",
   "ticker": "SQQQ",
   "price": "17.25",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-08-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1961149277213749669",
   "ticker": "VIXY",
   "price": "34.46",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-08-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1961335972421087236",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-08-31",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1962096880873300231",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-01",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1962374304768913599",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-02",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1962756943417876714",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1963417437891883406",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1965783974804132350",
   "ticker": "GME",
   "price": "21.54",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-11",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1966221733842792931",
   "ticker": "GLL",
   "price": "18.59",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA28 / MA57 / MA114 / MA228 / MA456 / MA911"
  }
 },
 {
  "date": "2025-09-11",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1966257028671893780",
   "ticker": "GLL",
   "price": "18.59",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-12",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1966493897980604496",
   "ticker": "GLL",
   "price": "18.59",
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-12",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1966494439162986583",
   "ticker": "GLL",
   "price": "18.25",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA228 / [GLL 3M 911 MA28 MA57 MA114 MA228 MA456 MA911] / MA28 / MA57 / MA114 / MA456 / MA911"
  }
 },
 {
  "date": "2025-09-12",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1966494563352412470",
   "ticker": "GLL",
   "price": "18.25",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-12",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1966495292846416168",
   "ticker": "GLL",
   "price": "18.25",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-12",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1966499291066958116",
   "ticker": "DXY",
   "price": null,
   "action": "hold",
   "co_executed": "GLL",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "sadogeenakamoto positive arbitrage outfit"
  }
 },
 {
  "date": "2025-09-12",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1966520996913098878",
   "ticker": "GLL",
   "price": "18.25",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968333733045600757",
   "ticker": "GME",
   "price": "21.54",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968335880973885719",
   "ticker": "VIXY",
   "price": "32.95",
   "action": "purchased",
   "co_executed": "SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "SVIX outfit / [SVIX outfit SMA 36 52 106 211 422 844]"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968336458194018713",
   "ticker": "VIXY",
   "price": "32.95",
   "action": "cut",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "[5M MA422] / MA422"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968338933525442618",
   "ticker": "VIXY",
   "price": "32.95",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968340071112917334",
   "ticker": "VIXY",
   "price": "32.95",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968353185665515764",
   "ticker": "VIXY",
   "price": "32.95",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968354504946172134",
   "ticker": "VIXY",
   "price": "32.95",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968355566931386377",
   "ticker": "VIXY",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968356612239929697",
   "ticker": "VIXY",
   "price": "32.95",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968374412211798143",
   "ticker": "VIXY",
   "price": "32.95",
   "action": "cut",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968376567614292018",
   "ticker": "SVIX",
   "price": "21.43",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "SVIX from 21.43 . 33 SMA outfit"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968377025682722944",
   "ticker": "VIXY",
   "price": "21.43",
   "action": "purchased",
   "co_executed": "SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "SVIX from 21.43 . 33 SMA outfit"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968377297725202717",
   "ticker": "VIXY",
   "price": "21.43",
   "action": null,
   "co_executed": "SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "SVIX from 21.43 . 33 SMA outfit"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968377889424121864",
   "ticker": "VIXY",
   "price": "21.43",
   "action": "purchased",
   "co_executed": "SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "SVIX from 21.43 . 33 SMA outfit"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968378249467306364",
   "ticker": "VIXY",
   "price": null,
   "action": "purchased",
   "co_executed": "SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968378463611666832",
   "ticker": "VIXY",
   "price": "21.43",
   "action": null,
   "co_executed": "SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "SVIX from 21.43 . 33 SMA outfit"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968378982644203810",
   "ticker": "SVIX",
   "price": "21.43",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968386354578145696",
   "ticker": "SVIX",
   "price": "21.43",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968387056138338566",
   "ticker": "VIXY",
   "price": "21.43",
   "action": "purchased",
   "co_executed": "SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968392364512411730",
   "ticker": "VIXY",
   "price": "21.43",
   "action": "purchased",
   "co_executed": "SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968397039282032956",
   "ticker": "RWM",
   "price": "17.00",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "33 outfit / MA66 / [parm:MA66]"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968397189475979287",
   "ticker": "RWM",
   "price": "17.00",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968397521086013566",
   "ticker": "RWM",
   "price": "17.00",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-18",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968668804839305502",
   "ticker": "RWM",
   "price": null,
   "action": "hold",
   "co_executed": "TZA",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-18",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968669096221810743",
   "ticker": "RWM",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-18",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968671343957647411",
   "ticker": "RWM",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-18",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968679380726558756",
   "ticker": "SPXU",
   "price": "13.90",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA37"
  }
 },
 {
  "date": "2025-09-18",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968679493683261872",
   "ticker": "SPXU",
   "price": "13.90",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-18",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968679787288760687",
   "ticker": "SPXU",
   "price": "13.90",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-18",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1968680320334500281",
   "ticker": "SPXU",
   "price": "13.90",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-24",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1970933134226288852",
   "ticker": "RWM",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-24",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1970933459737772395",
   "ticker": "RWM",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-24",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1970937200213926337",
   "ticker": "RWM",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-09-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1971209591905276324",
   "ticker": "RWM",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-10-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1975426730979709069",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-10-09",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1976300198868681174",
   "ticker": "RWM",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-10-09",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1976312003535962183",
   "ticker": "RWM",
   "price": "17.00",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "33 outfit / MA66 / [parm:MA66]"
  }
 },
 {
  "date": "2025-10-09",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1976335496482865447",
   "ticker": "RWM",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-10-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1976679370359202016",
   "ticker": "RWM",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-10-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1976739467265446281",
   "ticker": "RWM",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-10-12",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1977390794634887188",
   "ticker": "TZA",
   "price": null,
   "action": "purchased",
   "co_executed": "RWM, IWM",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-11-02",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1985106178226204739",
   "ticker": "SPY",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-11-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1985869156756177338",
   "ticker": "RWM",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-11-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1986545336375255368",
   "ticker": "GME",
   "price": "21.54",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-11-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1986573765061587275",
   "ticker": "RWM",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-11-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1986575647419081060",
   "ticker": "RWM",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-11-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1986821314657784182",
   "ticker": "RWM",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-11-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1986828767394980338",
   "ticker": "RWM",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-11-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1986833380349255925",
   "ticker": "RWM",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-11-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1987031376017903715",
   "ticker": "RWM",
   "price": "17.00",
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-11-11",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1988110621871927580",
   "ticker": "RWM",
   "price": "16.08",
   "action": "purchased",
   "co_executed": "SPX, DJI, IXIC",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "SMA outfit"
  }
 },
 {
  "date": "2025-11-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1989048436164030569",
   "ticker": "RWM",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "there was extremely high outfit / MA66 / [parm:MA66]"
  }
 },
 {
  "date": "2025-11-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1989066823397175405",
   "ticker": "RWM",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-11-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1990545998117294568",
   "ticker": "RWM",
   "price": null,
   "action": "hold",
   "co_executed": "IWM",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "iding scale based on how relevant a SMA outfit"
  }
 },
 {
  "date": "2025-11-18",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1990608328729465142",
   "ticker": "RWM",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-11-30",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1994921992521486813",
   "ticker": "RWM",
   "price": "16.08",
   "action": "cut",
   "co_executed": "TZA",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1998645681708482653",
   "ticker": "RWM",
   "price": "16.08",
   "action": "purchased",
   "co_executed": "TZA",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1998841386028904889",
   "ticker": "RWM",
   "price": null,
   "action": "sold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1998845074218926303",
   "ticker": "CONL",
   "price": "20.54",
   "action": "purchased",
   "co_executed": "COIN",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA548"
  }
 },
 {
  "date": "2025-12-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1998850892947403211",
   "ticker": "CONL",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-11",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1998950903240602121",
   "ticker": "CONL",
   "price": "20.54",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-11",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1998954099677737307",
   "ticker": "CONL",
   "price": null,
   "action": "purchased",
   "co_executed": "DJI, SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-12",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1999541245790786035",
   "ticker": "ETHU",
   "price": "56.96",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-12",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1999541530525360477",
   "ticker": "ETHU",
   "price": "56.96",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA30 / MA41 / MA81 / MA163 / MA325 / MA650"
  }
 },
 {
  "date": "2025-12-12",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1999564274314699003",
   "ticker": "DUST",
   "price": "7.58",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "e's an outfitting program at the 10M 47 outfit"
  }
 },
 {
  "date": "2025-12-12",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "1999578160162034145",
   "ticker": "DUST",
   "price": "7.58",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2000112468677607682",
   "ticker": "ETHU",
   "price": "56.96",
   "action": "sold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2000574617933824359",
   "ticker": "DUST",
   "price": "7.58",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2000576337732399240",
   "ticker": "DUST",
   "price": "7.58",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2000576736606769645",
   "ticker": "DUST",
   "price": "7.57",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2000577440968487061",
   "ticker": "ETHU",
   "price": "56.96",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2000579844002755061",
   "ticker": "DUST",
   "price": "7.58",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2000581805703913579",
   "ticker": "DUST",
   "price": "7.58",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2000582214602690856",
   "ticker": "DUST",
   "price": "7.58",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2000586907575517230",
   "ticker": "ETHU",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2000587082247405925",
   "ticker": "ETHU",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2000594126782554178",
   "ticker": "SOXL",
   "price": null,
   "action": "purchased",
   "co_executed": "SOX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "itting program operating on the 15M 180 outfit"
  }
 },
 {
  "date": "2025-12-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2000595608223306144",
   "ticker": "SOXL",
   "price": null,
   "action": null,
   "co_executed": "SOX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2000604262834090436",
   "ticker": "SOXL",
   "price": null,
   "action": null,
   "co_executed": "SOX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2000606471818789277",
   "ticker": "DUST",
   "price": "7.58",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-16",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2000936602995236883",
   "ticker": "DUST",
   "price": "7.58",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-16",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2000946250288713980",
   "ticker": "DUST",
   "price": "7.58",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-16",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2000961427646111823",
   "ticker": "DUST",
   "price": "7.58",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-16",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2000970430501544154",
   "ticker": "DUST",
   "price": "7.58",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-16",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2000971302715421163",
   "ticker": "DUST",
   "price": "7.58",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-16",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2001011356326354989",
   "ticker": "DUST",
   "price": "7.58",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2001317500919885905",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2001319052300394862",
   "ticker": "DUST",
   "price": "7.58",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2001341878726463722",
   "ticker": "DUST",
   "price": "7.58",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2001344289453064535",
   "ticker": "SOXL",
   "price": "36.40",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "SOXL 36.40 as risk. 2H 46 outfit / MA368 / MA23 / MA46 / MA92 / MA184 / MA736"
  }
 },
 {
  "date": "2025-12-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2001344775073751086",
   "ticker": "SOXL",
   "price": "36.40",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2001348476404470199",
   "ticker": "SOXL",
   "price": "36.40",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2001364549493305502",
   "ticker": "MUU",
   "price": "63.36",
   "action": "purchased",
   "co_executed": "MU",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "22 55 77 222 555 777 outfit / MA777"
  }
 },
 {
  "date": "2025-12-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2001364704183357580",
   "ticker": "MUU",
   "price": "63.36",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2001367009813237923",
   "ticker": "MUU",
   "price": "63.63",
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "ies analysis based on this specific SMA outfit / [MA777] / MA777"
  }
 },
 {
  "date": "2025-12-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2001392043549937838",
   "ticker": "MUU",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2001397647928684671",
   "ticker": "MUU",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2001398174834135400",
   "ticker": "MUU",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2001401694006198499",
   "ticker": "MUU",
   "price": "63.63",
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA777"
  }
 },
 {
  "date": "2025-12-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2001406423037809003",
   "ticker": "SQQQ",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-18",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2001535773708079389",
   "ticker": "MUU",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-18",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2001661721585553821",
   "ticker": "MUU",
   "price": "82.19",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-18",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2001670788613837309",
   "ticker": "MUU",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-18",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2001671020504363352",
   "ticker": "MUU",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-19",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2002042691748864401",
   "ticker": "MUU",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-19",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2002065874250027113",
   "ticker": "MUU",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-22",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2002955164215640300",
   "ticker": "MUU",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-24",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2003843231256305923",
   "ticker": "MUU",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-24",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2003848704063836383",
   "ticker": "SOXL",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-24",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2003889910907076870",
   "ticker": "XLE",
   "price": null,
   "action": "sold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-24",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2003890960661729589",
   "ticker": "XLE",
   "price": "91.97",
   "action": "sold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "XLE 404 outfit"
  }
 },
 {
  "date": "2025-12-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2004260601833705505",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2025-12-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2004262814903648716",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-03",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2007254546981245356",
   "ticker": "MUU",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-16",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2012246316592566437",
   "ticker": "MUU",
   "price": "000.00",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-21",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014046501136375927",
   "ticker": "MUU",
   "price": null,
   "action": "purchased",
   "co_executed": "MU",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-21",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014076817104314481",
   "ticker": "FAS",
   "price": "42.02",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-21",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014087397768610051",
   "ticker": "FAS",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-22",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014347621494931806",
   "ticker": "FAS",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-22",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014348083648446575",
   "ticker": null,
   "price": "42.02",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-22",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014386778892075032",
   "ticker": "FAS",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-22",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014392778864967866",
   "ticker": "TQQQ",
   "price": null,
   "action": "sold",
   "co_executed": "SOXL, SVIX, TSLA",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-22",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014398835351814638",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014709362917568811",
   "ticker": null,
   "price": "42.02",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014724323106553978",
   "ticker": "FAS",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014725898348724529",
   "ticker": null,
   "price": "42.02",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014727115011457243",
   "ticker": "XLF",
   "price": "53.07",
   "action": "purchased",
   "co_executed": "FAS",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA548"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014727358436278573",
   "ticker": "XLF",
   "price": "53.07",
   "action": "cut",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014727758581268679",
   "ticker": "XLF",
   "price": "53.07",
   "action": "purchased",
   "co_executed": "JPM",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014729074640621824",
   "ticker": "XLF",
   "price": "53.07",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014731502500852070",
   "ticker": "FAS",
   "price": "53.07",
   "action": "purchased",
   "co_executed": "XLF",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014740079252799871",
   "ticker": "FAS",
   "price": "53.07",
   "action": "purchased",
   "co_executed": "XLF",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014741209957466621",
   "ticker": "JPM",
   "price": "53.07",
   "action": "purchased",
   "co_executed": "XLF",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014744483280388239",
   "ticker": "XLF",
   "price": "53.07",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "[XLF 2h MA548] / MA548"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014745111209640452",
   "ticker": "XLF",
   "price": null,
   "action": "hold",
   "co_executed": "FAS, JPM",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA548"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014745907104002063",
   "ticker": "XLF",
   "price": null,
   "action": "hold",
   "co_executed": "FAS, JPM",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA548"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014750388096991319",
   "ticker": "XLF",
   "price": "53.07",
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014750834874290342",
   "ticker": "JPM",
   "price": "53.07",
   "action": "hold",
   "co_executed": "XLF",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA548"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014751796057821270",
   "ticker": "FAS",
   "price": "53.07",
   "action": "hold",
   "co_executed": "XLF",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA548"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014766131014467825",
   "ticker": "XLF",
   "price": null,
   "action": "hold",
   "co_executed": "FAS, JPM",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA548"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014766792284242065",
   "ticker": "XLF",
   "price": "53.07",
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA548"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014776242470588591",
   "ticker": "XLF",
   "price": "53.07",
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA548"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014779200763527382",
   "ticker": "MUU",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014799273272250598",
   "ticker": "XLF",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014803192081744184",
   "ticker": "XLF",
   "price": "53.07",
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA548"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014803687743557668",
   "ticker": "FAS",
   "price": "53.07",
   "action": "hold",
   "co_executed": "XLF",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA548"
  }
 },
 {
  "date": "2026-01-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2014804086991028730",
   "ticker": "JPM",
   "price": "53.07",
   "action": "hold",
   "co_executed": "XLF",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA548"
  }
 },
 {
  "date": "2026-01-26",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2015795404768735517",
   "ticker": "XLF",
   "price": "53.07",
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA548"
  }
 },
 {
  "date": "2026-01-26",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2015795860957954087",
   "ticker": "JPM",
   "price": "53.07",
   "action": "hold",
   "co_executed": "XLF",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA548"
  }
 },
 {
  "date": "2026-01-26",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2015796453197881589",
   "ticker": "FAS",
   "price": "53.07",
   "action": "purchased",
   "co_executed": "XLF",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA548"
  }
 },
 {
  "date": "2026-01-26",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2015892482920468919",
   "ticker": "XLF",
   "price": "53.07",
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA548"
  }
 },
 {
  "date": "2026-01-26",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2015892767655002587",
   "ticker": "JPM",
   "price": "53.07",
   "action": "hold",
   "co_executed": "XLF",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA548"
  }
 },
 {
  "date": "2026-01-26",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2015892989990863173",
   "ticker": "FAS",
   "price": "53.07",
   "action": "purchased",
   "co_executed": "XLF",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA548"
  }
 },
 {
  "date": "2026-01-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2016197027823288589",
   "ticker": "XLF",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA548"
  }
 },
 {
  "date": "2026-01-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2016215876698288568",
   "ticker": "XLF",
   "price": "53.07",
   "action": "purchased",
   "co_executed": "JPM, FAS",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "[XLF, magnetized buying algorithm at 2H MA548] / MA548"
  }
 },
 {
  "date": "2026-01-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2016216222975852828",
   "ticker": "XLF",
   "price": "52.84",
   "action": "sold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "[XLF, magnetized buying algorithm at 2H MA548] / MA548"
  }
 },
 {
  "date": "2026-01-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2016216519357993027",
   "ticker": "JPM",
   "price": "52.84",
   "action": "sold",
   "co_executed": "XLF",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "[XLF, magnetized buying algorithm at 2H MA548] / MA548"
  }
 },
 {
  "date": "2026-01-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2016216844911444079",
   "ticker": "FAS",
   "price": "52.84",
   "action": "sold",
   "co_executed": "XLF",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "[XLF, magnetized buying algorithm at 2H MA548] / MA548"
  }
 },
 {
  "date": "2026-01-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2016217271837012205",
   "ticker": "XLF",
   "price": "52.84",
   "action": "cut",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA548"
  }
 },
 {
  "date": "2026-01-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2016217526301295011",
   "ticker": "JPM",
   "price": "52.84",
   "action": "cut",
   "co_executed": "XLF",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA548"
  }
 },
 {
  "date": "2026-01-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2016217818216493524",
   "ticker": "FAS",
   "price": "52.84",
   "action": "cut",
   "co_executed": "XLF",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA548"
  }
 },
 {
  "date": "2026-01-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2016518453939814687",
   "ticker": "XLF",
   "price": "53.07",
   "action": "purchased",
   "co_executed": "JPM, FAS",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "[XLF, magnetized buying algorithm at 2H MA548] / MA548"
  }
 },
 {
  "date": "2026-01-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2016571190610186454",
   "ticker": "XLF",
   "price": "53.07",
   "action": "cut",
   "co_executed": "JPM",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2016571730383556959",
   "ticker": "JPM",
   "price": "53.07",
   "action": "cut",
   "co_executed": "XLF",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-01-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2016572242696745391",
   "ticker": "FAS",
   "price": "53.07",
   "action": "purchased",
   "co_executed": "XLF, JPM",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-02-02",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2018433025726697697",
   "ticker": "XLF",
   "price": "53.07",
   "action": "cut",
   "co_executed": "JPM",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-02-02",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2018433495354462394",
   "ticker": "FAS",
   "price": "53.07",
   "action": "purchased",
   "co_executed": "XLF, JPM",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-02-02",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2018433919805432136",
   "ticker": "JPM",
   "price": "53.07",
   "action": "purchased",
   "co_executed": "XLF",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-02-03",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2018705380092616932",
   "ticker": "JPM",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-02-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2019106873266635229",
   "ticker": "JPM",
   "price": "53.07",
   "action": "purchased",
   "co_executed": "XLF",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-02-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2019110309101994157",
   "ticker": "AMLD",
   "price": "12.43",
   "action": "purchased",
   "co_executed": "AMDL, AMD",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-02-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2019110497166192890",
   "ticker": "AMDL",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-02-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2019111303168835920",
   "ticker": "AMDL",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-02-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2019119629705310355",
   "ticker": "AMDL",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-02-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2019132694148571413",
   "ticker": "AMDL",
   "price": "12.43",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-02-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2019298722124013965",
   "ticker": "JPM",
   "price": null,
   "action": "purchased",
   "co_executed": "AI",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-02-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2019419149328699787",
   "ticker": "AMDL",
   "price": "374.24",
   "action": "cut",
   "co_executed": "SMH",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-02-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2019420261473559029",
   "ticker": "SMH",
   "price": "374.24",
   "action": "purchased",
   "co_executed": "SOXL, AMDL",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-02-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2019421171960410558",
   "ticker": "SMH",
   "price": null,
   "action": "purchased",
   "co_executed": "AMDL",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-02-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2019422041615876388",
   "ticker": "SMH",
   "price": "374.24",
   "action": null,
   "co_executed": "SOXL",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-02-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2019713430874472807",
   "ticker": "AMD",
   "price": "374.24",
   "action": "cut",
   "co_executed": "SMH, AMDL",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-02-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2019783075001934139",
   "ticker": "JPM",
   "price": "296.51",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-02-11",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2021670442252283910",
   "ticker": "SMH",
   "price": null,
   "action": "purchased",
   "co_executed": "SOXL",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-02-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2023821794273358211",
   "ticker": "JPM",
   "price": "296.51",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-02-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2023822790819016995",
   "ticker": "JPM",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-02-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2026701910535975107",
   "ticker": "SMH",
   "price": "374.24",
   "action": null,
   "co_executed": "SOXL",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-02",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2028563039373689323",
   "ticker": "SPXU",
   "price": "48.78",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "SPXU . 48.78 180 SMA outfit / MA720"
  }
 },
 {
  "date": "2026-03-02",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2028563190041530870",
   "ticker": "SPXU",
   "price": "48.78",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-02",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2028563596163285419",
   "ticker": "SPXU",
   "price": "48.78",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-02",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2028564309421490659",
   "ticker": "SPXU",
   "price": "48.78",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-02",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2028566507681349815",
   "ticker": "SPXU",
   "price": "48.78",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "180 SMA outfit"
  }
 },
 {
  "date": "2026-03-03",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2028692249966735543",
   "ticker": "SPXU",
   "price": null,
   "action": "purchased",
   "co_executed": "SPX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-03",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2028841770088550555",
   "ticker": "SPXU",
   "price": "48.78",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-03",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2028853859645616496",
   "ticker": "SPXU",
   "price": "48.78",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "P500 30M 180 outfit"
  }
 },
 {
  "date": "2026-03-03",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2028854393832100192",
   "ticker": "SPXU",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-03",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2028922437388386635",
   "ticker": "SPXU",
   "price": "48.78",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029219988142469309",
   "ticker": "DOG",
   "price": "23.23",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "DOG . 366 outfit"
  }
 },
 {
  "date": "2026-03-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029220227473653777",
   "ticker": "DOG",
   "price": null,
   "action": null,
   "co_executed": "SDOW",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029220663207281084",
   "ticker": "DOG",
   "price": "23.23",
   "action": "purchased",
   "co_executed": "SDOW",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "urchase at 23.23 operating from the 365 outfit / MA183 / MA23 / MA46 / MA91 / MA365 / MA730"
  }
 },
 {
  "date": "2026-03-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029221782620914021",
   "ticker": "DOG",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029222104185618825",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029225895911931997",
   "ticker": "DOG",
   "price": "23.23",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029226069497397343",
   "ticker": "DOG",
   "price": "23.23",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029229921739129138",
   "ticker": "DOG",
   "price": "23.23",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029238757841616924",
   "ticker": "DOG",
   "price": "23.23",
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA183"
  }
 },
 {
  "date": "2026-03-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029239441743856012",
   "ticker": "DOG",
   "price": "23.23",
   "action": "purchased",
   "co_executed": "SDOW",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "enced at 23.23 with banks using the 366 outfit / MA183"
  }
 },
 {
  "date": "2026-03-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029295057241817527",
   "ticker": "DOG",
   "price": null,
   "action": "purchased",
   "co_executed": "SDOW",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029297846860824966",
   "ticker": "DOG",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029297920269533385",
   "ticker": "DOG",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029301062306545849",
   "ticker": "DOG",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029318023623159870",
   "ticker": "DOG",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029571289036525615",
   "ticker": "DOG",
   "price": "23.23",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029571571934011845",
   "ticker": "DOG",
   "price": null,
   "action": null,
   "co_executed": "SDOW",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029574742622286142",
   "ticker": "PLTZ",
   "price": "26.37",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "PLTZ . Palantir's SMA outfit / MA150"
  }
 },
 {
  "date": "2026-03-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029575006469177444",
   "ticker": "PLTZ",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029575806473965635",
   "ticker": "PLTZ",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029579022003577315",
   "ticker": "DOG",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029580365023879233",
   "ticker": "DOG",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029581948201660857",
   "ticker": "PLTZ",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029589304692154713",
   "ticker": "PLTZ",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029612638842536030",
   "ticker": "DOG",
   "price": null,
   "action": "purchased",
   "co_executed": "SDOW",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029616027009700058",
   "ticker": "PLTZ",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029617140995870978",
   "ticker": "SPXU",
   "price": null,
   "action": "purchased",
   "co_executed": "DOG, SDOW, PLTZ",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029947955340542102",
   "ticker": "DOG",
   "price": "23.23",
   "action": "purchased",
   "co_executed": "SDOW",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2029948907279765601",
   "ticker": "SPXU",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-09",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2030802917356400762",
   "ticker": "SPXU",
   "price": null,
   "action": "purchased",
   "co_executed": "DOG, SDOW",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-12",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2032106086929744074",
   "ticker": "DOG",
   "price": "23.22",
   "action": "hold",
   "co_executed": "SDOW",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "366 outfit / MA183 / [366 Outfit Korea’s 9M at PARM:MA183 [coexecuted SDOW]"
  }
 },
 {
  "date": "2026-03-12",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2032112351613460771",
   "ticker": "SPXU",
   "price": "48.78",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2032547318797578643",
   "ticker": "SPXU",
   "price": "48.78",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2032552315274895660",
   "ticker": "SPXU",
   "price": "48.78",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "on the 30m 180 outfit"
  }
 },
 {
  "date": "2026-03-18",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2034304470096757001",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-18",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2034323806081499483",
   "ticker": "SPXU",
   "price": "48.78",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-18",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2034332362222473419",
   "ticker": "ORCX",
   "price": "9.43",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "Long ORCL ETF. 15M 33 66 99 333 666 999 outfit / MA333"
  }
 },
 {
  "date": "2026-03-18",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2034333800625504326",
   "ticker": "ORCX",
   "price": "9.43",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-19",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2034623555258945624",
   "ticker": "ORCX",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-19",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2034628973720973528",
   "ticker": "TQQQ",
   "price": null,
   "action": "purchased",
   "co_executed": "IXIC",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "TQQQ. IXIC at 21853. MA884 outfit / MA884 / MA28 / MA55 / MA111 / MA221 / MA442"
  }
 },
 {
  "date": "2026-03-19",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2034629667727269923",
   "ticker": "IXIC",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-19",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2034633160542327106",
   "ticker": "TSLR",
   "price": "23.98",
   "action": "purchased",
   "co_executed": "TSLQ, TSLA",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "2x Short TSLA Daily ETF. Dual Sequence outfit / MA39 / MA78 / MA156 / MA311 / MA622 / MA944"
  }
 },
 {
  "date": "2026-03-19",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2034633867580313825",
   "ticker": "TSLQ",
   "price": "23.98",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-19",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2034637427680407735",
   "ticker": "TSLQ",
   "price": "23.98",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-19",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2034639072279613941",
   "ticker": "IXIC",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-19",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2034686793053086058",
   "ticker": "TSLQ",
   "price": "23.98",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-19",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2034692995594035401",
   "ticker": "IXIC",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-19",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2034708701723185642",
   "ticker": "TQQQ",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-19",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2034721576567152989",
   "ticker": "IXIC",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2035014402731393235",
   "ticker": "TQQQ",
   "price": null,
   "action": "purchased",
   "co_executed": "IXIC",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA884 / MA28 / MA55 / MA111 / MA221 / MA442"
  }
 },
 {
  "date": "2026-03-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2035014685079347210",
   "ticker": "IXIC",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA884"
  }
 },
 {
  "date": "2026-03-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2035017100344140052",
   "ticker": "IXIC",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA884"
  }
 },
 {
  "date": "2026-03-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2035025592819884324",
   "ticker": "IXIC",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA884"
  }
 },
 {
  "date": "2026-03-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2035045580561686895",
   "ticker": "AAPU",
   "price": "26.73",
   "action": "purchased",
   "co_executed": "AAPL",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA31 / MA61 / MA122 / MA244 / MA466 / MA668"
  }
 },
 {
  "date": "2026-03-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2035068419922698641",
   "ticker": "IXIC",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2035069180983353516",
   "ticker": "IXIC",
   "price": "26.73",
   "action": "hold",
   "co_executed": "AAPU, AAPL",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "[AAPU Direxion AAPL Bull 2X Shares. 1D MA31 MA61 MA122 MA244 MA466 MA668 1D MA244 at 26.73.] / MA31 / MA61 / MA122 / MA244 / MA466 / MA668"
  }
 },
 {
  "date": "2026-03-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2035085169041011019",
   "ticker": "IXIC",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2035088719519391782",
   "ticker": "AAPL",
   "price": "246.00",
   "action": "purchased",
   "co_executed": "AAPU",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "dual sequencing program with the SMA outfit"
  }
 },
 {
  "date": "2026-03-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2035090043472318538",
   "ticker": "AAPL",
   "price": "246.00",
   "action": "purchased",
   "co_executed": "AAPU",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2035090070886371528",
   "ticker": "AAPL",
   "price": "246.00",
   "action": "cut",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2035092231527571485",
   "ticker": "AMDL",
   "price": null,
   "action": null,
   "co_executed": "SMH",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2035093264630784074",
   "ticker": "SPXU",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2035094418043412753",
   "ticker": "DOG",
   "price": null,
   "action": "sold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2035126272624640348",
   "ticker": "SPXU",
   "price": "48.78",
   "action": "sold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2035128247651115300",
   "ticker": "AAPL",
   "price": null,
   "action": "purchased",
   "co_executed": "AAPU, IXIC, TQQQ",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2035132151348490697",
   "ticker": "IXIC",
   "price": "246.00",
   "action": "purchased",
   "co_executed": "AAPU, AAPL",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2035136326794969092",
   "ticker": "USO",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036116170127052828",
   "ticker": "TQQQ",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-24",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036449671770677421",
   "ticker": "AAPL",
   "price": "246.00",
   "action": null,
   "co_executed": "AAPU",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-24",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036450170691592236",
   "ticker": "AAPL",
   "price": "246.00",
   "action": null,
   "co_executed": "AAPU",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036798265585537134",
   "ticker": "AAPU",
   "price": "246.00",
   "action": null,
   "co_executed": "AAPL",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036799020254015661",
   "ticker": "AAPL",
   "price": "246.00",
   "action": null,
   "co_executed": "AAPU",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036799949506310485",
   "ticker": "IXIC",
   "price": "246.00",
   "action": "purchased",
   "co_executed": "TQQQ",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036809380738535705",
   "ticker": "SMR",
   "price": "11.71",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "Octane outfit / MA102"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036810694721773812",
   "ticker": "SMR",
   "price": "11.71",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036812310266970543",
   "ticker": "SMR",
   "price": "11.71",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036816367727644858",
   "ticker": "SMR",
   "price": "11.71",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036820589596536979",
   "ticker": "SMR",
   "price": "11.71",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036825512644059237",
   "ticker": "SMR",
   "price": "11.52",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "SMR. 3M 818 Octane outfit / MA102"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036825616612508045",
   "ticker": "SMR",
   "price": "11.52",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036825785147986183",
   "ticker": "SMR",
   "price": "11.52",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA102"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036826336933933369",
   "ticker": "SMR",
   "price": "11.52",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "erating on a real time and threaded SMA outfit / MA102"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036826676869619756",
   "ticker": "SMR",
   "price": "11.52",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036827938558185556",
   "ticker": "SMR",
   "price": "11.52",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036828581561815213",
   "ticker": "SMR",
   "price": "11.52",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036830028890263696",
   "ticker": "SMR",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036832388723159480",
   "ticker": "MSTX",
   "price": "24.37",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA143"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036833013410201685",
   "ticker": "MSTX",
   "price": "24.37",
   "action": null,
   "co_executed": "MSTR",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA19 / MA37 / MA73 / MA143 / MA279 / MA548"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036833889919148193",
   "ticker": "MSTX",
   "price": "24.37",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036835338099044701",
   "ticker": "MSTX",
   "price": "24.37",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036835954493985224",
   "ticker": "MSTX",
   "price": "24.36",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA143"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036836094499750389",
   "ticker": "MSTX",
   "price": "24.36",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036836488240054462",
   "ticker": "MSTX",
   "price": "24.36",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA143"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036839363250929715",
   "ticker": "MSTX",
   "price": "24.28",
   "action": "cut",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "Octane outfit / MA409"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036839561733833169",
   "ticker": "MSTX",
   "price": "24.28",
   "action": null,
   "co_executed": "MSTR",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA409"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036840264434905391",
   "ticker": "MSTX",
   "price": "24.28",
   "action": null,
   "co_executed": "SMR, MSTR",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036842014650843488",
   "ticker": "MSTX",
   "price": "24.28",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036869498402398693",
   "ticker": "MSTX",
   "price": "24.20",
   "action": "purchased",
   "co_executed": "MSTR",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA26 / MA51 / MA102 / MA205 / MA409 / MA818"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036869847246921820",
   "ticker": "MSTX",
   "price": "24.20",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036870396755272176",
   "ticker": "MSTX",
   "price": "24.20",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036873535873048741",
   "ticker": "MSTX",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "positioning on MSTX here. This 30M 818 outfit"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036874851299021005",
   "ticker": "MSTR",
   "price": null,
   "action": "purchased",
   "co_executed": "MSTX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "quity higher for profit. For over 5 SMA outfit"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036876017189679561",
   "ticker": "MSTX",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036884600547647878",
   "ticker": "SCO",
   "price": "8.26",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA205"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036884734266269748",
   "ticker": "SCO",
   "price": "8.26",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036885220667060475",
   "ticker": "SCO",
   "price": "8.26",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "SCO at 8.26. 10M 818 outfit / MA205"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036886785721331974",
   "ticker": "SMR",
   "price": "11.52",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036891044110098718",
   "ticker": "SCO",
   "price": "8.26",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036893690229383415",
   "ticker": "DRN",
   "price": "8.16",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "t of trading divisions using the Octane outfit"
  }
 },
 {
  "date": "2026-03-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2036894930678014282",
   "ticker": "MSTX",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2037544193728581677",
   "ticker": "UPRO",
   "price": "92.10",
   "action": "purchased",
   "co_executed": "AAPL, AAPU",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA468"
  }
 },
 {
  "date": "2026-03-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2037544305779450017",
   "ticker": "UPRO",
   "price": "92.10",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2037545902492319989",
   "ticker": "TSLL",
   "price": "92.10",
   "action": "purchased",
   "co_executed": "UPRO",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "1st integer of 420 outfit"
  }
 },
 {
  "date": "2026-03-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2037553301991178744",
   "ticker": "TSLL",
   "price": "11.53",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2037560903865147693",
   "ticker": "TSLL",
   "price": "11.53",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2037563694050345236",
   "ticker": "FAS",
   "price": "92.10",
   "action": "purchased",
   "co_executed": "UPRO",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2037563827181736152",
   "ticker": "FAS",
   "price": "108.92",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2037567629167366561",
   "ticker": "UPRO",
   "price": "92.10",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2037574620338094354",
   "ticker": "DOG",
   "price": "24.93",
   "action": "purchased",
   "co_executed": "UDOW, NVDA, AAPL",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "Octuple and NVDA/AAPL Area Code outfit / MA26 / MA51 / MA102 / MA204 / MA408 / MA816"
  }
 },
 {
  "date": "2026-03-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2037575134006149219",
   "ticker": "UDOW",
   "price": "24.93",
   "action": "purchased",
   "co_executed": "DOG",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2037577250292564144",
   "ticker": "UDOW",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2037581439580111056",
   "ticker": "DOG",
   "price": "24.93",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2037582281611923902",
   "ticker": "DOG",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2037599878944346435",
   "ticker": "MYY",
   "price": "17.65",
   "action": "cut",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MYY at 17.65 . Palantir outfit / MA22 / MA55 / MA77 / MA220 / MA550 / MA770"
  }
 },
 {
  "date": "2026-03-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2037600851070771414",
   "ticker": "UMDD",
   "price": "17.65",
   "action": "purchased",
   "co_executed": "MYY",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "[Short: MYY at 2H MA550 at 17.65] / MA550"
  }
 },
 {
  "date": "2026-03-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2037601779547001298",
   "ticker": "UMDD",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2037605602860699813",
   "ticker": "UMDD",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2037618195495023006",
   "ticker": "UMDD",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-03-31",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2039076289769050555",
   "ticker": "IXIC",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-01",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2039405396633473274",
   "ticker": "UMDD",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041182549331030396",
   "ticker": "SSO",
   "price": "53.34",
   "action": "cut",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "om the flash higher on Putin's 2000 SMA outfit / MA500"
  }
 },
 {
  "date": "2026-04-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041182737688830428",
   "ticker": "SSO",
   "price": "53.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041187714662576389",
   "ticker": "SSO",
   "price": "53.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041190149082792243",
   "ticker": "SPXU",
   "price": "53.34",
   "action": "purchased",
   "co_executed": "SSO",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041190645810008082",
   "ticker": "SPXU",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041193924543615408",
   "ticker": "SSO",
   "price": "53.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041197104283209817",
   "ticker": "SSO",
   "price": "53.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041200121422209358",
   "ticker": "SSO",
   "price": "53.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041201064603742308",
   "ticker": "SPXU",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041202701267288493",
   "ticker": "SSO",
   "price": "53.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041203193334645104",
   "ticker": "SPXU",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041215716930793629",
   "ticker": "SSO",
   "price": "53.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041244638447915121",
   "ticker": "SSO",
   "price": "53.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041511299134472655",
   "ticker": "SSO",
   "price": "53.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041511990670327959",
   "ticker": "SPXU",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041516921842278726",
   "ticker": "SPXU",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041517589474730322",
   "ticker": "SSO",
   "price": "53.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041519045535768750",
   "ticker": "SSO",
   "price": "53.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041533813671764359",
   "ticker": "SSO",
   "price": "53.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041534277935149424",
   "ticker": "SPXU",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041581946376221167",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041593970703396964",
   "ticker": "SSO",
   "price": "53.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041596982767296923",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041886482408108236",
   "ticker": "IXIC",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041886968259473458",
   "ticker": "UMDD",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041890351473181169",
   "ticker": "ERX",
   "price": "86.13",
   "action": "purchased",
   "co_executed": "NVDA, AAPL",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "Octople and NVDA/AAPL Area outfit / MA26 / MA51 / MA102 / MA204 / MA408 / MA816"
  }
 },
 {
  "date": "2026-04-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041890508453376451",
   "ticker": "ERX",
   "price": "86.13",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041891420806770805",
   "ticker": "ERX",
   "price": "101.25",
   "action": null,
   "co_executed": "NVDA, AAPL",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "Octople and NVDA/AAPL Area outfit / MA26 / MA51 / MA102 / MA204 / MA408 / MA816"
  }
 },
 {
  "date": "2026-04-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041893229176791472",
   "ticker": "ERX",
   "price": "86.13",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041901884420813058",
   "ticker": "ERX",
   "price": "86.13",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041903753012605291",
   "ticker": "ERX",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041908256264876131",
   "ticker": "YANG",
   "price": "27.33",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA22 / MA55 / MA77 / MA222 / MA555 / MA777"
  }
 },
 {
  "date": "2026-04-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041908376289038359",
   "ticker": "YANG",
   "price": "27.33",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041909942735794328",
   "ticker": "YANG",
   "price": "27.33",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041913198979510275",
   "ticker": "ERX",
   "price": "86.13",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041921397149331902",
   "ticker": "YANG",
   "price": "27.33",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041924825158185089",
   "ticker": "YANG",
   "price": "27.33",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041931593158422980",
   "ticker": "YANG",
   "price": "27.33",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041941282831134796",
   "ticker": "YANG",
   "price": "27.33",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041944042196627866",
   "ticker": "YANG",
   "price": "27.33",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2041962503694119191",
   "ticker": "ERX",
   "price": "86.13",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-09",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2042259852341506330",
   "ticker": "ERX",
   "price": null,
   "action": "cut",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-09",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2042322287068922346",
   "ticker": "ERX",
   "price": "86.13",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-09",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2042323619356033251",
   "ticker": "YANG",
   "price": "27.33",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-12",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2043417341107859960",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2043486620171874330",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2043713380821995634",
   "ticker": "TSLZ",
   "price": "16.21",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2043713536531276006",
   "ticker": "TSLZ",
   "price": "16.21",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2043714268361900306",
   "ticker": "YANG",
   "price": "27.33",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2043714879576854916",
   "ticker": "ERX",
   "price": "86.13",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2043722925522715051",
   "ticker": "TSLZ",
   "price": "16.21",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2043729528674308566",
   "ticker": "TSLZ",
   "price": "16.21",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2043747229283037530",
   "ticker": "TSLZ",
   "price": "16.21",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2043784224206143496",
   "ticker": "ERX",
   "price": "86.13",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044061194953339231",
   "ticker": "SOXS",
   "price": "21.88",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA408"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044061367033069846",
   "ticker": "SOXS",
   "price": "21.88",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044061537862815886",
   "ticker": "SOXS",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044062827464536189",
   "ticker": "SOXS",
   "price": "21.88",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044065457226035556",
   "ticker": "SOXS",
   "price": "21.88",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044067730027098223",
   "ticker": "SOXS",
   "price": "21.74",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA200"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044067911346835740",
   "ticker": "SOXS",
   "price": "21.74",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044068200103731431",
   "ticker": "SOXS",
   "price": "21.74",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044068517662863860",
   "ticker": "SOXS",
   "price": "21.74",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044069570991010092",
   "ticker": "SOXS",
   "price": "21.74",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044070901713645705",
   "ticker": "SOXS",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044072611597176965",
   "ticker": "SOXS",
   "price": "21.74",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044074557724864943",
   "ticker": "SOXS",
   "price": "21.74",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044076717451686208",
   "ticker": "PLTZ",
   "price": "31.58",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "ort PLTR ETF 39 78 156 311 622 944 tslq outfit / MA311"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044094061313974682",
   "ticker": "BITI",
   "price": "23.13",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "BITI . I'll explain this outfit / MA124"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044096332521185323",
   "ticker": "BITI",
   "price": "23.13",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044098221623160887",
   "ticker": "BITI",
   "price": "23.13",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044100862998687898",
   "ticker": "SPXU",
   "price": "23.13",
   "action": "purchased",
   "co_executed": "BITI",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044101262216704017",
   "ticker": "SPXU",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044102803875049821",
   "ticker": "SPXU",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044103632262705441",
   "ticker": "SPXU",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044104693656498409",
   "ticker": "SPXU",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044107563558645804",
   "ticker": "BITI",
   "price": "23.13",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044109904315855328",
   "ticker": "SOXS",
   "price": "23.13",
   "action": "purchased",
   "co_executed": "BITI",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044110130682441829",
   "ticker": "SOXS",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044110421226074127",
   "ticker": "SOXS",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044114096912806290",
   "ticker": "PLTZ",
   "price": "31.58",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044118318009987434",
   "ticker": "SPXU",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044122373885178012",
   "ticker": "BITI",
   "price": "23.13",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044137485626929594",
   "ticker": "SOXS",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044137723737628938",
   "ticker": "SPXU",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044143673882136678",
   "ticker": "PLTZ",
   "price": "31.58",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044167246654980233",
   "ticker": "WEBS",
   "price": "23.13",
   "action": "purchased",
   "co_executed": "BITI",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044409410265772330",
   "ticker": "WEBS",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044409926077104203",
   "ticker": "SOXS",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044410282865574281",
   "ticker": "SPXU",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044410763671159184",
   "ticker": "PLTZ",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044411164990603761",
   "ticker": "BITI",
   "price": "23.13",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044437970187604128",
   "ticker": "SQQQ",
   "price": "23.13",
   "action": "purchased",
   "co_executed": "BITI, SOXS",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044438105370038597",
   "ticker": "SQQQ",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044438358546649120",
   "ticker": "SQQQ",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044438814496862619",
   "ticker": "SQQQ",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044441967481012264",
   "ticker": "SQQQ",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044448050433982763",
   "ticker": "SQQQ",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044457966305423520",
   "ticker": "SOXS",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044460458841940057",
   "ticker": "SOXS",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044480653539086537",
   "ticker": "UCO",
   "price": "41.22",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA200"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044480763656343600",
   "ticker": "UCO",
   "price": "41.22",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044480990127788480",
   "ticker": "UCO",
   "price": "41.22",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044481722457501753",
   "ticker": "UCO",
   "price": "41.22",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044483170394116195",
   "ticker": "UCO",
   "price": "41.22",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044486587350946009",
   "ticker": "UCO",
   "price": "41.22",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044488549777740246",
   "ticker": "UCO",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044489417444970591",
   "ticker": "UCO",
   "price": "41.22",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044492145181265956",
   "ticker": "UCO",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044498674588520570",
   "ticker": "UCO",
   "price": "41.13",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044498806562296259",
   "ticker": "UCO",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044501341897429413",
   "ticker": "UCO",
   "price": "41.13",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-16",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044778132197240926",
   "ticker": "UCO",
   "price": "41.13",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-16",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2044779205796483485",
   "ticker": "BITI",
   "price": "23.13",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2045135120412410325",
   "ticker": "SPXU",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2045135546729795871",
   "ticker": "SQQQ",
   "price": null,
   "action": "hold",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2047334923288350826",
   "ticker": "TZA",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2047337579713102119",
   "ticker": "UVIX",
   "price": "19.34",
   "action": "purchased",
   "co_executed": "SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2047338099148272088",
   "ticker": "UVIX",
   "price": "19.34",
   "action": "purchased",
   "co_executed": "SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA400"
  }
 },
 {
  "date": "2026-04-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2047339611509383611",
   "ticker": "UVIX",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2047340114599415960",
   "ticker": "SVIX",
   "price": "19.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2047341528524464336",
   "ticker": "SVIX",
   "price": "19.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2047342237764456736",
   "ticker": "UVIX",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2047346271657292082",
   "ticker": "UVIX",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2047346699899937066",
   "ticker": "SVIX",
   "price": "19.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2047347325174178061",
   "ticker": "TZA",
   "price": "48.60",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2047360708552298536",
   "ticker": "TZA",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2047361295377408335",
   "ticker": "UVIX",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2047362280925638964",
   "ticker": "SVIX",
   "price": "19.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2047364160363913237",
   "ticker": "TZA",
   "price": "48.60",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2047364883457753471",
   "ticker": "SVIX",
   "price": "19.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2047370395700035796",
   "ticker": "UVIX",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2048759686166650884",
   "ticker": "SVIX",
   "price": "19.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2048759990052425794",
   "ticker": "UVIX",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2048760591612022934",
   "ticker": "TZA",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2048761392313082367",
   "ticker": "SVIX",
   "price": null,
   "action": "purchased",
   "co_executed": "UVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2048761590858797430",
   "ticker": "SQQQ",
   "price": null,
   "action": "purchased",
   "co_executed": "TQQQ",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2048802020547854448",
   "ticker": "TZA",
   "price": "4.86",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2048802477307461947",
   "ticker": "SVIX",
   "price": "19.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049185638243819560",
   "ticker": "TZA",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049407656746688572",
   "ticker": "UVIX",
   "price": "19.34",
   "action": "purchased",
   "co_executed": "SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049408348957872166",
   "ticker": "UVIX",
   "price": "19.34",
   "action": "purchased",
   "co_executed": "SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049409417960124765",
   "ticker": "SVIX",
   "price": null,
   "action": "purchased",
   "co_executed": "UVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049481686367539329",
   "ticker": "SVIX",
   "price": "19.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049488902365560906",
   "ticker": "SVIX",
   "price": "19.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049490960149844434",
   "ticker": "SVIX",
   "price": "19.34",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049491286902841428",
   "ticker": "UVIX",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049493755653394851",
   "ticker": "UVIX",
   "price": "19.37",
   "action": "purchased",
   "co_executed": "SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "high frequency short operating on the outfit / [MA27 MA54 MA108 MA216 MA432 MA864] / MA27 / MA54 / MA108 / MA216 / MA432 / MA864"
  }
 },
 {
  "date": "2026-04-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049493891930640612",
   "ticker": "UVIX",
   "price": "19.37",
   "action": "purchased",
   "co_executed": "SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049493993059418350",
   "ticker": "UVIX",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049495012216553933",
   "ticker": "SVIX",
   "price": "19.37",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049496767943811497",
   "ticker": "SVIX",
   "price": "19.37",
   "action": "hold",
   "co_executed": "UVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049497790343245923",
   "ticker": "SVIX",
   "price": "19.37",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049499148236505220",
   "ticker": "TZA",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049501205303546328",
   "ticker": "SVIX",
   "price": "19.37",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049533862813090116",
   "ticker": "SVIX",
   "price": "19.37",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049534265667579930",
   "ticker": "UVIX",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049535061176053946",
   "ticker": "TZA",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049560832883974559",
   "ticker": "SVIX",
   "price": "19.37",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-30",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049682723871330574",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-30",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049855286719209917",
   "ticker": "SVIX",
   "price": "19.37",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-30",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049866837454889087",
   "ticker": "SVIX",
   "price": "19.37",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-30",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049867365484269888",
   "ticker": "SQQQ",
   "price": "19.37",
   "action": "purchased",
   "co_executed": "SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-30",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049867462574035413",
   "ticker": "SQQQ",
   "price": "52.22",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-30",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049868078151053823",
   "ticker": "SQQQ",
   "price": "52.22",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-30",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049874140447080515",
   "ticker": "SQQQ",
   "price": "52.22",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-30",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049874637350400266",
   "ticker": "SQQQ",
   "price": "52.22",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-30",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049892458197299244",
   "ticker": "SVIX",
   "price": "19.37",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-30",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049899610920104399",
   "ticker": "SVIX",
   "price": "19.37",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-30",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049899706915147885",
   "ticker": "UVIX",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-30",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049900295984218497",
   "ticker": "SQQQ",
   "price": "52.22",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-30",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049900874210935232",
   "ticker": "TZA",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-30",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049904459652931833",
   "ticker": "SQQQ",
   "price": "52.22",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-30",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049910913269104712",
   "ticker": "NVDX",
   "price": "17.67",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "NVDX at 17.67 as risk. Japan's 225 outfit / MA25 / MA45 / MA75 / MA225 / MA450 / MA900"
  }
 },
 {
  "date": "2026-04-30",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049911089065009434",
   "ticker": "NVDX",
   "price": "17.67",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-30",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049911930358526357",
   "ticker": "NVDX",
   "price": "17.67",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-30",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049923377843077577",
   "ticker": "MSFL",
   "price": "17.28",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MSFL . 22² or 484 outfit / MA22 / MA44 / MA121 / MA242 / MA484 / MA968"
  }
 },
 {
  "date": "2026-04-30",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049923939099697388",
   "ticker": "MSFT",
   "price": "17.28",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-04-30",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2049928834833907757",
   "ticker": "NVDX",
   "price": "17.67",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-01",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2050262228008591772",
   "ticker": "NVDX",
   "price": "17.67",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-01",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2050263357828284693",
   "ticker": "MSFL",
   "price": "17.28",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-01",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2050265445337542917",
   "ticker": "RIVN",
   "price": "15.14",
   "action": "purchased",
   "co_executed": "SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "RIVN . RIVN at 15.14 . SVIX outfit / MA26 / MA52 / MA106 / MA211 / MA422 / MA855"
  }
 },
 {
  "date": "2026-05-01",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2050265713584357758",
   "ticker": "RIVN",
   "price": "15.14",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2051317989748941058",
   "ticker": "MSFL",
   "price": "17.28",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2051700364823699643",
   "ticker": "RIVN",
   "price": "14.24",
   "action": "purchased",
   "co_executed": "RIVNL",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA636"
  }
 },
 {
  "date": "2026-05-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2052071128231985269",
   "ticker": "RIVN",
   "price": "14.24",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2052397766639542674",
   "ticker": "SABS",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA18 / MA36 / MA65 / MA180 / MA360 / MA650"
  }
 },
 {
  "date": "2026-05-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2052399306796302826",
   "ticker": "SABS",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2052411905772589379",
   "ticker": "PTIR",
   "price": "14.55",
   "action": "purchased",
   "co_executed": "PLTZ, SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA211"
  }
 },
 {
  "date": "2026-05-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2052413955893755999",
   "ticker": "MSFL",
   "price": "17.28",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2052419482786972078",
   "ticker": "PTIR",
   "price": "14.55",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2052450054200533149",
   "ticker": "SABS",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2052453681073897621",
   "ticker": "SABS",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2052478383708414032",
   "ticker": "PTIR",
   "price": "14.55",
   "action": null,
   "co_executed": "PLTZ",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2052777336790278542",
   "ticker": "PTIR",
   "price": "14.55",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2052800592247140355",
   "ticker": "SABS",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-11",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2053831420863463899",
   "ticker": "PTIR",
   "price": "14.55",
   "action": null,
   "co_executed": "PLTZ",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-12",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054080966688378897",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "this specific outfit"
  }
 },
 {
  "date": "2026-05-12",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054247722329469242",
   "ticker": "PTIR",
   "price": "14.55",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-12",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054255235603066934",
   "ticker": "MSTU",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA102"
  }
 },
 {
  "date": "2026-05-12",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054259744505012552",
   "ticker": "MSTU",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-12",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054266531169837333",
   "ticker": "PTIR",
   "price": "14.55",
   "action": null,
   "co_executed": "PLTZ",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-12",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054271103212937495",
   "ticker": "MSTR",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054564212165509203",
   "ticker": "PTIR",
   "price": "14.55",
   "action": null,
   "co_executed": "PLTZ",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054565385584955742",
   "ticker": "SABS",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA650"
  }
 },
 {
  "date": "2026-05-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054566763577380868",
   "ticker": "RIVN",
   "price": "13.87",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA16"
  }
 },
 {
  "date": "2026-05-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054567076384354373",
   "ticker": "RIVN",
   "price": "13.87",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054571133790548278",
   "ticker": "RIVN",
   "price": "13.87",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054571953143644484",
   "ticker": "PTIR",
   "price": "14.55",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054579626232660262",
   "ticker": "QPUX",
   "price": "24.76",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA125"
  }
 },
 {
  "date": "2026-05-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054581866481737762",
   "ticker": "QPUX",
   "price": "24.76",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054589108606144538",
   "ticker": "RIVN",
   "price": "13.87",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054589613029945538",
   "ticker": "SABS",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054946680202793429",
   "ticker": "QPUX",
   "price": "24.76",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054947040095092923",
   "ticker": "RIVN",
   "price": "13.87",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054948017476911474",
   "ticker": "MSFL",
   "price": "17.28",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054953480708866505",
   "ticker": "MSFL",
   "price": "17.28",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054954221699768495",
   "ticker": "MSFD",
   "price": "13.11",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MSFD on this drop. 32M 22² or 484 outfit / MA22 / MA44 / MA121 / MA242 / MA484 / MA968"
  }
 },
 {
  "date": "2026-05-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054960729418334580",
   "ticker": "MSFD",
   "price": "13.11",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054961258001301738",
   "ticker": "QID",
   "price": "13.11",
   "action": "purchased",
   "co_executed": "MSFD, QQQ",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "32M 22² or 484 outfit / [MSFD , 32M 22² or 484 outfit MA22 MA44 MA121 MA242 MA484 MA968 32M MA121 at 13.11] / MA22 / MA44 / MA121 / MA242 / MA484 / MA968"
  }
 },
 {
  "date": "2026-05-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054961414071353739",
   "ticker": "MSFD",
   "price": "13.11",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054961779751747633",
   "ticker": "QID",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054963642802864481",
   "ticker": "QID",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054972709818479051",
   "ticker": "QID",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054973399068467365",
   "ticker": "QPUX",
   "price": "24.76",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054973822244405526",
   "ticker": "RIVN",
   "price": "13.87",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054974331298697352",
   "ticker": "QID",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054977814852714598",
   "ticker": "MSFD",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054983944987431307",
   "ticker": "SPXS",
   "price": "13.11",
   "action": "purchased",
   "co_executed": "MSFD",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "32M 22² or 484 outfit / [MSFD , 32M 22² or 484 outfit MA22 MA44 MA121 MA242 MA484 MA968 32M MA121 at 13.11] / MA22 / MA44 / MA121 / MA242 / MA484 / MA968"
  }
 },
 {
  "date": "2026-05-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054984197274755119",
   "ticker": "SPXS",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054985545143689536",
   "ticker": "SPXS",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2054988977107833321",
   "ticker": "MSFD",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2055003032203780283",
   "ticker": "MSFL",
   "price": "17.28",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-14",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2055003620442333447",
   "ticker": "MSFD",
   "price": "13.11",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2055325569202757840",
   "ticker": "QID",
   "price": null,
   "action": "hold",
   "co_executed": "SPXS, MSFD",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2055352923216076863",
   "ticker": "MSFL",
   "price": "17.28",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2055364301763072361",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2055415952423166270",
   "ticker": "QID",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2055416523343470738",
   "ticker": "SPXS",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2056890353052254679",
   "ticker": "QID",
   "price": null,
   "action": "purchased",
   "co_executed": "SPXS",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2057093114683417065",
   "ticker": "SPXS",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2057093486709768412",
   "ticker": "QID",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2057101476858925126",
   "ticker": "NVDX",
   "price": "20.90",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA420"
  }
 },
 {
  "date": "2026-05-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2057104681047048229",
   "ticker": "NVDX",
   "price": "20.90",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-26",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2059285006204518754",
   "ticker": "UCO",
   "price": "45.41",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA600"
  }
 },
 {
  "date": "2026-05-26",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2059285080787578889",
   "ticker": "UCO",
   "price": "45.41",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-26",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2059294863896858915",
   "ticker": "UCO",
   "price": "45.41",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-26",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2059298644403376541",
   "ticker": "UCO",
   "price": "45.41",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "s 30 60 90 outfit"
  }
 },
 {
  "date": "2026-05-26",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2059348956640161875",
   "ticker": "UCO",
   "price": "45.41",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-26",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2059364012886999417",
   "ticker": "UCO",
   "price": "45.41",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-26",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2059366606342664332",
   "ticker": "UCO",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA600 / [parm:MA600]"
  }
 },
 {
  "date": "2026-05-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2059630977887170669",
   "ticker": "UCO",
   "price": null,
   "action": "purchased",
   "co_executed": "USO",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "UCO into this drop. There's a positive outfit / MA600"
  }
 },
 {
  "date": "2026-05-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2059631287934349373",
   "ticker": "UCO",
   "price": null,
   "action": "hold",
   "co_executed": "USO",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2059631532688789973",
   "ticker": "UCO",
   "price": null,
   "action": "purchased",
   "co_executed": "USO",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "positive microterm USO sma outfit / MA600"
  }
 },
 {
  "date": "2026-05-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2059647311098323075",
   "ticker": "USO",
   "price": null,
   "action": "hold",
   "co_executed": "UCO",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "[MA27 MA54 MA108 MA216 MA432 MA864.] / MA27 / MA54 / MA108 / MA216 / MA432 / MA864"
  }
 },
 {
  "date": "2026-05-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2059661871482106321",
   "ticker": "USO",
   "price": "129.78",
   "action": "purchased",
   "co_executed": "UCO",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2059662020153336090",
   "ticker": "USO",
   "price": "129.78",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2059662853137895543",
   "ticker": "USO",
   "price": "129.78",
   "action": null,
   "co_executed": "SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA108"
  }
 },
 {
  "date": "2026-05-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2059664651676500054",
   "ticker": "USO",
   "price": "129.78",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2059673280379072661",
   "ticker": "USO",
   "price": "129.78",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2059703832867917826",
   "ticker": "USO",
   "price": "129.78",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2059706833292664879",
   "ticker": "USO",
   "price": "129.64",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA512"
  }
 },
 {
  "date": "2026-05-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2059707409128640772",
   "ticker": "USO",
   "price": "129.64",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "n't know why this specific timeframe or outfit / MA512"
  }
 },
 {
  "date": "2026-05-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2059712830329512007",
   "ticker": "USO",
   "price": "129.64",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2059990777498066978",
   "ticker": "USO",
   "price": "129.64",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2060006218920493116",
   "ticker": "USO",
   "price": "127.77",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "USO as my final Oil trade. 22² or 484 outfit / MA22 / MA44 / MA121 / MA242 / MA484 / MA986"
  }
 },
 {
  "date": "2026-05-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2060006568440332687",
   "ticker": "USO",
   "price": "127.77",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2060008193103995078",
   "ticker": "SQQQ",
   "price": "127.77",
   "action": "purchased",
   "co_executed": "USO",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2060008676421960059",
   "ticker": "SPXU",
   "price": "127.77",
   "action": "purchased",
   "co_executed": "USO",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2060164674398888092",
   "ticker": "SOXS",
   "price": "5.48",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-05-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2060434673621422141",
   "ticker": "SCO",
   "price": "28.38",
   "action": "purchased",
   "co_executed": "UCO",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA770"
  }
 },
 {
  "date": "2026-05-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2060435028275052566",
   "ticker": "UCO",
   "price": "28.38",
   "action": "purchased",
   "co_executed": "SCO",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "[SCO 20M 22 55 77 220 550 770 20M MA770 at 28.38] / MA770"
  }
 },
 {
  "date": "2026-05-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2060435149138055678",
   "ticker": "UCO",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-01",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2061275088352371041",
   "ticker": "UCO",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-01",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2061443534503485603",
   "ticker": "UCO",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-01",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2061443547639984183",
   "ticker": "SCO",
   "price": "28.38",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-02",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2061837124975075546",
   "ticker": "SCO",
   "price": "28.38",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-02",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2061892473073610867",
   "ticker": "UCO",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-03",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2062193255362806007",
   "ticker": "UCO",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-03",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2062194158421553252",
   "ticker": "SCO",
   "price": "28.38",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-03",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2062194973664268646",
   "ticker": "SCO",
   "price": "28.38",
   "action": "cut",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2062591467361841455",
   "ticker": "UCO",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2062591954626757003",
   "ticker": "SCO",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2064036790475079836",
   "ticker": "UCO",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2064037355800150459",
   "ticker": "SCO",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-09",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2064378917478359410",
   "ticker": "SCO",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-09",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2064379658377080874",
   "ticker": "UCO",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-09",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2064387754113511775",
   "ticker": "UCO",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-09",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2064388276744790385",
   "ticker": "SCO",
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2064727684597629315",
   "ticker": "SVIX",
   "price": "20.01",
   "action": "purchased",
   "co_executed": "VIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA777"
  }
 },
 {
  "date": "2026-06-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2064728388926136544",
   "ticker": "SVIX",
   "price": "20.01",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2064729168420725118",
   "ticker": "SVIX",
   "price": "20.01",
   "action": "cut",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2064737081763742029",
   "ticker": "SVIX",
   "price": "20.01",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2064738410745745768",
   "ticker": "SVIX",
   "price": "19.95",
   "action": "purchased",
   "co_executed": "VIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA500"
  }
 },
 {
  "date": "2026-06-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2064738489909002728",
   "ticker": "SVIX",
   "price": "19.95",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2064738778405908544",
   "ticker": "UPRO",
   "price": "19.95",
   "action": "purchased",
   "co_executed": "SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2064738868138856633",
   "ticker": "UPRO",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2064739182237696155",
   "ticker": "TQQQ",
   "price": "19.95",
   "action": "purchased",
   "co_executed": "SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2064739349636518200",
   "ticker": "TQQQ",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2064742487630270722",
   "ticker": "SVIX",
   "price": "19.95",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2064743494137356597",
   "ticker": "UCO",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2064744005540470988",
   "ticker": "SCO",
   "price": "28.38",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2064745462033523008",
   "ticker": "SVIX",
   "price": "19.95",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "31 63 125 250 500 simple moving average outfit / MA500"
  }
 },
 {
  "date": "2026-06-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2064790307875811770",
   "ticker": "SVIX",
   "price": "19.95",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-11",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2065064353108525549",
   "ticker": "SVIX",
   "price": "19.95",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-11",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2065086193583407463",
   "ticker": "SVIX",
   "price": "19.95",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-11",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2065090270937649267",
   "ticker": "SPXU",
   "price": "41.31",
   "action": "purchased",
   "co_executed": "UPRO",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "31 . 33M 22 55 77 220 550 770 palantir outfit"
  }
 },
 {
  "date": "2026-06-11",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2065090409001574777",
   "ticker": "SPXU",
   "price": "41.31",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-11",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2065090770961670196",
   "ticker": "UPRO",
   "price": "41.31",
   "action": "purchased",
   "co_executed": "SPXU",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-11",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2065090880420389096",
   "ticker": "UPRO",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-11",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2065091446173257854",
   "ticker": "SPXU",
   "price": "41.31",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-11",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2065125327052079422",
   "ticker": "SPXU",
   "price": "41.31",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-11",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2065158583952753116",
   "ticker": "UPRO",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-11",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2065165376305156119",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2066325364247548339",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2066518386386084350",
   "ticker": "UCO",
   "price": "28.38",
   "action": "purchased",
   "co_executed": "SCO",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "[SCO 20M 22 55 77 220 550 770 20M MA770 at 28.38] / MA770"
  }
 },
 {
  "date": "2026-06-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2066519016743875046",
   "ticker": "UPRO",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-15",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2066519353869365390",
   "ticker": "SPXU",
   "price": "41.31",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-22",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2069056205562200341",
   "ticker": "SPXU",
   "price": "41.31",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-22",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2069056889523241067",
   "ticker": "UPRO",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-22",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2069068669100179889",
   "ticker": "GUSH",
   "price": "29.48",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "P Oil 2x 29.48 . 404 outfit / MA404"
  }
 },
 {
  "date": "2026-06-22",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2069068790604927380",
   "ticker": "GUSH",
   "price": "29.48",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-22",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2069069052925112656",
   "ticker": "GUSH",
   "price": "29.47",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-22",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2069103966240289100",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-22",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2069149534224331075",
   "ticker": "GUSH",
   "price": "29.48",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-23",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2069511580426092781",
   "ticker": "GUSH",
   "price": "29.48",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-24",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2069671768911118527",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-24",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2069792843288440859",
   "ticker": "GUSH",
   "price": "29.41",
   "action": "purchased",
   "co_executed": "SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "SH now. 4H SVIX's 26 52 106 211 422 844 outfit / MA422"
  }
 },
 {
  "date": "2026-06-24",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2069793870662320131",
   "ticker": "GUSH",
   "price": "29.23",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-24",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2069846278172012977",
   "ticker": "GUSH",
   "price": "29.23",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2070139435862335983",
   "ticker": "GUSH",
   "price": "29.23",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2070210599154577468",
   "ticker": "GUSH",
   "price": "29.23",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-06-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2070220600157880464",
   "ticker": "GUSH",
   "price": "29.23",
   "action": "purchased",
   "co_executed": "SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "SVIX's 26 52 106 211 422 844 outfit"
  }
 },
 {
  "date": "2026-06-25",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2079844121003610554",
   "ticker": "GUSH",
   "price": "29.23",
   "action": "purchased",
   "co_executed": "SVIX",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "SVIX's 26 52 106 211 422 844 outfit"
  }
 },
 {
  "date": "2026-06-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2071595712501219676",
   "ticker": "GUSH",
   "price": "29.23",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2074187308384092241",
   "ticker": "GUSH",
   "price": "29.23",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2074573625034985642",
   "ticker": "GUSH",
   "price": "29.23",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2074574241199223033",
   "ticker": "GUSH",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-07",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2086878153931432241",
   "ticker": "GUSH",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-08",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2074795288552939796",
   "ticker": "GUSH",
   "price": "29.23",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-09",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2075311433970319751",
   "ticker": "UPRO",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-09",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2075312179893669970",
   "ticker": "SPXU",
   "price": "41.31",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-09",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2075312700020994307",
   "ticker": "GUSH",
   "price": "29.23",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-12",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2076098582747426830",
   "ticker": "GUSH",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-12",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2086878089691459934",
   "ticker": "GUSH",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2076734736911958123",
   "ticker": "GUSH",
   "price": "29.23",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2078208525927690693",
   "ticker": "GUSH",
   "price": "29.23",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-19",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2078652675764392205",
   "ticker": null,
   "price": null,
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2081759657807560759",
   "ticker": "SPYU",
   "price": "30.65",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA332"
  }
 },
 {
  "date": "2026-07-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2081760100474393028",
   "ticker": "SPYU",
   "price": "30.65",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2081761432996298985",
   "ticker": "SPYU",
   "price": "30.65",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2081766261672014024",
   "ticker": "SPYU",
   "price": "30.65",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2081779210297962506",
   "ticker": "SPYU",
   "price": "30.65",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2081791790815084669",
   "ticker": "SPYU",
   "price": "30.65",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2081795896556257581",
   "ticker": "SPYU",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-27",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2081832451006169391",
   "ticker": "SPYU",
   "price": "30.65",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2082097424806650287",
   "ticker": "SPYU",
   "price": "30.65",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-28",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2082202132124676196",
   "ticker": "SPYU",
   "price": "30.65",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2082362989362212948",
   "ticker": "GUSH",
   "price": "30.00",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-07-29",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2082368156946104473",
   "ticker": "GUSH",
   "price": "29.41",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2084657627922051475",
   "ticker": "HIBS",
   "price": "17.92",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA19"
  }
 },
 {
  "date": "2026-08-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2084657778594087163",
   "ticker": "HIBS",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2084661311393485260",
   "ticker": "HIBS",
   "price": "17.92",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2084665626107461650",
   "ticker": "SPXU",
   "price": "17.92",
   "action": "purchased",
   "co_executed": "HIBS",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2084669086169240014",
   "ticker": "SQQQ",
   "price": "17.92",
   "action": "purchased",
   "co_executed": "HIBS, QQQ",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2084669211755073611",
   "ticker": "SQQQ",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-04",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2084672206534222118",
   "ticker": "SQQQ",
   "price": "17.92",
   "action": "purchased",
   "co_executed": "HIBS",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2085010457488998898",
   "ticker": "SPXU",
   "price": "120.00",
   "action": "purchased",
   "co_executed": "SQQQ, HIBS, HIBL",
   "outfit": null,
   "note": "gap era; date+ticker+price from text; outfit stated IN TEXT (rare) - see outfit_text",
   "outfit_text": "MA83"
  }
 },
 {
  "date": "2026-08-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2085010631313506765",
   "ticker": "HIBL",
   "price": "120.00",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2085011001859297344",
   "ticker": "SPXU",
   "price": "120.00",
   "action": "purchased",
   "co_executed": "HIBL",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2085011230285320458",
   "ticker": "SQQQ",
   "price": "120.00",
   "action": "purchased",
   "co_executed": "HIBL",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2085011484850217088",
   "ticker": "HIBS",
   "price": "120.00",
   "action": "purchased",
   "co_executed": "HIBL",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2085011740279132423",
   "ticker": "HIBS",
   "price": "120.00",
   "action": "purchased",
   "co_executed": "HIBL",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2085011948064903200",
   "ticker": "SQQQ",
   "price": "120.00",
   "action": "purchased",
   "co_executed": "HIBL",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2085012106437706058",
   "ticker": "SPXU",
   "price": "120.00",
   "action": "purchased",
   "co_executed": "HIBL",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2085018775053812136",
   "ticker": "HIBL",
   "price": "120.00",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2085093584395808779",
   "ticker": "HIBL",
   "price": "120.00",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2085093956480807220",
   "ticker": "HIBS",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2085094263214518506",
   "ticker": "SQQQ",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-05",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2085094510930079894",
   "ticker": "SPXU",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2085397233999163556",
   "ticker": "SPXU",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2085397678528360861",
   "ticker": "SQQQ",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2085397965183865111",
   "ticker": "HIBS",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-06",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2085398379534962883",
   "ticker": "HIBL",
   "price": "120.00",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2086863222720913501",
   "ticker": "GUSH",
   "price": "29.23",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-10",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2086863939489710550",
   "ticker": "GUSH",
   "price": "29.23",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-13",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2087935089120542889",
   "ticker": "SPXU",
   "price": "120.00",
   "action": "purchased",
   "co_executed": "SQQQ, HIBS",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2089389098238923018",
   "ticker": "HIBL",
   "price": "120.00",
   "action": "purchased",
   "co_executed": "SQQQ, SPXU, HIBS",
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2089403996373217460",
   "ticker": "HIBL",
   "price": "120.00",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2089442386120511901",
   "ticker": "SPXU",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2089442919099076884",
   "ticker": "SQQQ",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2089443325321642267",
   "ticker": "HIBS",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-17",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2089444337025466604",
   "ticker": "GUSH",
   "price": "29.23",
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-18",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2089804677814886771",
   "ticker": "SPXU",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2090527891960549445",
   "ticker": "SPXU",
   "price": null,
   "action": "purchased",
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 },
 {
  "date": "2026-08-20",
  "type": "gap_finding",
  "label": "Gap Finding",
  "category": "Gap Finding",
  "fields": {
   "post_id": "2090543213904052618",
   "ticker": "HIBL",
   "price": "120.00",
   "action": null,
   "co_executed": null,
   "outfit": null,
   "note": "gap era; date+ticker+price from text, outfit pending vision"
  }
 }
]);
