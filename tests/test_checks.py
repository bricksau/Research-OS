"""Tests for the checks. Run: python3 -m pytest -q"""
import subprocess
import sys
from decimal import Decimal
from pathlib import Path

import pytest
import yaml

import claims_check
import style_scan
import verify_ssot

ROOT = Path(__file__).resolve().parents[1]


def test_paths_anchor_to_repository():
    from src.core import paths
    assert paths.WORKSPACE_ROOT == ROOT
    assert paths.CONFIG_EXPECTED.exists()


@pytest.mark.parametrize("value,dec,want", [("0.05", 1, "0.1"), ("-0.05", 1, "-0.1"), ("1234.5", 0, "1,235"),
                                            ("2.675", 2, "2.68")])
def test_round_half_away_from_zero_once(value, dec, want):
    assert verify_ssot.fmt(Decimal(value), dec, True) == want


def test_typographic_minus_counts_as_minus():
    assert verify_ssot.norm("−US$420.7") == verify_ssot.norm("-US$420.7")


def _run_ssot(tmp_path, entry, manuscript_text):
    ms = tmp_path / "ms.md"
    ms.write_text(manuscript_text, encoding="utf-8")
    cfg = tmp_path / "exp.yaml"
    cfg.write_text(yaml.safe_dump({"manuscript": str(ms), "numbers": [entry]}), encoding="utf-8")
    return subprocess.run([sys.executable, str(ROOT / "src/analysis/verify_ssot.py"), "--config", str(cfg)],
                          capture_output=True, text=True)


ENTRY = {"id": "t", "source": "output/tables/example_trade_balance.csv", "row": {"year": "2024"},
         "column": "balance_musd", "scale": -1, "decimals": 1}


def test_ssot_passes_on_match(tmp_path):
    r = _run_ssot(tmp_path, dict(ENTRY, text="420.7"), "a deficit of US$420.7 million")
    assert r.returncode == 0 and "MISMATCH=0" in r.stdout


def test_ssot_catches_wrong_number(tmp_path):
    r = _run_ssot(tmp_path, dict(ENTRY, text="420.8"), "a deficit of US$420.8 million")
    assert r.returncode == 1 and "MISMATCH  t" in r.stdout


def test_ssot_catches_number_missing_from_text(tmp_path):
    r = _run_ssot(tmp_path, dict(ENTRY, text="420.7"), "a deficit of US$421 million")
    assert r.returncode == 1 and "MISSING" in r.stdout


def test_ssot_ambiguous_row_is_an_error(tmp_path):
    r = _run_ssot(tmp_path, dict(ENTRY, row={}, text="420.7"), "420.7")
    assert r.returncode == 1 and "rows match" in r.stdout


def test_repository_checks_pass():
    r = subprocess.run(["bash", str(ROOT / "scripts/checks/check_all.sh"), "--readonly"], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout


def test_claims_sections_and_stale(tmp_path, monkeypatch):
    f = tmp_path / "m.md"
    f.write_text("# 1. Intro\nWe find X.\n## 1.1 Sub\nimports drove the deficit\n# 2. Results\nY holds.\n", encoding="utf-8")
    monkeypatch.setattr(claims_check, "ROOT", tmp_path)
    reg = {"claims": [{"id": "c", "places": [{"file": "m.md", "section": "2", "phrases": ["Y holds."]},
                                             {"file": "m.md", "section": "1", "phrases": ["We find Z."]}],
                       "stale": ["/imports (?:caused|drove) the deficit/"]}]}
    assert claims_check.check(reg) == 2  # one MISSING (Z) + one STALE


def test_claims_retired_line_is_skipped(tmp_path, monkeypatch):
    f = tmp_path / "m.md"
    f.write_text("❌ “imports drove the deficit” — write: imports rose as the deficit widened\n", encoding="utf-8")
    monkeypatch.setattr(claims_check, "ROOT", tmp_path)
    reg = {"claims": [{"id": "c", "places": [{"file": "m.md", "phrases": []}], "stale": ["imports drove the deficit"]}]}
    assert claims_check.check(reg) == 0


def test_style_scan_flags_and_skips():
    text = ("# 1. Heading with crucial word\n"
            "This finding proves that tariffs drove the shift.\n"
            "<!-- it is worth noting -->\n"
            "| table | crucial |\n"
            "First, we examine the data.\n")
    hits = style_scan.scan(text)
    assert {"overclaim", "enumeration"} <= set(hits)
    assert "banned" not in hits  # heading, comment and table rows are skipped


def test_docx_mirror_roundtrip(tmp_path):
    docx = pytest.importorskip("docx")
    import docx_to_md
    d = docx.Document()
    d.add_heading("4. Results", level=1)
    d.add_paragraph("The balance fell to US$420.7 million.")
    t = d.add_table(rows=2, cols=2)
    t.cell(0, 0).text, t.cell(0, 1).text, t.cell(1, 0).text, t.cell(1, 1).text = "year", "balance", "2024", "-420.7"
    src = tmp_path / "M.docx"
    d.save(src)
    md = docx_to_md.convert(src)
    assert "# 4. Results" in md and "US$420.7 million" in md and "| 2024 | -420.7 |" in md


def test_number_is_matched_as_a_whole_token():
    assert verify_ssot.in_text("220.3", "a surplus of US$220.3 million.")
    assert verify_ssot.in_text("12.8%", "rose by 12.8% in")
    assert not verify_ssot.in_text("220.3", "US$1,220.3 million")
    assert not verify_ssot.in_text("220.3", "220.35")
