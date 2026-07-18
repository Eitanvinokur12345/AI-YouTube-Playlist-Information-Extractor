# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-542` (dept) · 2026-07-18T02:35:02.968780+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub API to search repositories tagged with both "AI" and "research".
2. Sort results by stars (descending) and last update date (descending).
3. Extract top 20 repositories with their names, descriptions, star counts, and last update dates.
4. Format results into a markdown table with columns: Rank, Repository, Description, Stars, Last Updated.
5. Output the table in GitHub markdown format.

**What changed:** Focused search to repositories tagged with both "AI" and "research" for higher relevance.
