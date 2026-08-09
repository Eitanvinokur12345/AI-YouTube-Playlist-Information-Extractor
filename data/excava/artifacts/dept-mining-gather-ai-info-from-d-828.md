# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-828` (dept) · 2026-08-05T03:46:58.730678+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, and upvotes from the results.
3. Cross-reference GitHub repositories linked in Product Hunt posts (if any) for additional AI-related code/data.
4. Manually scan Hacker News (HN) for AI-related discussions in the last 7 days, focusing on comments and threads.
5. Compile Reddit threads from r/artificial, r/MachineLearning, and r/learnmachinelearning published in the last 7 days.
6. Log all findings in a structured format (e.g., CSV/JSON) for further analysis.

**What changed:** Focus shifted from passive aggregation to active API-driven and manual sourcing across multiple platforms.
