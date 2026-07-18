# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-988` (dept) · 2026-07-18T01:34:57.665459+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Mine GitHub for repositories tagged with both "AI" and "research".
2. Return a ranked list of 50 projects sorted by stars (descending).
3. Include for each project: name, star count, last update date, and a concise description.
4. Exclude projects with fewer than 10 stars or no description.
5. Output results in GitHub-flavored markdown format.
6. Ensure diversity by filtering out forks and focusing on unique repositories.

**What changed:** Reduced scope from 100 to 50 projects and added "research" tag filter.
