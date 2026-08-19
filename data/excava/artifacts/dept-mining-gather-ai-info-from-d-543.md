# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-543` (dept) · 2026-08-19T13:28:23.852794+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 30 days.
2. Extract titles, descriptions, upvotes, and launch dates from the raw API response.
3. Cross-reference results with GitHub, Hacker News, Reddit, and Telegram for additional context.
4. Compile a consolidated dataset of AI-related product launches with diverse source attributions.
5. Apply a deduplication filter to remove duplicates across platforms.
6. Output the final dataset in a structured format (e.g., CSV/JSON) for further analysis.

**What changed:** Focused on Product Hunt API as the primary source, with cross-platform validation for diversity.
