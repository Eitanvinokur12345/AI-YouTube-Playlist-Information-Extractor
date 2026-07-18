# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-345` (dept) · 2026-07-18T01:28:54.442513+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub’s search API to query repositories tagged with both "AI" and "research."
2. Sort results by stars (descending) and limit to the top 100.
3. Extract project names, star counts, and descriptions for each result.
4. Format the output as a GitHub-flavored markdown table with columns: Rank, Name, Stars, Description.
5. Validate the data for completeness and remove duplicates or non-relevant entries.
6. Publish the final ranked list in the specified format.

**What changed:** Added "research" tag to GitHub query for higher-signal AI projects.
