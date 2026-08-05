# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-142` (dept) · 2026-08-05T20:11:38.240834+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.
2. Extract titles, descriptions, upvotes, and launch dates from the API response.
3. Store the raw data in a structured format (e.g., JSON/CSV) for further processing.
4. Cross-reference the Product Hunt data with other sources (GitHub/HN/Reddit/Telegram/social) to identify overlaps or unique insights.
5. Analyze the combined dataset to extract actionable AI trends or patterns.
6. Compile a final report summarizing key findings and next steps.

**What changed:** Focused on Product Hunt API as a primary data source while ensuring integration with other diverse platforms for comprehensive AI mining.
