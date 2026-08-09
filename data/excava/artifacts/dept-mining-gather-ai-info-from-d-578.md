# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-578` (dept) · 2026-08-07T03:32:35.751380+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.
2. Extract raw data: product names, descriptions, upvotes, and launch dates.
3. Filter results to ensure diversity (exclude duplicates, verify sources).
4. Store data in a structured format (e.g., JSON/CSV) for analysis.
5. Cross-reference with other platforms (GitHub/HN/Reddit/Telegram) to validate trends.
6. Compile a consolidated report of unique AI-related products and insights.

**What changed:** Focused on Product Hunt API as a primary source while ensuring cross-platform validation.
