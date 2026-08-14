#!/usr/bin/env python3
"""Validate data → extracted → result wiring after prompt or flow changes.

  python3 scripts/validate.py

Exits 0 if checks pass, 1 if any fail. Harbor-specific content checks run only
when the current data pack looks like Project Harbor.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import load_sources  # noqa: E402

DATA = ROOT / "data"
EXTRACTED = ROOT / "extracted"
RESULT = ROOT / "result"
RECIPE = ROOT / "prompts" / "status-synthesis.md"
EXEC = RESULT / "executive-summary.md"
TEAM = RESULT / "team-summary.md"
FACTS = EXTRACTED / "normalized-facts.json"

failures: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)


def read(path: Path) -> str:
    if not path.is_file():
        fail(f"missing file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def collect_people(obj: object) -> set[str]:
    names: set[str] = set()
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in {"name", "author", "oncall"} and isinstance(value, str) and " " in value:
                names.add(value.strip())
            else:
                names |= collect_people(value)
    elif isinstance(obj, list):
        for item in obj:
            names |= collect_people(item)
    return names


def check_data_sources() -> dict[str, object]:
    paths = load_sources.data_source_paths()
    if not paths:
        fail("data/ has no source files")
        return {}
    sources: dict[str, object] = {}
    for path in paths:
        try:
            sources[path.name] = load_sources._read_source(path)
        except json.JSONDecodeError as exc:
            fail(f"invalid JSON {path.name}: {exc}")
        except OSError as exc:
            fail(f"cannot read {path.name}: {exc}")
    return sources


def check_bundle(sources: dict[str, object]) -> None:
    try:
        bundle = load_sources.build_bundle()
    except Exception as exc:  # noqa: BLE001 — report any loader break
        fail(f"load_sources.build_bundle() raised: {exc}")
        return
    expected = sorted(sources)
    got = bundle.get("files_loaded")
    if got != expected:
        fail(f"bundle files_loaded {got!r} != data/ files {expected!r}")
    raw = load_sources.RAW_BUNDLE
    if not raw.is_file():
        fail("extracted/raw-bundle.json missing; run python3 scripts/load_sources.py")
        return
    on_disk = json.loads(raw.read_text(encoding="utf-8"))
    if on_disk.get("files_loaded") != expected:
        fail("extracted/raw-bundle.json is stale vs data/; re-run load_sources.py")


def check_folders() -> None:
    if not RESULT.is_dir():
        fail("result/ missing")
        return
    allowed = {"executive-summary.md", "team-summary.md"}
    found = {p.name for p in RESULT.iterdir() if p.is_file()}
    extra = found - allowed
    missing = allowed - found
    if extra:
        fail(f"result/ must only contain exec + team summaries; extra: {sorted(extra)}")
    if missing:
        fail(f"result/ missing: {sorted(missing)}")


def check_recipe_wiring() -> None:
    text = read(RECIPE)
    if not text:
        return
    for needle in (
        "extracted/raw-bundle.json",
        "extracted/normalized-facts.json",
        "result/executive-summary.md",
        "result/team-summary.md",
        "python3 scripts/load_sources.py",
    ):
        if needle not in text:
            fail(f"prompts/status-synthesis.md no longer references {needle}")
    if "Do not put that table on the exec note" not in text:
        fail("recipe no longer keeps the human-confirmation table off the exec note")


def check_exec_is_sendable(exec_text: str) -> None:
    banned = [
        ("Needs human confirmation", "exec is sendable; gaps belong on the team copy"),
        ("Tom Yap", "name is not in data/"),
        ("of 12", "program length is not in data/"),
        ("next week", "two-date failure is this 4pm, not next week"),
        ("see gap below", "exec must not point at scoring gaps"),
        ("not in the pack", "exec must not read like a process note"),
        ("not in the sources", "exec must not read like a process note"),
    ]
    lower = exec_text
    for needle, why in banned:
        if needle.lower() in lower.lower():
            fail(f"executive-summary.md contains {needle!r} ({why})")


def check_people(sources: dict[str, object], exec_text: str, team_text: str) -> None:
    people = collect_people(sources)
    if not people:
        return
    to_line = ""
    for line in exec_text.splitlines():
        if line.startswith("**To:**"):
            to_line = line
            break
    if not to_line:
        fail("executive-summary.md has no **To:** line")
        return
    mentioned = re.findall(r"[A-Z][a-z]+(?: [A-Z][a-z]+)+", to_line)
    skip = {"Weekly", "Project Harbor"}
    for name in mentioned:
        if name in skip:
            continue
        if name not in people:
            fail(f"executive-summary.md To: {name!r} is not a person in data/")


def is_harbor(sources: dict[str, object]) -> bool:
    blob = json.dumps(sources)
    return "Project Harbor" in blob and "MENU-280" in blob


def check_harbor_content(exec_text: str, team_text: str) -> None:
    for label, text, needles in (
        ("executive-summary.md", exec_text, ["Amber", "28 Aug", "4 Sep", "recommend", "20 Aug", "71%", "Priya"]),
        ("team-summary.md", team_text, ["Amber", "28 Aug", "4 Sep", "MENU-241", "INC-18472", "Needs human confirmation"]),
    ):
        for needle in needles:
            if needle not in text:
                fail(f"{label} missing expected Harbor fact {needle!r}")
    if (DATA / "jira_service_optimization.json").is_file():
        for label, text, needles in (
            ("executive-summary.md", exec_text, ["Microservice Optimization", "30 Sep", "legacy-auth"]),
            ("team-summary.md", team_text, ["SVC-15", "Kenji Watanabe"]),
        ):
            for needle in needles:
                if needle not in text:
                    fail(f"{label} missing second-program fact {needle!r}")
    if "Saturday 16 Aug" in exec_text and "Sunday" not in exec_text:
        fail("executive-summary.md states Saturday 16 Aug without the weekday conflict")
    if FACTS.is_file():
        facts = json.loads(FACTS.read_text(encoding="utf-8"))
        if "conflicts" not in facts or not facts["conflicts"]:
            fail("extracted/normalized-facts.json has no conflicts[]")
    if (DATA / "product_notes.txt").is_file():
        if "product_notes" not in team_text:
            fail("team-summary.md does not mention product_notes.txt after it was added to data/")
        if re.search(r"all tasks are completed", exec_text, re.I):
            fail("executive-summary.md treated the unsigned product note as fact")


def main() -> int:
    sources = check_data_sources()
    check_bundle(sources)
    check_folders()
    check_recipe_wiring()
    exec_text = read(EXEC)
    team_text = read(TEAM)
    if exec_text:
        check_exec_is_sendable(exec_text)
    if sources and exec_text:
        check_people(sources, exec_text, team_text)
    if sources and is_harbor(sources) and exec_text and team_text:
        print("Harbor pack checks running")
        check_harbor_content(exec_text, team_text)
    elif sources:
        print("Harbor pack checks skipped (current data/ is not Project Harbor).")

    if failures:
        print("FAIL")
        for item in failures:
            print(f"  - {item}")
        return 1
    print("OK — data/, extracted/, result/, and recipe wiring check out.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
