# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-598` (dept) · 2026-08-01T14:09:31.747173+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use HN’s API to fetch all posts tagged with "AI" from the last 7 days.
2. Filter results to retain only posts with titles containing "AI," "artificial intelligence," or related keywords.
3. Extract post titles, URLs, and upvote counts for each filtered entry.
4. Store the filtered list in a structured format (e.g., JSON or CSV) for downstream mining.
5. Cross-reference with other sources (GitHub/HN/Product Hunt/Reddit/Telegram) to validate trends.
6. Schedule periodic runs (e.g., daily/weekly) to maintain a dynamic dataset.

**What changed:** Focus shifted from broad social scraping to targeted HN API mining for high-signal AI content.
