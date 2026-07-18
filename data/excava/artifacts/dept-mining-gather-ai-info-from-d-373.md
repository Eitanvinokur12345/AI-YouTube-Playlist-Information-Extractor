# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-373` (dept) · 2026-07-18T03:04:19.056730+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Mine GitHub for repositories tagged with both "AI" and "research."
2. Sort results by stars (descending) and select the top 50.
3. Extract repository names, descriptions, star counts, and last update dates.
4. Format output as a GitHub-flavored markdown table with columns: Rank, Repository, Description, Stars, Last Updated.
5. Exclude forks and ensure results are from the last 2 years.
6. Validate data integrity by cross-checking star counts and update dates.

**What changed:** Reduced scope from 100 to 50 results and added "research" tag filter.
