#!/usr/bin/env bash
# Sync this computer with GitHub (macOS, or Git Bash on Windows).
#
#   scripts/sync/sync.sh              commit local changes (if any), get the other computers' changes, push
#   scripts/sync/sync.sh "message"    same, with your own commit message
#   scripts/sync/sync.sh --pull       only get the other computers' changes (refuses if you have local changes)
#
# Run it when you START working on a computer and again when you STOP.
# If the same Word/HWP file was changed on two computers, Git cannot merge it: the script stops,
# leaves everything as it was, and tells you which files clash.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

branch=$(git rev-parse --abbrev-ref HEAD)
if [ "$branch" = "HEAD" ]; then echo "Not on a branch (detached HEAD). Stop."; exit 1; fi
echo "== Branch: $branch"

if [ -n "$(git ls-files -u)" ] || [ -d .git/rebase-merge ] || [ -d .git/rebase-apply ] || [ -f .git/MERGE_HEAD ]; then
  echo "A previous merge or rebase is unfinished. Resolve it first (or ask Claude)."; exit 1
fi

pull_only=0
msg=""
if [ "${1:-}" = "--pull" ]; then pull_only=1; else msg="${1:-}"; fi

# 1) Save local changes as a commit
if [ -n "$(git status --porcelain)" ]; then
  if [ $pull_only -eq 1 ]; then
    echo "You have local changes; run without --pull to save and sync them:"; git status --short; exit 1
  fi
  echo "== Local changes:"; git status --short
  git add -A
  host=$(hostname -s 2>/dev/null || hostname)
  git commit -q -m "${msg:-sync: $host $(date '+%Y-%m-%d %H:%M')}"
  echo "== Committed."
fi

# 2) Get the other computers' changes
git fetch -q origin
if git rev-parse -q --verify "origin/$branch" >/dev/null; then
  if ! git rebase -q "origin/$branch"; then
    clash=$(git diff --name-only --diff-filter=U || true)
    git rebase --abort
    echo
    echo "!! The same files were changed here and on another computer:"
    echo "$clash" | sed 's/^/   /'
    echo "!! Nothing was lost: your changes are still committed on this computer, but not uploaded."
    echo "!! Decide which version to keep (or ask Claude), then run this script again."
    exit 1
  fi
fi

# 3) Upload
if [ $pull_only -eq 0 ]; then
  git push -q -u origin "$branch"
  echo "== Uploaded to GitHub."
fi
git log --oneline -3
echo "== Done. This computer is in sync with GitHub ($branch)."
