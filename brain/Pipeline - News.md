---
tags: [pipeline, news]
aliases: [News, News Stage, News Feed]
---

# Pipeline — News

Builds the **News tab** in three time windows: daily (last 24h), weekly (last 7d), monthly
(last 30d). Two sources feed it.

## 1. Video-derived news (from the playlist)
`src/fetch.py` → `classify_news()` buckets every playlist video by its publish date relative
to run time (24h / 7d / 30d; older than 30d is dropped), sorts newest→oldest, and writes
`daily_news.json` / `weekly_news.json` / `monthly_news.json`. Each file has a `header`
(`run_time`, `window`, `covered_from`, `covered_to`) and `entries`. Existing summaries are
preserved across runs.

## 2. Web news (from official sources)
`src/news.py` (workflow `news.yml`) pulls ~50 RSS/Atom feeds listed in `config.news_sources`
(OpenAI, DeepMind, Google, HF, arXiv, The Decoder, …). It writes the `*_web` companions and a
rolling `web_news_store.json`, and records per-feed reliability in `feeds_health.json`
(a `fail_streak` per feed; [[Pipeline - Improve]] Step 7b proposes dropping dead feeds).

## Rules
- **Verbatim summaries** (`config.news.summary_mode: "verbatim"`), capped length.
- News and skills are **separate outputs** — a news item is not auto-turned into a skill
  unless it also contains skill content (that's [[Pipeline - Analyze]]'s job).
- Everything is free: public Actions + standard HTTP, no paid API.

## Output
`data/daily_news.json`, `weekly_news.json`, `monthly_news.json` (+ `_web` variants),
`web_news_store.json`, `feeds_health.json`. Rendered by the News tab (see [[Tabs]]).
