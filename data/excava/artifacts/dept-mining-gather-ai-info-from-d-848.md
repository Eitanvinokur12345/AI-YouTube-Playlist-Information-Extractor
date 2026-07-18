# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-848` (dept) · 2026-07-18T02:52:37.839487+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub’s advanced search to query repositories tagged with both "AI" and "research."
2. Sort results by star count (descending) and limit to the top 10.
3. Extract for each repository: name, star count, description, and last update date.
4. Format the output as a GitHub-flavored markdown table with columns: `#`, `Repository`, `Stars`, `Description`, `Last Updated`.
5. Include a brief note on the search query used (e.g., `"AI" "research" in:topics stars:>1000`).
6. Append a one-line summary of the top 3 repositories by star count and recency.

**What changed:** Added "research" tag to refine results and included recency in ranking.
