# Gap findings - extracted fields

Gap era = posts after **GAP_START 2025-08-20** (the reference repo's last commit, later than the
newest case study 2025-08-15). Selection: has media **or** (ticker **and** action) in the caption.

**Extracted fields only - no raw post text.** No vision, no images.

## Summary

- gap findings: **748**  (2025-08-23 -> 2026-08-20)
- selected via media 661 / via ticker+action 384
- **outfit named in the caption: 144 (19.3%)** - these carry `outfit_source = text`.
  The remaining 604 are blank pending a chart read: the author records the outfit on the chart
  and most captions do not repeat it.

### Field-fill rate

| column | filled | rate |
|---|---|---|
| ticker | 720 | 96.3% |
| price | 478 | 63.9% |
| action | 384 | 51.3% |
| co_executed | 163 | 21.8% |
| outfit | 144 | 19.3% |
| timeframe | 123 | 16.4% |

## Findings

| date | ticker | price | action | co-executed | outfit | src | tf | post id |
|---|---|---|---|---|---|---|---|---|
| 2025-08-23 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1959102701213466710` |
| 2025-08-28 | SQQQ | 17.25 | purchased | NVDA | &nbsp; | &nbsp; | &nbsp; | `1961093841605546367` |
| 2025-08-28 | SQQQ | 17.25 | purchased | &nbsp; | MA33 | text | 30m | `1961094588015501816` |
| 2025-08-28 | SQQQ | 17.25 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1961100804015927602` |
| 2025-08-28 | VIXY | 34.46 | purchased | SQQQ | &nbsp; | &nbsp; | &nbsp; | `1961122723423556092` |
| 2025-08-28 | VIXY | 34.46 | &nbsp; | SQQQ | &nbsp; | &nbsp; | &nbsp; | `1961123434102231133` |
| 2025-08-28 | VIXY | 34.46 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1961128440427577806` |
| 2025-08-28 | VIXY | 34.46 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1961140960311824480` |
| 2025-08-28 | VIX | 34.46 | cut | SQQQ, SVIX | &nbsp; | &nbsp; | &nbsp; | `1961142198042595795` |
| 2025-08-28 | VIXY | 34.46 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1961143275970334729` |
| 2025-08-28 | SQQQ | 17.25 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1961143896135930065` |
| 2025-08-28 | VIXY | 34.46 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1961149277213749669` |
| 2025-08-29 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1961335972421087236` |
| 2025-08-31 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1962096880873300231` |
| 2025-09-01 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1962374304768913599` |
| 2025-09-02 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1962756943417876714` |
| 2025-09-04 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1963417437891883406` |
| 2025-09-10 | GME | 21.54 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1965783974804132350` |
| 2025-09-11 | GLL | 18.59 | purchased | &nbsp; | MA28 / MA57 / MA114 / MA228 / MA456 / MA911 | text | 3m | `1966221733842792931` |
| 2025-09-11 | GLL | 18.59 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1966257028671893780` |
| 2025-09-12 | GLL | 18.59 | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1966493897980604496` |
| 2025-09-12 | GLL | 18.25 | purchased | &nbsp; | MA228 / [GLL 3M 911 MA28 MA57 MA114 MA228 MA456 MA911] / MA28 / MA57 / MA114 / MA456 / MA911 | text | 3m | `1966494439162986583` |
| 2025-09-12 | GLL | 18.25 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1966494563352412470` |
| 2025-09-12 | GLL | 18.25 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1966495292846416168` |
| 2025-09-12 | DXY | &nbsp; | hold | GLL | sadogeenakamoto positive arbitrage outfit | text | &nbsp; | `1966499291066958116` |
| 2025-09-12 | GLL | 18.25 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1966520996913098878` |
| 2025-09-17 | GME | 21.54 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1968333733045600757` |
| 2025-09-17 | VIXY | 32.95 | purchased | SVIX | SVIX outfit / [SVIX outfit SMA 36 52 106 211 422 844] | text | 5m | `1968335880973885719` |
| 2025-09-17 | VIXY | 32.95 | cut | &nbsp; | [5M MA422] / MA422 | text | 5m | `1968336458194018713` |
| 2025-09-17 | VIXY | 32.95 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1968338933525442618` |
| 2025-09-17 | VIXY | 32.95 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1968340071112917334` |
| 2025-09-17 | VIXY | 32.95 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1968353185665515764` |
| 2025-09-17 | VIXY | 32.95 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1968354504946172134` |
| 2025-09-17 | VIXY | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1968355566931386377` |
| 2025-09-17 | VIXY | 32.95 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1968356612239929697` |
| 2025-09-17 | VIXY | 32.95 | cut | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1968374412211798143` |
| 2025-09-17 | SVIX | 21.43 | purchased | &nbsp; | SVIX from 21.43 . 33 SMA outfit | text | &nbsp; | `1968376567614292018` |
| 2025-09-17 | VIXY | 21.43 | purchased | SVIX | SVIX from 21.43 . 33 SMA outfit | text | &nbsp; | `1968377025682722944` |
| 2025-09-17 | VIXY | 21.43 | &nbsp; | SVIX | SVIX from 21.43 . 33 SMA outfit | text | &nbsp; | `1968377297725202717` |
| 2025-09-17 | VIXY | 21.43 | purchased | SVIX | SVIX from 21.43 . 33 SMA outfit | text | &nbsp; | `1968377889424121864` |
| 2025-09-17 | VIXY | &nbsp; | purchased | SVIX | &nbsp; | &nbsp; | &nbsp; | `1968378249467306364` |
| 2025-09-17 | VIXY | 21.43 | &nbsp; | SVIX | SVIX from 21.43 . 33 SMA outfit | text | &nbsp; | `1968378463611666832` |
| 2025-09-17 | SVIX | 21.43 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1968378982644203810` |
| 2025-09-17 | SVIX | 21.43 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1968386354578145696` |
| 2025-09-17 | VIXY | 21.43 | purchased | SVIX | &nbsp; | &nbsp; | &nbsp; | `1968387056138338566` |
| 2025-09-17 | VIXY | 21.43 | purchased | SVIX | &nbsp; | &nbsp; | &nbsp; | `1968392364512411730` |
| 2025-09-17 | RWM | 17.00 | purchased | &nbsp; | 33 outfit / MA66 / [parm:MA66] | text | 3m | `1968397039282032956` |
| 2025-09-17 | RWM | 17.00 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1968397189475979287` |
| 2025-09-17 | RWM | 17.00 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1968397521086013566` |
| 2025-09-18 | RWM | &nbsp; | hold | TZA | &nbsp; | &nbsp; | &nbsp; | `1968668804839305502` |
| 2025-09-18 | RWM | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1968669096221810743` |
| 2025-09-18 | RWM | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1968671343957647411` |
| 2025-09-18 | SPXU | 13.90 | purchased | &nbsp; | MA37 | text | 10m | `1968679380726558756` |
| 2025-09-18 | SPXU | 13.90 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1968679493683261872` |
| 2025-09-18 | SPXU | 13.90 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1968679787288760687` |
| 2025-09-18 | SPXU | 13.90 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1968680320334500281` |
| 2025-09-24 | RWM | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1970933134226288852` |
| 2025-09-24 | RWM | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1970933459737772395` |
| 2025-09-24 | RWM | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | 3m | `1970937200213926337` |
| 2025-09-25 | RWM | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1971209591905276324` |
| 2025-10-07 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1975426730979709069` |
| 2025-10-09 | RWM | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1976300198868681174` |
| 2025-10-09 | RWM | 17.00 | purchased | &nbsp; | 33 outfit / MA66 / [parm:MA66] | text | 3m | `1976312003535962183` |
| 2025-10-09 | RWM | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1976335496482865447` |
| 2025-10-10 | RWM | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1976679370359202016` |
| 2025-10-10 | RWM | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1976739467265446281` |
| 2025-10-12 | TZA | &nbsp; | purchased | RWM, IWM | &nbsp; | &nbsp; | &nbsp; | `1977390794634887188` |
| 2025-11-02 | SPY | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1985106178226204739` |
| 2025-11-05 | RWM | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1985869156756177338` |
| 2025-11-06 | GME | 21.54 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1986545336375255368` |
| 2025-11-06 | RWM | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1986573765061587275` |
| 2025-11-06 | RWM | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1986575647419081060` |
| 2025-11-07 | RWM | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1986821314657784182` |
| 2025-11-07 | RWM | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1986828767394980338` |
| 2025-11-07 | RWM | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1986833380349255925` |
| 2025-11-08 | RWM | 17.00 | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1987031376017903715` |
| 2025-11-11 | RWM | 16.08 | purchased | SPX, DJI, IXIC | SMA outfit | text | &nbsp; | `1988110621871927580` |
| 2025-11-13 | RWM | &nbsp; | hold | &nbsp; | there was extremely high outfit / MA66 / [parm:MA66] | text | 3m | `1989048436164030569` |
| 2025-11-13 | RWM | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1989066823397175405` |
| 2025-11-17 | RWM | &nbsp; | hold | IWM | iding scale based on how relevant a SMA outfit | text | 3m | `1990545998117294568` |
| 2025-11-18 | RWM | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1990608328729465142` |
| 2025-11-30 | RWM | 16.08 | cut | TZA | &nbsp; | &nbsp; | &nbsp; | `1994921992521486813` |
| 2025-12-10 | RWM | 16.08 | purchased | TZA | &nbsp; | &nbsp; | &nbsp; | `1998645681708482653` |
| 2025-12-10 | RWM | &nbsp; | sold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1998841386028904889` |
| 2025-12-10 | CONL | 20.54 | purchased | COIN | MA548 | text | 10m | `1998845074218926303` |
| 2025-12-10 | CONL | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1998850892947403211` |
| 2025-12-11 | CONL | 20.54 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1998950903240602121` |
| 2025-12-11 | CONL | &nbsp; | purchased | DJI, SVIX | &nbsp; | &nbsp; | &nbsp; | `1998954099677737307` |
| 2025-12-12 | ETHU | 56.96 | purchased | &nbsp; | &nbsp; | &nbsp; | 20m | `1999541245790786035` |
| 2025-12-12 | ETHU | 56.96 | &nbsp; | &nbsp; | MA30 / MA41 / MA81 / MA163 / MA325 / MA650 | text | 20m | `1999541530525360477` |
| 2025-12-12 | DUST | 7.58 | purchased | &nbsp; | e's an outfitting program at the 10M 47 outfit | text | 10m | `1999564274314699003` |
| 2025-12-12 | DUST | 7.58 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `1999578160162034145` |
| 2025-12-14 | ETHU | 56.96 | sold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2000112468677607682` |
| 2025-12-15 | DUST | 7.58 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2000574617933824359` |
| 2025-12-15 | DUST | 7.58 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2000576337732399240` |
| 2025-12-15 | DUST | 7.57 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2000576736606769645` |
| 2025-12-15 | ETHU | 56.96 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2000577440968487061` |
| 2025-12-15 | DUST | 7.58 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2000579844002755061` |
| 2025-12-15 | DUST | 7.58 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2000581805703913579` |
| 2025-12-15 | DUST | 7.58 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2000582214602690856` |
| 2025-12-15 | ETHU | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2000586907575517230` |
| 2025-12-15 | ETHU | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2000587082247405925` |
| 2025-12-15 | SOXL | &nbsp; | purchased | SOX | itting program operating on the 15M 180 outfit | text | 15m | `2000594126782554178` |
| 2025-12-15 | SOXL | &nbsp; | &nbsp; | SOX | &nbsp; | &nbsp; | &nbsp; | `2000595608223306144` |
| 2025-12-15 | SOXL | &nbsp; | &nbsp; | SOX | &nbsp; | &nbsp; | &nbsp; | `2000604262834090436` |
| 2025-12-15 | DUST | 7.58 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2000606471818789277` |
| 2025-12-16 | DUST | 7.58 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2000936602995236883` |
| 2025-12-16 | DUST | 7.58 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2000946250288713980` |
| 2025-12-16 | DUST | 7.58 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2000961427646111823` |
| 2025-12-16 | DUST | 7.58 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2000970430501544154` |
| 2025-12-16 | DUST | 7.58 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2000971302715421163` |
| 2025-12-16 | DUST | 7.58 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2001011356326354989` |
| 2025-12-17 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2001317500919885905` |
| 2025-12-17 | DUST | 7.58 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2001319052300394862` |
| 2025-12-17 | DUST | 7.58 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2001341878726463722` |
| 2025-12-17 | SOXL | 36.40 | purchased | &nbsp; | SOXL 36.40 as risk. 2H 46 outfit / MA368 / MA23 / MA46 / MA92 / MA184 / MA736 | text | 2h | `2001344289453064535` |
| 2025-12-17 | SOXL | 36.40 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2001344775073751086` |
| 2025-12-17 | SOXL | 36.40 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2001348476404470199` |
| 2025-12-17 | MUU | 63.36 | purchased | MU | 22 55 77 222 555 777 outfit / MA777 | text | 30m | `2001364549493305502` |
| 2025-12-17 | MUU | 63.36 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2001364704183357580` |
| 2025-12-17 | MUU | 63.63 | hold | &nbsp; | ies analysis based on this specific SMA outfit / [MA777] / MA777 | text | &nbsp; | `2001367009813237923` |
| 2025-12-17 | MUU | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2001392043549937838` |
| 2025-12-17 | MUU | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2001397647928684671` |
| 2025-12-17 | MUU | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2001398174834135400` |
| 2025-12-17 | MUU | 63.63 | hold | &nbsp; | MA777 | text | &nbsp; | `2001401694006198499` |
| 2025-12-17 | SQQQ | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2001406423037809003` |
| 2025-12-18 | MUU | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2001535773708079389` |
| 2025-12-18 | MUU | 82.19 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2001661721585553821` |
| 2025-12-18 | MUU | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2001670788613837309` |
| 2025-12-18 | MUU | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2001671020504363352` |
| 2025-12-19 | MUU | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2002042691748864401` |
| 2025-12-19 | MUU | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2002065874250027113` |
| 2025-12-22 | MUU | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2002955164215640300` |
| 2025-12-24 | MUU | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2003843231256305923` |
| 2025-12-24 | SOXL | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2003848704063836383` |
| 2025-12-24 | XLE | &nbsp; | sold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2003889910907076870` |
| 2025-12-24 | XLE | 91.97 | sold | &nbsp; | XLE 404 outfit | text | &nbsp; | `2003890960661729589` |
| 2025-12-25 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2004260601833705505` |
| 2025-12-25 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2004262814903648716` |
| 2026-01-03 | MUU | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2007254546981245356` |
| 2026-01-16 | MUU | 000.00 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2012246316592566437` |
| 2026-01-21 | MUU | &nbsp; | purchased | MU | &nbsp; | &nbsp; | &nbsp; | `2014046501136375927` |
| 2026-01-21 | FAS | 42.02 | purchased | &nbsp; | &nbsp; | &nbsp; | 2h | `2014076817104314481` |
| 2026-01-21 | FAS | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2014087397768610051` |
| 2026-01-22 | FAS | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | 2h | `2014347621494931806` |
| 2026-01-22 | &nbsp; | 42.02 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2014348083648446575` |
| 2026-01-22 | FAS | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | 2h | `2014386778892075032` |
| 2026-01-22 | TQQQ | &nbsp; | sold | SOXL, SVIX, TSLA | &nbsp; | &nbsp; | &nbsp; | `2014392778864967866` |
| 2026-01-22 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2014398835351814638` |
| 2026-01-23 | &nbsp; | 42.02 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2014709362917568811` |
| 2026-01-23 | FAS | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2014724323106553978` |
| 2026-01-23 | &nbsp; | 42.02 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2014725898348724529` |
| 2026-01-23 | XLF | 53.07 | purchased | FAS | MA548 | text | 2h | `2014727115011457243` |
| 2026-01-23 | XLF | 53.07 | cut | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2014727358436278573` |
| 2026-01-23 | XLF | 53.07 | purchased | JPM | &nbsp; | &nbsp; | &nbsp; | `2014727758581268679` |
| 2026-01-23 | XLF | 53.07 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2014729074640621824` |
| 2026-01-23 | FAS | 53.07 | purchased | XLF | &nbsp; | &nbsp; | &nbsp; | `2014731502500852070` |
| 2026-01-23 | FAS | 53.07 | purchased | XLF | &nbsp; | &nbsp; | &nbsp; | `2014740079252799871` |
| 2026-01-23 | JPM | 53.07 | purchased | XLF | &nbsp; | &nbsp; | &nbsp; | `2014741209957466621` |
| 2026-01-23 | XLF | 53.07 | &nbsp; | &nbsp; | [XLF 2h MA548] / MA548 | text | 2h | `2014744483280388239` |
| 2026-01-23 | XLF | &nbsp; | hold | FAS, JPM | MA548 | text | &nbsp; | `2014745111209640452` |
| 2026-01-23 | XLF | &nbsp; | hold | FAS, JPM | MA548 | text | 2h | `2014745907104002063` |
| 2026-01-23 | XLF | 53.07 | hold | &nbsp; | &nbsp; | &nbsp; | 2h | `2014750388096991319` |
| 2026-01-23 | JPM | 53.07 | hold | XLF | MA548 | text | 2h | `2014750834874290342` |
| 2026-01-23 | FAS | 53.07 | hold | XLF | MA548 | text | 2h | `2014751796057821270` |
| 2026-01-23 | XLF | &nbsp; | hold | FAS, JPM | MA548 | text | 2h | `2014766131014467825` |
| 2026-01-23 | XLF | 53.07 | hold | &nbsp; | MA548 | text | 2h | `2014766792284242065` |
| 2026-01-23 | XLF | 53.07 | hold | &nbsp; | MA548 | text | 2h | `2014776242470588591` |
| 2026-01-23 | MUU | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2014779200763527382` |
| 2026-01-23 | XLF | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | 2h | `2014799273272250598` |
| 2026-01-23 | XLF | 53.07 | hold | &nbsp; | MA548 | text | 2h | `2014803192081744184` |
| 2026-01-23 | FAS | 53.07 | hold | XLF | MA548 | text | 2h | `2014803687743557668` |
| 2026-01-23 | JPM | 53.07 | hold | XLF | MA548 | text | 2h | `2014804086991028730` |
| 2026-01-26 | XLF | 53.07 | hold | &nbsp; | MA548 | text | 2h | `2015795404768735517` |
| 2026-01-26 | JPM | 53.07 | hold | XLF | MA548 | text | 2h | `2015795860957954087` |
| 2026-01-26 | FAS | 53.07 | purchased | XLF | MA548 | text | 2h | `2015796453197881589` |
| 2026-01-26 | XLF | 53.07 | hold | &nbsp; | MA548 | text | 2h | `2015892482920468919` |
| 2026-01-26 | JPM | 53.07 | hold | XLF | MA548 | text | 2h | `2015892767655002587` |
| 2026-01-26 | FAS | 53.07 | purchased | XLF | MA548 | text | 2h | `2015892989990863173` |
| 2026-01-27 | XLF | &nbsp; | hold | &nbsp; | MA548 | text | 2h | `2016197027823288589` |
| 2026-01-27 | XLF | 53.07 | purchased | JPM, FAS | [XLF, magnetized buying algorithm at 2H MA548] / MA548 | text | 2h | `2016215876698288568` |
| 2026-01-27 | XLF | 52.84 | sold | &nbsp; | [XLF, magnetized buying algorithm at 2H MA548] / MA548 | text | 2h | `2016216222975852828` |
| 2026-01-27 | JPM | 52.84 | sold | XLF | [XLF, magnetized buying algorithm at 2H MA548] / MA548 | text | 2h | `2016216519357993027` |
| 2026-01-27 | FAS | 52.84 | sold | XLF | [XLF, magnetized buying algorithm at 2H MA548] / MA548 | text | 2h | `2016216844911444079` |
| 2026-01-27 | XLF | 52.84 | cut | &nbsp; | MA548 | text | 2h | `2016217271837012205` |
| 2026-01-27 | JPM | 52.84 | cut | XLF | MA548 | text | 2h | `2016217526301295011` |
| 2026-01-27 | FAS | 52.84 | cut | XLF | MA548 | text | 2h | `2016217818216493524` |
| 2026-01-28 | XLF | 53.07 | purchased | JPM, FAS | [XLF, magnetized buying algorithm at 2H MA548] / MA548 | text | 2h | `2016518453939814687` |
| 2026-01-28 | XLF | 53.07 | cut | JPM | &nbsp; | &nbsp; | &nbsp; | `2016571190610186454` |
| 2026-01-28 | JPM | 53.07 | cut | XLF | &nbsp; | &nbsp; | &nbsp; | `2016571730383556959` |
| 2026-01-28 | FAS | 53.07 | purchased | XLF, JPM | &nbsp; | &nbsp; | &nbsp; | `2016572242696745391` |
| 2026-02-02 | XLF | 53.07 | cut | JPM | &nbsp; | &nbsp; | &nbsp; | `2018433025726697697` |
| 2026-02-02 | FAS | 53.07 | purchased | XLF, JPM | &nbsp; | &nbsp; | &nbsp; | `2018433495354462394` |
| 2026-02-02 | JPM | 53.07 | purchased | XLF | &nbsp; | &nbsp; | &nbsp; | `2018433919805432136` |
| 2026-02-03 | JPM | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2018705380092616932` |
| 2026-02-04 | JPM | 53.07 | purchased | XLF | &nbsp; | &nbsp; | &nbsp; | `2019106873266635229` |
| 2026-02-04 | AMLD | 12.43 | purchased | AMDL, AMD | &nbsp; | &nbsp; | &nbsp; | `2019110309101994157` |
| 2026-02-04 | AMDL | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2019110497166192890` |
| 2026-02-04 | AMDL | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2019111303168835920` |
| 2026-02-04 | AMDL | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2019119629705310355` |
| 2026-02-04 | AMDL | 12.43 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2019132694148571413` |
| 2026-02-05 | JPM | &nbsp; | purchased | AI | &nbsp; | &nbsp; | &nbsp; | `2019298722124013965` |
| 2026-02-05 | AMDL | 374.24 | cut | SMH | &nbsp; | &nbsp; | &nbsp; | `2019419149328699787` |
| 2026-02-05 | SMH | 374.24 | purchased | SOXL, AMDL | &nbsp; | &nbsp; | &nbsp; | `2019420261473559029` |
| 2026-02-05 | SMH | &nbsp; | purchased | AMDL | &nbsp; | &nbsp; | &nbsp; | `2019421171960410558` |
| 2026-02-05 | SMH | 374.24 | &nbsp; | SOXL | &nbsp; | &nbsp; | &nbsp; | `2019422041615876388` |
| 2026-02-06 | AMD | 374.24 | cut | SMH, AMDL | &nbsp; | &nbsp; | &nbsp; | `2019713430874472807` |
| 2026-02-06 | JPM | 296.51 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2019783075001934139` |
| 2026-02-11 | SMH | &nbsp; | purchased | SOXL | &nbsp; | &nbsp; | &nbsp; | `2021670442252283910` |
| 2026-02-17 | JPM | 296.51 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2023821794273358211` |
| 2026-02-17 | JPM | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2023822790819016995` |
| 2026-02-25 | SMH | 374.24 | &nbsp; | SOXL | &nbsp; | &nbsp; | &nbsp; | `2026701910535975107` |
| 2026-03-02 | SPXU | 48.78 | purchased | &nbsp; | SPXU . 48.78 180 SMA outfit / MA720 | text | &nbsp; | `2028563039373689323` |
| 2026-03-02 | SPXU | 48.78 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2028563190041530870` |
| 2026-03-02 | SPXU | 48.78 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2028563596163285419` |
| 2026-03-02 | SPXU | 48.78 | purchased | &nbsp; | &nbsp; | &nbsp; | 30m | `2028564309421490659` |
| 2026-03-02 | SPXU | 48.78 | purchased | &nbsp; | 180 SMA outfit | text | &nbsp; | `2028566507681349815` |
| 2026-03-03 | SPXU | &nbsp; | purchased | SPX | &nbsp; | &nbsp; | 500s | `2028692249966735543` |
| 2026-03-03 | SPXU | 48.78 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2028841770088550555` |
| 2026-03-03 | SPXU | 48.78 | purchased | &nbsp; | P500 30M 180 outfit | text | 30m | `2028853859645616496` |
| 2026-03-03 | SPXU | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2028854393832100192` |
| 2026-03-03 | SPXU | 48.78 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2028922437388386635` |
| 2026-03-04 | DOG | 23.23 | purchased | &nbsp; | DOG . 366 outfit | text | 9m | `2029219988142469309` |
| 2026-03-04 | DOG | &nbsp; | &nbsp; | SDOW | &nbsp; | &nbsp; | &nbsp; | `2029220227473653777` |
| 2026-03-04 | DOG | 23.23 | purchased | SDOW | urchase at 23.23 operating from the 365 outfit / MA183 / MA23 / MA46 / MA91 / MA365 / MA730 | text | &nbsp; | `2029220663207281084` |
| 2026-03-04 | DOG | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2029221782620914021` |
| 2026-03-04 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2029222104185618825` |
| 2026-03-04 | DOG | 23.23 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2029225895911931997` |
| 2026-03-04 | DOG | 23.23 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2029226069497397343` |
| 2026-03-04 | DOG | 23.23 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2029229921739129138` |
| 2026-03-04 | DOG | 23.23 | hold | &nbsp; | MA183 | text | &nbsp; | `2029238757841616924` |
| 2026-03-04 | DOG | 23.23 | purchased | SDOW | enced at 23.23 with banks using the 366 outfit / MA183 | text | 9m | `2029239441743856012` |
| 2026-03-04 | DOG | &nbsp; | purchased | SDOW | &nbsp; | &nbsp; | &nbsp; | `2029295057241817527` |
| 2026-03-04 | DOG | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2029297846860824966` |
| 2026-03-04 | DOG | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2029297920269533385` |
| 2026-03-04 | DOG | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2029301062306545849` |
| 2026-03-04 | DOG | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2029318023623159870` |
| 2026-03-05 | DOG | 23.23 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2029571289036525615` |
| 2026-03-05 | DOG | &nbsp; | &nbsp; | SDOW | &nbsp; | &nbsp; | &nbsp; | `2029571571934011845` |
| 2026-03-05 | PLTZ | 26.37 | purchased | &nbsp; | PLTZ . Palantir's SMA outfit / MA150 | text | 1h | `2029574742622286142` |
| 2026-03-05 | PLTZ | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2029575006469177444` |
| 2026-03-05 | PLTZ | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2029575806473965635` |
| 2026-03-05 | DOG | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2029579022003577315` |
| 2026-03-05 | DOG | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2029580365023879233` |
| 2026-03-05 | PLTZ | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2029581948201660857` |
| 2026-03-05 | PLTZ | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2029589304692154713` |
| 2026-03-05 | DOG | &nbsp; | purchased | SDOW | &nbsp; | &nbsp; | &nbsp; | `2029612638842536030` |
| 2026-03-05 | PLTZ | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2029616027009700058` |
| 2026-03-05 | SPXU | &nbsp; | purchased | DOG, SDOW, PLTZ | &nbsp; | &nbsp; | &nbsp; | `2029617140995870978` |
| 2026-03-06 | DOG | 23.23 | purchased | SDOW | &nbsp; | &nbsp; | &nbsp; | `2029947955340542102` |
| 2026-03-06 | SPXU | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2029948907279765601` |
| 2026-03-09 | SPXU | &nbsp; | purchased | DOG, SDOW | &nbsp; | &nbsp; | &nbsp; | `2030802917356400762` |
| 2026-03-12 | DOG | 23.22 | hold | SDOW | 366 outfit / MA183 / [366 Outfit Korea’s 9M at PARM:MA183 [coexecuted SDOW] | text | 9m | `2032106086929744074` |
| 2026-03-12 | SPXU | 48.78 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2032112351613460771` |
| 2026-03-13 | SPXU | 48.78 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2032547318797578643` |
| 2026-03-13 | SPXU | 48.78 | purchased | &nbsp; | on the 30m 180 outfit | text | 30m | `2032552315274895660` |
| 2026-03-18 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2034304470096757001` |
| 2026-03-18 | SPXU | 48.78 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2034323806081499483` |
| 2026-03-18 | ORCX | 9.43 | purchased | &nbsp; | Long ORCL ETF. 15M 33 66 99 333 666 999 outfit / MA333 | text | 15m | `2034332362222473419` |
| 2026-03-18 | ORCX | 9.43 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2034333800625504326` |
| 2026-03-19 | ORCX | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2034623555258945624` |
| 2026-03-19 | TQQQ | &nbsp; | purchased | IXIC | TQQQ. IXIC at 21853. MA884 outfit / MA884 / MA28 / MA55 / MA111 / MA221 / MA442 | text | &nbsp; | `2034628973720973528` |
| 2026-03-19 | IXIC | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2034629667727269923` |
| 2026-03-19 | TSLR | 23.98 | purchased | TSLQ, TSLA | 2x Short TSLA Daily ETF. Dual Sequence outfit / MA39 / MA78 / MA156 / MA311 / MA622 / MA944 | text | 2h | `2034633160542327106` |
| 2026-03-19 | TSLQ | 23.98 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2034633867580313825` |
| 2026-03-19 | TSLQ | 23.98 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2034637427680407735` |
| 2026-03-19 | IXIC | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2034639072279613941` |
| 2026-03-19 | TSLQ | 23.98 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2034686793053086058` |
| 2026-03-19 | IXIC | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2034692995594035401` |
| 2026-03-19 | TQQQ | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2034708701723185642` |
| 2026-03-19 | IXIC | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2034721576567152989` |
| 2026-03-20 | TQQQ | &nbsp; | purchased | IXIC | MA884 / MA28 / MA55 / MA111 / MA221 / MA442 | text | 2h | `2035014402731393235` |
| 2026-03-20 | IXIC | &nbsp; | &nbsp; | &nbsp; | MA884 | text | 2h | `2035014685079347210` |
| 2026-03-20 | IXIC | &nbsp; | &nbsp; | &nbsp; | MA884 | text | 2h | `2035017100344140052` |
| 2026-03-20 | IXIC | &nbsp; | purchased | &nbsp; | MA884 | text | &nbsp; | `2035025592819884324` |
| 2026-03-20 | AAPU | 26.73 | purchased | AAPL | MA31 / MA61 / MA122 / MA244 / MA466 / MA668 | text | &nbsp; | `2035045580561686895` |
| 2026-03-20 | IXIC | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2035068419922698641` |
| 2026-03-20 | IXIC | 26.73 | hold | AAPU, AAPL | [AAPU Direxion AAPL Bull 2X Shares. 1D MA31 MA61 MA122 MA244 MA466 MA668 1D MA244 at 26.73.] / MA31 / MA61 / MA122 / MA244 / MA466 / MA668 | text | &nbsp; | `2035069180983353516` |
| 2026-03-20 | IXIC | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2035085169041011019` |
| 2026-03-20 | AAPL | 246.00 | purchased | AAPU | dual sequencing program with the SMA outfit | text | &nbsp; | `2035088719519391782` |
| 2026-03-20 | AAPL | 246.00 | purchased | AAPU | &nbsp; | &nbsp; | &nbsp; | `2035090043472318538` |
| 2026-03-20 | AAPL | 246.00 | cut | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2035090070886371528` |
| 2026-03-20 | AMDL | &nbsp; | &nbsp; | SMH | &nbsp; | &nbsp; | &nbsp; | `2035092231527571485` |
| 2026-03-20 | SPXU | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2035093264630784074` |
| 2026-03-20 | DOG | &nbsp; | sold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2035094418043412753` |
| 2026-03-20 | SPXU | 48.78 | sold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2035126272624640348` |
| 2026-03-20 | AAPL | &nbsp; | purchased | AAPU, IXIC, TQQQ | &nbsp; | &nbsp; | &nbsp; | `2035128247651115300` |
| 2026-03-20 | IXIC | 246.00 | purchased | AAPU, AAPL | &nbsp; | &nbsp; | &nbsp; | `2035132151348490697` |
| 2026-03-20 | USO | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2035136326794969092` |
| 2026-03-23 | TQQQ | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2036116170127052828` |
| 2026-03-24 | AAPL | 246.00 | &nbsp; | AAPU | &nbsp; | &nbsp; | &nbsp; | `2036449671770677421` |
| 2026-03-24 | AAPL | 246.00 | &nbsp; | AAPU | &nbsp; | &nbsp; | &nbsp; | `2036450170691592236` |
| 2026-03-25 | AAPU | 246.00 | &nbsp; | AAPL | &nbsp; | &nbsp; | &nbsp; | `2036798265585537134` |
| 2026-03-25 | AAPL | 246.00 | &nbsp; | AAPU | &nbsp; | &nbsp; | &nbsp; | `2036799020254015661` |
| 2026-03-25 | IXIC | 246.00 | purchased | TQQQ | &nbsp; | &nbsp; | &nbsp; | `2036799949506310485` |
| 2026-03-25 | SMR | 11.71 | purchased | &nbsp; | Octane outfit / MA102 | text | 20m | `2036809380738535705` |
| 2026-03-25 | SMR | 11.71 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2036810694721773812` |
| 2026-03-25 | SMR | 11.71 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2036812310266970543` |
| 2026-03-25 | SMR | 11.71 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2036816367727644858` |
| 2026-03-25 | SMR | 11.71 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2036820589596536979` |
| 2026-03-25 | SMR | 11.52 | purchased | &nbsp; | SMR. 3M 818 Octane outfit / MA102 | text | 3m | `2036825512644059237` |
| 2026-03-25 | SMR | 11.52 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2036825616612508045` |
| 2026-03-25 | SMR | 11.52 | &nbsp; | &nbsp; | MA102 | text | 3m | `2036825785147986183` |
| 2026-03-25 | SMR | 11.52 | purchased | &nbsp; | erating on a real time and threaded SMA outfit / MA102 | text | &nbsp; | `2036826336933933369` |
| 2026-03-25 | SMR | 11.52 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2036826676869619756` |
| 2026-03-25 | SMR | 11.52 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2036827938558185556` |
| 2026-03-25 | SMR | 11.52 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2036828581561815213` |
| 2026-03-25 | SMR | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2036830028890263696` |
| 2026-03-25 | MSTX | 24.37 | purchased | &nbsp; | MA143 | text | 2m | `2036832388723159480` |
| 2026-03-25 | MSTX | 24.37 | &nbsp; | MSTR | MA19 / MA37 / MA73 / MA143 / MA279 / MA548 | text | 2m | `2036833013410201685` |
| 2026-03-25 | MSTX | 24.37 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2036833889919148193` |
| 2026-03-25 | MSTX | 24.37 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2036835338099044701` |
| 2026-03-25 | MSTX | 24.36 | purchased | &nbsp; | MA143 | text | 15m | `2036835954493985224` |
| 2026-03-25 | MSTX | 24.36 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2036836094499750389` |
| 2026-03-25 | MSTX | 24.36 | &nbsp; | &nbsp; | MA143 | text | 15m | `2036836488240054462` |
| 2026-03-25 | MSTX | 24.28 | cut | &nbsp; | Octane outfit / MA409 | text | 1m | `2036839363250929715` |
| 2026-03-25 | MSTX | 24.28 | &nbsp; | MSTR | MA409 | text | 1m | `2036839561733833169` |
| 2026-03-25 | MSTX | 24.28 | &nbsp; | SMR, MSTR | &nbsp; | &nbsp; | 3m | `2036840264434905391` |
| 2026-03-25 | MSTX | 24.28 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2036842014650843488` |
| 2026-03-25 | MSTX | 24.20 | purchased | MSTR | MA26 / MA51 / MA102 / MA205 / MA409 / MA818 | text | 30m | `2036869498402398693` |
| 2026-03-25 | MSTX | 24.20 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2036869847246921820` |
| 2026-03-25 | MSTX | 24.20 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2036870396755272176` |
| 2026-03-25 | MSTX | &nbsp; | hold | &nbsp; | positioning on MSTX here. This 30M 818 outfit | text | 30m | `2036873535873048741` |
| 2026-03-25 | MSTR | &nbsp; | purchased | MSTX | quity higher for profit. For over 5 SMA outfit | text | &nbsp; | `2036874851299021005` |
| 2026-03-25 | MSTX | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2036876017189679561` |
| 2026-03-25 | SCO | 8.26 | purchased | &nbsp; | MA205 | text | &nbsp; | `2036884600547647878` |
| 2026-03-25 | SCO | 8.26 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2036884734266269748` |
| 2026-03-25 | SCO | 8.26 | &nbsp; | &nbsp; | SCO at 8.26. 10M 818 outfit / MA205 | text | 10m | `2036885220667060475` |
| 2026-03-25 | SMR | 11.52 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2036886785721331974` |
| 2026-03-25 | SCO | 8.26 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2036891044110098718` |
| 2026-03-25 | DRN | 8.16 | purchased | &nbsp; | t of trading divisions using the Octane outfit | text | &nbsp; | `2036893690229383415` |
| 2026-03-25 | MSTX | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2036894930678014282` |
| 2026-03-27 | UPRO | 92.10 | purchased | AAPL, AAPU | MA468 | text | &nbsp; | `2037544193728581677` |
| 2026-03-27 | UPRO | 92.10 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2037544305779450017` |
| 2026-03-27 | TSLL | 92.10 | purchased | UPRO | 1st integer of 420 outfit | text | &nbsp; | `2037545902492319989` |
| 2026-03-27 | TSLL | 11.53 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2037553301991178744` |
| 2026-03-27 | TSLL | 11.53 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2037560903865147693` |
| 2026-03-27 | FAS | 92.10 | purchased | UPRO | &nbsp; | &nbsp; | &nbsp; | `2037563694050345236` |
| 2026-03-27 | FAS | 108.92 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2037563827181736152` |
| 2026-03-27 | UPRO | 92.10 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2037567629167366561` |
| 2026-03-27 | DOG | 24.93 | purchased | UDOW, NVDA, AAPL | Octuple and NVDA/AAPL Area Code outfit / MA26 / MA51 / MA102 / MA204 / MA408 / MA816 | text | 4h | `2037574620338094354` |
| 2026-03-27 | UDOW | 24.93 | purchased | DOG | &nbsp; | &nbsp; | &nbsp; | `2037575134006149219` |
| 2026-03-27 | UDOW | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2037577250292564144` |
| 2026-03-27 | DOG | 24.93 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2037581439580111056` |
| 2026-03-27 | DOG | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2037582281611923902` |
| 2026-03-27 | MYY | 17.65 | cut | &nbsp; | MYY at 17.65 . Palantir outfit / MA22 / MA55 / MA77 / MA220 / MA550 / MA770 | text | 2h | `2037599878944346435` |
| 2026-03-27 | UMDD | 17.65 | purchased | MYY | [Short: MYY at 2H MA550 at 17.65] / MA550 | text | 2h | `2037600851070771414` |
| 2026-03-27 | UMDD | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2037601779547001298` |
| 2026-03-27 | UMDD | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2037605602860699813` |
| 2026-03-27 | UMDD | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2037618195495023006` |
| 2026-03-31 | IXIC | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2039076289769050555` |
| 2026-04-01 | UMDD | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2039405396633473274` |
| 2026-04-06 | SSO | 53.34 | cut | &nbsp; | om the flash higher on Putin's 2000 SMA outfit / MA500 | text | 15m | `2041182549331030396` |
| 2026-04-06 | SSO | 53.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041182737688830428` |
| 2026-04-06 | SSO | 53.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041187714662576389` |
| 2026-04-06 | SPXU | 53.34 | purchased | SSO | &nbsp; | &nbsp; | &nbsp; | `2041190149082792243` |
| 2026-04-06 | SPXU | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041190645810008082` |
| 2026-04-06 | SSO | 53.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041193924543615408` |
| 2026-04-06 | SSO | 53.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041197104283209817` |
| 2026-04-06 | SSO | 53.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041200121422209358` |
| 2026-04-06 | SPXU | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041201064603742308` |
| 2026-04-06 | SSO | 53.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041202701267288493` |
| 2026-04-06 | SPXU | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041203193334645104` |
| 2026-04-06 | SSO | 53.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041215716930793629` |
| 2026-04-06 | SSO | 53.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041244638447915121` |
| 2026-04-07 | SSO | 53.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041511299134472655` |
| 2026-04-07 | SPXU | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041511990670327959` |
| 2026-04-07 | SPXU | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041516921842278726` |
| 2026-04-07 | SSO | 53.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041517589474730322` |
| 2026-04-07 | SSO | 53.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041519045535768750` |
| 2026-04-07 | SSO | 53.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041533813671764359` |
| 2026-04-07 | SPXU | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041534277935149424` |
| 2026-04-07 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041581946376221167` |
| 2026-04-07 | SSO | 53.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041593970703396964` |
| 2026-04-07 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041596982767296923` |
| 2026-04-08 | IXIC | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041886482408108236` |
| 2026-04-08 | UMDD | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041886968259473458` |
| 2026-04-08 | ERX | 86.13 | purchased | NVDA, AAPL | Octople and NVDA/AAPL Area outfit / MA26 / MA51 / MA102 / MA204 / MA408 / MA816 | text | 2h | `2041890351473181169` |
| 2026-04-08 | ERX | 86.13 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041890508453376451` |
| 2026-04-08 | ERX | 101.25 | &nbsp; | NVDA, AAPL | Octople and NVDA/AAPL Area outfit / MA26 / MA51 / MA102 / MA204 / MA408 / MA816 | text | 5m | `2041891420806770805` |
| 2026-04-08 | ERX | 86.13 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041893229176791472` |
| 2026-04-08 | ERX | 86.13 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041901884420813058` |
| 2026-04-08 | ERX | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041903753012605291` |
| 2026-04-08 | YANG | 27.33 | purchased | &nbsp; | MA22 / MA55 / MA77 / MA222 / MA555 / MA777 | text | 30m | `2041908256264876131` |
| 2026-04-08 | YANG | 27.33 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041908376289038359` |
| 2026-04-08 | YANG | 27.33 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041909942735794328` |
| 2026-04-08 | ERX | 86.13 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041913198979510275` |
| 2026-04-08 | YANG | 27.33 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041921397149331902` |
| 2026-04-08 | YANG | 27.33 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041924825158185089` |
| 2026-04-08 | YANG | 27.33 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041931593158422980` |
| 2026-04-08 | YANG | 27.33 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041941282831134796` |
| 2026-04-08 | YANG | 27.33 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041944042196627866` |
| 2026-04-08 | ERX | 86.13 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2041962503694119191` |
| 2026-04-09 | ERX | &nbsp; | cut | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2042259852341506330` |
| 2026-04-09 | ERX | 86.13 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2042322287068922346` |
| 2026-04-09 | YANG | 27.33 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2042323619356033251` |
| 2026-04-12 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2043417341107859960` |
| 2026-04-13 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2043486620171874330` |
| 2026-04-13 | TSLZ | 16.21 | purchased | &nbsp; | &nbsp; | &nbsp; | 5m | `2043713380821995634` |
| 2026-04-13 | TSLZ | 16.21 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2043713536531276006` |
| 2026-04-13 | YANG | 27.33 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2043714268361900306` |
| 2026-04-13 | ERX | 86.13 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2043714879576854916` |
| 2026-04-13 | TSLZ | 16.21 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2043722925522715051` |
| 2026-04-13 | TSLZ | 16.21 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2043729528674308566` |
| 2026-04-13 | TSLZ | 16.21 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2043747229283037530` |
| 2026-04-13 | ERX | 86.13 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2043784224206143496` |
| 2026-04-14 | SOXS | 21.88 | purchased | &nbsp; | MA408 | text | 2m | `2044061194953339231` |
| 2026-04-14 | SOXS | 21.88 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044061367033069846` |
| 2026-04-14 | SOXS | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044061537862815886` |
| 2026-04-14 | SOXS | 21.88 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044062827464536189` |
| 2026-04-14 | SOXS | 21.88 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044065457226035556` |
| 2026-04-14 | SOXS | 21.74 | purchased | &nbsp; | MA200 | text | 2m | `2044067730027098223` |
| 2026-04-14 | SOXS | 21.74 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044067911346835740` |
| 2026-04-14 | SOXS | 21.74 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044068200103731431` |
| 2026-04-14 | SOXS | 21.74 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044068517662863860` |
| 2026-04-14 | SOXS | 21.74 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044069570991010092` |
| 2026-04-14 | SOXS | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044070901713645705` |
| 2026-04-14 | SOXS | 21.74 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044072611597176965` |
| 2026-04-14 | SOXS | 21.74 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044074557724864943` |
| 2026-04-14 | PLTZ | 31.58 | purchased | &nbsp; | ort PLTR ETF 39 78 156 311 622 944 tslq outfit / MA311 | text | 10m | `2044076717451686208` |
| 2026-04-14 | BITI | 23.13 | purchased | &nbsp; | BITI . I'll explain this outfit / MA124 | text | 1h | `2044094061313974682` |
| 2026-04-14 | BITI | 23.13 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044096332521185323` |
| 2026-04-14 | BITI | 23.13 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044098221623160887` |
| 2026-04-14 | SPXU | 23.13 | purchased | BITI | &nbsp; | &nbsp; | &nbsp; | `2044100862998687898` |
| 2026-04-14 | SPXU | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044101262216704017` |
| 2026-04-14 | SPXU | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044102803875049821` |
| 2026-04-14 | SPXU | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044103632262705441` |
| 2026-04-14 | SPXU | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044104693656498409` |
| 2026-04-14 | BITI | 23.13 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044107563558645804` |
| 2026-04-14 | SOXS | 23.13 | purchased | BITI | &nbsp; | &nbsp; | &nbsp; | `2044109904315855328` |
| 2026-04-14 | SOXS | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044110130682441829` |
| 2026-04-14 | SOXS | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044110421226074127` |
| 2026-04-14 | PLTZ | 31.58 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044114096912806290` |
| 2026-04-14 | SPXU | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044118318009987434` |
| 2026-04-14 | BITI | 23.13 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044122373885178012` |
| 2026-04-14 | SOXS | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044137485626929594` |
| 2026-04-14 | SPXU | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044137723737628938` |
| 2026-04-14 | PLTZ | 31.58 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044143673882136678` |
| 2026-04-14 | WEBS | 23.13 | purchased | BITI | &nbsp; | &nbsp; | &nbsp; | `2044167246654980233` |
| 2026-04-15 | WEBS | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044409410265772330` |
| 2026-04-15 | SOXS | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044409926077104203` |
| 2026-04-15 | SPXU | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044410282865574281` |
| 2026-04-15 | PLTZ | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044410763671159184` |
| 2026-04-15 | BITI | 23.13 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044411164990603761` |
| 2026-04-15 | SQQQ | 23.13 | purchased | BITI, SOXS | &nbsp; | &nbsp; | &nbsp; | `2044437970187604128` |
| 2026-04-15 | SQQQ | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044438105370038597` |
| 2026-04-15 | SQQQ | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044438358546649120` |
| 2026-04-15 | SQQQ | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044438814496862619` |
| 2026-04-15 | SQQQ | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044441967481012264` |
| 2026-04-15 | SQQQ | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044448050433982763` |
| 2026-04-15 | SOXS | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044457966305423520` |
| 2026-04-15 | SOXS | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044460458841940057` |
| 2026-04-15 | UCO | 41.22 | purchased | &nbsp; | MA200 | text | 2m | `2044480653539086537` |
| 2026-04-15 | UCO | 41.22 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044480763656343600` |
| 2026-04-15 | UCO | 41.22 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044480990127788480` |
| 2026-04-15 | UCO | 41.22 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044481722457501753` |
| 2026-04-15 | UCO | 41.22 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044483170394116195` |
| 2026-04-15 | UCO | 41.22 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044486587350946009` |
| 2026-04-15 | UCO | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044488549777740246` |
| 2026-04-15 | UCO | 41.22 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044489417444970591` |
| 2026-04-15 | UCO | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044492145181265956` |
| 2026-04-15 | UCO | 41.13 | purchased | &nbsp; | &nbsp; | &nbsp; | 15m | `2044498674588520570` |
| 2026-04-15 | UCO | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044498806562296259` |
| 2026-04-15 | UCO | 41.13 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044501341897429413` |
| 2026-04-16 | UCO | 41.13 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044778132197240926` |
| 2026-04-16 | BITI | 23.13 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2044779205796483485` |
| 2026-04-17 | SPXU | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2045135120412410325` |
| 2026-04-17 | SQQQ | &nbsp; | hold | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2045135546729795871` |
| 2026-04-23 | TZA | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2047334923288350826` |
| 2026-04-23 | UVIX | 19.34 | purchased | SVIX | &nbsp; | &nbsp; | &nbsp; | `2047337579713102119` |
| 2026-04-23 | UVIX | 19.34 | purchased | SVIX | MA400 | text | 1h | `2047338099148272088` |
| 2026-04-23 | UVIX | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2047339611509383611` |
| 2026-04-23 | SVIX | 19.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2047340114599415960` |
| 2026-04-23 | SVIX | 19.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2047341528524464336` |
| 2026-04-23 | UVIX | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2047342237764456736` |
| 2026-04-23 | UVIX | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2047346271657292082` |
| 2026-04-23 | SVIX | 19.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2047346699899937066` |
| 2026-04-23 | TZA | 48.60 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2047347325174178061` |
| 2026-04-23 | TZA | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2047360708552298536` |
| 2026-04-23 | UVIX | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2047361295377408335` |
| 2026-04-23 | SVIX | 19.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2047362280925638964` |
| 2026-04-23 | TZA | 48.60 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2047364160363913237` |
| 2026-04-23 | SVIX | 19.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2047364883457753471` |
| 2026-04-23 | UVIX | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2047370395700035796` |
| 2026-04-27 | SVIX | 19.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2048759686166650884` |
| 2026-04-27 | UVIX | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2048759990052425794` |
| 2026-04-27 | TZA | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2048760591612022934` |
| 2026-04-27 | SVIX | &nbsp; | purchased | UVIX | &nbsp; | &nbsp; | &nbsp; | `2048761392313082367` |
| 2026-04-27 | SQQQ | &nbsp; | purchased | TQQQ | &nbsp; | &nbsp; | &nbsp; | `2048761590858797430` |
| 2026-04-27 | TZA | 4.86 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2048802020547854448` |
| 2026-04-27 | SVIX | 19.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2048802477307461947` |
| 2026-04-28 | TZA | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049185638243819560` |
| 2026-04-29 | UVIX | 19.34 | purchased | SVIX | &nbsp; | &nbsp; | &nbsp; | `2049407656746688572` |
| 2026-04-29 | UVIX | 19.34 | purchased | SVIX | &nbsp; | &nbsp; | &nbsp; | `2049408348957872166` |
| 2026-04-29 | SVIX | &nbsp; | purchased | UVIX | &nbsp; | &nbsp; | &nbsp; | `2049409417960124765` |
| 2026-04-29 | SVIX | 19.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049481686367539329` |
| 2026-04-29 | SVIX | 19.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049488902365560906` |
| 2026-04-29 | SVIX | 19.34 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049490960149844434` |
| 2026-04-29 | UVIX | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049491286902841428` |
| 2026-04-29 | UVIX | 19.37 | purchased | SVIX | high frequency short operating on the outfit / [MA27 MA54 MA108 MA216 MA432 MA864] / MA27 / MA54 / MA108 / MA216 / MA432 / MA864 | text | &nbsp; | `2049493755653394851` |
| 2026-04-29 | UVIX | 19.37 | purchased | SVIX | &nbsp; | &nbsp; | &nbsp; | `2049493891930640612` |
| 2026-04-29 | UVIX | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049493993059418350` |
| 2026-04-29 | SVIX | 19.37 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049495012216553933` |
| 2026-04-29 | SVIX | 19.37 | hold | UVIX | &nbsp; | &nbsp; | &nbsp; | `2049496767943811497` |
| 2026-04-29 | SVIX | 19.37 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049497790343245923` |
| 2026-04-29 | TZA | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049499148236505220` |
| 2026-04-29 | SVIX | 19.37 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049501205303546328` |
| 2026-04-29 | SVIX | 19.37 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049533862813090116` |
| 2026-04-29 | UVIX | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049534265667579930` |
| 2026-04-29 | TZA | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049535061176053946` |
| 2026-04-29 | SVIX | 19.37 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049560832883974559` |
| 2026-04-30 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049682723871330574` |
| 2026-04-30 | SVIX | 19.37 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049855286719209917` |
| 2026-04-30 | SVIX | 19.37 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049866837454889087` |
| 2026-04-30 | SQQQ | 19.37 | purchased | SVIX | &nbsp; | &nbsp; | &nbsp; | `2049867365484269888` |
| 2026-04-30 | SQQQ | 52.22 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049867462574035413` |
| 2026-04-30 | SQQQ | 52.22 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049868078151053823` |
| 2026-04-30 | SQQQ | 52.22 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049874140447080515` |
| 2026-04-30 | SQQQ | 52.22 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049874637350400266` |
| 2026-04-30 | SVIX | 19.37 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049892458197299244` |
| 2026-04-30 | SVIX | 19.37 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049899610920104399` |
| 2026-04-30 | UVIX | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049899706915147885` |
| 2026-04-30 | SQQQ | 52.22 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049900295984218497` |
| 2026-04-30 | TZA | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049900874210935232` |
| 2026-04-30 | SQQQ | 52.22 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049904459652931833` |
| 2026-04-30 | NVDX | 17.67 | purchased | &nbsp; | NVDX at 17.67 as risk. Japan's 225 outfit / MA25 / MA45 / MA75 / MA225 / MA450 / MA900 | text | 30m | `2049910913269104712` |
| 2026-04-30 | NVDX | 17.67 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049911089065009434` |
| 2026-04-30 | NVDX | 17.67 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049911930358526357` |
| 2026-04-30 | MSFL | 17.28 | purchased | &nbsp; | MSFL . 22² or 484 outfit / MA22 / MA44 / MA121 / MA242 / MA484 / MA968 | text | 32m | `2049923377843077577` |
| 2026-04-30 | MSFT | 17.28 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049923939099697388` |
| 2026-04-30 | NVDX | 17.67 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2049928834833907757` |
| 2026-05-01 | NVDX | 17.67 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2050262228008591772` |
| 2026-05-01 | MSFL | 17.28 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2050263357828284693` |
| 2026-05-01 | RIVN | 15.14 | purchased | SVIX | RIVN . RIVN at 15.14 . SVIX outfit / MA26 / MA52 / MA106 / MA211 / MA422 / MA855 | text | 2h | `2050265445337542917` |
| 2026-05-01 | RIVN | 15.14 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2050265713584357758` |
| 2026-05-04 | MSFL | 17.28 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2051317989748941058` |
| 2026-05-05 | RIVN | 14.24 | purchased | RIVNL | MA636 | text | &nbsp; | `2051700364823699643` |
| 2026-05-06 | RIVN | 14.24 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2052071128231985269` |
| 2026-05-07 | SABS | &nbsp; | purchased | &nbsp; | MA18 / MA36 / MA65 / MA180 / MA360 / MA650 | text | 2h | `2052397766639542674` |
| 2026-05-07 | SABS | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2052399306796302826` |
| 2026-05-07 | PTIR | 14.55 | purchased | PLTZ, SVIX | MA211 | text | 15m | `2052411905772589379` |
| 2026-05-07 | MSFL | 17.28 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2052413955893755999` |
| 2026-05-07 | PTIR | 14.55 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2052419482786972078` |
| 2026-05-07 | SABS | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2052450054200533149` |
| 2026-05-07 | SABS | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2052453681073897621` |
| 2026-05-07 | PTIR | 14.55 | &nbsp; | PLTZ | &nbsp; | &nbsp; | &nbsp; | `2052478383708414032` |
| 2026-05-08 | PTIR | 14.55 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2052777336790278542` |
| 2026-05-08 | SABS | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2052800592247140355` |
| 2026-05-11 | PTIR | 14.55 | &nbsp; | PLTZ | &nbsp; | &nbsp; | &nbsp; | `2053831420863463899` |
| 2026-05-12 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | this specific outfit | text | &nbsp; | `2054080966688378897` |
| 2026-05-12 | PTIR | 14.55 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054247722329469242` |
| 2026-05-12 | MSTU | &nbsp; | purchased | &nbsp; | MA102 | text | 32m | `2054255235603066934` |
| 2026-05-12 | MSTU | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054259744505012552` |
| 2026-05-12 | PTIR | 14.55 | &nbsp; | PLTZ | &nbsp; | &nbsp; | &nbsp; | `2054266531169837333` |
| 2026-05-12 | MSTR | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054271103212937495` |
| 2026-05-13 | PTIR | 14.55 | &nbsp; | PLTZ | &nbsp; | &nbsp; | &nbsp; | `2054564212165509203` |
| 2026-05-13 | SABS | &nbsp; | purchased | &nbsp; | MA650 | text | 2h | `2054565385584955742` |
| 2026-05-13 | RIVN | 13.87 | purchased | &nbsp; | MA16 | text | 20m | `2054566763577380868` |
| 2026-05-13 | RIVN | 13.87 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054567076384354373` |
| 2026-05-13 | RIVN | 13.87 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054571133790548278` |
| 2026-05-13 | PTIR | 14.55 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054571953143644484` |
| 2026-05-13 | QPUX | 24.76 | purchased | &nbsp; | MA125 | text | 55m | `2054579626232660262` |
| 2026-05-13 | QPUX | 24.76 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054581866481737762` |
| 2026-05-13 | RIVN | 13.87 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054589108606144538` |
| 2026-05-13 | SABS | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054589613029945538` |
| 2026-05-14 | QPUX | 24.76 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054946680202793429` |
| 2026-05-14 | RIVN | 13.87 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054947040095092923` |
| 2026-05-14 | MSFL | 17.28 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054948017476911474` |
| 2026-05-14 | MSFL | 17.28 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054953480708866505` |
| 2026-05-14 | MSFD | 13.11 | purchased | &nbsp; | MSFD on this drop. 32M 22² or 484 outfit / MA22 / MA44 / MA121 / MA242 / MA484 / MA968 | text | 32m | `2054954221699768495` |
| 2026-05-14 | MSFD | 13.11 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054960729418334580` |
| 2026-05-14 | QID | 13.11 | purchased | MSFD, QQQ | 32M 22² or 484 outfit / [MSFD , 32M 22² or 484 outfit MA22 MA44 MA121 MA242 MA484 MA968 32M MA121 at 13.11] / MA22 / MA44 / MA121 / MA242 / MA484 / MA968 | text | 32m | `2054961258001301738` |
| 2026-05-14 | MSFD | 13.11 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054961414071353739` |
| 2026-05-14 | QID | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054961779751747633` |
| 2026-05-14 | QID | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054963642802864481` |
| 2026-05-14 | QID | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054972709818479051` |
| 2026-05-14 | QPUX | 24.76 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054973399068467365` |
| 2026-05-14 | RIVN | 13.87 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054973822244405526` |
| 2026-05-14 | QID | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054974331298697352` |
| 2026-05-14 | MSFD | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054977814852714598` |
| 2026-05-14 | SPXS | 13.11 | purchased | MSFD | 32M 22² or 484 outfit / [MSFD , 32M 22² or 484 outfit MA22 MA44 MA121 MA242 MA484 MA968 32M MA121 at 13.11] / MA22 / MA44 / MA121 / MA242 / MA484 / MA968 | text | 32m | `2054983944987431307` |
| 2026-05-14 | SPXS | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054984197274755119` |
| 2026-05-14 | SPXS | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054985545143689536` |
| 2026-05-14 | MSFD | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2054988977107833321` |
| 2026-05-14 | MSFL | 17.28 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2055003032203780283` |
| 2026-05-14 | MSFD | 13.11 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2055003620442333447` |
| 2026-05-15 | QID | &nbsp; | hold | SPXS, MSFD | &nbsp; | &nbsp; | &nbsp; | `2055325569202757840` |
| 2026-05-15 | MSFL | 17.28 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2055352923216076863` |
| 2026-05-15 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2055364301763072361` |
| 2026-05-15 | QID | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2055415952423166270` |
| 2026-05-15 | SPXS | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2055416523343470738` |
| 2026-05-20 | QID | &nbsp; | purchased | SPXS | &nbsp; | &nbsp; | &nbsp; | `2056890353052254679` |
| 2026-05-20 | SPXS | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2057093114683417065` |
| 2026-05-20 | QID | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2057093486709768412` |
| 2026-05-20 | NVDX | 20.90 | &nbsp; | &nbsp; | MA420 | text | 10m | `2057101476858925126` |
| 2026-05-20 | NVDX | 20.90 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2057104681047048229` |
| 2026-05-26 | UCO | 45.41 | purchased | &nbsp; | MA600 | text | 20m | `2059285006204518754` |
| 2026-05-26 | UCO | 45.41 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2059285080787578889` |
| 2026-05-26 | UCO | 45.41 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2059294863896858915` |
| 2026-05-26 | UCO | 45.41 | purchased | &nbsp; | s 30 60 90 outfit | text | &nbsp; | `2059298644403376541` |
| 2026-05-26 | UCO | 45.41 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2059348956640161875` |
| 2026-05-26 | UCO | 45.41 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2059364012886999417` |
| 2026-05-26 | UCO | &nbsp; | purchased | &nbsp; | MA600 / [parm:MA600] | text | 20m | `2059366606342664332` |
| 2026-05-27 | UCO | &nbsp; | purchased | USO | UCO into this drop. There's a positive outfit / MA600 | text | 20m | `2059630977887170669` |
| 2026-05-27 | UCO | &nbsp; | hold | USO | &nbsp; | &nbsp; | &nbsp; | `2059631287934349373` |
| 2026-05-27 | UCO | &nbsp; | purchased | USO | positive microterm USO sma outfit / MA600 | text | 20m | `2059631532688789973` |
| 2026-05-27 | USO | &nbsp; | hold | UCO | [MA27 MA54 MA108 MA216 MA432 MA864.] / MA27 / MA54 / MA108 / MA216 / MA432 / MA864 | text | 1m | `2059647311098323075` |
| 2026-05-27 | USO | 129.78 | purchased | UCO | &nbsp; | &nbsp; | &nbsp; | `2059661871482106321` |
| 2026-05-27 | USO | 129.78 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2059662020153336090` |
| 2026-05-27 | USO | 129.78 | &nbsp; | SVIX | MA108 | text | 1m | `2059662853137895543` |
| 2026-05-27 | USO | 129.78 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2059664651676500054` |
| 2026-05-27 | USO | 129.78 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2059673280379072661` |
| 2026-05-27 | USO | 129.78 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2059703832867917826` |
| 2026-05-27 | USO | 129.64 | purchased | &nbsp; | MA512 | text | 44m | `2059706833292664879` |
| 2026-05-27 | USO | 129.64 | &nbsp; | &nbsp; | n't know why this specific timeframe or outfit / MA512 | text | 44m | `2059707409128640772` |
| 2026-05-27 | USO | 129.64 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2059712830329512007` |
| 2026-05-28 | USO | 129.64 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2059990777498066978` |
| 2026-05-28 | USO | 127.77 | purchased | &nbsp; | USO as my final Oil trade. 22² or 484 outfit / MA22 / MA44 / MA121 / MA242 / MA484 / MA986 | text | 2h | `2060006218920493116` |
| 2026-05-28 | USO | 127.77 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2060006568440332687` |
| 2026-05-28 | SQQQ | 127.77 | purchased | USO | &nbsp; | &nbsp; | &nbsp; | `2060008193103995078` |
| 2026-05-28 | SPXU | 127.77 | purchased | USO | &nbsp; | &nbsp; | &nbsp; | `2060008676421960059` |
| 2026-05-29 | SOXS | 5.48 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2060164674398888092` |
| 2026-05-29 | SCO | 28.38 | purchased | UCO | MA770 | text | 20m | `2060434673621422141` |
| 2026-05-29 | UCO | 28.38 | purchased | SCO | [SCO 20M 22 55 77 220 550 770 20M MA770 at 28.38] / MA770 | text | 20m | `2060435028275052566` |
| 2026-05-29 | UCO | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2060435149138055678` |
| 2026-06-01 | UCO | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2061275088352371041` |
| 2026-06-01 | UCO | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2061443534503485603` |
| 2026-06-01 | SCO | 28.38 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2061443547639984183` |
| 2026-06-02 | SCO | 28.38 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2061837124975075546` |
| 2026-06-02 | UCO | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2061892473073610867` |
| 2026-06-03 | UCO | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2062193255362806007` |
| 2026-06-03 | SCO | 28.38 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2062194158421553252` |
| 2026-06-03 | SCO | 28.38 | cut | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2062194973664268646` |
| 2026-06-04 | UCO | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2062591467361841455` |
| 2026-06-04 | SCO | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2062591954626757003` |
| 2026-06-08 | UCO | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2064036790475079836` |
| 2026-06-08 | SCO | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2064037355800150459` |
| 2026-06-09 | SCO | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2064378917478359410` |
| 2026-06-09 | UCO | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2064379658377080874` |
| 2026-06-09 | UCO | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2064387754113511775` |
| 2026-06-09 | SCO | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2064388276744790385` |
| 2026-06-10 | SVIX | 20.01 | purchased | VIX | MA777 | text | 20m | `2064727684597629315` |
| 2026-06-10 | SVIX | 20.01 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2064728388926136544` |
| 2026-06-10 | SVIX | 20.01 | cut | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2064729168420725118` |
| 2026-06-10 | SVIX | 20.01 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2064737081763742029` |
| 2026-06-10 | SVIX | 19.95 | purchased | VIX | MA500 | text | 33m | `2064738410745745768` |
| 2026-06-10 | SVIX | 19.95 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2064738489909002728` |
| 2026-06-10 | UPRO | 19.95 | purchased | SVIX | &nbsp; | &nbsp; | &nbsp; | `2064738778405908544` |
| 2026-06-10 | UPRO | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2064738868138856633` |
| 2026-06-10 | TQQQ | 19.95 | purchased | SVIX | &nbsp; | &nbsp; | &nbsp; | `2064739182237696155` |
| 2026-06-10 | TQQQ | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2064739349636518200` |
| 2026-06-10 | SVIX | 19.95 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2064742487630270722` |
| 2026-06-10 | UCO | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2064743494137356597` |
| 2026-06-10 | SCO | 28.38 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2064744005540470988` |
| 2026-06-10 | SVIX | 19.95 | purchased | &nbsp; | 31 63 125 250 500 simple moving average outfit / MA500 | text | 33m | `2064745462033523008` |
| 2026-06-10 | SVIX | 19.95 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2064790307875811770` |
| 2026-06-11 | SVIX | 19.95 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2065064353108525549` |
| 2026-06-11 | SVIX | 19.95 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2065086193583407463` |
| 2026-06-11 | SPXU | 41.31 | purchased | UPRO | 31 . 33M 22 55 77 220 550 770 palantir outfit | text | 33m | `2065090270937649267` |
| 2026-06-11 | SPXU | 41.31 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2065090409001574777` |
| 2026-06-11 | UPRO | 41.31 | purchased | SPXU | &nbsp; | &nbsp; | &nbsp; | `2065090770961670196` |
| 2026-06-11 | UPRO | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2065090880420389096` |
| 2026-06-11 | SPXU | 41.31 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2065091446173257854` |
| 2026-06-11 | SPXU | 41.31 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2065125327052079422` |
| 2026-06-11 | UPRO | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2065158583952753116` |
| 2026-06-11 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2065165376305156119` |
| 2026-06-15 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2066325364247548339` |
| 2026-06-15 | UCO | 28.38 | purchased | SCO | [SCO 20M 22 55 77 220 550 770 20M MA770 at 28.38] / MA770 | text | 20m | `2066518386386084350` |
| 2026-06-15 | UPRO | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2066519016743875046` |
| 2026-06-15 | SPXU | 41.31 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2066519353869365390` |
| 2026-06-22 | SPXU | 41.31 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2069056205562200341` |
| 2026-06-22 | UPRO | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2069056889523241067` |
| 2026-06-22 | GUSH | 29.48 | purchased | &nbsp; | P Oil 2x 29.48 . 404 outfit / MA404 | text | &nbsp; | `2069068669100179889` |
| 2026-06-22 | GUSH | 29.48 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2069068790604927380` |
| 2026-06-22 | GUSH | 29.47 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2069069052925112656` |
| 2026-06-22 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2069103966240289100` |
| 2026-06-22 | GUSH | 29.48 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2069149534224331075` |
| 2026-06-23 | GUSH | 29.48 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2069511580426092781` |
| 2026-06-24 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2069671768911118527` |
| 2026-06-24 | GUSH | 29.41 | purchased | SVIX | SH now. 4H SVIX's 26 52 106 211 422 844 outfit / MA422 | text | 4h | `2069792843288440859` |
| 2026-06-24 | GUSH | 29.23 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2069793870662320131` |
| 2026-06-24 | GUSH | 29.23 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2069846278172012977` |
| 2026-06-25 | GUSH | 29.23 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2070139435862335983` |
| 2026-06-25 | GUSH | 29.23 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2070210599154577468` |
| 2026-06-25 | GUSH | 29.23 | purchased | SVIX | SVIX's 26 52 106 211 422 844 outfit | text | &nbsp; | `2070220600157880464` |
| 2026-06-25 | GUSH | 29.23 | purchased | SVIX | SVIX's 26 52 106 211 422 844 outfit | text | &nbsp; | `2079844121003610554` |
| 2026-06-29 | GUSH | 29.23 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2071595712501219676` |
| 2026-07-06 | GUSH | 29.23 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2074187308384092241` |
| 2026-07-07 | GUSH | 29.23 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2074573625034985642` |
| 2026-07-07 | GUSH | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2074574241199223033` |
| 2026-07-07 | GUSH | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2086878153931432241` |
| 2026-07-08 | GUSH | 29.23 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2074795288552939796` |
| 2026-07-09 | UPRO | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2075311433970319751` |
| 2026-07-09 | SPXU | 41.31 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2075312179893669970` |
| 2026-07-09 | GUSH | 29.23 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2075312700020994307` |
| 2026-07-12 | GUSH | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2076098582747426830` |
| 2026-07-12 | GUSH | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2086878089691459934` |
| 2026-07-13 | GUSH | 29.23 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2076734736911958123` |
| 2026-07-17 | GUSH | 29.23 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2078208525927690693` |
| 2026-07-19 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2078652675764392205` |
| 2026-07-27 | SPYU | 30.65 | purchased | &nbsp; | MA332 | text | 2h | `2081759657807560759` |
| 2026-07-27 | SPYU | 30.65 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2081760100474393028` |
| 2026-07-27 | SPYU | 30.65 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2081761432996298985` |
| 2026-07-27 | SPYU | 30.65 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2081766261672014024` |
| 2026-07-27 | SPYU | 30.65 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2081779210297962506` |
| 2026-07-27 | SPYU | 30.65 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2081791790815084669` |
| 2026-07-27 | SPYU | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2081795896556257581` |
| 2026-07-27 | SPYU | 30.65 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2081832451006169391` |
| 2026-07-28 | SPYU | 30.65 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2082097424806650287` |
| 2026-07-28 | SPYU | 30.65 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2082202132124676196` |
| 2026-07-29 | GUSH | 30.00 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2082362989362212948` |
| 2026-07-29 | GUSH | 29.41 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2082368156946104473` |
| 2026-08-04 | HIBS | 17.92 | purchased | &nbsp; | MA19 | text | 1h | `2084657627922051475` |
| 2026-08-04 | HIBS | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2084657778594087163` |
| 2026-08-04 | HIBS | 17.92 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2084661311393485260` |
| 2026-08-04 | SPXU | 17.92 | purchased | HIBS | &nbsp; | &nbsp; | &nbsp; | `2084665626107461650` |
| 2026-08-04 | SQQQ | 17.92 | purchased | HIBS, QQQ | &nbsp; | &nbsp; | &nbsp; | `2084669086169240014` |
| 2026-08-04 | SQQQ | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2084669211755073611` |
| 2026-08-04 | SQQQ | 17.92 | purchased | HIBS | &nbsp; | &nbsp; | &nbsp; | `2084672206534222118` |
| 2026-08-05 | SPXU | 120.00 | purchased | SQQQ, HIBS, HIBL | MA83 | text | 2h | `2085010457488998898` |
| 2026-08-05 | HIBL | 120.00 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2085010631313506765` |
| 2026-08-05 | SPXU | 120.00 | purchased | HIBL | &nbsp; | &nbsp; | &nbsp; | `2085011001859297344` |
| 2026-08-05 | SQQQ | 120.00 | purchased | HIBL | &nbsp; | &nbsp; | &nbsp; | `2085011230285320458` |
| 2026-08-05 | HIBS | 120.00 | purchased | HIBL | &nbsp; | &nbsp; | &nbsp; | `2085011484850217088` |
| 2026-08-05 | HIBS | 120.00 | purchased | HIBL | &nbsp; | &nbsp; | &nbsp; | `2085011740279132423` |
| 2026-08-05 | SQQQ | 120.00 | purchased | HIBL | &nbsp; | &nbsp; | &nbsp; | `2085011948064903200` |
| 2026-08-05 | SPXU | 120.00 | purchased | HIBL | &nbsp; | &nbsp; | &nbsp; | `2085012106437706058` |
| 2026-08-05 | HIBL | 120.00 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2085018775053812136` |
| 2026-08-05 | HIBL | 120.00 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2085093584395808779` |
| 2026-08-05 | HIBS | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2085093956480807220` |
| 2026-08-05 | SQQQ | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2085094263214518506` |
| 2026-08-05 | SPXU | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2085094510930079894` |
| 2026-08-06 | SPXU | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2085397233999163556` |
| 2026-08-06 | SQQQ | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2085397678528360861` |
| 2026-08-06 | HIBS | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2085397965183865111` |
| 2026-08-06 | HIBL | 120.00 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2085398379534962883` |
| 2026-08-10 | GUSH | 29.23 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2086863222720913501` |
| 2026-08-10 | GUSH | 29.23 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2086863939489710550` |
| 2026-08-13 | SPXU | 120.00 | purchased | SQQQ, HIBS | &nbsp; | &nbsp; | &nbsp; | `2087935089120542889` |
| 2026-08-17 | HIBL | 120.00 | purchased | SQQQ, SPXU, HIBS | &nbsp; | &nbsp; | &nbsp; | `2089389098238923018` |
| 2026-08-17 | HIBL | 120.00 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2089403996373217460` |
| 2026-08-17 | SPXU | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2089442386120511901` |
| 2026-08-17 | SQQQ | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2089442919099076884` |
| 2026-08-17 | HIBS | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2089443325321642267` |
| 2026-08-17 | GUSH | 29.23 | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2089444337025466604` |
| 2026-08-18 | SPXU | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2089804677814886771` |
| 2026-08-20 | SPXU | &nbsp; | purchased | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2090527891960549445` |
| 2026-08-20 | HIBL | 120.00 | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | `2090543213904052618` |
