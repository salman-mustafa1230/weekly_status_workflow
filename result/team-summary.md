# Weekly status for the delivery team — Friday 14 Aug 2026

Two programs. Harbor facts below are unchanged. Microservice Optimization is Jira-only.

**From:** TPM

---

# Program 1 — Project Harbor (Amber)

**To:** Catalog Platform, Merchant App, Data, Ops, MY, Product  
**Aligns with:** Harbor sponsor note for **today 4pm**. **To:** Elena Goh (Director of Engineering), Siti Rahman (Director of Product).

This is the working copy. Sponsors are not being asked to read this.

## Read this first

Committed SG go-live is still **28 Aug** (MENU-280, sponsor slides). Daniel will not sign 28 Aug. **4 Sep is not the new date.** It is the earliest he will sign, after Priya is back on **20 Aug** and we have backfill drain plus a week of lag soak.

If **today’s 4pm** does not pick one number, **this** brief contains **both** dates. Product has asked for any engineering date change **in writing today**. Until that decision is logged:

- Do not tell merchants, CS, or MY ops that we have moved to 4 Sep.
- Do not tell them we are still healthy for 28 Aug.
- Say: *date decision is in sponsor review today; working to one number.*

### Sponsor options

| Option | Meaning | What it does to your work |
|---|---|---|
| **A — Move committed SG date to 4 Sep** | TPM recommendation | Replan MENU-280; Farah replans MY 18 Sep (**at risk**, not already moved) |
| **B — Keep 28 Aug** | Gates unmet; Daniel will not sign | Same stale-menu failure mode as INC-18472 if backfill is incomplete |
| **C — No decision at 4pm** | Failure mode | Two dates in **today’s** brief |

---

## Workstream status

| Workstream | Ticket | Jira | Working call | Owner this week | Evidence |
|---|---|---|---|---|---|
| Catalog producer | MENU-180 | In Progress | Shadow ~98% vs ≥99% gate — **not met** | Daniel Koh | Tech lead note, 13 Aug |
| Consumer lag (cutover gate) | MENU-255 | In Progress | **Blocked** — no active owner | Priya Nair (OOO through 20 Aug) | Jira last update **11 Aug**; Marcus Slack **13 Aug 09:05** |
| Merchant App | MENU-201 | In Progress | Conditional — needs lag numbers | Marcus Lim | Staging happy path; prod-ready blocked on 255 |
| SG backfill | MENU-241 | **Done** | **In progress** (not Done) | Wei Ming (ticket) / Arjun (ops) | Arjun: 62% on 12 Aug, **71% on 13 Aug 15:30**, ETA **16 Aug** (weekday conflict below) |
| SG cutover milestone | MENU-280 | In Progress, due **28 Aug** | Date **unresolved** | Daniel Koh (ticket) · Siti Rahman holds the committed date | Slides still 28 Aug; Daniel earliest-sign **Friday 4 Sep** |
| Ops playbook | MENU-268 | In Progress | Draft in; rollback unsigned | Jin Park | Slack 12 Aug; due 25 Aug |
| MY dual-run | MENU-305 | **On Track** / 18 Sep | Locally unblocked, **gated on SG** | Farah Hassan | Farah green 13 Aug; Daniel: 18 Sep **at risk** if SG slips |
| Observability | MENU-312 | To Do | Not a go-live blocker | Marcus Lim | Linked to P3 INC-18301 only |

### Gates (none met)

| Gate | Target | Current | Met? |
|---|---|---|---|
| Producer shadow parity | ≥99% sample match vs batch | ~98% | No |
| Consumer lag, SG dinner peak | p95 < 60s for **7 consecutive days** | 4–7 minutes | No |
| SG backfill | 100% drained + freshness audit | Job running; last % is 71% (13 Aug 15:30) | No |

Sourced calendar: Priya back **20 Aug** → fix lag (duration not in sources) → **7-day soak** → Daniel’s earliest *sign* is **Friday 4 Sep**.

---

## Conflicts to stop arguing past

### 1. MENU-241 is not done
Wei closed it on 12 Aug when the DAG *started*. Arjun: 71% as of 13 Aug 15:30, finish **16 Aug**. Cutting over on 28 Aug with leftover merchants is the same failure mode as last week’s P2.

**Action:** Wei — reopen MENU-241 until 100% + audit. Arjun — post 14 Aug % before 4pm.

### 2. MENU-255 has an assignee, not an owner
Priya is OOO from 12 Aug through 20 Aug. Nothing has moved since 11 Aug on the ticket. Daniel cannot cover it and asked Elena for a loan.

**Action:** Elena / Daniel — name a covering owner today. Marcus — do not call MENU-201 production-ready until lag numbers exist.

### 3. MY is green only because it has not started
No local MY blockers. Dual-run waits on SG producer live. If SG slips, 18 Sep is at risk. MENU-305 has not been changed.

**Action:** Farah — hold MENU-305 until 4pm. Replan 18 Sep only if Option A is logged.

### 4. “No open incidents” is true and incomplete
INC-18472 (P2, 6 Aug, 18:22–21:45 SGT) is resolved; `follow_up_tickets` is empty. Batch is still SG production. INC-18301 (P3 Grafana) is not a go-live risk.

**Action:** Jin — file a Harbor follow-up, link INC-18472. Daniel — rollback sign-off on MENU-268.

### 5. Unsigned product note vs named evidence
`product_notes.txt`: “all tasks are completed perfectly, only its not updated on JIRA. so we can meet the deadline.” No author, no date, no ticket list, no which deadline.

Do not treat this as a Green flip. It conflicts with Daniel (will not sign 28 Aug), Arjun (backfill 71%), and Priya OOO / lag gate unmet.

**Action:** Siti — confirm if this note is yours and which deadline it means. Until then it is one claim, not program status.

---

## Dated items that are in the sources

| When | What the pack says |
|---|---|
| **Today, Fri 14 Aug, 4pm** | Siti: sponsor review; date change in writing today |
| **16 Aug** | Arjun backfill ETA (weekday conflict below) |
| **20 Aug** | Priya back |
| **Friday 4 Sep** | Daniel: earliest date he will *sign* |

---

## Needs human confirmation

| Gap | What the sources say | Ask |
|---|---|---|
| Backfill % on Fri 14 Aug morning | Last reading 71%, 13 Aug 15:30 | Arjun: number before 4pm |
| Arjun’s “Saturday 16 Aug” | Friday 14 Aug ⇒ **16 Aug is Sunday**, **15 Aug is Saturday** | Confirm Sat 15 vs Sun 16 |
| Elena loan yes/no | Asked; no reply in Slack | Covering owner for MENU-255 |
| Has Product seen Daniel’s note? | Audience: engineering only | Siti + Daniel: one two-option slide |
| 4pm attendee list | Elena Goh (Director of Engineering), Siti Rahman (Director of Product) | Confirm if anyone else must be in the room |
| Next check-in after 4pm | None scheduled | Set standup / audit date |
| Merchant / CS holding language | Not named | Name the owner if Option A |
| How long the lag fix takes | Gate is 7-day soak; fix duration unknown | Do not treat 4 Sep as slack |
| `product_notes.txt` | Unsigned, undated: all tasks done, Jira stale, can meet deadline | Who wrote it, when, which tasks, which deadline |

## What I need from you

| Person | Need |
|---|---|
| Daniel Koh | Confirm 4 Sep is still earliest *sign*. One slide with Siti at 4pm. |
| Siti Rahman | Director of Product. Carry A vs B. Confirm whether `product_notes.txt` is yours. Do not brief Jira-healthy / 28 Aug as the status. |
| Wei Ming Tan | Reopen backfill tracking. |
| Arjun Patel | Friday % and a corrected ETA weekday. |
| Marcus Lim | Keep 201 conditional on 255. |
| Priya Nair | (OOO) Covering owner must be named without her. |
| Jin Park | INC-18472 follow-up; rollback unsigned. |
| Farah Hassan | No MY date change until SG committed date changes. |
| Elena Goh | Director of Engineering. Loan yes/no. |

---

# Program 2 — Microservice Optimization (Amber)

Jira project **SVC** only. No Slack, incidents, or eng note in the pack.

| Ticket | Service | Jira | Working call | Owner |
|---|---|---|---|---|
| SVC-1 | Epic (due **30 Sep**) | In Progress | At risk — see SVC-15 | Kenji Watanabe |
| SVC-11 | checkout-tax | Done | Optimized | Linh Tran |
| SVC-12 | promo-engine | Done | Optimized | Linh Tran |
| SVC-13 | session-gateway | In Progress | Updated, not optimized | Omar Haddad |
| SVC-14 | notify-dispatch | In Progress | Updated, not optimized | Omar Haddad |
| SVC-15 | legacy-auth | **Blocked** | Deprecate blocked: Identity cannot leave this service this sprint | Kenji Watanabe |

Count from Jira: **2 optimized, 4 updated, 3 remaining.** Ticket text on SVC-15: this blocks the **30 Sep** epic deadline. No Identity name. No migrate-by date.

**Action:** Kenji — say whether 30 Sep still holds. Do not brief on-time.

## Needs human confirmation (SVC)

| Gap | What Jira says | Ask |
|---|---|---|
| Identity owner | “Identity team” only | Who to escalate to |
| When Identity can leave legacy-auth | No date | Date or “will not move this quarter” |
| Separate sponsor review for SVC? | Harbor has 4pm; SVC has none | Do we brief SVC in the same 4pm or separately |
| Slack / eng note for SVC | None in the pack | Any ops evidence beyond Jira |

## What I need from you (SVC)

| Person | Need |
|---|---|
| Kenji Watanabe | 30 Sep yes/no given SVC-15. |
| Linh Tran / Omar Haddad | Keep SVC-13/14 honest (updated ≠ optimized). |
| Elena Goh | Director of Engineering. Named as SVC-1 reporter. Confirm if this is in today’s Harbor 4pm or a different review. |
