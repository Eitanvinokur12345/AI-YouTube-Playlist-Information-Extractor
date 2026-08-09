# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-933` (dept) · 2026-08-06T03:53:18.460840+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 30 days.
2. Extract titles, descriptions, and engagement metrics (upvotes, comments) from the raw list.
3. Cross-reference GitHub repositories linked in Product Hunt posts (if any) for additional AI-related code/data.
4. Supplement with top AI-related threads from Hacker News (last 30 days) via Algolia API.
5. Manually scan Reddit (r/MachineLearning, r/artificial, r/learnmachinelearning) for trending AI discussions.
6. Aggregate all data into a structured JSON/CSV for downstream analysis.

**What changed:** Focused on Product Hunt API first, then layered GitHub/HN/Reddit for diversity.
