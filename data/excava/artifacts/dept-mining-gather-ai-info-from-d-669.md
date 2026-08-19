# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-669` (dept) · 2026-08-19T15:05:48.743033+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 7 days.
2. Extract raw data: product names, descriptions, upvotes, and launch dates.
3. Filter results to exclude duplicates or irrelevant entries (e.g., non-AI products).
4. Store filtered data in a structured format (e.g., JSON/CSV) for further analysis.
5. Cross-reference with other sources (GitHub/HN/Reddit/Telegram) to validate and enrich data.
6. Generate a consolidated report of diverse AI-related products and trends.

**What changed:** Focus shifted from broad social scraping to targeted API-based mining for efficiency.
