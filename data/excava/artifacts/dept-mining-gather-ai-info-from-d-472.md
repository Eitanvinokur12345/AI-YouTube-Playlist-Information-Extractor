# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-472` (dept) · 2026-08-05T03:16:24.642718+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 7 days.
2. Parse results to extract titles, descriptions, upvotes, and launch dates.
3. Cross-reference with GitHub’s API to identify repositories linked in posts (if any).
4. Supplement with Reddit’s r/MachineLearning and r/artificial subreddits for community discussions.
5. Manually check Telegram AI channels (e.g., AI News, Future of AI) for recent posts.
6. Compile findings into a structured dataset for analysis.

**What changed:** Prioritized Product Hunt API query as the first step to gather diverse, recent AI product launches.
