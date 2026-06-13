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
- **Single-tab guarantee** (`src/cross_tab_check.py`): a name/slug must live in exactly ONE tab. Matches on **slug** (not display name) so it catches mismatched names; keeps the genuine skill, removes the duplicate tool (reversible backup in `data/_removed_cross_tab.json`); frozen/starred never touched. Runs every `bulk_analyze` cycle → self-heals. Audit in `data/cross_tab_conflicts.json`.
- **Live knowledge graph** in the dashboard's **Dev Construction** tab: `src/build_graph.py` → `data/brain_graph.json` (force-directed canvas graph, pan/zoom/drag/hover/click-to-open), regenerated each `bulk_analyze` cycle. It mirrors the Obsidian vault's links (the desktop Obsidian graph remains the full-detail view).

## PHASE 1 — GET THE OUTPUT OUT (this is ~90% of the value; do it FIRST)
The whole system is starved: only ~95 of 1,257 videos (7.5%) have a real transcript, and you
CANNOT extract skills/tools from a description. Everything downstream is blocked on this. So:
1. **Drain transcripts — the single highest lever.** `transcribe.yml` is every 2h / bigger
   batches; VERIFY via `gh` logs that it's actually producing transcripts (read a transcribe run
   end-to-end). If cloud Whisper/caption-backfill is throttled, make it aggressive (parallel
   matrix of jobs, higher `--limit`) and/or run the local residential backfill. Goal: get most
   of the 1,160 caption-less videos transcribed in days, not weeks.
2. **Speed the free analysis lane (≈3×).** Add `OPENROUTER_API_KEY` (free DeepSeek) +
   `GROQ_API_KEY`; re-check the `CEREBRAS_API_KEY` (403 = account/key, owner must verify). The
   pool auto-uses whatever's present. More engines = the backlog of transcripts gets analyzed
   into skills/tools faster. This is where the 10× more data comes from.
3. **A TINY progress readout only** (for visibility, NOT the full self-improvement): a small
   script/step that writes counts to `health.json` — `transcripts X/1257, skills Y, tools Z` —
   so the owner can watch it climb. Keep it minimal; the real self-improvement is Phase 2.

## PHASE 2 — REFINE (only once MOST of the info is extracted)
4. **Fix self-improve.** `improve.yml` runs but its Claude step does nothing (no `health.json`,
   no `improvement_audit.json`, `self_check.json` frozen). Write **`src/self_check.py`**
   (mechanical 50-question check) + curation on its own schedule, independent of the
   token-starved Claude step. (Pointless before there's a full library to curate.)
5. **SKILL.md → Desktop + brain refresh.** Packages are in the repo; the Desktop
   `claude skills of eitan` folder + the Obsidian vault only refresh when the owner runs
   `sync/sync-skills.ps1` / `python -m src.build_brain "<vault>"`. Optionally wire both into the
   local sync. Keep the brain graph fully connected (0 orphans).
6. **Comment-gated resolver.** `DISCOVER.md` Step 2 resolves "comment X to get it" resources via
   PUBLIC search (no bot — ToS). `data/comment_gated.json` is still empty (few videos analyzed);
   once it fills, run the resolver and MEASURE the real recovery % (estimate ~50%, higher for
   named repos/tools, ~0% for DM-only).
7. **Optional, owner-gated:** channel auto-add to the YouTube playlist (`src/oauth_setup.py` →
   `YOUTUBE_OAUTH_CLIENT_ID/SECRET/REFRESH_TOKEN` secrets → `add_to_playlist.py`); the formal
   developer-build 2-part Markdown spec (the dashboard's **Dev Construction** tab already has the
   substance — export it if the owner wants the file).

## Constraints (always)
Free only (public Actions + Pro subscription token + free tiers, graceful-skip). Owner is on **Claude Pro ($20)** = tiny weekly bucket → heavy Claude is night-gated (Israel 01:00-07:00) and most analysis is offloaded to the free lane. Never commit secrets / `make_icon.py` / `.claude/`. Push automatically. Never touch frozen/starred records. NEVER build a YouTube comment bot (ToS/ban).

---

## PASTE THIS INTO THE NEXT SESSION:
```
Use C:\Users\eitan\AI-YouTube-Skills . Read NEXT_SESSION.md and SESSION_HANDOFF.md in full,
then continue Excavatortron. gh is installed at "/c/Program Files/GitHub CLI/gh.exe" — use it to
read Actions logs and verify what's ACTUALLY running before changing anything.

THE PRIORITY IS OUTPUT, NOT SELF-IMPROVEMENT. The library is starved (~7.5% of videos have a
transcript), so almost nothing has been extracted yet. Do Phase 1 first and don't move on until
most of the information is actually out:
  1. Get transcripts draining fast (verify transcribe.yml is producing them; make it more
     aggressive/parallel if throttled).
  2. Speed the FREE analysis lane so the transcripts turn into skills/tools fast (add the free
     OpenRouter/Groq keys; the pool auto-uses them).
  3. Add only a tiny health.json progress readout (counts) so I can watch it climb.
Only AFTER most of the data is extracted, do Phase 2 (fix self-improve via src/self_check.py,
etc.). Free engines only; honor the Pro-budget night-gating; NEVER build a YouTube comment bot.
Show me real evidence (gh logs + climbing counts), commit and push each change.
```
