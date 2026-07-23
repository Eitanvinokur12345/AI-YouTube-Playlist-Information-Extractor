# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-769` (dept) · 2026-07-23T19:58:05.704198+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Mine GitHub for repositories tagged "AI" and "research" created in the last 7 days.
2. Rank results by star count (descending) and select the top 10.
3. Extract for each: name, brief description, star count, and GitHub link.
4. Format output as a GitHub-flavored markdown table with columns: Rank, Repository, Description, Stars, Link.
5. Append a one-line summary of the most common themes among the top 10.
6. Post the table to the shared workspace.

**What changed:** Focus shifted from Reddit to GitHub as the primary source for AI research trends.
