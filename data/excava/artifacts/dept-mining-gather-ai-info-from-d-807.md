# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-807` (dept) · 2026-08-17T07:35:30.826966+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.
2. Extract titles, descriptions, upvotes, and comment counts from the API response.
3. Filter results to ensure diversity of sources (exclude duplicates or reposts).
4. Store raw data in a structured format (e.g., JSON/CSV) for further processing.
5. Cross-reference with other platforms (GitHub/HN/Reddit/Telegram) to validate trends.
6. Generate a summary report highlighting top-performing AI launches.

**What changed:** Focused on Product Hunt API as a primary data source while ensuring cross-platform validation.
