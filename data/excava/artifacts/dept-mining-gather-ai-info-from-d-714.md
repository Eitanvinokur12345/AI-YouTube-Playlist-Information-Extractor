# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-714` (dept) · 2026-07-31T17:47:38.531093+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Fetch Product Hunt’s "AI" launches from the last 7 days via API or scraping.
2. Extract titles, descriptions, and upvotes into a structured list (JSON/CSV).
3. Filter for relevance (e.g., exclude non-AI or low-quality entries).
4. Cross-reference with other sources (GitHub/HN/Reddit) for validation.
5. Store the dataset in a GitHub repo with clear documentation.
6. Share the raw dataset for further analysis.

**What changed:** Focused on Product Hunt as a primary source for recent AI launches, prioritizing structured data extraction.
