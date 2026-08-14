# Weekly status — Friday 14 Aug 2026

Two programs are in this pack. They do not share a date or a RAG.

**To:** Elena Goh (Director of Engineering), Siti Rahman (Director of Product)  
**From:** TPM  
**Meeting:** Harbor sponsor review, 4pm today. No meeting named for Microservice Optimization.

---

## 1. Project Harbor — Amber

SG cutover is still committed to **28 Aug**. Engineering will not sign that date. This meeting needs one number.

### Decision

| Option | Date | If we choose this |
|---|---|---|
| **A — recommend** | Move committed date to **4 Sep** | Earliest Daniel will sign. Priya is back 20 Aug; lag and backfill still need soak. MY 18 Sep is at risk. |
| **B** | Keep **28 Aug** | Gates will not be met. Engineering will not sign. Incomplete backfill repeats the 6 Aug stale-menu incident. |

No decision means this room briefs **both** dates. **4 Sep is not decided.**

### Situation

- **Producer:** SG shadow at ~98% (gate ≥99%). Not met.
- **Backfill (MENU-241):** Jira is Done. Last ops reading is 71% on 13 Aug, ETA 16 Aug. Treat as in progress.
- **Lag (MENU-255):** No owner this week. Priya is on leave until 20 Aug. Daniel cannot cover it.
- **MY:** No local blockers. Dual-run has not started. 18 Sep is at risk if SG slips.
- **Incidents:** None open. The 6 Aug P2 has no follow-up ticket. Batch is still the SG production path.
- **Product note:** An unsigned file says work is done and we can hit the deadline. That does not match engineering or ops readings. We are not briefing Green.

### Asks

1. Choose **A or B** before we leave. We will update slides, MENU-280, and the MY plan from that date.
2. Elena: covering engineer for MENU-255 until 20 Aug — yes or no.

---

## 2. Microservice Optimization — Amber

Jira only (SVC). No Slack, no tech-lead note.

**Deadline:** 30 Sep 2026 (SVC-1).  
**Progress:** five services in scope; **four updated**; **two optimized** (checkout-tax, promo-engine); **three remaining** (session-gateway, notify-dispatch, legacy-auth).

**Blocker:** SVC-15 `legacy-auth` is Blocked. We plan to deprecate it. Identity still depends on it and cannot move off this sprint. The ticket says this **blocks hitting 30 Sep**. No migrate-by date, and no Identity owner named.

### Ask

Kenji: is 30 Sep still the committed date, or do we replan now given SVC-15?
