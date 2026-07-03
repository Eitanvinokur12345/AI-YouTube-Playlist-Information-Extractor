# PROJECT MEMORY — the contract every AI tool follows here

**The rule: you do not start from scratch. Ever.** This project remembers every change and
addition, however small — in `data/project_memory/` (episode ledger + brain graph, fed
automatically from git history and the EXCAVA bus every beat). Whatever tool you are —
Claude (any model), an EXCAVA agent, Cursor, Copilot, ChatGPT, Gemini, anything that can run
a command — you start from what is already known. That is how this project keeps token use
minimal: context is RECALLED, not re-derived.

## Before you change ANYTHING
```
python -m src.project_memory recall "<what you're about to touch>"
```
Examples: `recall "cockpit mode chip"` · `recall "transcript backfill"` · `recall "docs/dashboard.js"`.
You get a compact context pack: the recent episodes touching that area, the files involved,
the WHYs, and the hand-off docs. **Read it and start from there.** If your tool can't run
commands, ask the human to paste the pack.

## After a meaningful change
Log the WHY that git can't see (one line, seconds):
```
python -m src.project_memory log --what "moved mode chip to strip" --why "cockpit h3 was overcrowded" --files "docs/dashboard.js" --by "cursor"
```
Commits and EXCAVA hand-offs are ingested automatically — you only add the intent.

## Where things live (so recall means something to you)
- `EXCAVA_PROGRAM.md` — the plan (phases 0-9). `SESSION_HANDOFF.md` — current state + rules.
- `QUESTIONS.md` — parked owner decisions. `data/excava/` — the OS bus/traces/hand-offs.
- `src/` — pipeline + OS code. `docs/` — the dashboard (bump APP_BUILD + sw.js on change).
- Standing rules: free-only forever · quality over quantity · gate before outward actions.

## Maintenance (automatic)
Every EXCAVA beat runs `ingest` (new commits + bus events → episodes); `rollup` compresses
episodes older than 90 days into monthly digests, so the ledger stays small forever.
