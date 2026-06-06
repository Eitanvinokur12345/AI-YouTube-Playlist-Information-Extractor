---
tags: [home, moc]
aliases: [Home, Index, MOC]
---

# Excavatortron Brain

**Excavatortron** is a self-running, self-improving dashboard that mines a YouTube
playlist of AI videos and turns everything it finds — techniques, tools, models,
MCP connectors, slash commands, tips, and news — into a clean, searchable web
dashboard. It runs in the cloud for free and improves itself on a schedule, with
**no babysitting and no new paid cost**.

> Core promise: the owner shouldn't have to intervene, and shouldn't have to pay
> anything beyond what they already have (a Claude Pro/Max subscription + free
> public-repo GitHub Actions + free external API tiers).

## Start here
- [[Architecture]] — the cloud pipeline and how the stages connect.
- [[Skills vs Tools]] — the #1 content rule (techniques vs products are separate).
- [[Tabs]] — what each dashboard tab shows and which data file feeds it.
- [[Operations and Setup]] — tokens, secrets, running it, renewing the yearly token.

## The pipeline (map of content)
1. [[Pipeline - Fetch]] — pull new videos + transcripts from the playlist.
2. [[Pipeline - Analyze]] — Claude reads each video and extracts structured data.
3. [[Pipeline - News]] — build the news feeds (video-derived + web).
4. [[Pipeline - Improve]] — the weekly **deep pass**: tidy, calibrate, self-check.
5. [[Pipeline - Review]] — the 3-agent quality gate (see [[Three-Agent Review]]).

## The engines (authoritative specs)
- [[Engines]] — `CLAUDE.md`, `IMPROVE.md`, `REVIEW.md`, `REFERENCE_SPEC.md`.

## Key systems
- [[Cadence]] — high-frequency ingest + one weekly deep pass at night Israel time.
- [[Dynamic Tabs]] — the dashboard grows new tabs from recurring anecdotes.
- [[Reference Self-Check]] — the 50-question loop that keeps us true to the original spec.
- [[Three-Agent Review]] — Claude first, then an external engine, plus CodeQL.
- [[Self-Improvement Loop]] — how the system curates and proposes changes safely.
- [[Stars and Freezing]] — proven records are frozen and never auto-changed.

## Reference
- [[Data Files]] — every `data/*.json` and what it's for.
- [[Config Reference]] — the important `config.json` blocks.
- [[Glossary]] — terms in one place.
- [[Obsidian Access (MCP)]] — how to let Claude read/write this vault.

---
*This vault is committed inside the repo at `brain/`. A copy can be mirrored to the
Desktop by the local runner (see [[Operations and Setup]]).*
