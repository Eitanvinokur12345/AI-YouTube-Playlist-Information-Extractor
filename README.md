# YouTube AI Skills Tracker

Automated tracker that pulls videos from a YouTube playlist and maintains five
"tabs" of data: a Skills Library, a Models Ranking, an Improvement/merge log,
a Tips & Commands library, and a News Feed. Runs on a schedule via GitHub
Actions and publishes a dashboard via GitHub Pages.

## How it works
1. **GitHub Actions** runs the pipeline every 48h (`.github/workflows/pipeline.yml`).
2. `src/fetch.py` calls the YouTube Data API + transcripts (deterministic).
3. The **Claude Code GitHub Action** analyzes the new videos and updates all
   tabs, using a Pro/Max subscription token (no separate API billing).
4. Results are committed to `data/` and `skills/`, and the **GitHub Pages**
   dashboard in `docs/` renders them.

## Configuration
Edit `config.json` — playlist ID, paths, timezone, etc. All output goes to
`./data` and `./skills` by default. On a Windows machine you can point
`paths` at your OneDrive folders instead.

## Secrets (set in GitHub → Settings → Secrets and variables → Actions)
- `YOUTUBE_API_KEY` — YouTube Data API v3 key.
- `CLAUDE_CODE_OAUTH_TOKEN` — from `claude setup-token` (Pro/Max), OR use
  `ANTHROPIC_API_KEY` instead if you prefer pay-as-you-go API analysis.

Never commit real keys. `.env` is gitignored; `.env.example` documents the names.

See `PIPELINE.md` for the full per-tab specification.
