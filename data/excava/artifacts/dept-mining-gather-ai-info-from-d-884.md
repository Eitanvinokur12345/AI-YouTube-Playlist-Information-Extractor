# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-884` (dept) · 2026-07-20T23:28:04.478998+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Mine GitHub for repositories tagged "AI" and "research" created in the last 7 days.
2. Rank results by stars (descending) and filter out forks.
3. Select the top 10 repositories with brief reasons (e.g., novelty, engagement, or relevance to AI trends).
4. Output a GitHub-flavored markdown list with repo name, star count, and 1-line rationale.
5. Include a note on the timeframe and filtering criteria.

**What changed:** Switched from Reddit to GitHub mining to prioritize diverse, code-centric AI sources.
