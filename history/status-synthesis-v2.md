# Project Harbor — Weekly Status (AI draft v2)

> Iteration on v1. Change: **do not select 4 Sep as the program date.** Frame the two dates Daniel actually described, and the decision that is due this week.
>
> Source: `output/01-normalized-facts.json` (F004, F028, C001 updated)  
> Week ending **14 Aug 2026** (week 8 / 12)

## Overall status: Amber

Committed SG go-live is still **28 Aug** on slides and in MENU-280. Engineering will not sign that date. A second date (**4 Sep**) exists only as Daniel’s earliest *sign-off* floor. Sponsors have not chosen. If we do not decide **this week**, directors get briefed with **two different dates**.

## SG date — two numbers in circulation (not a new baseline)

v1’s mistake: the draft call was “Use **4 Sep**.” That is not what the tech lead note says.

| Date | What it is | Who holds it | Status |
|---|---|---|---|
| **28 Aug 2026** | Committed SG go-live | MENU-280, sponsor slides, Product (Siti) | Still the public date. Daniel **will not sign**. |
| **4 Sep 2026** | Earliest date Daniel *will sign* | Tech lead note (engineering only; not yet with Product) | **Not** a new committed go-live. |

**Why 4 Sep is on the table at all:** Priya is back **20 Aug**. Lag is still 4–7 minutes and the gate is p95 < 60s for **7 consecutive days**, plus backfill drain and a freshness audit. Daniel’s 4 Sep is “a week after Priya is back and after backfill drain for soak.” It is a sign-off floor, not a schedule we have already moved to.

**What has to happen this week:** pick one date (or explicitly accept 28 Aug with unmet gates). Siti has asked for any engineering date change **in writing today** ahead of the 4pm sponsor review. Daniel: *we need a date decision this week or we will brief directors with two different dates.*

### Options for sponsors (do not hide the fork)

| Option | What we tell directors | Consequence |
|---|---|---|
| **A — Move committed date to 4 Sep** | One date. Engineering can sign if lag soak and backfill drain actually land. | MY 18 Sep becomes at risk; MENU-305 should be replanned. |
| **B — Keep 28 Aug** | One date, gates unmet (lag, backfill, no owner on MENU-255). | Engineering will not sign. Same stale-menu failure mode as INC-18472 if backfill is incomplete. |
| **C — No decision this week** | Directors hear **28 Aug from Product and 4 Sep from Engineering**. | This is the outcome v1 accidentally created by “picking” 4 Sep in a status that Product has not accepted. |

TPM recommendation in this draft: **bring Option A vs B to 4pm as a decision, not a status update.** Do not publish 4 Sep as the date until directors choose.

---

## Snapshot for 4pm sponsor review

| Item | What Jira says | What other sources say | Draft call |
|---|---|---|---|
| SG go-live | MENU-280 due **28 Aug** | Daniel: will not sign 28 Aug; earliest sign **4 Sep** after Priya returns + soak | **Unresolved.** Two dates in circulation. Decision due this week. |
| Backfill (MENU-241) | **Done** (12 Aug) | Arjun: **71%** as of 13 Aug 15:30, ETA **16 Aug** | Treat as **in progress**, ~2 days late |
| Consumer lag (MENU-255) | In Progress, Priya | Priya **OOO until 20 Aug**, no backup | **Blocked** — no active owner until she is back, unless a loan is approved |
| MY (MENU-305) | **On Track** / 18 Sep | Farah: green. Daniel: 18 Sep at risk if SG slips | Locally unblocked; **gated on SG date decision** |
| Open incidents | (none in Jira) | INC-18472 P2 resolved 6 Aug; **no follow-up ticket** | No open incidents; residual untracked risk |

### Highlights
- Producer is in SG shadow mode at ~98% sample parity (gate is ≥99%) — close, not met.
- Merchant App staging happy path is good (MENU-201); production-ready still depends on lag work.
- Ops playbook draft exists; rollback unsigned (MENU-268).

### Blockers
1. MENU-255 dinner-peak lag (4–7 min vs p95 < 60s for 7 days) has no owner this week. Priya returns 20 Aug; soak still required after the fix.
2. Date conflict: 28 Aug (committed) vs 4 Sep (earliest engineering sign). Unresolved going into sponsor review.
3. Backfill still running; a 28 Aug cutover with incomplete backfill repeats INC-18472.

### Decisions needed this week (4pm)
1. **One SG date for directors** — Option A (move to 4 Sep) or Option B (keep 28 Aug, unmet gates). Do not leave both in the brief.
2. Loaned engineer for MENU-255 while Priya is out (Daniel asked Elena; outcome unknown). Even with a loan, 28 Aug still has to clear a 7-day lag soak that cannot start until the fix exists.

### Next 7 days (depends on the date decision)
- Finish backfill (~16 Aug) and run freshness audit.
- Cover MENU-255; lag soak cannot honestly start until there is an owner and a fix. Priya is back 20 Aug.
- File a Jira follow-up for INC-18472.
- Replan MY 18 Sep **only if** SG committed date actually moves.

---

## Team version (longer)

### Workstream notes

**Catalog Platform.** MENU-180 producer shadowing. Lag gate (MENU-255) is the cutover gate and is uncovered while Priya is on leave through 20 Aug. Daniel cannot take it this week. 4 Sep only works if work resumes after she is back *and* soak completes — that is why it is a sign-off floor, not this week’s new date.

**Data.** Wei closed MENU-241 when the DAG started. Arjun’s later readings (62% on 12 Aug, 71% on 13 Aug) are the better operational picture. Do not report backfill as done.

**Merchant App.** MENU-201 on track for 21 Aug *if* lag work lands. Conditional, not independent green.

**Ops.** Playbook in progress. Jin flagged that “no open incidents” would be technically true and incomplete.

**MY.** Farah is green because there are no local MY blockers. Dual-run has not started; it waits on SG producer live. If SG committed date moves, 18 Sep should be re-planned. MENU-305 has not been updated.

### Unresolved conflicts (from normalize)

- **C001** SG date: 28 Aug committed vs 4 Sep earliest-sign; decision needed this week or directors hear both
- **C002** Backfill: Jira Done vs 71% running
- **C003** MENU-255: Jira has an owner vs Slack says owner is on leave until 20 Aug
- **C004** MY: On Track vs gated on a slipping SG
- **C005** P2 follow-up: incident resolved, program risk untracked

### Open questions
- Did Elena approve a loaned engineer?
- Backfill % on Friday morning 14 Aug?
- Has Product seen Daniel’s note? (Audience is still engineering only.) If not, 4pm is the first time the two-date problem is made explicit to sponsors.

---

## What changed from v1

| v1 | v2 |
|---|---|
| Draft call: “Use **4 Sep**” | 4 Sep kept as **earliest sign-off**, not the new committed date |
| Decision: “Move to 4 Sep” | Decision: **A vs B this week**, or directors get two dates |
| Soak mentioned as “tight for 4 Sep” | Soak tied to **Priya back 20 Aug**, then 7-day lag gate + backfill drain |
| Fake 72% confidence | Removed |
| MENU-190 in highlights | Removed (stale low risk) |
