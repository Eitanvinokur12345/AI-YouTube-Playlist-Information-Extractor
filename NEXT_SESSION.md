# Excavatortron — Next-Session Handoff (as of 2026-06-11)

> Paste the prompt at the bottom into a fresh session. The project lives locally at
> `C:\Users\eitan\AI-YouTube-Skills` (a git clone of GitHub `Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor`).
> **Nothing to upload** — a Claude Code session in this environment already has the repo on disk.
> Read `SESSION_HANDOFF.md` (full architecture) + the dashboard's **Dev Construction** tab.

## What is already true (don't redo)
- The cloud pipeline runs autonomously: **12 workflows active, 0 failures.** `gh` CLI is installed + authed (use it to read Actions logs / trigger runs: `"/c/Program Files/GitHub CLI/gh.exe"`).
- **Free analysis lane WORKS** (`bulk_analyze.yml`, `gpt-4.1-mini` via GitHub Models) — extracts clean, specific records, ZERO Claude-Pro tokens. Pool auto-skips dead engines.
- Counts (climbing): ~171 skills, ~290 tools, 15 prompts, 42 connectors.
- The free lane now **writes SKILL.md packages** (`skills/<slug>/`, `other-skills/<tool>/<slug>/`).
- **Obsidian brain** generated at `C:\Users\eitan\OneDrive\Documents\Excavatortron obsidian brain\Excavatortorn` (~573 notes, verified **0 orphans** — every note links to a category/tool/Connectors hub → Home → project notes). Regenerate with `python -m src.build_brain "<vault path>"`. **Always keep the graph fully connected (no orphan nodes); if you add a note type, give it a hub link.**
- Secrets set in GitHub: `YOUTUBE_API_KEY`, `CLAUDE_CODE_OAUTH_TOKEN_REAL` (Pro), `EXTERNAL_REVIEW_API_KEY` (Gemini), `GH_MODELS_TOKEN` (works). Optional/unset: `CEREBRAS_API_KEY` (403 — owner must re-check), `OPENROUTER_API_KEY`, `GROQ_API_KEY`.

## The real problems to fix (in priority order)
1. **TRANSCRIPTS — the root cause of "everything is ~10× too low".** Only ~95 of 1,257 videos (7.5%) have a real transcript; the rest are description-only, and you CANNOT extract skills from a description. `transcribe.yml` was bumped to every 2h / bigger batches to drain the ~1,160-video backlog (~2-3 days). VERIFY it's actually producing transcripts (read the transcribe run logs); if cloud Whisper/caption-backfill is throttled, make it more aggressive (matrix/parallel) or run local backfill.
2. **SELF-IMPROVE IS BROKEN.** `improve.yml` runs but its Claude step does nothing ("nothing to commit") — no `health.json`, no `improvement_audit.json`, `self_check.json` frozen at a manual seed. FIX: write a plain **`src/self_check.py`** (mechanical 50-question check + `health.json`) on its own schedule so the self-improvement loop produces VISIBLE output regardless of the token-starved Claude step.
3. **SKILL.md → Desktop.** Packages are in the repo, but the owner's Desktop `claude skills of eitan` folder only updates when `sync/sync-skills.ps1` runs (he hasn't enabled the local runner). Either he runs it, or note it.
4. **Brain auto-refresh.** `build_brain.py` is manual; optionally wire it into `sync/sync-skills.ps1` so the vault refreshes locally.
5. **Comment-gated resolver.** `DISCOVER.md` Step 2 resolves "comment X to get it" resources via PUBLIC search (no bot — ToS). Measure the real recovery % on `data/comment_gated.json`.
6. **Speed:** add `OPENROUTER_API_KEY` (free DeepSeek) + `GROQ_API_KEY` to ~3× the free lane.

## Constraints (always)
Free only (public Actions + Pro subscription token + free tiers, graceful-skip). Owner is on **Claude Pro ($20)** = tiny weekly bucket → heavy Claude is night-gated (Israel 01:00-07:00) and most analysis is offloaded to the free lane. Never commit secrets / `make_icon.py` / `.claude/`. Push automatically. Never touch frozen/starred records. NEVER build a YouTube comment bot (ToS/ban).

---

## PASTE THIS INTO THE NEXT SESSION:
```
Use C:\Users\eitan\AI-YouTube-Skills . Read NEXT_SESSION.md and SESSION_HANDOFF.md in full,
then continue Excavatortron. gh is installed at "/c/Program Files/GitHub CLI/gh.exe" — use it
to read Actions logs and verify what's actually running before changing anything.
Priorities: (1) confirm transcripts are draining and counts climbing; (2) fix self-improve by
writing src/self_check.py (mechanical self-check + health.json) on its own schedule;
(3) then iterate. Free engines only; honor the Pro-budget night-gating; never build a comment bot.
Show me real evidence (gh logs / counts), commit and push each change.
```
