# TPM Weekly Status Update — Scenario 2: Status synthesis

This repo is the submission: stakeholder notes plus AI process documentation.

## For the reviewer

| Brief asks for | Where it is |
|---|---|
| **Completed task** (something you’d share with stakeholders) | [`result/executive-summary.md`](result/executive-summary.md) · [`result/team-summary.md`](result/team-summary.md) |
| **Tools & setup** | [below](#tools--setup) |
| **Your approach** (process, prompts, workflow, iterations) | [below](#your-approach) |
| **Critical assessment** (what AI got wrong; what I added) | [below](#critical-assessment) |
| **1-page reflection** | [below](#brief-reflection) |

**Scenario:** Status synthesis. Mock program updates in `data/` → normalize → exec + team weekly status. Two programs in the current pack: **Project Harbor** (XYZFood menu-sync cutover) and **Microservice Optimization** (Jira only).

**How to regenerate:** open this repo in **Claude Code** and run `/weekly-status`.  
Command: [`.claude/commands/weekly-status.md`](.claude/commands/weekly-status.md) · Recipe: [`prompts/status-synthesis.md`](prompts/status-synthesis.md)

```text
data/*  →  scripts/load_sources.py  →  extracted/raw-bundle.json
        →  recipe (normalize, keep conflicts open)
        →  extracted/normalized-facts.json
        →  result/executive-summary.md
        →  result/team-summary.md
        →  human TPM validates, then sends
```

`result/` contains only the two sendable notes. Facts and the raw bundle live in `extracted/`. First-pass drafts are in `history/` (not the pipeline).

---

## Tools & setup

| Tool | Role | Why this one |
|---|---|---|
| **Cursor** | Authoring this weekly status update (data, recipe, validator, the critique loop) | Fast file edits next to the model. Not the weekly run path. |
| **Claude Code** | The command a teammate or reviewer uses | `/weekly-status` is one slash command. The recipe is a file, not a chat transcript. |
| **Python** (`scripts/load_sources.py`, `scripts/validate.py`) | Deterministic load + wiring checks | JSON/text in → bundle out, no model. Validator catches invented names and exec/team contract drift. |

**Why both Cursor and Claude Code:** I built and challenged the work in Cursor. I did not want the *recipe* trapped in that session, so the steps live in `prompts/status-synthesis.md`. I then put a **single** run instruction in this README — Claude Code `/weekly-status` — so the submission is not “operate two IDEs every Friday.” Portability of the recipe; one supported generator.

**What I did not use:** ChatGPT, Gemini, Zapier/n8n, live Jira/Slack, MCP. Mock files in `data/` so a reviewer can open the inputs next to the report.

---

## Your approach

### Process

1. **Lock a scenario I could fact-check.** Harbor week 8, 14 Aug 2026. Planted conflicts (stale Jira Done, two go-live dates, owner on leave, untracked P2, MY “on track” gated on SG).
2. **Split extract from decide.** A script concatenates `data/`. The model normalizes to claims with `source` + `as_of`. Conflicts stay `resolution: null`. I set RAG and the sponsor ask.
3. **Two altitudes, same story.** Exec note is sendable (decision + asks). Team note has tickets, evidence, and gaps that need a human. Sponsors do not see the kitchen.
4. **Iterate on real misses**, then freeze a recipe so `/weekly-status` is repeatable. I later dropped in an unsigned product note and a second Jira project to see whether the flow blended RAGs or invented Green.

### Workflow and configuration

- **Slash command** (Claude Code):

```markdown
Follow `prompts/status-synthesis.md` exactly. Start by reading that file.
Argument (audience): $ARGUMENTS   # exec | team | both
```

- **Recipe rules that matter:** source-only (no invented names/dates); unsigned “we’re done” notes are claims, not a Green flip; multiple projects get separate sections and separate RAGs; human-confirmation table on the **team** copy only.
- **After prompt or script edits:** `python3 scripts/load_sources.py` then `python3 scripts/validate.py`.

### Prompts I actually used (shape)

Not one mega-prompt. Three layers:

1. **Load** — `python3 scripts/load_sources.py` (no model).
2. **Normalize** — extract claims; do not pick a winner on dates or Done vs still-running.
3. **Synthesize** — draft exec + team from the fact file; 4 Sep is earliest *sign-off*, not a new committed date.

The standing prompt is [`prompts/status-synthesis.md`](prompts/status-synthesis.md). Early chat prompts were the same idea in weaker form (that is how v1 picked 4 Sep).

### Iterations

| Pass | Artifact | What I changed after seeing it |
|---|---|---|
| v1 | [`history/status-synthesis-v1.md`](history/status-synthesis-v1.md) | Model **chose 4 Sep**. I made it a decision fork, not a new baseline. |
| v2 | [`history/status-synthesis-v2.md`](history/status-synthesis-v2.md) | Two dates in play; still mixed process notes into the draft. |
| Sendable | [`result/`](result/) | Exec = A vs B today. Team = evidence + gaps. No scoring table on the exec note. |
| Recipe not Harbor-specific | [`prompts/status-synthesis.md`](prompts/status-synthesis.md) | Conflict *types*, not MENU-280. |
| Folders | `extracted/` vs `result/` | Reviewer opens `result/` and sees only two notes. |
| `product_notes.txt` | unsigned “all tasks completed” | Status stayed **Amber**; note is one claim. |
| Second program | [`data/jira_service_optimization.json`](data/jira_service_optimization.json) | Own section, own 30 Sep risk; does not inherit Harbor’s dates. |

---

## Critical assessment

### What AI got wrong or missed

| AI said | Why it was wrong | What I did |
|---|---|---|
| Use **4 Sep** as the date | Daniel’s earliest *sign*, after Priya is back 20 Aug + soak. Product still holds **28 Aug**. No decision ⇒ directors hear **two dates this week** | Exec is A vs B **today**. 4 Sep is not decided. |
| Tom Yap, “week 8 of 12”, next week’s director brief | Not in `data/` | Source-only rule. Gaps on the team copy. |
| 16 Aug as Saturday in the team plan | Status week is **Friday 14 Aug** ⇒ 16 Aug is Sunday | Flag Sat 15 vs Sun 16; do not invent a weekend plan. |
| Human-confirmation table on the **exec** note | Directors will not read scoring notes | Table is team-only. |
| JSON-only loader | `product_notes.txt` would have been invisible | Loader takes every file in `data/`. |
| Restyle the team note on `/weekly-status` with no new defect | Command rewrote both files | I called it out; later runs should change a summary only when the pack or a real defect requires it. |
| Unsigned “we can meet the deadline” | Would have gone Green / kept 28 Aug | Claim vs named ops evidence. RAG stays Amber. |

### What I added that AI could not

- The **judgment**: Amber, recommend moving Harbor to 4 Sep, do not brief Green, do not merge SVC into Harbor’s RAG.
- **Who hears what, and in what order:** directors pick one SG date at 4pm *first*. Until that is logged, nobody tells merchants or customer support “we slipped to 4 Sep” or “we are still fine for 28 Aug.” AI will happily draft all three audiences at once; a TPM does not.
- **What to withhold:** 4 Sep is not a committed date until directors choose; the engineering-only note is not a slide.
- **Titles vs ticket owners:** Siti Rahman is Director of Product (reporter, not assignee). Elena Goh is Director of Engineering. MENU-280 is assigned to Daniel; MENU-190 to Jin.

### Where AI was not helpful — what I did instead

Picking the date, inventing an audience, and writing process commentary into a sponsor doc. I corrected against `data/`, then encoded the correction in the recipe and `validate.py` so the next run could not quietly undo it.

---

## How to swap data or check wiring

1. Replace files in `data/` (JSON, text, mixed schemas). Do not edit the prompt to name the new feature.
2. In Claude Code, `/weekly-status`.
3. `python3 scripts/validate.py` after prompt or flow changes.

---

## Brief reflection

**Where was AI most helpful in this task?**  
Collating mixed schemas (Jira, Slack, a tech-lead note, incidents, later a `.txt` and a second Jira project) into a sourced claim list. I would not want to do that by hand every Friday. It was also useful for two altitudes from one fact table: a page for directors and a working copy for the team.

**Where was it least helpful or even counterproductive?**  
It decides too fast. v1 treated 4 Sep as the new go-live. It invented people and a program length. It put a scoring table on the exec note. It restyled the team summary when I only re-ran the command. An unsigned “all tasks completed” note is the failure mode I care about as a TPM: confident Green on a source that has no author and no timestamp. I had to treat that as a claim, not a status.

**What would I do differently next time?**  
Lock the fact table and a “do not invent” check *before* any stakeholder prose. Put `validate.py` in on day one, not after Tom Yap. Do not let `/weekly-status` overwrite sendable notes unless `data/` changed. Write the exec ask myself from the facts, then use AI to tighten — not the other way around. Date decisions are the expensive part; generating bullets is not.

**How might I apply this AI process to other TPM work?**  
Same loop: extract → keep conflicts unresolved → human sets RAG and the ask → send. Incident comms (resolved vs still untracked). Weekly RAID from Jira + Slack. Launch reviews where Product says on track and engineering will not sign. I would not use it to pick a date, name an owner who is not in the pack, or write customer copy. I would use it so Friday’s packet is evidence-linked, and so the room owes **one** decision instead of two dates and a stale Done chip.

The value is not faster writing. It is a repeatable way not to brief two dates, a stale Done ticket, and an unsigned “we’re fine” note as if they were one story.
