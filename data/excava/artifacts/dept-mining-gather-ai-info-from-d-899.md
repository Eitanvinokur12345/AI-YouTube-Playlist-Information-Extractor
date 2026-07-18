# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-899` (dept) · 2026-07-18T01:46:33.331621+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub’s API to search repositories tagged with both "AI" and "research".
2. Sort results by star count in descending order.
3. Extract the top 20 repositories, including their names, descriptions, star counts, and last update dates.
4. Format the output as a GitHub-flavored markdown table with columns: Rank, Repository, Description, Stars, Last Updated.
5. Ensure no duplicates or forks of the same project are included.
6. Validate that all entries are research-oriented (e.g., papers, frameworks, datasets).

**What changed:** Focus narrowed from generic "AI" to "AI" + "research" to ensure higher-quality, research-centric results.
