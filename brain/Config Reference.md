---
tags: [reference, config]
aliases: [Config Reference, config.json]
---

# Config Reference

The important blocks in **`config.json`** (the central knobs). Engines read this first and obey
it. See also [[Data Files]] and [[Cadence]].

## Core
- `playlist_id` — the source playlist.
- `transcript_languages` `["en","he"]`, `output_language` `"en"` (output is always English;
  the source transcript is never edited — a [[Standing Constraints|constraint]]).
- `rate_limit_seconds` 0.5 — pause between videos.
- `categories` (14) and `general_tip_topics` (7) — the approved vocabularies.

## extraction  *(updated)*
`exhaustive: true`, `transcript_chars: 80000`, **`capture_stats`**, **`capture_comments`**,
**`max_comments: 15`**, `capture_tab_candidates`. "Everything the video AND its surroundings
offer" — transcript + full description + links + stats + tags + duration + top comments. See
[[Pipeline - Fetch]] and [[Pipeline - Analyze]].

## link_following
`enabled`, `max_links_per_video: 3`, `max_items_per_resource: 15`, `denylist_domains`
(social/store/donation). Feeds [[Pipeline - Analyze]] Step 2c.

## catch_up
`surge_threshold: 100`, `batch_size: 1000`, `order: newest_first`, `frequent_cron */30`.
Auto-activates on a big burst, drains newest-first, auto-returns. See [[Cadence]].

## self_improvement
`autonomy: safe_auto_suggest_risky`, `modules{…}`, `safe_auto[]` vs `suggest_only[]`,
`caps{}`, `token_budget_per_run`, `stars{}`, `dynamic_tabs{}`. Drives [[Pipeline - Improve]],
[[Stars and Freezing]], [[Dynamic Tabs]].

## reference_self_check
`spec_path: docs/REFERENCE_SPEC.md`, `questions: 50`, `results_file`, `tasks_file`,
`auto_fix_next_run: true`. Drives [[Reference Self-Check]].

## review
`dimensions: [usability, cut_the_bullshit, deep_code_bugs]`, `claude_first_then_external`,
`usability.competitors`, `external_engine{gemini, secret_name, graceful_skip}`,
`first_week_intensive`. Drives [[Three-Agent Review]].

## cadence
`mode: high_freq_plus_weekly_deep`, `weekly_deep_pass{}`, `first_week{started_at}`,
`throughput_target{100 videos / 48h}`. See [[Cadence]].

## video_quality, news, news_sources
Source-quality scoring (Step 2b), news windows + verbatim summaries, and the ~50 RSS feeds for
[[Pipeline - News]].
