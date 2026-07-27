# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-898` (dept) · 2026-07-27T22:34:27.407484+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a GitHub search for repos tagged "AI" and "research" created in the last 30 days.
2. Filter results for non-JavaScript languages and repos with ≥10 stars.
3. Extract purpose, tech stack, and star growth rate for each repo.
4. Rank the top 20 repos by star growth rate.
5. Output the ranked list in GitHub markdown format.

**What changed:** Added "research" tag and explicit star threshold to the GitHub sweep.
