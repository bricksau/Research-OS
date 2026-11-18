#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SSOT check: every number listed in config/expected_numbers.yaml is recomputed from its CSV and looked up in the
manuscript. Nothing is typed by hand: if the CSV changes, the check fails until the manuscript and the YAML follow.

    python3 src/analysis/verify_ssot.py            # all entries
    python3 src/analysis/verify_ssot.py --list     # what is covered, one line each

Prints one line per problem and ends with "MISMATCH=<n>"; exit code 1 when n > 0.
Rounding: half away from zero, once, at the end (Decimal), so 0.05 -> 0.1 as a reader expects.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CONFIG = ROOT / "config" / "expected_numbers.yaml"
MINUS = {"−": "-", "–": "-"}  # typographic minus and en dash count as "-"


def norm(s: str) -> str:
    for k, v in MINUS.items():
        s = s.replace(k, v)
    return s.replace(" ", " ")


def in_text(number: str, text: str) -> bool:
    """The number as a whole token: 220.3 is not found inside 1,220.3 or 220.35."""
    return re.search(r"(?<![\d.,])" + re.escape(number) + r"(?![\d]|[.,]\d)", text) is not None


def fmt(value: Decimal, decimals: int, thousands: bool) -> str:
    q = Decimal(1).scaleb(-decimals)
    v = value.quantize(q, rounding=ROUND_HALF_UP)
    return f"{v:,.{decimals}f}" if thousands else f"{v:.{decimals}f}"


def cell(entry: dict) -> Decimal:
    path = ROOT / entry["source"]
    with path.open(encoding="utf-8-sig") as f:
        rows = [r for r in csv.DictReader(f)
                if all(str(r.get(k, "")).strip() == str(v) for k, v in (entry.get("row") or {}).items())]
    if len(rows) != 1:
        raise ValueError(f"{len(rows)} rows match {entry.get('row')} in {entry['source']} (need exactly 1)")
    raw = rows[0].get(entry["column"])
    if raw in (None, ""):
        raise ValueError(f"column {entry['column']!r} is empty or missing in {entry['source']}")
    return Decimal(raw.replace(",", "")) * Decimal(str(entry.get("scale", 1)))


def manuscript_text(cfg: dict) -> tuple[str, str]:
    rel = cfg.get("manuscript", "")
    path = ROOT / rel
    if path.suffix == ".docx":
        path = path.with_suffix(".md")
        rel = str(path.relative_to(ROOT))
    if not path.exists():
        raise SystemExit(f"manuscript not found: {rel} (for a Word master run scripts/checks/docx_to_md.py first)")
    return rel, norm(path.read_text(encoding="utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default=str(CONFIG))
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    cfg = yaml.safe_load(Path(a.config).read_text(encoding="utf-8")) or {}
    numbers, sentences = cfg.get("numbers") or [], cfg.get("must_contain") or []
    if a.list:
        for e in numbers:
            print(f"{e['id']:<32} {e['text']:>14}  <- {e['source']} [{e['column']}] {e.get('row', '')}")
        for s in sentences:
            print(f"{'sentence':<32} {s['text'][:70]}")
        return 0
    rel, text = manuscript_text(cfg)
    bad = 0
    for e in numbers:
        want = norm(str(e["text"]))
        try:
            got = fmt(cell(e), int(e.get("decimals", 1)), bool(e.get("thousands", True))) + e.get("suffix", "")
        except (OSError, ValueError, KeyError, ArithmeticError) as err:
            print(f"ERROR     {e.get('id')}: {err}")
            bad += 1
            continue
        if norm(got) != want:
            print(f"MISMATCH  {e['id']}: data gives {got}, YAML says {e['text']} ({e['source']})")
            bad += 1
        if not in_text(want, text):
            print(f"MISSING   {e['id']}: {e['text']!r} not found in {rel}")
            bad += 1
    for s in sentences:
        if norm(s["text"]) not in text:
            print(f"MISSING   sentence: {s['text'][:80]!r} not found in {rel} ({s.get('why', '')})")
            bad += 1
    print(f"numbers {len(numbers)}, sentences {len(sentences)}: MISMATCH={bad}"
          + (" — SSOT CHECKS PASSED" if not bad else ""))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
