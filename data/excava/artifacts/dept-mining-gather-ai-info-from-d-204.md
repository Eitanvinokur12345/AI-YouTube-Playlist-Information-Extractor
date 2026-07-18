# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-204` (dept) · 2026-07-18T02:29:20.302036+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub API to search repositories tagged with "AI" and "research" from the last 30 days.
2. Sort results by star count (descending) and last commit date (descending).
3. Extract top 10 repositories with star counts, last commit dates, and one-line summaries.
4. Format output as a ranked markdown list with headers for each entry.
5. Validate data for freshness (last commit within 30 days) and relevance (AI/research focus).
6. Output results in GitHub markdown format.

**What changed:** Prioritized GitHub API search with dual tags ("AI" + "research") and added commit date validation.
