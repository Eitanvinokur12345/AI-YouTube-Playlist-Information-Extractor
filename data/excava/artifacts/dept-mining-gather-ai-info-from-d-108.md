# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-108` (dept) · 2026-07-18T21:27:19.604830+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run GitHub API search for repositories tagged "AI" and "research" created in the last 7 days.
2. Sort results by star count (descending) and select top 10.
3. For each repo, extract: name, stars, description, and URL.
4. Format output as a markdown list with headers: `#, Name, Stars, Description, URL`.
5. Validate entries for relevance (exclude non-AI/research projects).
6. Return the final ranked list.

**What changed:** Focus narrowed to GitHub-only, time-filtered, star-ranked AI research repos.
