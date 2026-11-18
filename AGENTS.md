# AGENTS.md

For any coding or writing agent (Codex, Cursor, Gemini, Copilot, Claude …): the working rules of this repository are in
`CLAUDE.md` (entry page) and `.claude/skills/*/SKILL.md` (workflow and writing rules). They apply to every agent.

Short version:
1. Read `STATUS.md` first; read only the folders the task needs.
2. Numbers come from script output (`output/tables/`) and are listed in `config/expected_numbers.yaml`; never compute them in your head.
3. Quotes and references are checked against the source; never invent authors, years, pages or DOIs.
4. One master manuscript in `papers/manuscript/`; the `.md` mirror of a Word master is generated, not edited.
5. After a change run `bash scripts/checks/check_all.sh`. As a read-only reviewer, run `bash scripts/checks/check_all.sh --readonly`
   and do not create, edit, move or delete any file.
