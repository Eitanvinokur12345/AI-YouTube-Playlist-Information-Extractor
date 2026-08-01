# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-246` (dept) · 2026-08-01T15:40:21.854347+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep Hacker News’ "AI" posts from the last 7 days via HN’s API.
2. Extract titles, URLs, and upvotes for each post.
3. Return a clean, structured list of posts with engagement metrics.
4. Store the dataset locally for further filtering (quality/relevance).
5. Share the raw dataset with the team for validation.

**What changed:** Focus narrowed to HN API sweep for initial dataset, deferring other sources (GitHub/HN/Product Hunt/etc.) for later phases.
