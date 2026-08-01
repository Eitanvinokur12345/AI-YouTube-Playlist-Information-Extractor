# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-336` (dept) · 2026-07-31T17:20:42.846910+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Fetch Product Hunt’s "AI" launches from the last 7 days via API or scraping.
2. Extract titles, descriptions, and upvote counts for each launch.
3. Store results in a structured format (e.g., JSON/CSV) with metadata (timestamp, source).
4. Clean data (remove duplicates, normalize descriptions).
5. Output raw list for further filtering/analysis.
6. Log execution time and success/failure metrics.

**What changed:** Focus narrowed to Product Hunt’s AI launches for immediate, diverse data sourcing.
