# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-606` (dept) · 2026-07-17T15:58:26.894944+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub API to search repositories tagged with "AI" and "research".
2. Filter results to exclude forks and empty repositories.
3. Rank results by star count in descending order.
4. Extract top 20 repositories with their descriptions and star counts.
5. Format output as a markdown list with repository name, star count, and description.
6. Output only the top 20 results.

**What changed:** Added "research" tag to GitHub search criteria.
