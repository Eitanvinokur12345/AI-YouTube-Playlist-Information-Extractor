# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-302` (dept) · 2026-07-31T22:29:59.957913+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep GitHub’s AI-related repos created in the last 7 days.
2. Filter results to include only repositories with ≥10 stars.
3. Extract top 20 repos by star count, including names, descriptions, and creation dates.
4. Output results in GitHub markdown format (one repo per line, tab-separated: `Rank | Name | Stars | Description | Creation Date`).
5. Exclude forks and archived repos.

**What changed:** Focus narrowed to GitHub-only, 7-day window, top 20 by stars.
