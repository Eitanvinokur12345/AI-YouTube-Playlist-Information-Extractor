---
tags: [system, dynamic-tabs, dashboard]
aliases: [Dynamic Tabs, Dynamic Tab Discovery]
---

# Dynamic Tabs

Instead of a fixed "Trends" tab, the dashboard **grows new tabs** from recurring themes the
videos reveal (a [[Locked Decisions|locked decision]]). This is how the project notices a
rising topic (AI robotics, mental-health apps, data-center infra…) without us hard-coding it.

## How it works
1. **Capture** — [[Pipeline - Analyze]] (CLAUDE.md Step 8b) notices off-tab anecdotes and
   appends them to `data/tab_candidates.json` as
   `{theme, label, note, video_id, source_url, ts}`.
2. **Cluster & promote** — [[Pipeline - Improve]] Step 7 groups candidates by theme. When a
   theme has **≥ `dynamic_tabs.min_evidence_videos`** (default 5) distinct videos, it is
   promoted to `data/extra_tabs.json` with `created_at`, `badge_until`
   (= `created_at` + `new_badge_days`, default 7), and a `description` built from the
   anecdotes. Capped at `max_total_active` (6).
3. **Render** — the dashboard renders extra tabs generically, each with a **NEW badge** that
   **auto-expires** (`tabIsNew()` honours `badge_until`, falling back to created_at + 7d).

## Current state
`tab_candidates.json` has captured several themes, but the largest cluster so far is only ~2
videos — below the threshold of 5 — so `extra_tabs.json` is correctly still empty. A tab
appears once a theme earns enough independent evidence.

## Config
`config.self_improvement.dynamic_tabs`: `enabled`, `autonomy: auto_create_and_announce`,
`min_evidence_videos`, `max_total_active`, `new_badge_days`, `candidates_file`,
`reserved_tab_ids` (the built-in tabs that can't be shadowed). See [[Config Reference]] and
[[Data Files]].
