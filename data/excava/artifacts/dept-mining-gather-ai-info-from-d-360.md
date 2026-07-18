# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-360` (dept) · 2026-07-18T01:15:50.772180+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub's advanced search to query repositories tagged with both "AI" and "research."
2. Sort results by stars (descending) and limit to the top 100.
3. Extract repository names, descriptions, and star counts for each entry.
4. Format the output as a GitHub-flavored markdown table with columns: Rank, Repository, Description, Stars.
5. Save the table to a `.md` file named `github_ai_research_top100.md`.
6. Validate the data for completeness and correct sorting.

**What changed:** Added "research" tag to GitHub search for higher-quality AI repositories.
