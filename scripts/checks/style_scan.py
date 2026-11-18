#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""List candidate writing problems in a Markdown manuscript, with line numbers.

    python3 scripts/checks/style_scan.py FILE [--section 4.2] [--notes]

It only lists candidates; read each one in context and change only what makes the text better. Headings, tables,
HTML comments and footnote lines ("[^n]: …") are skipped (--notes includes footnotes). Rules: config/style_rules.yaml.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
RULES = ROOT / "config" / "style_rules.yaml"
REGISTER = ROOT / "config" / "claims_register.yaml"

BUILTIN = [
    ("enumeration", r"\b(?:First|Second|Third|Fourth|Fifth)(?:ly)?, |첫째|둘째|셋째|第一，|第二，|第三，"),
    ("list-in-text", r"^\s*(?:[-*•]|\d+[.)])\s+\S"),
    ("overclaim", r"\bprove[sdn]?\b|\bdemonstrat(?:es|ed) that\b|\bestablish(?:es|ed) that\b|\bconfirm(?:s|ed) that\b"
                  r"|\bcaused\b|\bdrove\b|\bled to\b|\bresulted in\b|证明了|입증"),
    ("drafting-history", r"(?i)earlier (?:version|draft)|the committee|\badvisor\b|\bsupervisor\b|post hoc"
                         r"|pre-?specified|after seeing the data|导师|评委|看了数据以后|지도교수"),
    ("signpost", r"^This (?:section|chapter|subsection) (?:will )?(?:discuss|examine|present|explore)s?\b|^本(?:节|章)将"),
]


def load_rules() -> tuple[list[tuple[str, str]], set[str]]:
    cfg = yaml.safe_load(RULES.read_text(encoding="utf-8")) if RULES.exists() else {}
    cfg = cfg or {}
    checks = list(BUILTIN)
    words = [w for w in cfg.get("banned") or [] if w]
    if words:
        parts = [(r"\b" + re.escape(w) + r"\b") if re.match(r"[A-Za-z]", w) else re.escape(w) for w in words]
        checks.append(("banned", "(?i)" + "|".join(parts)))
    for item in cfg.get("extra") or []:
        if isinstance(item, (list, tuple)) and len(item) == 2:
            checks.append((str(item[0]), str(item[1])))
    if REGISTER.exists():
        reg = yaml.safe_load(REGISTER.read_text(encoding="utf-8")) or {}
        for c in reg.get("claims") or []:
            for ph in c.get("stale") or []:
                pat = ph[1:-1] if len(ph) > 2 and ph.startswith("/") and ph.endswith("/") else re.escape(ph)
                checks.append(("retired", pat))
    return checks, set(cfg.get("disable") or [])


def section_lines(lines: list[str], sec: str) -> set[int]:
    keep, inside = set(), False
    for i, line in enumerate(lines, 1):
        m = re.match(r"^#{1,4} (\S+)", line)
        if m:
            num = m.group(1).rstrip(".")
            inside = num == sec or num.startswith(sec + ".")
        if inside:
            keep.add(i)
    return keep


def scan(text: str, section: str | None = None, notes: bool = False) -> dict[str, list[tuple[int, str]]]:
    checks, off = load_rules()
    lines = text.split("\n")
    only = section_lines(lines, section.rstrip(".")) if section else None
    hits: dict[str, list[tuple[int, str]]] = {}
    in_comment = False
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if s.startswith("<!--"):
            in_comment = "-->" not in s
            continue
        if in_comment:
            in_comment = "-->" not in s
            continue
        if only is not None and i not in only:
            continue
        if not s or s.startswith(("#", "|", "```")) or (s.startswith("[^") and not notes):
            continue
        body = re.sub(r"\[\^\w+\]", "", line)
        for name, pat in checks:
            if name in off:
                continue
            for m in re.finditer(pat, body):
                hits.setdefault(name, []).append((i, body[max(0, m.start() - 50):m.end() + 50].strip()))
                if name in ("list-in-text", "signpost"):
                    break
    return hits


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--section")
    ap.add_argument("--notes", action="store_true")
    a = ap.parse_args()
    hits = scan(Path(a.file).read_text(encoding="utf-8"), a.section, a.notes)
    if not hits:
        print("no candidates")
        return 0
    for name, items in hits.items():
        print(f"== {name}: {len(items)}")
        for i, snip in items[:40]:
            print(f"  {i}: …{snip}…")
        if len(items) > 40:
            print(f"  ({len(items) - 40} more)")
    print("\nCandidates only: read each in context; change only what improves the text.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
