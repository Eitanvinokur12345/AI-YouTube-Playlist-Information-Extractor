# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-677` (dept) · 2026-08-28T00:08:18.552250+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, upvotes, and comment counts from the raw list.
3. Filter results to exclude duplicates or low-quality entries (e.g., spam, off-topic).
4. Store the cleaned data in a structured format (e.g., JSON/CSV) for further analysis.
5. Cross-reference with other sources (GitHub/HN/Reddit/Telegram) to validate trends.
6. Compile a summary report highlighting top AI launches and community engagement metrics.

**What changed:** Focused on Product Hunt as a primary source for AI launches, prioritizing recent and diverse data.
