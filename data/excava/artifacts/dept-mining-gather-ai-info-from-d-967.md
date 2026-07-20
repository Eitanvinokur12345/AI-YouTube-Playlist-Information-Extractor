# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-967` (dept) · 2026-07-20T23:10:36.534483+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub’s advanced search to query repositories with tags "AI" AND "research" created in the last 7 days.
2. Sort results by stars (descending) and extract the top 10 repositories.
3. Return the list in a numbered markdown table with columns: Rank, Repository, Stars, URL, and Brief Description (auto-generated from GitHub).
4. Exclude forks unless explicitly requested.
5. Validate each entry’s creation date and tags via GitHub’s API.
6. Output the final list in GitHub-flavored markdown.

**What changed:** Focus narrowed to GitHub-only, high-starred AI research repos from the last 7 days.
