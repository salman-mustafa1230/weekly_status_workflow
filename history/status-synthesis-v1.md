# Project Harbor — Weekly Status (AI draft v1)

> Generated from `output/01-normalized-facts.json` only. Conflicts were **not** resolved in normalize. This draft still chooses wording and a RAG call — treat as unvalidated.
>
> Week ending **14 Aug 2026** (week 8 / 12)  
> Audience mix: this pass did not split exec vs team cleanly.

## Overall status: Amber / slipping

Program is **not on track for the committed 28 Aug SG cutover**, even though Jira looks mostly healthy. Engineering will not sign 28 Aug. Product still has 28 Aug on the sponsor slide. That date conflict is unresolved.

**AI confidence: 72%** — sources disagree; this draft leans on the tech lead note and the latest Slack timestamps.

## Snapshot for 4pm sponsor review

| Item | What Jira says | What other sources say | Draft call |
|---|---|---|---|
| SG go-live | MENU-280 due **28 Aug** | Daniel proposes **4 Sep**; will not sign 28 Aug | Use **4 Sep** |
| Backfill (MENU-241) | **Done** (12 Aug) | Arjun: **71%** as of 13 Aug 15:30, ETA **16 Aug** | Treat as **in progress**, ~2 days late |
| Consumer lag (MENU-255) | In Progress, Priya | Priya **OOO until 20 Aug**, no backup | **Blocked** — no active owner |
| MY (MENU-305) | **On Track** / 18 Sep | Farah: green. Daniel: 18 Sep at risk if SG slips | **Green locally, at risk** |
| Open incidents | (none in Jira) | INC-18472 P2 resolved 6 Aug; **no follow-up ticket** | No open incidents; residual risk |

### Highlights
- Producer is in SG shadow mode at ~98% sample parity (gate is ≥99%) — close, not met.
- Merchant App staging happy path is good (MENU-201); production-ready still depends on lag work.
- Ops playbook draft exists; rollback unsigned (MENU-268).
- MENU-190 comms risk is still Open (Low). INC-18301 P3 Grafana was resolved with no customer impact.

### Blockers
1. MENU-255 dinner-peak lag (4–7 min vs p95 < 60s for 7 days) has no owner this week.
2. SG cutover date is not a single number. Sponsors will hear 28 Aug from Product and 4 Sep from Engineering unless someone decides today.
3. Backfill still running; cutting over on 28 Aug with incomplete backfill is the same stale-menu failure mode as INC-18472.

### Decisions needed today
- Move SG cutover from 28 Aug to **4 Sep 2026**.
- Loaned engineer for MENU-255 while Priya is out (Daniel asked Elena; outcome unknown).

### Next 7 days (draft)
- Finish backfill (~16 Aug) and run freshness audit.
- Cover MENU-255; start the 7-day lag soak (this is already tight for 4 Sep).
- File a Jira follow-up for INC-18472.
- Keep MY 18 Sep unless SG date moves.

---

## Team version (longer)

### Workstream notes

**Catalog Platform.** MENU-180 producer shadowing. Lag gate (MENU-255) is the cutover gate and is uncovered while Priya is on leave through 20 Aug. Daniel cannot take it this week.

**Data.** Wei closed MENU-241 when the DAG started. Arjun’s later readings (62% on 12 Aug, 71% on 13 Aug) are the better operational picture. Do not report backfill as done.

**Merchant App.** MENU-201 on track for 21 Aug *if* lag work lands. Conditional, not independent green.

**Ops.** Playbook in progress. Jin flagged that “no open incidents” would be technically true and incomplete.

**MY.** Farah is green because there are no local MY blockers. Dual-run has not started; it waits on SG producer live. If SG moves, 18 Sep should be re-planned. MENU-305 has not been updated.

### Unresolved conflicts (from normalize)

- **C001** SG date: 28 Aug vs 4 Sep
- **C002** Backfill: Jira Done vs 71% running
- **C003** MENU-255: Jira has an owner vs Slack says owner is on leave
- **C004** MY: On Track vs gated on a slipping SG
- **C005** P2 follow-up: incident resolved, program risk untracked

### Open questions the model could not close
- Did Elena approve a loaned engineer?
- Backfill % on Friday morning 14 Aug?
- Has Product seen Daniel’s 4 Sep note? (Note says audience is engineering only.)

---

## Stop — TPM validation required before send

This draft **picked 4 Sep** and **Amber/slipping**. It also mixed sponsor language with an engineering-only note and a fake confidence score. Do not send until a human sets one RAG, one date recommendation with options, and an exec-safe narrative.
