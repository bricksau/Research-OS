import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for sub in ("", "scripts/checks", "src/analysis"):
    p = str(ROOT / sub)
    if p not in sys.path:
        sys.path.insert(0, p)
