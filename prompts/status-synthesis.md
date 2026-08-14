# Weekly status synthesis — agent recipe

Works for any program. Inputs are whatever files sit in `data/` (JSON, text, mixed schemas). Do not assume Harbor, a region, a ticket prefix, or a particular go-live date.

Do not read `notes/`. That folder is a human scoring key.

Optional argument: `exec` | `team` | `both` (default `both`).

## Step 1 — Load sources

Run:

```bash
python3 scripts/load_sources.py
```

Done when `extracted/raw-bundle.json` exists and `files_loaded` matches every file in `data/` (not only `*.json`). If the folder is empty, stop and say so.

## Step 2 — Discover context

From the bundle only, infer:

- Program / feature name
- Status week (or `as_of` if no week is stated)
- Workstreams
- Named audiences (sponsors vs delivery team). If none are named, exec = leadership, team = delivery leads in the sources.

If more than one program/project appears in the pack, section both summaries by program. Do not fold them into a single RAG or a single date decision. A program that only has tracker tickets is still a program — write what Jira supports and put missing Slack/eng notes in the team **Needs human confirmation** table.

Done when you can state those four in one short recap. If a field is missing, write `unknown`.

## Source-only rule

Every name, title, date, weekday, metric, and meeting in the summaries must appear in `data/` (or be simple calendar arithmetic from a sourced weekday, e.g. Friday 14 Aug → 16 Aug is Sunday).

If a fact is missing or two sources disagree on a weekday/date:

- Put it in a **Needs human confirmation** table in `result/team-summary.md` only.
- State what the pack *does* say, then the ask.
- Leave the gap empty. Do not fill it with a plausible person, title, horizon (e.g. “week 8 of 12”), checkpoint, or comms owner.

`result/executive-summary.md` is sendable. No scoring tables, no “not in the pack,” no “see gap below.” Unknowns become a single ask (e.g. yes/no in the room) or stay on the team copy.

## Step 3 — Normalize

Write `extracted/normalized-facts.json`.

Each claim: `id`, `theme`, `claim`, `value`, `workstream`, `source` (`file` + `ref`), `as_of`, `actor`.

Schemas will differ across files. Map whatever shape you find (tickets, chat, notes, incidents, docs) into that claim list. Keep conflicting claims as separate rows. Put them in `conflicts[]` with `resolution: null`. Do not pick a winner. Do not invent tickets, dates, owners, or metrics.

Scan for these conflict *types* (only create a conflict when the sources actually disagree):

| Type | What disagreement looks like |
|---|---|
| Milestone date | Committed / slide / tracker date vs engineering earliest-sign, forecast, or “will not sign” |
| Tracker vs operations | Ticket Done / On Track vs later operational evidence that work is still running |
| Nominal vs actual owner | Assignee on the ticket vs out-of-office, leave, or “no backup” in chat |
| Downstream gated on upstream | A later workstream marked green/on track while it is blocked on an unmet predecessor |
| Closed incident, open risk | Incident resolved with no follow-up work in the tracker |
| Stale / noise | Old low-priority items or internal-only blips that should not drive RAG |

Done when every source file is represented in `claims[]`, and `conflicts[]` covers every real disagreement of the types above.

## Step 4 — Synthesize stakeholder drafts

Write only the files requested by the argument (`both` → both files). `result/` holds stakeholder summaries and nothing else — no bundles, no facts, no drafts.

- `result/executive-summary.md` — sponsors / leadership. One page. RAG, the decision (if any), recommendation, asks. No ticket archaeology. No “needs human confirmation” section.
- `result/team-summary.md` — delivery team. Same RAG and same decisions as exec. Ticket-level evidence, named actions, gaps that need a human.

Both files must tell the same story. Team copy may add detail; it must not add a third timeline.

### Milestone dates

If sources disagree on a milestone:

- List each date with **who holds it** and **what kind of date it is** (committed, slide, forecast, earliest sign-off).
- An engineering “earliest I will sign” date is not a newly committed go-live. Do not write “use [later date]” as if the program already moved.
- If a later date depends on someone returning, a soak period, or unmet gates, say that dependency.
- If leadership would otherwise be briefed with two numbers, the exec ask is to pick one this cycle. Options to offer when that pattern appears:
  - **A** — move the committed date to the earliest-sign / forecast date
  - **B** — keep the committed date and accept unmet gates
  - **C** — no decision → two dates in the brief
- Recommend A vs B in the exec note. Do not publish the uncommitted date as decided.

If sources agree on a single milestone, state it once. Do not invent a fork.

### Other calls

- Prefer later operational evidence over a tracker chip when they disagree; keep both claims in normalize.
- An unsigned or undated note that says “everything is done / we can hit the date” is a claim, not a status flip. Keep it next to named, timestamped evidence. Do not change RAG to Green on that note alone.
- A workstream that is “on track” but gated on a slipping predecessor is locally unblocked, not independently green.
- A resolved incident with empty follow-up tickets is residual risk, not “no issues.”
- Omit stale low-priority process risks and internal-only noise from exec highlights.
- Overall RAG is a human-shaped call you draft. On the exec note, state it as the status (Amber / Green / Red) without calling it a draft. Do not average conflicting dates into a vague window.
- If a source weekday contradicts calendar arithmetic from another sourced weekday, keep both and put the contradiction in the team **Needs human confirmation** table. Do not pick one silently. Do not put that table on the exec note.

## Step 5 — Stop

Print a short recap: program name (or `unknown`), files written, conflict types found, any date fork in one sentence. Do not send. A human TPM validates before anything leaves the folder.

Done when `result/` contains only the requested summaries and the recap is printed.
