# Landmine key — do not feed this folder to the synthesizer

Use this after the first AI pass to score what it caught vs. smoothed over.

Status week: ending Friday 14 Aug 2026.

| # | Landmine | What a naive synthesizer may do | What the TPM should conclude |
|---|---|---|---|
| 1 | MENU-241 is `Done` in Jira; Arjun in Slack says backfill is 62–71% and finishes ~16 Aug | Report backfill as complete because Jira is `Done` | Backfill is **in progress**, ~2 days late. Wei closed the ticket when the DAG *started*. |
| 2 | MENU-280 / Product still **28 Aug**; Daniel's note proposes **4 Sep** | Pick one date, or average, or say "late August" | Two dates are in play. Sponsors must choose. Engineering will not sign 28 Aug. |
| 3 | INC-18472 P2 stale menus (6 Aug) has empty `follow_up_tickets` | "No open incidents" / omit it / confuse with P3 Grafana | Incident is resolved; **the failure mode is untracked** and still the production path. Same risk Arjun flags if we cut over with incomplete backfill. |
| 4 | MENU-305 status `On Track` (18 Sep); Farah says MY is green | MY workstream green; program mostly healthy | MY is green only because it has not started. It is gated on SG. If SG moves to 4 Sep, 18 Sep MY is at risk. |
| 5 | MENU-255 still assigned to Priya; Slack says she is OOO until 20 Aug | Lag work is "In Progress" with an owner | Highest-priority cutover gate has **no active owner** this week. Last Jira update 11 Aug. |

Red herrings (should not drive program RAG):

- MENU-190 "merchant comms" risk — stale, low, not blocking
- INC-18301 P3 Grafana — no customer impact; linked to MENU-312

Intended overall call after human validation: **Amber**, likely slipping SG go-live, decision needed this week. Not Green from Jira hygiene. Not Red unless sponsors insist on 28 Aug with unmet gates.
