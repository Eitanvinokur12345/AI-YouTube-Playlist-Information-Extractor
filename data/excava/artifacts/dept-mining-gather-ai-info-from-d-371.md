# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-371` (dept) · 2026-09-03T03:44:30.858424+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, upvotes, and launch dates into a structured dataset.
3. Cross-reference GitHub repositories linked in Product Hunt posts for additional metadata (stars, forks, activity).
4. Supplement with top HN/Reddit threads (past 7 days) discussing AI tools, filtering for diverse perspectives.
5. Aggregate Telegram channel archives (if accessible) for AI-related announcements or discussions.
6. Compile all data into a unified CSV/JSON format for analysis.

**What changed:** Prioritized Product Hunt API query as the primary data source, then layered in GitHub/HN/Reddit/Telegram for diversity.
