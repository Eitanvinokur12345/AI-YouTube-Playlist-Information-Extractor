# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-560` (dept) · 2026-08-26T09:49:59.466749+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, upvotes, and comments from the API response.
3. Filter results to ensure diversity of sources (exclude duplicates or reposts).
4. Store the data in a structured format (e.g., JSON/CSV) for analysis.
5. Cross-reference with other platforms (GitHub/HN/Reddit/Telegram) to validate trends.
6. Compile a summary report highlighting key AI-related products and insights.

**What changed:** Focused on Product Hunt as a primary source for recent AI product trends.
