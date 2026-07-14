# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-508` (dept) · 2026-07-14T22:59:41.224066+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query GitHub API for AI repositories created/updated in the last 30 days, sorted by stars, forks, and issue activity.
2. Scrape Hacker News (via Algolia API) for top AI-related posts in the last 30 days, filtering by engagement (comments, upvotes).
3. Extract trending AI tools from Product Hunt’s API (last 30 days), prioritizing those with high maker/commenter activity.
4. Mine Reddit (r/MachineLearning, r/artificial, r/learnmachinelearning) for posts with >50 upvotes in the last 30 days, excluding spam.
5. Search Telegram AI channels (e.g., @AIProjects, @MLTools) for pinned/forwarded links with >10 reactions or shares.
6. Cross-reference all sources to deduplicate, then compile a curated list with links, descriptions, and engagement metrics.

**What changed:** Focused on **active, high-signal sources** (GitHub, HN, Product Hunt, Reddit, Telegram) with **30-day recency filters** and **engagement thresholds** to exclude noise.
