# Excavatortron — Next-Session Handoff (as of 2026-06-14)

> **SESSION 2026-06-14 — big expansion shipped (owner directive). Done + pushed:**
> - **Security review + hardening**: repo is PUBLIC; `claude.yml` now requires a trusted
>   `author_association` (defense-in-depth). Cloud has zero PC access; secrets only in Actions;
>   3rd-party data flows are public-only. Added a recurring security check to the self-improve loop
>   (`IMPROVE.md` Module 12 + `REVIEW.md` `security_and_privacy` dimension + config).
> - **NEW Effectiveness tab + `src/effectiveness.py`**: scores every retrieval/analysis lane
>   (quality/quantity/form/time/tokens/ease_external/ease_project/ease_user + rigidity) →
>   `data/effectiveness.json`, recomputed each cycle; self-improve targets the weakest lanes
>   (`IMPROVE.md` Module 10). Recurring weak dim = **ease_external** → north-star task: build a
>   machine-readable hub index/API for external systems (NOT built yet — top queued item).
> - **Self-improve priorities encoded** (`config.self_improvement`): north_star (hub goal),
>   priorities_top3 (effectiveness, professional **design top-3**, use-info-to-improve-skills),
>   + Modules 10–13 in `IMPROVE.md`.
> - **Dashboard**: per-tab "• Updates:" cadence line; Quick-read now really summarizes (first
>   sentence/~24 words, not just CSS clamp); sw cache v12. (Browser preview harness here is
>   sandboxed away from the repo — verified via node syntax + functional tests, not a live browser.)
> - **Brain granularity**: tools now cluster by **Vendor** + every Category/Tool/Vendor hub LISTS
>   its members, so specific tools are reachable from the centre (`src/build_brain.py`).
> - **Dev tab**: +3 precise technical sections (transcript reality, effectiveness internals,
>   security model). It's still a STATIC `data/dev_construction.json` — an **auto-generator is queued**.
> - Move-off-PC: decided — the repo is 33 MB & already cloud; **keep the tiny local clone** for
>   session draining. His PC can't stay on, so bulk transcript recovery = drain during sessions.
>
> **QUEUED (next sessions):** (1) build the public **hub index/API** (ease_external, north star);
> (2) a **dev-doc auto-generator** (always-current technical doc from real code/crons/schemas);
> (3) the **exhaustive every-file review** the owner asked for; (4) first real pass of self-improve
> Modules 10–13 runs on the weekly improve. **Owner TODO unchanged:** add the 4 free secrets.

# Excavatortron — Next-Session Handoff (as of 2026-06-13)

> **⚠ SESSION 2026-06-13 — verified reality via `gh` Actions logs (READ THIS FIRST):**
> - The cloud **`transcribe.yml` produces EXACTLY 0 transcripts** — YouTube hard-blocks BOTH the
>   caption API AND yt-dlp audio from GitHub's datacenter IP. It is **NOT throttling**; do NOT
>   "make it more parallel" (old advice — it's wrong). Already cut to a daily safety-net.
> - The **only fast free lever is the RESIDENTIAL backfill** (`src/backfill_transcripts.py`) from
>   Eitan's home IP. A random sample shows **~85–88% of the 1,112 caption-less videos DO have an
>   English caption** fetchable from home. **But his PC can't be left on**, so the nightly runner
>   isn't viable — the model is: **drain at the START of every session** (gentle, block-aware);
>   the cloud free lane analyzes 24/7. See `[[feedback-excavatortron-drain-every-session]]`.
> - **DON'T BURST**: YouTube's rate-limit ESCALATES; fast batches lock the IP out. Start
>   `--sleep ~2.0`, small `--limit`, single pass, stop on first block. (Bursting cost the rest of
>   the day's headroom on 2026-06-13.)
> - **Proven chain:** drained 50 → free pool produced **+33 skills, +20 tools, +4 prompts**, 0
>   Claude tokens. Counts now: transcripts **145/1257 (11.5%)**, skills **204**, tools **308**,
>   connectors 44, prompts 19. Watch the new `data/health.json` climb.
> - **Unattended PC-free path wired:** `src/supadata_fetch.py` (Step 0 of `transcribe.yml`,
>   graceful-skip) — Supadata free tier (~100/mo) fetches on their infra. Needs `SUPADATA_API_KEY`.
> - **Owner TODO (only Eitan can):** add free secrets `OPENROUTER_API_KEY`, `GROQ_API_KEY`
>   (analysis pool 2→4 engines), re-check `CEREBRAS_API_KEY` (dead, returns 0), optional
>   `SUPADATA_API_KEY`. Run `gh secret set <NAME>` in the repo.

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
  1. Drain transcripts FIRST thing (the cloud transcribe.yml is hard-IP-blocked and produces 0 —
     do NOT make it more parallel). Run the RESIDENTIAL backfill gently from this PC:
     `python -m src.backfill_transcripts --limit 150 --sleep 2.0` (block-aware; never burst).
  2. Speed the FREE analysis lane so the transcripts turn into skills/tools fast (add the free
     OpenRouter/Groq keys; the pool auto-uses them).
  3. Add only a tiny health.json progress readout (counts) so I can watch it climb.
Only AFTER most of the data is extracted, do Phase 2 (fix self-improve via src/self_check.py,
etc.). Free engines only; honor the Pro-budget night-gating; NEVER build a YouTube comment bot.
Show me real evidence (gh logs + climbing counts), commit and push each change.
```
