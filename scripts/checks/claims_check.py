#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Core claims stay the same everywhere; retired wording does not come back.

    python3 scripts/checks/claims_check.py                     # check config/claims_register.yaml
    python3 scripts/checks/claims_check.py --where "phrase"    # every place a phrase is said, with its section

--where is the quick way to find a sentence before changing it (instead of opening files one by one).
Exit code 1 when a listed phrase is missing or retired wording is found.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "config" / "claims_register.yaml"
HEAD = re.compile(r"^(#{1,4}) (.*)$")
RETIRED_LINE = re.compile(r"❌|\bretired\b|废止|作废|폐기")


def key_of(title: str) -> str:
    first = title.split(" ")[0]
    return first.rstrip(".") if re.match(r"\d", first) else title


def sections(lines: list[str]) -> list[tuple[str, str, int, int]]:
    heads = [(i, len(m.group(1)), m.group(2)) for i, ln in enumerate(lines) if (m := HEAD.match(ln))]
    out = []
    for k, (i, lev, title) in enumerate(heads):
        end = next((j for j, l2, _ in heads[k + 1:] if l2 <= lev), len(lines))
        out.append((key_of(title), title, i, end))
    return out


def where_said(i: int, secs) -> str:
    inside = [s for s in secs if s[2] <= i < s[3]]
    return inside[-1][1][:60] if inside else "front matter"


def matches(phrase: str, text: str) -> bool:
    if len(phrase) > 2 and phrase.startswith("/") and phrase.endswith("/"):
        return re.search(phrase[1:-1], text) is not None
    return phrase in text


def live_part(line: str) -> str:
    """In a 'do not say' line the quoted retired wording comes before the dash; only the part after it is checked."""
    if not RETIRED_LINE.search(line):
        return line
    for dash in ("——", " — ", " – "):
        if dash in line:
            return line.split(dash, 1)[1]
    return ""


def load(path: Path = REGISTER) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def check(reg: dict) -> int:
    bad = 0
    cache: dict[str, list[str]] = {}

    def lines_of(f: str) -> list[str]:
        if f not in cache:
            p = ROOT / f
            cache[f] = p.read_text(encoding="utf-8").split("\n") if p.exists() else []
            if not p.exists():
                print(f"NOFILE   {f}")
        return cache[f]

    for c in reg.get("claims") or []:
        files = []
        for p in c.get("places") or []:
            lines = lines_of(p["file"])
            files.append(p["file"])
            scope = lines
            if p.get("section"):
                want = str(p["section"]).rstrip(".")
                hit = [s for s in sections(lines) if s[0] == want]
                if len(hit) != 1:
                    print(f"SECTION  {c['id']}: {p['file']} has {len(hit)} headings numbered {want!r}")
                    bad += 1
                    continue
                scope = lines[hit[0][2]:hit[0][3]]
            joined = "\n".join(scope)
            for ph in p.get("phrases") or []:
                if not matches(ph, joined):
                    print(f"MISSING  {c['id']}: {p['file']} §{p.get('section', '')}: {ph!r}")
                    bad += 1
        for f in dict.fromkeys(files):
            lines = lines_of(f)
            secs = sections(lines)
            for ph in c.get("stale") or []:
                for i, ln in enumerate(lines):
                    if matches(ph, live_part(ln)):
                        print(f"STALE    {c['id']}: {f}:{i + 1} ({where_said(i, secs)}): {ph!r}")
                        bad += 1
    n = sum(len(p.get("phrases") or []) for c in reg.get("claims") or [] for p in c.get("places") or [])
    print(f"claims {len(reg.get('claims') or [])}, phrases {n}: " + ("all consistent" if not bad else f"{bad} problem(s)"))
    return bad


def where(reg: dict, phrase: str) -> int:
    found = 0
    for f in reg.get("search") or []:
        p = ROOT / f
        if not p.exists():
            continue
        lines = p.read_text(encoding="utf-8").split("\n")
        secs = sections(lines)
        for i, ln in enumerate(lines):
            k = ln.lower().find(phrase.lower())
            if k >= 0:
                found += 1
                print(f"{f}:{i + 1} [{where_said(i, secs)}] …{ln[max(0, k - 70):k + len(phrase) + 70]}…")
    if not found:
        print(f"not found in {len(reg.get('search') or [])} file(s): {phrase!r}")
    return 0


if __name__ == "__main__":
    reg = load()
    if len(sys.argv) > 2 and sys.argv[1] == "--where":
        sys.exit(where(reg, " ".join(sys.argv[2:])))
    sys.exit(1 if check(reg) else 0)
