/* ---------------------------------------------------------------------------
 * TICKER DIRECTION MAP  --  THIS FILE IS THE EDITABLE SOURCE OF TRUTH.
 *
 * Correct classifications HERE. index.html reads this and nothing else to decide
 * a day cell's directional tint; it hardcodes no ticker of its own. Edit a value,
 * reload the page, the tint changes. Adding a new symbol needs no code change.
 *
 * VALUES  (exactly these three strings)
 *   "bearish"  inverse / short ETFs, and LONG-volatility products
 *   "bullish"  the underlying itself, leveraged-LONG ETFs, and SHORT-volatility
 *   "unknown"  not confident -- NOT a guess. Cells tint only on known symbols,
 *              so an "unknown" is inert rather than wrong.
 *
 * Many entries below were confirmed from chart headers actually read during the
 * archive's vision pass (e.g. NVD = "GraniteShares 2x Short NVDA Daily ETF",
 * SVIX = "-1x Short VIX Futures ETF", PTIR = "GraniteShares 2x Long PLTR Daily
 * ETF"), not from memory alone.
 *
 * The unknowns are grouped at the bottom, deliberately, so they are easy to find
 * and rule on. Anything ambiguous went there rather than into a guess: a wrong
 * tint is worse than no tint.
 * --------------------------------------------------------------------------- */

window.TICKER_DIRECTION = {

  /* ---- BEARISH: inverse / short ETFs ------------------------------------ */
  "SQQQ":  "bearish",   /* ProShares UltraPro Short QQQ */
  "QID":   "bearish",   /* ProShares UltraShort QQQ */
  "SPXU":  "bearish",   /* ProShares UltraPro Short S&P500 */
  "SPXS":  "bearish",   /* Direxion Daily S&P 500 Bear 3X */
  "SDOW":  "bearish",   /* ProShares UltraPro Short Dow30 */
  "DOG":   "bearish",   /* ProShares Short Dow30 */
  "RWM":   "bearish",   /* ProShares Short Russell2000 */
  "TZA":   "bearish",   /* Direxion Daily Small Cap Bear 3X */
  "MYY":   "bearish",   /* ProShares Short MidCap400 */
  "SOXS":  "bearish",   /* Direxion Daily Semiconductor Bear 3X */
  "HIBS":  "bearish",   /* Direxion Daily S&P High Beta Bear 3X */
  "LABD":  "bearish",   /* Direxion Daily S&P Biotech Bear 3X */
  "WEBS":  "bearish",   /* Direxion Daily Dow Jones Internet Bear 3X */
  "YANG":  "bearish",   /* Direxion Daily FTSE China Bear 3X */
  "DUST":  "bearish",   /* Direxion Daily Gold Miners Bear 2X */
  "GLL":   "bearish",   /* ProShares UltraShort Gold */
  "SCO":   "bearish",   /* ProShares UltraShort Bloomberg Crude Oil */
  "BITI":  "bearish",   /* ProShares Short Bitcoin */
  "NVD":   "bearish",   /* GraniteShares 2x Short NVDA */
  "MSFD":  "bearish",   /* Direxion Daily MSFT Bear 1X */
  "TSLQ":  "bearish",   /* Tradr 2X Short TSLA */
  "TSLZ":  "bearish",   /* 2x short TSLA */

  /* ---- BEARISH: long-volatility ---------------------------------------- */
  "UVIX":  "bearish",   /* 2x Long VIX Futures */
  "VIXY":  "bearish",   /* ProShares VIX Short-Term Futures */
  "UVXY":  "bearish",   /* ProShares Ultra VIX Short-Term Futures */
  "VXX":   "bearish",   /* iPath B S&P 500 VIX Short-Term Futures */

  /* ---- BULLISH: indices and underlyings --------------------------------- */
  "SPX":   "bullish",
  "SPY":   "bullish",
  "IXIC":  "bullish",
  "QQQ":   "bullish",
  "DJI":   "bullish",
  "IWM":   "bullish",
  "SOX":   "bullish",
  "SMH":   "bullish",   /* VanEck Semiconductor ETF */
  "XLF":   "bullish",   /* Financial Select Sector SPDR */
  "XLE":   "bullish",   /* Energy Select Sector SPDR */
  "IYR":   "bullish",   /* iShares US Real Estate */
  "USO":   "bullish",   /* United States Oil Fund */
  "AAPL":  "bullish",
  "MSFT":  "bullish",
  "NVDA":  "bullish",
  "AMD":   "bullish",
  "MU":    "bullish",
  "JPM":   "bullish",
  "TSLA":  "bullish",
  "COIN":  "bullish",
  "MSTR":  "bullish",
  "GME":   "bullish",
  "RIVN":  "bullish",
  "SMR":   "bullish",   /* NuScale Power */
  "AI":    "bullish",   /* C3.ai */

  /* ---- BULLISH: leveraged long ----------------------------------------- */
  "TQQQ":  "bullish",   /* ProShares UltraPro QQQ */
  "UPRO":  "bullish",   /* ProShares UltraPro S&P500 */
  "SSO":   "bullish",   /* ProShares Ultra S&P500 */
  "SPYU":  "bullish",   /* 4x long S&P 500 */
  "UDOW":  "bullish",   /* ProShares UltraPro Dow30 */
  "UMDD":  "bullish",   /* ProShares UltraPro MidCap400 */
  "SOXL":  "bullish",   /* Direxion Daily Semiconductor Bull 3X */
  "HIBL":  "bullish",   /* Direxion Daily S&P High Beta Bull 3X */
  "FAS":   "bullish",   /* Direxion Daily Financial Bull 3X */
  "DRN":   "bullish",   /* Direxion Daily Real Estate Bull 3X */
  "ERX":   "bullish",   /* Direxion Daily Energy Bull 2X */
  "GUSH":  "bullish",   /* Direxion Daily Oil & Gas E&P Bull 2X */
  "UCO":   "bullish",   /* ProShares Ultra Bloomberg Crude Oil */
  "AAPU":  "bullish",   /* Direxion Daily AAPL Bull 2X */
  "MSFL":  "bullish",   /* GraniteShares 2x Long MSFT */
  "NVDX":  "bullish",   /* T-REX 2X Long NVIDIA */
  "AMDL":  "bullish",   /* GraniteShares 2x Long AMD */
  "CONL":  "bullish",   /* GraniteShares 2x Long COIN */
  "MSTX":  "bullish",   /* Defiance Daily Target 2X Long MSTR */
  "MSTU":  "bullish",   /* 2x long MSTR */
  "PTIR":  "bullish",   /* GraniteShares 2x Long PLTR */
  "GGLL":  "bullish",   /* Direxion Daily GOOGL Bull 2X */
  "TSLL":  "bullish",   /* Direxion Daily TSLA Bull 2X */
  "TSLT":  "bullish",   /* T-REX 2X Long TSLA */
  "TSLR":  "bullish",   /* 2x long TSLA */
  "RIVNL": "bullish",   /* 2x long RIVN */
  "ETHU":  "bullish",   /* 2x long Ether */

  /* ---- BULLISH: short-volatility --------------------------------------- */
  "SVIX":  "bullish",   /* -1x Short VIX Futures */
  "SVXY":  "bullish",   /* ProShares Short VIX Short-Term Futures */

  /* ---- UNKNOWN: rule on these ------------------------------------------
     Left unclassified on purpose. Each is either a symbol I could not identify
     with confidence, or one whose direction is not an equity long/short call at
     all. Set a value above and the tint follows immediately.                */
  "MUU":   "unknown",   /* seen 19x. Possibly a 2x long MU product -- not confirmed */
  "PLTZ":  "unknown",   /* seen 16x. "Z" suffix suggests short PLTR -- not confirmed */
  "SABS":  "unknown",   /* seen 7x. Unidentified */
  "QPUX":  "unknown",   /* seen 4x. Unidentified */
  "ORCX":  "unknown",   /* seen 3x. Oracle-linked, direction unclear */
  "AMLD":  "unknown",   /* seen 1x. Possibly a mis-typed AMDL -- not assumed */
  "VIX":   "unknown",   /* the index itself, not a position: no inherent direction */
  "DXY":   "unknown"    /* US Dollar Index: not an equity long/short */
};
