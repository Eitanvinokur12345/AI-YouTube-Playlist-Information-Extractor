# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-707` (dept) · 2026-07-18T17:32:47.335983+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Mine GitHub for repositories tagged "AI" and "research" using the GitHub API.
2. Filter results to include only repositories created or updated in the last 7 days.
3. Rank the top 10 repositories by star count (descending).
4. Output a markdown table with columns: **Rank**, **Repository Name**, **Description**, **Stars**, **URL**.
5. Share the table with the team for evaluation.

**What changed:** Prioritized GitHub mining over Product Hunt search to align with the goal of gathering AI research from diverse, technical sources.
