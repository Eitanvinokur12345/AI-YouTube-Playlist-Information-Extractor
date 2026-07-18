# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-700` (dept) · 2026-07-18T02:40:48.790652+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub’s advanced search to query repositories tagged with both "AI" and "research".
2. Sort results by stars (descending) and limit to the top 100.
3. Extract project names, descriptions, star counts, and URLs for each result.
4. Format the output as a markdown table with columns: Rank, Project Name, Stars, Description, Link.
5. Validate links and descriptions for accuracy before finalizing.
6. Output the table in GitHub markdown format.

**What changed:** Added "research" tag to refine search scope and improve relevance.
