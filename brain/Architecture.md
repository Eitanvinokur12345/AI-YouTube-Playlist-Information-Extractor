---
tags: [architecture]
---

# Architecture

Excavatortron is a **cloud pipeline** built entirely on GitHub Actions, plus an
optional **local runner** for the one step that needs a residential IP (fetching
from YouTube). Everything the user sees is a static dashboard served by GitHub Pages.

## The big picture

```
YouTube playlist
      │  (local runner OR cloud, see below)
      ▼
[ fetch ]  → data/_pending/*.json        (one file per new video + transcript)
      │
      ▼
[ analyze ] → skills/tools/models/...     (Claude reads CLAUDE.md, extracts data)
      │        commits + pushes after EACH video
      ▼
[ news ]   → daily/weekly/monthly feeds   (video-derived + web)
      │
      ▼
[ improve ] → tidy, calibrate, self-check (weekly DEEP PASS, reads IMPROVE.md)
      │
      ▼
[ review ] → review_findings.json         (3 agents, reads REVIEW.md)
      │
      ▼
docs/  ──► GitHub Pages ──► the live dashboard (vanilla JS, reads ../data/*.json)
```

Each stage is a separate workflow in `.github/workflows/`. They never share a run;
GitHub concurrency groups keep them from overlapping or fighting over the git tree.

## The stages
- [[Pipeline - Fetch]] (`fetch.yml`, `src/fetch.py`) — needs `YOUTUBE_API_KEY`.
- [[Pipeline - Analyze]] (`analyze.yml`, `CLAUDE.md`) — the extraction brain.
- [[Pipeline - News]] (`news.yml`, `src/news.py`) — the news feeds.
- [[Pipeline - Improve]] (`improve.yml`, `IMPROVE.md`) — the weekly deep pass.
- [[Pipeline - Review]] (`review.yml`, `REVIEW.md`) + CodeQL (`codeql.yml`).

## Why this shape
- **Free.** Public-repo GitHub Actions are free; analysis/curation/review use the
  Claude **Pro/Max subscription token** (`CLAUDE_CODE_OAUTH_TOKEN_REAL`), not paid
  API billing. The external reviewer uses a **free tier** and skips gracefully if
  absent. See [[Operations and Setup]].
- **Crash-safe.** Analyze commits + pushes after **each** video, so an interrupted
  run never loses work; the next run picks up the remainder.
- **Self-healing.** [[Cadence|Catch-up mode]] drains big bursts of new videos; the
  [[Self-Improvement Loop]] fixes drift; the [[Reference Self-Check]] keeps us
  matched to the original spec; the [[Three-Agent Review]] catches regressions.

## The "live" specs vs. dead code
The Markdown engine files are what actually run in the cloud (Claude reads them).
Some Python files (`src/process_video.py`, `src/analyze_batch.py`) are **legacy/dead
code** kept for reference — the live analysis is driven by `CLAUDE.md`. See [[Engines]].

## Local vs cloud fetch
Fetching from YouTube can be rate-limited or blocked from datacenter IPs. The
**local runner** (Windows Task Scheduler, see [[Operations and Setup]]) runs
`python -m src.fetch` from a residential IP, commits the new `data/_pending/*`
files, and pushes — then the cloud takes over from analyze onward.

## Related
- [[Data Files]] · [[Config Reference]] · [[Tabs]]
