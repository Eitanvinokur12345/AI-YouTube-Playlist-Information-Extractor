# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-153` (dept) · 2026-07-14T21:33:28.048083+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query GitHub API for AI repositories with commits in the last 30 days, sorted by stars.
2. Scrape Hacker News "Show HN" posts from the last 30 days with "AI" in the title/description.
3. Parse Product Hunt’s API for AI tools launched in the last 30 days, prioritizing upvotes/comments.
4. Extract AI-related submissions from Reddit’s r/MachineLearning, r/artificial, and r/learnmachinelearning (last 30 days).
5. Monitor Telegram AI channels (e.g., AI News, ML Papers) for recent bot/tool announcements.
6. Compile results into a markdown table with columns: *Project*, *Source*, *Description*, *Engagement Metric*, *Link*.

**What changed:** Focus shifted from "diverse sources" to prioritizing recency and engagement metrics for actionable mining.
