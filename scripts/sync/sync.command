#!/usr/bin/env bash
# Double-click in Finder (macOS): syncs this computer with GitHub.
cd "$(dirname "$0")/../.." && bash scripts/sync/sync.sh "$@"
echo; read -r -p "Press Return to close." _
