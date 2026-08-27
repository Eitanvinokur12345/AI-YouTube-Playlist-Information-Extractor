# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-519` (dept) · 2026-08-27T14:33:05.785834+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.
2. Extract raw data (product names, votes, discussions, and metadata) from the API response.
3. Parse and clean the data to isolate key trends (e.g., top-voted products, recurring themes).
4. Cross-reference with GitHub/HN/Reddit/Telegram/social for validation and additional context.
5. Compile insights into a structured report (e.g., GitHub markdown table or JSON).
6. Automate future queries to maintain a live dataset for ongoing analysis.

**What changed:** Focused on Product Hunt API as the primary source for AI product launches, with cross-platform validation.
