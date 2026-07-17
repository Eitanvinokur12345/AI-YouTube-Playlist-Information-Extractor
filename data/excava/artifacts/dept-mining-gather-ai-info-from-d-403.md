# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-403` (dept) · 2026-07-17T19:46:23.545342+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub’s advanced search to query repositories tagged with both "AI" and "research."
2. Sort results by stars (descending) and limit to the top 100 entries.
3. Extract for each entry: repository name, star count, description, and direct link.
4. Format the output as a markdown table with columns: `# | Repository | Stars | Description | Link`.
5. Include a timestamp in the filename (e.g., `ai_research_github_YYYYMMDD.md`).
6. Validate links and descriptions for accuracy before finalizing.

**What changed:** Scope expanded from generic "AI" to "AI" + "research" for higher relevance.
