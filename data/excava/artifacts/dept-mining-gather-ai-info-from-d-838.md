# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-838` (dept) · 2026-08-15T01:18:08.634102+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.
2. Extract raw JSON data containing titles, descriptions, upvotes, comments, and launch dates.
3. Parse and clean the data to remove duplicates or irrelevant entries.
4. Store the processed data in a structured format (e.g., CSV or database) for further analysis.
5. Cross-reference with other sources (GitHub/HN/Reddit/Telegram) to validate and enrich the dataset.
6. Generate a summary report highlighting trends, top products, and key insights.

**What changed:** Focused on Product Hunt API as a primary source for AI product data, integrating it with other platforms for diversity.
