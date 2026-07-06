#!/usr/bin/env bash
# Lint checks for system-design-db.
set -euo pipefail

python3 meta/scripts/validate-vault.sh
python3 meta/scripts/validate-canonical-refs.py

