# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-740` (dept) · 2026-08-07T01:02:35.756451+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.
2. Extract titles, descriptions, and engagement metrics (upvotes, comments, etc.) from the results.
3. Cross-reference the Product Hunt data with GitHub, Hacker News, Reddit, and Telegram for additional insights.
4. Compile a consolidated dataset of AI-related trends, tools, and discussions across sources.
5. Analyze engagement patterns to identify high-impact AI projects or discussions.
6. Store the final dataset in a structured format (e.g., CSV/JSON) for further analysis.

**What changed:** Focus narrowed to Product Hunt API as the primary initial source, with cross-referencing to other platforms for diversity.
