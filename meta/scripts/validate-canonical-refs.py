#!/usr/bin/env python3
"""Validate that known canonical entities are referenced with Markdown links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
MAP_PATH = ROOT / "meta" / "canonical-map.json"
SCAN_DIRS = [ROOT / "patterns", ROOT / "tools"]
EXCLUDE_PREFIXES = (ROOT / "meta", ROOT / "sources", ROOT / "assets", ROOT / ".git")
SHORT_ALIASES = frozenset({"api", "slo", "sql", "nosql"})


def load_canonical_map() -> dict:
    if not MAP_PATH.exists():
        print(f"{MAP_PATH} not found. Run meta/scripts/generate-canonical-map.py first.", file=sys.stderr)
        sys.exit(2)
    return json.loads(MAP_PATH.read_text(encoding="utf-8"))


def build_name_lookup(can_map: dict) -> dict[str, dict]:
    out = {}
    for _slug, info in can_map.items():
        if info.get("path") and info.get("name"):
            out[info["name"].lower()] = {"path": info["path"], "name": info["name"]}
            for alias in info.get("aliases", []):
                out[alias.lower()] = {"path": info["path"], "name": info["name"]}
    return out


def find_files(directory: Path) -> list[Path]:
    if not directory.exists():
        return []
    return sorted(
        fpath
        for fpath in directory.rglob("*.md")
        if not any(fpath.is_relative_to(prefix) for prefix in EXCLUDE_PREFIXES)
        and not fpath.name.startswith("_")
        and fpath.name != "OVERVIEW.md"
    )


def strip_inline_code(line: str) -> str:
    return re.sub(r"`[^`]*`", "", line)


def find_bare_mentions(text: str, filepath: Path, name_to_path: dict[str, dict]) -> list[dict]:
    violations = []
    in_code_block = False

    for lineno, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        if line.startswith("#"):
            continue
        if "[" in line:
            continue
        if "|" in line:
            continue
        if line.lower().startswith(("url:", "tags:", "title:", "added:", "status:", "category:", "type:")):
            continue

        line_to_check = strip_inline_code(line)
        for name_lower, path_info in name_to_path.items():
            if name_lower in SHORT_ALIASES:
                continue

            target = ROOT / path_info["path"]
            if target.exists() and filepath.samefile(target):
                continue

            pattern = rf"(?<![A-Za-z0-9_-]){re.escape(path_info['name'])}(?![A-Za-z0-9_-])"
            if re.search(pattern, line_to_check, flags=re.IGNORECASE):
                violations.append({
                    "line": lineno,
                    "text": raw_line.rstrip(),
                    "name": path_info["name"],
                    "target": path_info["path"],
                })

    return violations


def main() -> int:
    name_to_path = build_name_lookup(load_canonical_map())
    all_violations = []

    for scan_dir in SCAN_DIRS:
        for fpath in find_files(scan_dir):
            text = fpath.read_text(encoding="utf-8")
            for violation in find_bare_mentions(text, fpath, name_to_path):
                violation["file"] = str(fpath.relative_to(ROOT))
                all_violations.append(violation)

    if not all_violations:
        print("No bare mentions found; canonical references look good.")
        return 0

    print(f"{len(all_violations)} bare mention(s) found. Use Markdown links to canonical pages:\n")
    for violation in all_violations:
        print(f"  {violation['file']}:{violation['line']}")
        print(f"    mention: {violation['name']} -> {violation['target']}")
        print(f"    text: {violation['text'][:140]}")
        print()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

