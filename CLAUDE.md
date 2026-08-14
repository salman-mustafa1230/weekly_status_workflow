# Weekly status synthesis

When the user asks for weekly status, exec/team updates, `/weekly-status`, or `/harbor-status`, follow `prompts/status-synthesis.md`.

That recipe is program-agnostic. Infer the program from `data/*.json`. Do not assume Harbor, a ticket prefix, or a go-live date.

Do not read `notes/` while generating status. Load sources with `python3 scripts/load_sources.py` first.

Write `extracted/raw-bundle.json` and `extracted/normalized-facts.json` for machine artifacts. Write only `result/executive-summary.md` and `result/team-summary.md` into `result/`. After prompt or script changes, run `python3 scripts/validate.py`.
