#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Research-OS bootstrap: run once after cloning, and again whenever something looks broken.

    python3 bootstrap.py

It (1) checks the Python version and the packages the checks need, (2) creates the working folders that Git does
not keep, (3) builds the local SQLite database from database/schema.sql, (4) turns on the pre-commit hook
(.githooks/), and (5) runs the checks once. It never overwrites a file that already exists.

Earlier versions (2.0) carried a second copy of src/core/*.py and the YAML files inside this script; the two copies
drifted apart. The files now live only in the repository, and this script only checks that they are there.
"""

import importlib.util
import shutil
import sqlite3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

if sys.version_info < (3, 11):
    sys.exit("Python 3.11+ is required (found %d.%d)." % sys.version_info[:2])

FOLDERS = [
    "data/raw", "data/interim", "data/processed",
    "output/tables", "output/figures",
    "papers/manuscript", "papers/review", "papers/references_pdf",
    "logs", "workspace", "advisor", "handoff",
]
REQUIRED = ["config/settings.yaml", "config/expected_numbers.yaml", "config/claims_register.yaml",
            "config/style_rules.yaml", "database/schema.sql", "STATUS.md", "CLAUDE.md"]
PACKAGES = {"yaml": "pyyaml (all checks)", "docx": "python-docx (Word master -> Markdown mirror)",
            "pandas": "pandas (analysis)", "pytest": "pytest (tests/)"}


def main() -> int:
    print("=== Research-OS bootstrap ===")
    for rel in FOLDERS:
        (ROOT / rel).mkdir(parents=True, exist_ok=True)
    print(f"  folders: {len(FOLDERS)} present")

    missing = [rel for rel in REQUIRED if not (ROOT / rel).exists()]
    for rel in missing:
        print(f"  MISSING {rel}  (restore it from the template: git checkout -- {rel})")

    absent = [f"{mod} -> pip install {desc.split(' ')[0]}  [{desc}]"
              for mod, desc in PACKAGES.items() if importlib.util.find_spec(mod) is None]
    for line in absent:
        print(f"  package missing: {line}")
    if not absent:
        print("  packages: pyyaml, python-docx, pandas, pytest present")
    print(f"  R: {'found' if shutil.which('Rscript') else 'not found (only needed for src/r_scripts/)'}")

    db, schema = ROOT / "database" / "research_os.db", ROOT / "database" / "schema.sql"
    if schema.exists():
        with sqlite3.connect(db) as conn:
            conn.executescript(schema.read_text(encoding="utf-8"))
        print(f"  database: {db.relative_to(ROOT)} (schema applied; the .db file is not tracked by Git)")

    if (ROOT / ".git").exists() and (ROOT / ".githooks").is_dir():
        subprocess.run(["git", "-C", str(ROOT), "config", "core.hooksPath", ".githooks"], check=False)
        print("  git hook: core.hooksPath = .githooks (pre-commit runs the read-only checks)")

    if importlib.util.find_spec("yaml") is not None:
        print("\n=== first run of the checks ===", flush=True)
        subprocess.run(["bash", str(ROOT / "scripts" / "checks" / "check_all.sh"), "--readonly"], check=False)
    print("\nNext: fill in STATUS.md, then read CLAUDE.md (entry point for you and for AI assistants).")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
