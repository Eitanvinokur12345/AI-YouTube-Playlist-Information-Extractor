# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-240` (dept) · 2026-07-18T19:44:03.744274+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Mine GitHub for repositories tagged "AI" and "research," output a ranked list of top 10 by stars and forks.
2. Filter the list for repositories with recent commits (last 30 days).
3. Further filter for repositories with a README describing a research focus.
4. Output the final list in GitHub markdown format.

**What changed:** Focus shifted from Reddit to GitHub for mining AI research repositories.
