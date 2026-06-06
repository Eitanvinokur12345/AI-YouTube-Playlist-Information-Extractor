---
tags: [dashboard, content]
---

# Tabs

The dashboard (`docs/index.html` + `docs/dashboard.js`) is a vanilla-JS single page.
The nav bar has these **core tabs**, plus any auto-created [[Dynamic Tabs]].

| Tab | Data file | Shows |
|-----|-----------|-------|
| **Skills Library** | `data/skills.json` | Techniques you can apply ([[Skills vs Tools|skills]]), starrable/frozen. |
| **Tools** | `data/tools.json` | Products/apps/services, with a "mentioned N×" popularity badge. |
| **Models Ranking** | `data/models.json` | The model podium 🥇🥈🥉 (a subset of tools). |
| **Improvement Log** | `data/improvement_*` | What the system changed over time. |
| **Tips & Commands** | `data/tips.json`, `data/commands.json` | Curated tips + slash commands. |
| **News Feed** | `data/*_news.json` | Daily/weekly/monthly news (video-derived + web). |
| **Connectors** | `data/connectors.json` | MCP servers/connectors (free/paid, where they run). |
| **Self-Improvement** | many (below) | Health, self-check, review findings, suggestion queue. |

## The Self-Improvement tab in detail
`renderSelfImprove()` pulls together the system's introspection:
- **Data health** — `data/health.json` (score /100 + metrics).
- **Reference self-check** — `data/self_check.json` (score **X/50** + gaps). See [[Reference Self-Check]].
- **Self-check fix tasks** — `data/improvement_tasks.json` (open gaps the next run fixes).
- **Latest review** — `data/review_findings.json`: per-dimension scores, reviewers,
  top actions, **competitor benchmark**, and open findings. See [[Three-Agent Review]].
- **Suggestion queue** — `data/improvement_suggestions.json` + `approvals.json`
  (approve/dismiss from the offline MCP). See [[Self-Improvement Loop]].
- **Starred & frozen** — `data/stars.json`. See [[Stars and Freezing]].
- **Last run** — `data/improvement_audit.json`.

## Dynamic tabs
New tabs can appear automatically when a recurring off-tab theme is detected. They
carry a **NEW** badge and a description banner that **auto-expires** (`badge_until`).
The whole mechanism is in [[Dynamic Tabs]].

## Offline & installable
A service worker (`docs/sw.js`) caches the app shell (network-first) so the page
loads offline and installs as a PWA; data is always fetched network-first so you see
fresh JSON when online.

## Related
- [[Skills vs Tools]] · [[Data Files]] · [[Dynamic Tabs]]
