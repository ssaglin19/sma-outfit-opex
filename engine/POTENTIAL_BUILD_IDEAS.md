# Potential Build Ideas

## 1. Program Lifecycle Tracking (Proximity Zone Monitor)
**Concept:** Track each alert as a "program" with states: ACTIVE → RESOLVED (accepted/denied/timeout).

- Alert fires → program enters ACTIVE state
- Price stays in SMA proximity zone → still ACTIVE (absorbing, waiting for catalyst)
- Price leaves the SMA proximity zone and doesn't return within N bars:
  - Leaves in signal direction → ACCEPTED
  - Leaves against signal direction → DENIED
- Neither happens within window → TIMEOUT

**Resolution signal:** Price leaving the SMA proximity zone decisively. Not a fixed % move — it's relative to the SMA level the program is operating on.

**Add-on to existing system.** Data already in InfluxDB. Would layer on top of the alerts bucket as a state machine.
