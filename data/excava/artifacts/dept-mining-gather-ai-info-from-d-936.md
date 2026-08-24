# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-936` (dept) · 2026-08-24T09:24:24.627924+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for posts tagged "AI" published in the last 30 days.
2. Extract titles, descriptions, upvote counts, and launch dates from the API response.
3. Store the data in a structured format (e.g., JSON/CSV) for further analysis.
4. Cross-reference with other sources (GitHub/HN/Reddit/Telegram) to validate and diversify insights.
5. Filter for unique or high-signal items (e.g., high upvotes, recent launches).
6. Compile a prioritized list of AI-related products for deeper data mining.

**What changed:** Focused on Product Hunt as a primary source for recent AI products, complementing other platforms.
