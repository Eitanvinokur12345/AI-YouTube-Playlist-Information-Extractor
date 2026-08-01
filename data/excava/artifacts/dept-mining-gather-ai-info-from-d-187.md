# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-187` (dept) · 2026-07-31T22:04:41.213818+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub API to query AI-related repos created in the last 7 days, filtering by topics like `ai`, `machine-learning`, `deep-learning`, etc.
2. Extract for each repo: name, brief feature description, license type, and star count.
3. Filter results to retain only 10–15 projects with the highest star growth or relevance.
4. Format output as a GitHub-flavored markdown table with columns: `#`, `Name`, `Feature`, `License`, `Stars`.
5. Validate data for accuracy (e.g., exclude forks, verify license presence).
6. Output the final list with a one-line summary header.

**What changed:** Scope narrowed to GitHub only, last 7 days, and output limited to 10–15 top projects.
