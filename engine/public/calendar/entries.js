/* ---------------------------------------------------------------------------
 * CALENDAR ENTRIES  --  data layer for archive/calendar/index.html
 *
 * Loaded via <script src="entries.js"> and assigned to a global, NOT fetched,
 * so the dashboard works from file:// with no CORS problems and no server.
 *
 * SCHEMA -- every entry is a plain object:
 *
 *   {
 *     date:     "YYYY-MM-DD",     // required. Local calendar date.
 *     type:     "case_study",     // required. Free-form. Each distinct value
 *                                 //   automatically becomes its own toggleable
 *                                 //   layer in the UI. e.g. "opex", "custom".
 *     label:    "Case Study #7",  // required. Shown on the chip and in the panel.
 *     category: "Precision Buy",  // optional. Drives the colour. Unknown values
 *                                 //   fall back to a neutral grey automatically.
 *     fields:   { any: "value" }, // optional. Arbitrary key/value pairs. The detail
 *                                 //   panel renders WHATEVER keys are present, so a
 *                                 //   new entry type with different fields needs no
 *                                 //   code change at all.
 *     link:     "../path/file.md" // optional. Relative to this folder.
 *   }
 *
 * ADDING MORE
 *   - More case studies: append objects with type "case_study".
 *   - A whole new layer: append objects with a new `type` (e.g. "opex"). A
 *     checkbox for it appears by itself; months containing it join the
 *     prev/next navigation and the jump dropdown by themselves.
 *   - New colours: add to CATEGORY_COLOURS in index.html. Not required -- any
 *     unknown category renders grey and still works.
 *
 * Nothing in index.html hardcodes "case_study". It renders whatever is here.
 *
 * GENERATED from archive/catalog_table.csv. Regenerating overwrites hand edits,
 * so append new layers in a separate file or re-apply them after a rebuild.
 * --------------------------------------------------------------------------- */

window.CALENDAR_ENTRIES = [
 {
  "date": "2023-03-22",
  "type": "case_study",
  "label": "Case Study #8",
  "category": "Precision Buy",
  "fields": {
   "outfit": "MA222",
   "timeframe": "2m",
   "ticker": "SQQQ",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/01_1638591891926315008/thread.md"
 },
 {
  "date": "2023-06-05",
  "type": "case_study",
  "label": "Case Study #17",
  "category": "Precision Buy",
  "fields": {
   "outfit": "AAPL has been using the 420 outfit / MA420",
   "timeframe": "15s",
   "ticker": "AAPL",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/02_1665724472509489153/thread.md"
 },
 {
  "date": "2023-07-17",
  "type": "case_study",
  "label": "Case Study #9",
  "category": "Precision Buy",
  "fields": {
   "outfit": "22/55",
   "timeframe": "15s",
   "ticker": "TQQQ",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/03_1680939924688891907/thread.md"
 },
 {
  "date": "2023-09-12",
  "type": "case_study",
  "label": "Case Study #18",
  "category": "Precision Buy",
  "fields": {
   "outfit": "MA200",
   "timeframe": "2m",
   "ticker": "IXIC",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/04_1701648625942823328/thread.md"
 },
 {
  "date": "2023-09-21",
  "type": "case_study",
  "label": "Case Study #6",
  "category": "Precision Buy",
  "fields": {
   "outfit": "Well happening just now is the Biden MA outfit / MA368",
   "timeframe": "15s",
   "ticker": "SQQQ",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/05_1704869290284085405/thread.md"
 },
 {
  "date": "2023-10-06",
  "type": "case_study",
  "label": "Case Study #7",
  "category": "Precision Buy",
  "fields": {
   "outfit": "MA25 MA51 MA101 MA202 MA404 MA808",
   "timeframe": "15s",
   "ticker": "TQQQ",
   "status": "OK",
   "source": "image"
  },
  "link": "../threads/06_1710286567292670381/thread.md"
 },
 {
  "date": "2023-10-31",
  "type": "case_study",
  "label": "Case Study #16",
  "category": "Precision Buy",
  "fields": {
   "outfit": "MA808",
   "timeframe": "2m",
   "ticker": "TQQQ",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/07_1719392379776758111/thread.md"
 },
 {
  "date": "2023-11-08",
  "type": "case_study",
  "label": "Case Study #5",
  "category": "Precision Buy",
  "fields": {
   "outfit": "2m ma528 . The 33rd Day outfit / MA528",
   "timeframe": "2m",
   "ticker": "IXIC",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/08_1722300546579906918/thread.md"
 },
 {
  "date": "2023-11-09",
  "type": "case_study",
  "label": "Case Study #4",
  "category": "Precision Buy",
  "fields": {
   "outfit": "World Trade outfit",
   "timeframe": "2m",
   "ticker": "TQQQ",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/09_1722639754444112000/thread.md"
 },
 {
  "date": "2023-11-21",
  "type": "case_study",
  "label": "Case Study #3",
  "category": "Precision Buy",
  "fields": {
   "outfit": "MA999",
   "timeframe": "2m",
   "ticker": "TQQQ",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/10_1726988134590865457/thread.md"
 },
 {
  "date": "2023-11-22",
  "type": "case_study",
  "label": "Case Study #2",
  "category": "Precision Buy",
  "fields": {
   "outfit": "15s 46 outfit / MA736",
   "timeframe": "15s",
   "ticker": "TQQQ",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/11_1727346193087521118/thread.md"
 },
 {
  "date": "2023-12-05",
  "type": "case_study",
  "label": "Case Study #1",
  "category": "Precision Buy",
  "fields": {
   "outfit": "MA25 MA51 MA101 MA202 MA404 MA808",
   "timeframe": "3m",
   "ticker": "IXIC",
   "status": "OK",
   "source": "image"
  },
  "link": "../threads/12_1732096473830129976/thread.md"
 },
 {
  "date": "2023-12-14",
  "type": "case_study",
  "label": "Case Study #1",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "MA404",
   "ticker": "SQQQ",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/13_1735328921116434754/thread.md"
 },
 {
  "date": "2024-01-08",
  "type": "case_study",
  "label": "Case Study #14",
  "category": "Precision Buy",
  "fields": {
   "outfit": "hey've operated the Dollar using Elon's outfit",
   "timeframe": "20m",
   "ticker": "DXY",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/14_1744426109792637303/thread.md"
 },
 {
  "date": "2024-02-06",
  "type": "case_study",
  "label": "Case Study #15",
  "category": "Precision Buy",
  "fields": {
   "outfit": "ate the NASDAQ like this. The 22/55 sma outfit / MA555 / 22/55",
   "timeframe": "2m",
   "ticker": "IXIC",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/15_1754948852875133242/thread.md"
 },
 {
  "date": "2024-03-18",
  "type": "case_study",
  "label": "Case Study #13",
  "category": "Precision Buy",
  "fields": {
   "outfit": "MA420",
   "timeframe": "3m",
   "ticker": "TSLA",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/16_1769777022702592176/thread.md"
 },
 {
  "date": "2024-03-28",
  "type": "case_study",
  "label": "Case Study #12",
  "category": "Precision Buy",
  "fields": {
   "outfit": "at 443.73. That's the Waring's Problem outfit / MA279",
   "timeframe": "2m",
   "ticker": "QQQ",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/17_1773401391211680189/thread.md"
 },
 {
  "date": "2024-04-18",
  "type": "case_study",
  "label": "Case Study #11",
  "category": "Precision Buy",
  "fields": {
   "timeframe": "1m",
   "ticker": "TQQQ",
   "status": "REVIEW (no outfit)",
   "source": "image"
  },
  "link": "../threads/18_1781030313558446458/thread.md"
 },
 {
  "date": "2024-04-19",
  "type": "case_study",
  "label": "Case Study #10",
  "category": "Precision Buy",
  "fields": {
   "outfit": "MA22",
   "timeframe": "30s",
   "ticker": "TQQQ",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/19_1781374864101929388/thread.md"
 },
 {
  "date": "2024-05-14",
  "type": "case_study",
  "label": "Case Study #19",
  "category": "Precision Buy",
  "fields": {
   "outfit": "triggering the 30/60 SMA outfit / 30/60",
   "timeframe": "2m",
   "ticker": "TQQQ GME",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/20_1790431830908477912/thread.md"
 },
 {
  "date": "2024-06-04",
  "type": "case_study",
  "label": "Case Study #20",
  "category": "Precision Buy",
  "fields": {
   "outfit": "MA60",
   "timeframe": "5m",
   "ticker": "DJI",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/21_1798025296303812840/thread.md"
 },
 {
  "date": "2024-06-12",
  "type": "case_study",
  "label": "Case Study #21",
  "category": "Precision Buy",
  "fields": {
   "outfit": "nt of arbitrage operating on the 47 SMA outfit / MA99",
   "timeframe": "5m",
   "ticker": "TQQQ",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/22_1800979221155881206/thread.md"
 },
 {
  "date": "2024-06-27",
  "type": "case_study",
  "label": "Case Study #22",
  "category": "Precision Buy",
  "fields": {
   "outfit": "MA20 MA100 MA250",
   "timeframe": "20m",
   "ticker": "SOXS",
   "direction": "long",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/23_1806322176234278947/thread.md"
 },
 {
  "date": "2024-06-28",
  "type": "case_study",
  "label": "Case Study #1",
  "category": "Hard Stop",
  "fields": {
   "outfit": "MA448",
   "timeframe": "3m",
   "ticker": "TQQQ",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/24_1806729697952465164/thread.md"
 },
 {
  "date": "2024-06-28",
  "type": "case_study",
  "label": "Case Study #1",
  "category": "Automated Short",
  "fields": {
   "outfit": "ore context now. Remember that SAME sma outfit",
   "timeframe": "30s",
   "ticker": "TQQQ",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/25_1806754622008389809/thread.md"
 },
 {
  "date": "2024-07-01",
  "type": "case_study",
  "label": "Case Study #23",
  "category": "Precision Buy",
  "fields": {
   "outfit": "MA200",
   "timeframe": "2m",
   "ticker": "QQQ",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/26_1807859031392018829/thread.md"
 },
 {
  "date": "2024-07-08",
  "type": "case_study",
  "label": "Case Study #24",
  "category": "Precision Buy",
  "fields": {
   "outfit": "MA25 MA50 MA100 MA200 MA400 MA600",
   "timeframe": "2m",
   "ticker": "IXIC",
   "direction": "long",
   "status": "OK",
   "source": "image"
  },
  "link": "../threads/27_1810385042373480462/thread.md"
 },
 {
  "date": "2024-07-10",
  "type": "case_study",
  "label": "Case Study #2",
  "category": "Hard Stop",
  "fields": {
   "outfit": "144 MA outfit / MA144",
   "timeframe": "3m",
   "ticker": "GME",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/28_1811106996160188797/thread.md"
 },
 {
  "date": "2024-07-10",
  "type": "case_study",
  "label": "Case Study #2",
  "category": "Automated Short",
  "fields": {
   "outfit": "specific sma outfit / MA72",
   "timeframe": "3m",
   "ticker": "GME",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/29_1811111465740554585/thread.md"
 },
 {
  "date": "2024-07-19",
  "type": "case_study",
  "label": "Case Study #25",
  "category": "Precision Buy",
  "fields": {
   "outfit": "MA808",
   "timeframe": "2m",
   "ticker": "SPXU",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/30_1814382183920050199/thread.md"
 },
 {
  "date": "2024-07-22",
  "type": "case_study",
  "label": "Case Study #26",
  "category": "Precision Buy",
  "fields": {
   "outfit": "TQQQ 72.12 . 3m MA188 47 outfit / MA188",
   "timeframe": "3m",
   "ticker": "TQQQ",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/31_1815414234634977687/thread.md"
 },
 {
  "date": "2024-08-09",
  "type": "case_study",
  "label": "Case Study #2",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "MA444",
   "timeframe": "1m",
   "ticker": "QQQ",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/32_1821944746127831132/thread.md"
 },
 {
  "date": "2024-08-16",
  "type": "case_study",
  "label": "Case Study #27",
  "category": "Precision Buy",
  "fields": {
   "outfit": "Speaker of the House outfit / MA224",
   "timeframe": "1m",
   "ticker": "QQQ",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/33_1824513003234226409/thread.md"
 },
 {
  "date": "2024-08-22",
  "type": "case_study",
  "label": "Case Study #3",
  "category": "Optimized Buy",
  "fields": {
   "timeframe": "2m",
   "ticker": "SQQQ",
   "direction": "long",
   "status": "REVIEW (no outfit)",
   "source": "text"
  },
  "link": "../threads/34_1826614964129554523/thread.md"
 },
 {
  "date": "2024-08-27",
  "type": "case_study",
  "label": "Case Study #28",
  "category": "Precision Buy",
  "fields": {
   "outfit": "MA52",
   "timeframe": "30s",
   "ticker": "TQQQ",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/35_1828458249819140212/thread.md"
 },
 {
  "date": "2024-08-27",
  "type": "case_study",
  "label": "Case Study #3",
  "category": "Automated Short",
  "fields": {
   "outfit": "MA844",
   "timeframe": "3m",
   "ticker": "IXIC",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/36_1828533657545638205/thread.md"
 },
 {
  "date": "2024-08-28",
  "type": "case_study",
  "label": "Case Study #4",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "MA100 / MA250",
   "ticker": "SVIX TQQQ NVDA",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/37_1828864244819095888/thread.md"
 },
 {
  "date": "2024-08-28",
  "type": "case_study",
  "label": "Case Study #29",
  "category": "Precision Buy",
  "fields": {
   "outfit": "ng the SVIX on this drop while this SMA outfit",
   "ticker": "SVIX",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/38_1828868949095883126/thread.md"
 },
 {
  "date": "2024-09-06",
  "type": "case_study",
  "label": "Case Study #5",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "30/60/90/300/600/900",
   "timeframe": "15m",
   "ticker": "DJI",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/39_1832092949821419752/thread.md"
 },
 {
  "date": "2024-09-11",
  "type": "case_study",
  "label": "Case Study #6",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "MA100",
   "timeframe": "20m",
   "ticker": "DJI",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/40_1833869111249830387/thread.md"
 },
 {
  "date": "2024-09-17",
  "type": "case_study",
  "label": "Case Study #30",
  "category": "Precision Buy",
  "fields": {
   "outfit": "erating on the 10M Waring's Problem SMA outfit / MA279",
   "timeframe": "10m",
   "ticker": "SVIX VIX",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/41_1836091941202858086/thread.md"
 },
 {
  "date": "2024-09-20",
  "type": "case_study",
  "label": "Case Study #7",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "he visually concise and streamlined SMA outfit",
   "ticker": "TQQQ",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/42_1837202985765531734/thread.md"
 },
 {
  "date": "2024-10-01",
  "type": "case_study",
  "label": "Case Study #31",
  "category": "Precision Buy",
  "fields": {
   "outfit": "MA512",
   "timeframe": "5m",
   "ticker": "SPXU",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/43_1841185720612110398/thread.md"
 },
 {
  "date": "2024-10-04",
  "type": "case_study",
  "label": "Case Study #32",
  "category": "Precision Buy",
  "fields": {
   "outfit": "MA20 MA40 MA80 MA160 MA320 MA640",
   "timeframe": "5m",
   "ticker": "UVIX",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/44_1842195776489066924/thread.md"
 },
 {
  "date": "2025-01-07",
  "type": "case_study",
  "label": "Case Study #34",
  "category": "Precision Buy",
  "fields": {
   "outfit": "integer 20 outfit / MA320",
   "timeframe": "5m",
   "ticker": "IXIC",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/45_1876730644643877321/thread.md"
 },
 {
  "date": "2025-01-08",
  "type": "case_study",
  "label": "Case Study #33",
  "category": "Precision Buy",
  "fields": {
   "outfit": "onductors and China. This is the XI SMA outfit",
   "ticker": "SOXL",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/46_1877047004276080858/thread.md"
 },
 {
  "date": "2025-01-08",
  "type": "case_study",
  "label": "Case Study #35",
  "category": "Precision Buy",
  "fields": {
   "outfit": "onductors and China. This is the XI SMA outfit",
   "ticker": "SOXL",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/47_1877047004276080858/thread.md"
 },
 {
  "date": "2025-01-10",
  "type": "case_study",
  "label": "Case Study #11",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "MA512",
   "timeframe": "1h",
   "ticker": "QQQ",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/48_1877736761671172278/thread.md"
 },
 {
  "date": "2025-01-13",
  "type": "case_study",
  "label": "Case Study #8",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "SMA outfit / MA512",
   "timeframe": "1h",
   "ticker": "QQQ",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/49_1878828879642779906/thread.md"
 },
 {
  "date": "2025-01-30",
  "type": "case_study",
  "label": "Case Study #9",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "etized buying algorithm on the 30M SVIX outfit / MA26 / MA52 / MA116 / MA211 / MA422 / MA844",
   "timeframe": "30m",
   "ticker": "RWM SVIX",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/50_1884973416471839009/thread.md"
 },
 {
  "date": "2025-01-30",
  "type": "case_study",
  "label": "Case Study #12",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "etized buying algorithm on the 30M SVIX outfit / MA26 / MA52 / MA116 / MA211 / MA422 / MA844",
   "timeframe": "30m",
   "ticker": "RWM SVIX",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/51_1884973416471839009/thread.md"
 },
 {
  "date": "2025-02-06",
  "type": "case_study",
  "label": "Case Study #10",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "etized buying algorithm on the 30M SVIX outfit / MA26 / MA52 / MA116 / MA211 / MA422 / MA844",
   "timeframe": "30m",
   "ticker": "RWM SVIX",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/52_1887521789670269384/thread.md"
 },
 {
  "date": "2025-02-06",
  "type": "case_study",
  "label": "Case Study #13",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "etized buying algorithm on the 30M SVIX outfit / MA26 / MA52 / MA116 / MA211 / MA422 / MA844",
   "timeframe": "30m",
   "ticker": "RWM SVIX",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/53_1887521789670269384/thread.md"
 },
 {
  "date": "2025-03-28",
  "type": "case_study",
  "label": "Case Study #3",
  "category": "Hard Stop",
  "fields": {
   "outfit": "singular penny break of 91.97. 404 SMA outfit",
   "ticker": "XLE",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/54_1905679351645176076/thread.md"
 },
 {
  "date": "2025-05-22",
  "type": "case_study",
  "label": "Case Study #4",
  "category": "Hard Stop",
  "fields": {
   "outfit": "world trade outfit / MA114",
   "ticker": "SQQQ",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/55_1925556780178055173/thread.md"
 },
 {
  "date": "2025-05-22",
  "type": "case_study",
  "label": "Case Study #36",
  "category": "Precision Buy",
  "fields": {
   "outfit": "[MA23 MA46 MA91 MA183 MA365 MA730] / MA365 / MA23 / MA46 / MA91 / MA183 / MA730",
   "timeframe": "3m",
   "ticker": "SQQQ",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/56_1925629925949579475/thread.md"
 },
 {
  "date": "2025-06-02",
  "type": "case_study",
  "label": "Case Study #5",
  "category": "Hard Stop",
  "fields": {
   "outfit": "y orders. So I've picked up XLE. 3M 404 outfit",
   "timeframe": "3m",
   "ticker": "XLE",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/57_1929608902343381373/thread.md"
 },
 {
  "date": "2025-06-05",
  "type": "case_study",
  "label": "Case Study #6",
  "category": "Hard Stop",
  "fields": {
   "outfit": "MA22 MA55 MA77 MA222 MA555 MA777",
   "timeframe": "30m",
   "ticker": "ERX",
   "direction": "long",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/58_1930648319723766134/thread.md"
 },
 {
  "date": "2025-06-10",
  "type": "case_study",
  "label": "Case Study #7",
  "category": "Hard Stop",
  "fields": {
   "outfit": "4H Xi outfit / [MA28 MA56 MA112 MA224 MA448 MA976] / MA28 / MA56 / MA112 / MA224 / MA448 / MA976",
   "timeframe": "4h",
   "ticker": "SCO",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/59_1932466222467285249/thread.md"
 },
 {
  "date": "2025-06-11",
  "type": "case_study",
  "label": "Case Study #8",
  "category": "Hard Stop",
  "fields": {
   "outfit": "MA224",
   "timeframe": "2m",
   "ticker": "SOXL",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/60_1932828618344051095/thread.md"
 },
 {
  "date": "2025-06-11",
  "type": "case_study",
  "label": "Case Study #14",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "ries analysis' to trigger the UK PM SMA outfit / MA180",
   "timeframe": "3m",
   "ticker": "SPX UPRO SPY",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/61_1932836814257336587/thread.md"
 },
 {
  "date": "2025-06-11",
  "type": "case_study",
  "label": "Case Study #9",
  "category": "Hard Stop",
  "fields": {
   "outfit": "rated specifically to move on from Xi's outfit / MA777 / MA22 / MA55 / MA77 / MA222 / MA555",
   "timeframe": "3m",
   "ticker": "TQQQ",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/62_1932863224170607030/thread.md"
 },
 {
  "date": "2025-06-11",
  "type": "case_study",
  "label": "Case Study #37",
  "category": "Precision Buy",
  "fields": {
   "outfit": "MA464.ISMA outfit / MA464 / MA29 / MA58 / MA116 / MA232 / MA928",
   "timeframe": "5m",
   "ticker": "SPY",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/63_1932867631956263205/thread.md"
 },
 {
  "date": "2025-06-12",
  "type": "case_study",
  "label": "Case Study #38",
  "category": "Precision Buy",
  "fields": {
   "outfit": "MA33 / MA66 / MA99 / MA333 / MA666 / MA999",
   "timeframe": "3m",
   "ticker": "VXX",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/64_1933222790502781333/thread.md"
 },
 {
  "date": "2025-06-13",
  "type": "case_study",
  "label": "Case Study #10",
  "category": "Hard Stop",
  "fields": {
   "outfit": "MA50 / 10/50/200",
   "ticker": "SQQQ",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/65_1933520636426793325/thread.md"
 },
 {
  "date": "2025-06-13",
  "type": "case_study",
  "label": "Case Study #11",
  "category": "Hard Stop",
  "fields": {
   "outfit": "MA16 / MA32 / MA64 / MA128 / MA256 / MA512",
   "timeframe": "3m",
   "ticker": "SQQQ",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/66_1933523365807206567/thread.md"
 },
 {
  "date": "2025-06-13",
  "type": "case_study",
  "label": "Case Study #39",
  "category": "Precision Buy",
  "fields": {
   "outfit": "ould have waited for this one. REVERSAL outfit / MA180",
   "ticker": "SQQQ",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/67_1933558926118969700/thread.md"
 },
 {
  "date": "2025-06-13",
  "type": "case_study",
  "label": "Case Study #12",
  "category": "Hard Stop",
  "fields": {
   "outfit": "SVIX EXT ON SVIX at 13.55 . 47 US Admin outfit / MA24 / MA47 / MA94 / MA188 / MA376 / MA752",
   "ticker": "SVIX",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/68_1933598128156123641/thread.md"
 },
 {
  "date": "2025-06-23",
  "type": "case_study",
  "label": "Case Study #40",
  "category": "Precision Buy",
  "fields": {
   "outfit": "[MA24 MA48 MA96 MA192 MA384 MA768] / MA24 / MA48 / MA96 / MA192 / MA384 / MA768",
   "ticker": "SVXY VIX",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/69_1937196577145401345/thread.md"
 },
 {
  "date": "2025-06-24",
  "type": "case_study",
  "label": "Case Study #13",
  "category": "Hard Stop",
  "fields": {
   "outfit": "MA31 MA63 MA125 MA250 MA500 Russia. 365 outfit / MA16 / MA31 / MA63 / MA125 / MA250 / MA500",
   "ticker": "AAPL",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/70_1937512126815641782/thread.md"
 },
 {
  "date": "2025-06-25",
  "type": "case_study",
  "label": "Case Study #14",
  "category": "Hard Stop",
  "fields": {
   "outfit": "[MA23 MA46 MA92 MA184 MA368 MA736] / MA23 / MA46 / MA92 / MA184 / MA368 / MA736",
   "ticker": "TSLT",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/71_1937877644076622067/thread.md"
 },
 {
  "date": "2025-06-26",
  "type": "case_study",
  "label": "Case Study #16",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "MA33 MA66 MA99 MA333 MA666 MA999",
   "timeframe": "30m",
   "ticker": "IYR",
   "direction": "long",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/72_1938241569012015183/thread.md"
 },
 {
  "date": "2025-06-30",
  "type": "case_study",
  "label": "Case Study #15",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "MA19 MA37 MA73 MA143 MA279 MA548",
   "timeframe": "20m",
   "ticker": "NVD",
   "direction": "long",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/73_1939681230595006602/thread.md"
 },
 {
  "date": "2025-07-01",
  "type": "case_study",
  "label": "Case Study #41",
  "category": "Precision Buy",
  "fields": {
   "outfit": "MA25 MA51 MA101 MA202 MA404 MA808",
   "timeframe": "15m",
   "ticker": "NVDX",
   "direction": "long",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/74_1940075634740666865/thread.md"
 },
 {
  "date": "2025-07-03",
  "type": "case_study",
  "label": "Case Study #17",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "MA27 MA53 MA105 MA210 MA420 MA840",
   "timeframe": "1h",
   "ticker": "VXX",
   "direction": "long",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/75_1940774997536264255/thread.md"
 },
 {
  "date": "2025-07-06",
  "type": "case_study",
  "label": "Case Study #4",
  "category": "Automated Short",
  "fields": {
   "outfit": "MA420",
   "timeframe": "2h",
   "ticker": "SVXY VXX",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/76_1942033479023411515/thread.md"
 },
 {
  "date": "2025-07-07",
  "type": "case_study",
  "label": "Case Study #42",
  "category": "Precision Buy",
  "fields": {
   "outfit": "MA27 MA53 MA105 MA210 MA420 MA840",
   "timeframe": "1d",
   "ticker": "GME",
   "status": "OK",
   "source": "image"
  },
  "link": "../threads/77_1942221360190943352/thread.md"
 },
 {
  "date": "2025-07-09",
  "type": "case_study",
  "label": "Case Study #18",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "SMA outfit",
   "ticker": "RWM",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/78_1942946413027242243/thread.md"
 },
 {
  "date": "2025-07-09",
  "type": "case_study",
  "label": "Case Study #43",
  "category": "Precision Buy",
  "fields": {
   "outfit": "MA16 / MA32 / MA64 / MA256 / MA512 / MA128",
   "timeframe": "1d",
   "ticker": "LABD",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/79_1943035665417146734/thread.md"
 },
 {
  "date": "2025-07-11",
  "type": "case_study",
  "label": "Case Study #44",
  "category": "Precision Buy",
  "fields": {
   "outfit": "MA25 MA50 MA100 MA200 MA400 MA800",
   "timeframe": "10m",
   "ticker": "GGLL",
   "direction": "long",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/80_1943674970741068045/thread.md"
 },
 {
  "date": "2025-07-21",
  "type": "case_study",
  "label": "Case Study #19",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "MA27 MA54 MA108 MA216 MA432 MA864",
   "timeframe": "10m",
   "ticker": "VXX",
   "direction": "long",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/81_1947314924121940314/thread.md"
 },
 {
  "date": "2025-07-21",
  "type": "case_study",
  "label": "Case Study #5",
  "category": "Automated Short",
  "fields": {
   "outfit": "high frequency short operating on the outfit / [MA27 MA54 MA108 MA216 MA432 MA864] / MA27 / MA54 / MA108 / MA216 / MA432 / MA864",
   "ticker": "SVIX",
   "direction": "short",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/82_1947315205622645048/thread.md"
 },
 {
  "date": "2025-07-23",
  "type": "case_study",
  "label": "Case Study #20",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "MA30 MA60 MA90 MA300 MA600 MA900",
   "timeframe": "8m",
   "ticker": "SOXS",
   "direction": "long",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/83_1948088844764741770/thread.md"
 },
 {
  "date": "2025-07-23",
  "type": "case_study",
  "label": "Case Study #21",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "MA30 / MA60 / MA90 / MA300 / MA600 / MA900",
   "timeframe": "8m",
   "ticker": "SQQQ SOXS VXX",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/84_1948099281543704984/thread.md"
 },
 {
  "date": "2025-07-24",
  "type": "case_study",
  "label": "Case Study #23",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "MA33 MA66 MA131 MA262 MA626 MA919",
   "timeframe": "10m",
   "ticker": "SPXU SOXS",
   "direction": "long",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/85_1948399995012686153/thread.md"
 },
 {
  "date": "2025-07-25",
  "type": "case_study",
  "label": "Case Study #24",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "MA30 MA60 MA90 MA300 MA600 MA900",
   "timeframe": "8m",
   "ticker": "VXX SOXS",
   "direction": "long",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/86_1948790338631729527/thread.md"
 },
 {
  "date": "2025-07-28",
  "type": "case_study",
  "label": "Case Study #22",
  "category": "Optimized Buy",
  "fields": {
   "outfit": "MA25 MA50 MA100 MA200 MA400 MA600",
   "timeframe": "30m",
   "ticker": "SDOW",
   "direction": "long",
   "status": "OK",
   "source": "text+image"
  },
  "link": "../threads/87_1949835108959285454/thread.md"
 },
 {
  "date": "2025-08-15",
  "type": "case_study",
  "label": "Case Study #15",
  "category": "Hard Stop",
  "fields": {
   "outfit": "MA25",
   "timeframe": "30m",
   "ticker": "RWM",
   "direction": "long",
   "status": "OK",
   "source": "text"
  },
  "link": "../threads/88_1956390689404768587/thread.md"
 }
];
