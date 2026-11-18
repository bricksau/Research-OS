#!/usr/bin/env python3
"""Example of the analysis layer: raw data in, one table out, nothing typed by hand.

    python3 src/analysis/example_table.py

Reads data/raw/example/example_trade.csv (synthetic) and writes output/tables/example_trade_balance.csv.
Replace with your own scripts; R scripts in src/r_scripts/ follow the same rule (read data/, write output/).
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "data" / "raw" / "example" / "example_trade.csv"
OUT = ROOT / "output" / "tables" / "example_trade_balance.csv"


def main() -> None:
    with SRC.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["year", "exports_musd", "imports_musd", "balance_musd", "import_growth_pct"])
        prev = None
        for r in rows:
            exp, imp = float(r["exports_musd"]), float(r["imports_musd"])
            growth = "" if prev is None else f"{(imp / prev - 1) * 100:.4f}"
            w.writerow([r["year"], f"{exp:.4f}", f"{imp:.4f}", f"{exp - imp:.4f}", growth])
            prev = imp
    print(f"wrote {OUT.relative_to(ROOT)} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
