---
tags: [protocols, systems, reference]
aliases: [Protocols, Systems, Systems and Protocols]
---

# Systems & Protocols

Every system and protocol in Excavatortron in one place — so nothing is forgotten. Part of
[[Excavatortron Brain]]. (The pipeline basics live in [[Architecture]] / the `Pipeline - *` notes;
this note captures the **full** set, including the newer protocols.)

## Transcript acquisition (the #1 hard problem)
- **Datacenter-IP block.** YouTube hard-blocks GitHub Actions (datacenter IP) for BOTH the caption
  API and `yt-dlp` audio. The cloud `transcribe.yml` produced exactly 0 — verified in Actions logs.
  It is NOT throttling; do not "parallelise" it.
- **Supadata (cloud, UNATTENDED) — the autonomy baseline.** `src/supadata_fetch.py` fetches captions
  on Supadata's infra (`/v1/youtube/transcript`, `mode=native`, browser User-Agent to clear
  Cloudflare 1010), so no datacenter block. `transcribe.yml` runs it daily, `--limit 3` to stay in
  the ~100/month free tier. **No PC required.** Dead videos (404) recorded in `data/dead_videos.json`
  and never retried, to protect the quota.
- **Residential backfill — the optional turbo.** `src/backfill_transcripts.py` from a home IP
  recovers ~85% of caption-less videos fast + translates foreign captions. YouTube's rate-limit
  ESCALATES on bursts, so the script raises `RateLimited` and STOPS (`--sleep ≥1.5`, never burst).
  Run during a session; not required for autonomy.

## Analysis lanes (transcripts -> skills/tools/connectors/prompts/commands)
- **Free engine pool** (`src/bulk_analyze.py`, `bulk_analyze.yml`, every 3h): rotates over the free
  engines you have keys for — quotas ADD UP, the pool auto-drops any that error 3× in a row. Verified
  working: **GitHub Models (gpt-4.1-mini), Groq (llama-3.3-70b), Gemini**; OpenRouter/Cerebras
  config'd. Browser User-Agent on every call (Groq/Cerebras/OpenRouter sit behind Cloudflare).
  **Zero Claude-Pro tokens.**
- **Claude deep lane** (`analyze.yml`): highest quality but **night-gated** to Israel 01:00–07:00 to
  protect the small Pro budget — reserved for curation/self-improve, not bulk.

## External (non-playlist) acquisition
- **Web news** (`src/news.py`, `news.yml`, every 6h): **83 RSS sources** across labs, research
  (arXiv/BAIR/MIT/Microsoft/Apple), community (Reddit/Hacker News) and top analysts. Dead feeds
  auto-prune via `feeds_health.json`.
- **Tool discovery** (`discover.yml`, Sun/Tue/Thu) and **channel/source suggestion**
  (`src/suggest_channels.py`, daily → Grow Sources tab).

## The hub (machine-readable, for external/future systems)
- **`data/hub.json`** (`src/build_hub_index.py`) — a versioned manifest of every dataset (public URL,
  count, fields). GitHub Pages serves the repo root with `Access-Control-Allow-Origin: *`, so any
  program can fetch the whole library from one URL, no key. Documented in `HUB_API.md`.
- **Models mirror** (`src/build_models.py`): the AI models subset of tools → `data/models.json`,
  ranked, name+version-deduped.

## Activation (use the catalogue, don't copy-paste) — the north-star layer
- **Activator skill** (`skills/excavatortron-activator/`): an Agent Skill that FINDS the best
  skill/tool/connector for a task (`find.py`, over local data or the public hub) and ACTIVATES it
  (`activate.py`): installs a SKILL.md into `~/.claude/skills/`, emits the MCP `mcpServers` config /
  `claude mcp add`, or a tool-specific deploy block for any non-Claude tool. Verified: an installed
  SKILL.md was picked up live by Claude Code.
- **Dashboard "⌁ Use this skill"**: per-skill deploy steps + one-click ready-to-paste block (and the
  same for connectors → MCP config).

## Self-improvement
- **Mechanical self-check** (`src/self_check.py`): answers the 50 reference questions by INSPECTING
  the data (no Claude) every cycle → `data/self_check.json`; queues each "no" into
  `data/improvement_tasks.json`. Currently 49/50. This un-froze the loop (it was stale).
- **Effectiveness scoreboard** (`src/effectiveness.py` → `data/effectiveness.json`, Effectiveness
  tab): scores each retrieval/analysis lane on quality/quantity/form/time/tokens/ease-of-access(×3)
  + rigidity; the self-improve pass targets the weakest lanes (`IMPROVE.md` Modules 10–13:
  effectiveness, professional design [top-3], security/privacy, improve-existing-skills).
- **3-agent review** (`REVIEW.md`, `review.yml`, weekly): usability, professional_design,
  security_and_privacy, cut_the_bullshit, deep_code_bugs → `data/review_findings.json`; + CodeQL.
- **Dynamic tabs** ([[Dynamic Tabs]]), **stars/freezing** ([[Stars and Freezing]]), dedup/merge
  (`merge_dupes.py`, `merge_log.json`).

## Security & data-privacy
- Repo is **PUBLIC**. The `@claude` workflow requires a trusted `author_association`
  (OWNER/MEMBER/COLLABORATOR) — a stranger's comment can't start a runner. Scheduled workflows are
  least-privilege; CodeQL is read-only. Secrets live ONLY in GitHub Actions (encrypted). Third-party
  engines/Supadata receive PUBLIC YouTube content only (no PII). `self_check` Q44 scans data/+docs
  for leaked keys every cycle.

## Visibility & UX
- Health readout (`src/health.py` → `data/health.json`), per-tab "Updates:" cadence line, real
  Quick-read (first-sentence summarise), header leads with the hub's SCALE, knowledge graph
  (black/white professional), dev-doc auto-generator (`src/build_dev_doc.py`).

## Constraints (always)
Free only; no babysitting; never commit secrets / `make_icon.py` / `.claude/`; push automatically;
never touch frozen/starred records; output English; never edit the source transcript; NEVER build a
YouTube comment bot. See [[Standing Constraints]] and [[Locked Decisions]].
