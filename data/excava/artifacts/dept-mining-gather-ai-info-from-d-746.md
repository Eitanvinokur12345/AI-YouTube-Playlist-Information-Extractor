# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-746` (dept) · 2026-07-27T18:40:42.503004+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a Reddit search for AI-related posts in the last 7 days using `site:reddit.com/r/ai OR site:reddit.com/r/MachineLearning OR site:reddit.com/r/artificial "AI"` with a `pastweek` filter.
2. Extract the top 20 results, including titles, URLs, upvotes, and comment counts.
3. Store the raw data in a structured format (e.g., JSON/CSV) for downstream filtering.
4. Cross-reference with other sources (GitHub/HN/Product Hunt/Telegram) to identify overlaps or gaps.
5. Apply a lightweight relevance filter (e.g., keyword matching for "AI," "ML," "neural," etc.) to remove noise.
6. Generate a prioritized list of high-engagement posts for deeper analysis.

**What changed:** Focus shifted from broad social scraping to a targeted Reddit feed as the first step in a multi-source pipeline.
