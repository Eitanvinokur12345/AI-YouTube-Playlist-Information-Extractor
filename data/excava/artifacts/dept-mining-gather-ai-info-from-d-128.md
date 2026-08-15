# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-128` (dept) · 2026-08-15T00:47:57.727683+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.

**Plan:**
1. Use Product Hunt’s API to fetch posts tagged "AI" from the last 7 days.
2. Extract titles, descriptions, and upvotes for each post.
3. Store raw data in a structured format (e.g., JSON/CSV).
4. Cross-reference with other sources (GitHub/HN/Reddit/Telegram) for diversity.
5. Filter for unique or high-signal entries (e.g., upvotes > threshold).
6. Compile a consolidated list for further analysis.

**What changed:**
Focused on Product Hunt as a primary source for recent AI launches, prioritizing diversity and recency.
