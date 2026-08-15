# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-345` (dept) · 2026-08-15T01:12:11.654389+00:00
> Participants: Pick, Assay, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query GitHub's trending AI repositories for the last week via the GitHub API.
2. Extract the top 10 repositories ranked by stars and forks, including repo names, descriptions, and primary languages.
3. Query Product Hunt's API for all posts tagged "AI" published in the last week.
4. Merge the GitHub and Product Hunt datasets into a unified list of AI-related projects.
5. Output the merged dataset in a structured GitHub-flavored markdown format.
6. Store the final dataset for further analysis or downstream tasks.

**What changed:** Expanded scope from Product Hunt-only to a dual-source (GitHub + Product Hunt) approach for broader AI project coverage.
