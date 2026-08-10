# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-495` (dept) · 2026-08-10T08:16:45.444869+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 30 days.
2. Extract product names, descriptions, upvotes, and launch dates from the raw API response.
3. Filter results to exclude duplicates or non-relevant entries (e.g., non-AI products mislabeled).
4. Store the cleaned dataset in a structured format (e.g., JSON/CSV) for further analysis.
5. Cross-reference with other sources (GitHub/HN/Reddit) to validate or supplement AI-related data.
6. Output a prioritized list of AI products based on upvotes/launch recency for deeper mining.

**What changed:** Focused on Product Hunt as a primary source while ensuring integration with other platforms for diversity.
