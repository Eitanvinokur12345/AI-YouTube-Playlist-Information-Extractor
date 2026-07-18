# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-209` (dept) · 2026-07-18T01:58:09.110374+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a GitHub search for repositories tagged with "AI," sorted by stars (descending), excluding forks.
2. Extract the top 100 results, capturing project names, star counts, and descriptions.
3. Filter the list to retain only projects with ≥100 stars and clearly AI-related descriptions.
4. Rank the filtered projects by star count and relevance to AI.
5. Output a markdown list of the top 20 projects with their star counts and descriptions.
6. Proceed to Boulder’s next action (review/filter for high-quality candidates).

**What changed:** Focus narrowed from raw GitHub search to a curated, high-signal subset for deeper mining.
