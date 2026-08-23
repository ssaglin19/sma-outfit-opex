/* ---------------------------------------------------------------------------
 * OPEX LAYER  --  code-generated, deterministic, no data source, no network.
 *
 * APPENDS to the shared global, so include order relative to entries.js does
 * not matter:
 *     window.CALENDAR_ENTRIES = window.CALENDAR_ENTRIES || [];
 *     window.CALENDAR_ENTRIES.push(...);
 *
 * All entries use type "opex", so the whole set shares ONE toggle in the UI.
 * `category` carries the sub-kind and drives the colour.
 *
 * RULES (2023-01-01 .. 2026-12-31)
 *   Monthly OPEX     3rd Friday of every month.
 *   Triple Witching  3rd Friday of Mar / Jun / Sep / Dec. These months emit a
 *                    Triple Witching entry INSTEAD of a Monthly OPEX one, so a
 *                    date is never double-marked with two names for one event.
 *   VIX Expiration   3rd-Friday(next month) minus 30 days -- normally a Wednesday.
 *
 * HOLIDAY ADJUSTMENT (NYSE closures hardcoded in the generator)
 *   A 3rd Friday landing on a holiday moves to the preceding business day.
 *   A VIX Wednesday landing on a holiday/weekend moves to the preceding
 *   business day. Adjusted entries carry fields.holiday_adjusted = true.
 *
 * REGENERATE: re-run the generator that produced this file. Do NOT hand-edit --
 * edits are lost on the next run. entries.js (the case-study layer) is a
 * separate file and is never touched by this one.
 * --------------------------------------------------------------------------- */

window.CALENDAR_ENTRIES = window.CALENDAR_ENTRIES || [];
window.CALENDAR_ENTRIES.push.apply(window.CALENDAR_ENTRIES, [
 {
  "date": "2023-01-18",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-01-20",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-02-15",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-02-17",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-03-17",
  "type": "opex",
  "label": "Triple Witching",
  "category": "Triple Witching",
  "fields": {
   "kind": "Triple Witching",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-03-22",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-04-19",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-04-21",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-05-17",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-05-19",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-06-16",
  "type": "opex",
  "label": "Triple Witching",
  "category": "Triple Witching",
  "fields": {
   "kind": "Triple Witching",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-06-21",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-07-19",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-07-21",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-08-16",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-08-18",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-09-15",
  "type": "opex",
  "label": "Triple Witching",
  "category": "Triple Witching",
  "fields": {
   "kind": "Triple Witching",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-09-20",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-10-18",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-10-20",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-11-15",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-11-17",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-12-15",
  "type": "opex",
  "label": "Triple Witching",
  "category": "Triple Witching",
  "fields": {
   "kind": "Triple Witching",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2023-12-20",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-01-17",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-01-19",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-02-14",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-02-16",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-03-15",
  "type": "opex",
  "label": "Triple Witching",
  "category": "Triple Witching",
  "fields": {
   "kind": "Triple Witching",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-03-20",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-04-17",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-04-19",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-05-17",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-05-22",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-06-18",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Tue",
   "holiday_adjusted": true
  }
 },
 {
  "date": "2024-06-21",
  "type": "opex",
  "label": "Triple Witching",
  "category": "Triple Witching",
  "fields": {
   "kind": "Triple Witching",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-07-17",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-07-19",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-08-16",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-08-21",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-09-18",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-09-20",
  "type": "opex",
  "label": "Triple Witching",
  "category": "Triple Witching",
  "fields": {
   "kind": "Triple Witching",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-10-16",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-10-18",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-11-15",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-11-20",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-12-18",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2024-12-20",
  "type": "opex",
  "label": "Triple Witching",
  "category": "Triple Witching",
  "fields": {
   "kind": "Triple Witching",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-01-17",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-01-22",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-02-19",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-02-21",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-03-19",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-03-21",
  "type": "opex",
  "label": "Triple Witching",
  "category": "Triple Witching",
  "fields": {
   "kind": "Triple Witching",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-04-16",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-04-17",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Thu",
   "holiday_adjusted": true
  }
 },
 {
  "date": "2025-05-16",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-05-21",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-06-18",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-06-20",
  "type": "opex",
  "label": "Triple Witching",
  "category": "Triple Witching",
  "fields": {
   "kind": "Triple Witching",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-07-16",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-07-18",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-08-15",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-08-20",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-09-17",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-09-19",
  "type": "opex",
  "label": "Triple Witching",
  "category": "Triple Witching",
  "fields": {
   "kind": "Triple Witching",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-10-17",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-10-22",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-11-19",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-11-21",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-12-17",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2025-12-19",
  "type": "opex",
  "label": "Triple Witching",
  "category": "Triple Witching",
  "fields": {
   "kind": "Triple Witching",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-01-16",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-01-21",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-02-18",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-02-20",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-03-18",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-03-20",
  "type": "opex",
  "label": "Triple Witching",
  "category": "Triple Witching",
  "fields": {
   "kind": "Triple Witching",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-04-15",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-04-17",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-05-15",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-05-20",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-06-17",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-06-18",
  "type": "opex",
  "label": "Triple Witching",
  "category": "Triple Witching",
  "fields": {
   "kind": "Triple Witching",
   "weekday": "Thu",
   "holiday_adjusted": true
  }
 },
 {
  "date": "2026-07-17",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-07-22",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-08-19",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-08-21",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-09-16",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-09-18",
  "type": "opex",
  "label": "Triple Witching",
  "category": "Triple Witching",
  "fields": {
   "kind": "Triple Witching",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-10-16",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-10-21",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-11-18",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-11-20",
  "type": "opex",
  "label": "Monthly OPEX",
  "category": "Monthly OPEX",
  "fields": {
   "kind": "Monthly OPEX",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-12-16",
  "type": "opex",
  "label": "VIX Expiration",
  "category": "VIX Expiration",
  "fields": {
   "kind": "VIX Expiration",
   "weekday": "Wed",
   "holiday_adjusted": false
  }
 },
 {
  "date": "2026-12-18",
  "type": "opex",
  "label": "Triple Witching",
  "category": "Triple Witching",
  "fields": {
   "kind": "Triple Witching",
   "weekday": "Fri",
   "holiday_adjusted": false
  }
 }
]);
