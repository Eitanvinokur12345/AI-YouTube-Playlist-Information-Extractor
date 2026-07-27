# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-570` (dept) · 2026-07-27T17:30:26.296787+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a Reddit search for AI-related posts in the last 7 days using `site:reddit.com/r/ai OR site:reddit.com/r/MachineLearning OR site:reddit.com/r/artificial "AI" after:2023-11-01` (adjust date as needed).
2. Extract the top 20 posts by upvotes, including titles, upvote counts, and direct links.
3. Store the dataset in a structured format (e.g., CSV/JSON) for further filtering.
4. Cross-reference with other sources (GitHub/HN/Product Hunt/Telegram) to ensure diversity.
5. Apply initial filtering (e.g., relevance, recency) to refine the dataset.
6. Output the final curated list for analysis.

**What changed:** Focus shifted from broad social scraping to prioritizing Reddit as a high-signal source for recent AI discussions, with plans to integrate other platforms.
