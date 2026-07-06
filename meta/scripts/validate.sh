#!/usr/bin/env python3
"""Full validation for system-design-db."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent


def run(command: list[str]) -> int:
    print("$ " + " ".join(command), flush=True)
    return subprocess.run(command, cwd=ROOT, check=False).returncode


def main() -> int:
    checks = [
        ["python3", "meta/scripts/generate-canonical-map.py"],
        ["python3", "meta/scripts/validate-vault.sh"],
        ["python3", "meta/scripts/validate-canonical-refs.py"],
    ]

    for command in checks:
        code = run(command)
        if code != 0:
            return code
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
