# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-768` (dept) · 2026-07-18T03:17:15.431667+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub API to search repositories tagged with "AI" and "research".
2. Sort results by star count in descending order.
3. Extract top 10 repositories with their star counts and descriptions.
4. Format the output as a markdown list with repository names, star counts, and descriptions.
5. Output the list in descending order of stars.

**What changed:** Added "research" tag to GitHub search for higher relevance.
