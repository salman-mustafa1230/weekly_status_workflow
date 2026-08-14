#!/usr/bin/env python3
"""Load every source file in data/ into one bundle. No interpretation."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
EXTRACTED = ROOT / "extracted"
RAW_BUNDLE = EXTRACTED / "raw-bundle.json"


def data_source_paths() -> list[Path]:
    return sorted(
        p for p in DATA.iterdir() if p.is_file() and not p.name.startswith(".")
    )


def data_json_paths() -> list[Path]:
    return [p for p in data_source_paths() if p.suffix.lower() == ".json"]


def _read_source(path: Path) -> object:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    return {"format": "text", "body": text}


def build_bundle() -> dict:
    paths = data_source_paths()
    if not paths:
        raise SystemExit(f"No source files in {DATA}")
    sources: dict[str, object] = {}
    for path in paths:
        sources[path.name] = _read_source(path)
    return {
        "source_dir": "data/",
        "files_loaded": [p.name for p in paths],
        "sources": sources,
    }


def write_bundle() -> Path:
    EXTRACTED.mkdir(parents=True, exist_ok=True)
    bundle = build_bundle()
    RAW_BUNDLE.write_text(json.dumps(bundle, indent=2) + "\n", encoding="utf-8")
    return RAW_BUNDLE


def main() -> None:
    path = write_bundle()
    n = len(json.loads(path.read_text(encoding="utf-8"))["files_loaded"])
    print(f"Wrote {path} ({n} files)")


if __name__ == "__main__":
    main()
