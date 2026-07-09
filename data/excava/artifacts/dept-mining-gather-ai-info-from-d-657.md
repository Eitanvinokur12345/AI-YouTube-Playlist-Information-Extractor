# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-657` (dept) · 2026-07-09T14:41:54.049788+00:00
> Participants: Pick, Assay, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**
Mine GitHub’s *trending* AI repos by *stars gained* in last 30 days (not commits) + HN’s "Show HN" AI posts sorted by *recent* engagement, then filter for odd gems with real-not-display value.

**Plan:**
1. GitHub: Scrape trending AI repos by stars gained in last 30 days (filter >100 stars, top 200).
2. HN: Scrape top 50 "Show HN" AI posts by recent engagement (comments + upvotes).
3. Filter results for repos/posts with *real* technical depth (e.g., novel architectures, benchmarks, or niche tools).
4. Deduplicate and normalize data (remove forks, dead links, or low-signal entries).
5. Export GitHub results to `github_ai.json` (name, url, stars_gained, description).
6. Export HN results to `hn_ai.json` (title, url, engagement_score, discussion_summary).

**What changed:**
Shifted from *creation date* and *commits* to *stars gained* and *recent engagement* for relevance.
