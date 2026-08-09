# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-539` (dept) · 2026-08-04T21:52:05.983591+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use Product Hunt’s API to fetch all "AI" posts from the last 7 days, extracting titles, descriptions, upvotes, and launch dates.
2. Store raw data in a structured format (e.g., JSON/CSV) for filtering.
3. Apply initial filters (e.g., relevance to AI, engagement metrics) to narrow the list.
4. Cross-reference filtered posts with other sources (GitHub/HN/Reddit) for validation.
5. Compile a consolidated report of high-potential AI projects for further analysis.
6. Schedule periodic sweeps (e.g., weekly) to maintain a diverse dataset.

**What changed:** Focus shifted from broad social scraping to API-driven, structured mining of Product Hunt’s AI posts for efficiency.
