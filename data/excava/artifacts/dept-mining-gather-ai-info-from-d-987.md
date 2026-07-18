# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-987` (dept) · 2026-07-18T02:23:22.060470+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub’s advanced search to query repositories tagged with both "AI" and "research."
2. Sort results by stars (descending) and limit to the top 100 entries.
3. Extract for each repository: name, description, star count, and URL.
4. Format the output as a markdown table with columns: Rank, Repository, Description, Stars, Link.
5. Validate entries for relevance (e.g., exclude non-research AI projects like tutorials or apps).
6. Output the final table in GitHub-flavored markdown.

**What changed:** Prioritized GitHub research repositories over generic "AI" tags.
