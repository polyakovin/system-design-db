#!/usr/bin/env python3
"""Validate Markdown vault links and source frontmatter."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
EXCLUDE_PREFIXES = ("meta/", ".git/", "assets/")
REQUIRED_SOURCE_FIELDS = ("title", "url", "type", "category", "tags", "added", "status")


def find_md_files(root: Path):
    for fpath in root.rglob("*.md"):
        rel = fpath.relative_to(root)
        if any(str(rel).startswith(prefix) for prefix in EXCLUDE_PREFIXES):
            continue
        yield fpath


def resolve_href(source_file: Path, href: str) -> Path | None:
    if href.startswith(("http://", "https://", "mailto:")):
        return None
    if href.rsplit(".", 1)[-1].lower() in {"svg", "png", "jpg", "jpeg", "gif", "ico", "webp"}:
        return None

    href_clean = href.split("#")[0]
    if not href_clean:
        return None
    if href_clean.startswith("/"):
        return ROOT / href_clean.lstrip("/")
    return (source_file.parent / href_clean).resolve()


def extract_md_links(text: str):
    return re.findall(r"\[([^]]*)\]\(([^)]+)\)", text)


def strip_fenced_code(text: str) -> list[str]:
    in_code_block = False
    clean_lines = []
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            clean_lines.append("")
            continue
        clean_lines.append("" if in_code_block else line)
    return clean_lines


def parse_frontmatter(text: str) -> dict[str, str] | None:
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None
    out = {}
    for raw_line in match.group(1).splitlines():
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        out[key.strip()] = value.strip()
    return out


def validate_source_frontmatter(fpath: Path) -> list[str]:
    rel = fpath.relative_to(ROOT)
    if not str(rel).startswith("sources/") or fpath.name == "OVERVIEW.md":
        return []

    text = fpath.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text)
    if frontmatter is None:
        return [f"Missing frontmatter: {rel}"]

    missing = [field for field in REQUIRED_SOURCE_FIELDS if field not in frontmatter]
    return [f"Missing source field '{field}': {rel}" for field in missing]


def main() -> int:
    errors = []

    for fpath in find_md_files(ROOT):
        text = fpath.read_text(encoding="utf-8")
        clean_lines = strip_fenced_code(text)

        for line_no, line in enumerate(clean_lines, start=1):
            for label, href in extract_md_links(line):
                target = resolve_href(fpath, href)
                if target is None:
                    continue
                if not target.exists():
                    rel = fpath.relative_to(ROOT)
                    errors.append(f"Broken link: {rel}:{line_no} -> [{label}]({href}) -> {target}")

        errors.extend(validate_source_frontmatter(fpath))

    if errors:
        print("\n".join(errors))
        print(f"\nVault validation failed: {len(errors)} error(s).")
        return 1

    print("All links valid.")
    print("Vault validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

