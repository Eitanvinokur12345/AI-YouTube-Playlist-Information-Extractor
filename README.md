# YouTube AI Skills Tracker

Automated tracker that extracts AI knowledge from a YouTube playlist and maintains **six
tabs** of data: a **Skills Library**, a **Models Ranking** (podium + full table), a
**Skills Improvement / merge log**, a **Tips & Commands** library, a **News Feed**
(daily/weekly/monthly, US-Eastern), and a **Connectors** list (Claude connectors & MCP
servers). The News Feed always **merges two streams**: AI news mentioned in the videos **and**
fresh posts pulled directly from **50 official AI sources** (OpenAI, Google, Anthropic-adjacent
labs, arXiv, etc.) — so it stays current every day even between video runs. Every skill also
carries a **video-quality score**: low-quality source videos are still mined, but their skills
are flagged with a badge, capped in score, and hideable with one toggle. It also **follows
AI-relevant links in video descriptions** (e.g. a GitHub repo full of agents/skills) and folds
those resources into the tabs. It builds in the
cloud (runs even when your PC is off), syncs results to local Desktop folders, and ships a
**searchable** dashboard + a local offline MCP server. A **self-improvement stage** (every ~3
days) then curates the data (dedup, ratings calibration, a health report), can **auto-create a
new tab** when a strong trend emerges, and lets you **star** proven skills to freeze them so
nothing ever changes them.

## How it works
1. **Fetch (cloud, every 48h)** — `.github/workflows/fetch.yml` runs `src/fetch.py`: pulls
   the playlist + transcripts (English → Hebrew → description → title, used verbatim),
   classifies news, and writes `data/_pending/*.json` + `data/status.json`.
2. **Analyze (cloud, every few hours)** — `.github/workflows/analyze.yml` runs the Claude
   Code Action, which follows **`CLAUDE.md`** to fill all six tabs. For every video it first
   computes a **video-quality score** (Step 2b: an AI content review of the transcript +
   a recency adjustment); videos scoring below `low_quality_threshold` (5) are still mined but
   their skills/connectors/news get `low_quality_source:true` and their score is capped.
   It also **follows AI-relevant links** in each description with WebFetch (Step 2c) — a linked
   GitHub repo of agents/skills, a docs site, a tool's homepage — and mines those resources into
   the tabs as independent `linked_resource` records (scored on their own merits, not capped by
   the video). It processes up to 50 videos per run and **commits after every video**, so nothing
   is lost if a run is interrupted; the next run resumes from whatever is left in `data/_pending/`.
   Uses a Pro/Max subscription token — **no separate API billing**.
3. **Web news (cloud, every 12h)** — `.github/workflows/news.yml` runs `src/news.py`: it pulls
   the **50 official AI sources** in `config.news_sources` (public RSS/Atom — **no API keys, no
   tokens, $0**), windows them into daily/weekly/monthly (US-Eastern), and writes
   `data/daily_web_news.json` etc. The dashboard and MCP server **merge** these with the
   video-derived news at display time, so the original files are never clobbered.
4. **Self-improve (cloud, every ~3 days)** — `.github/workflows/improve.yml` runs the Claude
   Code Action following **`IMPROVE.md`**: it auto-applies *safe* fixes (build `index.json`, schema
   repair, exact-duplicate merge, fill missing summaries, cross-tab consistency, write
   `health.json`) and writes *risky* proposals (fuzzy merges, rescores, recategorize, UI
   tweaks, star suggestions, **dropping dead news feeds**) to `data/improvement_suggestions.json`
   for you to approve. It also monitors **news-feed health** — sources that keep failing to fetch
   are proposed for removal once their failure streak crosses the threshold. When a
   strong trend appears across many videos it can **auto-create a new dashboard tab** (logged to
   `data/extra_tabs.json`, announced on the dashboard with a NEW badge; capped per week). It
   **never** changes a **starred/frozen** skill, and **idle-exits cheaply** on days when nothing
   changed. Governed by the `self_improvement` block in `config.json` (cadence, safe-auto vs
   suggest-risky, caps, token budget).
5. **Sync (local)** — `sync/sync-skills.ps1` git-pulls and copies results to your Desktop:
   `skills/` → `claude skills of eitan`, `other-skills/<tool>/` → `<tool> skills of eitan`,
   `data/` → `AI Skills Data`.
6. **View** — the **GitHub Pages** dashboard in `docs/` (Desktop shortcut, also installable to
   your phone or computer home screen as a PWA), or the **offline MCP server** in `mcp_server/`
   queried from Claude Desktop. The dashboard has a header **search box** that filters every tab,
   and shows a **reliability banner** (red if the last analyze run failed — e.g. an expired token;
   amber if the pipeline looks stalled). Star/approve and inspect from the MCP server: `star_skill`,
   `unstar_skill`, `list_suggestions`, `approve_suggestion`, `dismiss_suggestion`,
   `list_dynamic_tabs`, `dismiss_dynamic_tab`, `catch_up_status`, `set_catch_up`,
   `news_feed_health`, `pipeline_status`, `run_improve`.

## First-time setup
1. **Secrets** (repo → Settings → Secrets and variables → Actions):
   - `YOUTUBE_API_KEY` — YouTube Data API v3 key.
   - `CLAUDE_CODE_OAUTH_TOKEN_REAL` — from `claude setup-token` (Pro/Max). Expires ~yearly.
2. **GitHub Pages**: Settings → Pages → Deploy from branch → `main` → `/ (root)`. The
   dashboard then lives at `…github.io/<repo>/docs/`.
3. **Local sync**: run `sync/setup-sync.ps1` once (clones repo, registers a daily sync task,
   creates the Desktop "AI Skills Dashboard" shortcut).
4. **MCP server** (offline querying): `pip install -r mcp_server/requirements.txt`, then add
   the block from `mcp_server/claude_desktop_config.example.json` to your Claude Desktop
   config and restart it.
5. **(Optional) one-click force-run + starring/approvals** from the MCP server: create a
   fine-grained GitHub token and set it as `GITHUB_PAT` in the MCP env. Give it *Actions:
   Read and write* (for force-run) and *Contents: Read and write* (so `star_skill` /
   `approve_suggestion` can commit `data/stars.json` / `data/approvals.json`). Without it,
   querying still works fully offline; only these write/trigger actions need it.

## Massive additions (catch-up mode)
If you dump a large batch of videos in at once — e.g. you merge another playlist into your
tracked one — Excavatortron handles it automatically, like a fresh first run:
- **Trigger:** when a single fetch finds **100+** new videos (`catch_up.surge_threshold`), it
  flips `data/catch_up.json` to active. You can also force it with the MCP tool
  `set_catch_up('on')` / `set_catch_up('off')` (`'auto'` restores automatic behavior).
- **Sprint:** the analyze workflow switches to a large batch and a **`*/30` cron** that runs
  back-to-back (newest videos first) until the backlog clears, then **auto-returns to normal**.
  All free — public-repo Actions are unlimited and analysis uses your subscription token.
- **Light curation meanwhile:** while catching up, the daily self-improvement run does only
  cheap, safe fixes and defers dedup/rescore/stars/trend-tabs until the backlog is gone, so it
  never curates half-ingested data.
- **Visibility:** the dashboard shows a blue "⛏️ CATCHING UP — N still to analyze" banner; the
  MCP tool `catch_up_status` reports the same. No action needed from you.

## The only recurring task
The Claude login token (`CLAUDE_CODE_OAUTH_TOKEN_REAL`) expires about **once a year**. When
analysis starts failing with an auth error, run `claude setup-token` and paste the new value
into that secret. The dashboard shows a prominent reminder with these steps.

## Configuration
Edit `config.json` — playlist ID, `transcript_languages` (`["en","he"]`), timezone,
`run_interval_hours` (48), `analyze_batch_size` (50), categories, tip topics. Newer blocks:
`news_sources` (the 50 official feeds), `link_following` (follow AI-relevant description links —
max links/video, per-resource cap, host denylist), `video_quality` (scale, `low_quality_threshold`,
recency penalties, `downweight_and_flag` action), `self_improvement.cadence` (`every_3_days`),
`self_improvement.feed_health.fail_streak_threshold` (when to suggest dropping a dead feed), and
`self_improvement.dynamic_tabs` (auto-create-and-announce trend tabs, min evidence videos, weekly cap).

Never commit real keys. `.env`, `*.key` are gitignored.

See `PIPELINE.md` for the architecture, `CLAUDE.md` for the exact per-tab analysis spec, and
`IMPROVE.md` for the self-improvement protocol.
