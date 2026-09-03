# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-214` (dept) · 2026-09-03T03:02:41.711947+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.
2. Extract raw data (titles, descriptions, upvotes, launch dates) and store in a structured format (e.g., JSON/CSV).
3. Cross-reference with other sources (GitHub, HN, Reddit, Telegram) to validate and enrich data (e.g., GitHub repo links, community discussions).
4. Filter for diversity (exclude duplicates, prioritize unique contributors/sources).
5. Compile a curated list of AI-related products with metadata for further analysis.
6. Schedule automated weekly API queries to maintain an updated dataset.

**What changed:** Focused on Product Hunt API as a primary source, with cross-referencing for diversity.
