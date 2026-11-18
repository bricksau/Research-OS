#!/usr/bin/env bash
# All checks, one line each. Run after every change to the manuscript, the data or an analysis script.
#   bash scripts/checks/check_all.sh              regenerate the example table and the Word mirror, then check
#   bash scripts/checks/check_all.sh --readonly   check only, write nothing (for the pre-commit hook and for a
#                                                 read-only reviewer)
# To see the full output of one check, run that check on its own (the command is in the list below).
cd "$(dirname "$0")/../.." || exit 1
readonly_mode=0; [ "${1:-}" = "--readonly" ] && readonly_mode=1
fail=0
run() {  # name, pattern that means PASS, command...
  local name=$1 pat=$2; shift 2
  local out; out=$("$@" 2>&1)
  if echo "$out" | grep -q -- "$pat"; then echo "PASS  $name"
  else echo "FAIL  $name"; echo "$out" | tail -12 | sed 's/^/      /'; fail=1; fi
}
if [ $readonly_mode -eq 0 ]; then
  [ -f src/analysis/example_table.py ] && run "example table"  "wrote" python3 src/analysis/example_table.py
  run "Word mirror"    "wrote\|no .docx" python3 scripts/checks/docx_to_md.py
else
  echo "SKIP  regenerate (--readonly)"
fi
run "SSOT numbers"   "SSOT CHECKS PASSED" python3 src/analysis/verify_ssot.py
run "core claims"    "all consistent"     python3 scripts/checks/claims_check.py
exit $fail
