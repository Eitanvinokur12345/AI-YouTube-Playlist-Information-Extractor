# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-504` (dept) · 2026-08-06T14:57:21.621693+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.

**Plan:**
1. Use Product Hunt’s API to fetch posts tagged "AI" from the last 7 days.
2. Parse the raw JSON response to extract post titles, descriptions, and URLs.
3. Filter out duplicates or irrelevant entries (e.g., non-AI products mislabeled).
4. Store the cleaned data in a structured format (e.g., CSV/JSON) for further analysis.
5. Cross-reference with other sources (GitHub/HN/Reddit) to validate or supplement findings.
6. Output the final dataset for downstream AI mining tasks.

**What changed:**
Focused on Product Hunt’s API as the primary source for recent AI product launches.
