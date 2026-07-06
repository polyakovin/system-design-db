#!/usr/bin/env python3
"""Generate meta/canonical-map.json from patterns/ and tools/."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PATTERNS = ROOT / "patterns"
TOOLS = ROOT / "tools"
MAP_PATH = ROOT / "meta" / "canonical-map.json"
EXCLUDE_FILES = {"OVERVIEW.md", "index.md", "summary.md", "_sidebar.md"}


def extract_frontmatter_title(text: str) -> str | None:
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None
    for line in match.group(1).splitlines():
        if line.startswith("title:"):
            value = line[len("title:") :].strip().strip("\"'")
            if value:
                return value
    return None


def extract_h1(text: str) -> str | None:
    match = re.search(r"^#\s+(.+)", text, re.MULTILINE)
    return match.group(1).strip() if match else None


def kebab_to_title(name: str) -> str:
    return " ".join(word.capitalize() for word in name.replace("-", " ").split())


def find_canonical_files(root: Path) -> list[Path]:
    if not root.exists():
        return []
    return sorted(
        fpath
        for fpath in root.rglob("*.md")
        if fpath.name not in EXCLUDE_FILES and not any(part.startswith(".") for part in fpath.relative_to(root).parts)
    )


def build_map() -> dict:
    canonical_files = find_canonical_files(PATTERNS) + find_canonical_files(TOOLS)
    can_map = {}

    for fpath in canonical_files:
        rel = fpath.relative_to(ROOT)
        slug = fpath.stem
        text = fpath.read_text(encoding="utf-8")
        name = extract_frontmatter_title(text) or extract_h1(text) or kebab_to_title(slug)

        can_map[slug] = {
            "name": name,
            "path": str(rel),
        }

    return dict(sorted(can_map.items()))


def main() -> int:
    can_map = build_map()
    MAP_PATH.write_text(json.dumps(can_map, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"canonical-map.json: {len(can_map)} entries -> {MAP_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

