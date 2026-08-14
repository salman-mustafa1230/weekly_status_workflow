# Scenario lock — Status synthesis (Scenario 2)

Status: locked. Do not expand scope without a reason.

## Chosen scenario

XYZ TPM take-home, Scenario 2: Status Synthesis.

Build a lightweight, repeatable workflow that reads scattered mock project updates from local JSON files and produces a stakeholder-ready weekly status report. A human (TPM) validates conflicts before the report is “sent.”

No live integrations. No MCP. No Slack/Jira APIs.

## Why JSON files and not MCP

- Reviewers can open the inputs and check the output against them.
- The run is reproducible on a laptop in minutes.
- Fits a 3–4 hour time box.
- Still counts as programmatic collation: files in → structured snapshot → report.
- MCP would add auth, flaky tools, and extra surface area without making the TPM judgment clearer.

## Program context (fictional, XYZ-plausible)

**Program:** Project Harbor — migrate XYZFood merchant menu sync from a nightly batch pipeline to an event-driven catalog service.

**Scope this cycle:** Singapore first; Malaysia is gated on SG being stable.

**Horizon:** 12-week program. This status is for **week 8** (week ending Friday 14 Aug 2026).

**Original SG go-live:** 28 Aug 2026.  
**Question the report must settle:** are we still on 28 Aug, or is that date already dead?

**Audience of the weekly report:**
- Primary: Eng Director + Product Director (program sponsors)
- Secondary: Catalog Platform, Merchant App, Data, Ops leads

**Workstreams:** Catalog Platform, Merchant App, Data backfill, Ops playbook, MY readiness (blocked on SG).

## Source files (4 JSON files, different shapes)

Keep schemas inconsistent on purpose. The synthesizer has to normalize; you do not pre-clean everything into one perfect model.

| File | Stands in for | Shape |
|---|---|---|
| `data/jira_issues.json` | Tracker | tickets, status, owner, sprint, due date |
| `data/slack_updates.json` | Standups / channel | timestamp, channel, author, free-text |
| `data/tech_lead_update.json` | Weekly eng note | narrative + a couple of dates |
| `data/incidents.json` | On-call | severity, start/end, services, still-open? |
| `data/dependency_notes.json`. Default is four files. |

## Landmines the mock data must contain

These are the critical-thinking hooks. The first AI pass should get at least two of them wrong.

1. **Stale green in Jira:** `MENU-241` is `Done`, but Slack from Data says the backfill is still running and will slip ~2 days.
2. **Conflicting go-live dates:** Tech lead says SG cutover **4 Sep 2026**. Product/Jira target is still **28 Aug 2026**.
3. **Untracked incident:** A P2 “stale menus in SG” incident last week is in `incidents.json` and not reflected as a Jira risk.
4. **False MY green:** MY readiness ticket is `On Track`, but it is gated on SG cutover that is slipping.
5. **Hidden owner gap:** The catalog consumer-lag blocker owner is on leave (only mentioned in Slack). Jira still lists them as assignee.

## What the automation does vs what you do

**Automation (script or repeatable Cursor workflow):**
- Read all JSON files from `data/`
- Emit a structured snapshot: highlights, blockers, risks, decisions needed, evidence, confidence, open questions
- Draft a one-page weekly status + a slightly longer team version

**You (TPM):**
- Resolve date and status conflicts from evidence, not from model confidence
- Set overall RAG (red / amber / green)
- Decide what sponsors need to do this week
- Catch hallucinated tickets, dates, or owners
- Write the recommendation (slip SG to 4 Sep vs. cut scope vs. add help)

## Out of scope

- Live MCP / Slack / Jira
- A dashboard, database, or scheduler
- Multi-week historical trends
- Real XYZ internal names, metrics, or confidential data
- Perfect data model before synthesis

## Success for the submission

1. Stakeholder status report you would actually send.
2. `data/*.json` reviewers can inspect.
3. Process doc: prompts, iterations, what the model got wrong on the landmines.
4. One-page reflection.
