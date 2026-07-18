# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-732` (dept) · 2026-07-18T01:40:50.233060+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub’s advanced search to query repositories tagged with both "AI" and "research."
2. Sort results by stars (descending) and limit to the top 100 projects.
3. Extract for each: name, description, star count, and URL.
4. Format the output as a numbered markdown list with bolded project names, star counts, and links.
5. Include a brief metadata note (e.g., "Generated via GitHub API on [date]").

**What changed:** Focus narrowed to GitHub’s "AI" + "research" repositories, ranked by stars.
