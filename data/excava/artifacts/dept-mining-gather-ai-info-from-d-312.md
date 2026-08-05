# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-312` (dept) · 2026-08-05T02:57:34.984307+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, upvotes, and launch dates from the raw API response.
3. Filter results to ensure diversity of sources (exclude duplicates or reposts).
4. Store the cleaned data in a structured format (e.g., JSON/CSV) for downstream analysis.
5. Cross-reference with other platforms (GitHub/HN/Reddit) to validate or supplement findings.
6. Generate a summary report highlighting top AI products by engagement (upvotes/launch activity).

**What changed:** Focused on Product Hunt API as a primary source for AI product discovery, prioritizing recency and structured data extraction.
