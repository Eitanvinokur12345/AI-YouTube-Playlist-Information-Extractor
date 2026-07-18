# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-595` (dept) · 2026-07-18T02:58:24.013943+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub's advanced search to query repositories tagged with both "AI" and "research."
2. Sort results by stars (descending) and limit to the top 20.
3. Extract for each: name, star count, description, and URL.
4. Format as a markdown table with columns: **Rank**, **Repository**, **Stars**, **Description**, **URL**.
5. Validate that all entries are research-focused (filter out non-research projects if needed).
6. Output the table in GitHub-flavored markdown.

**What changed:** Prioritized GitHub search for "AI" + "research" over generic "AI" tag to ensure research relevance.
