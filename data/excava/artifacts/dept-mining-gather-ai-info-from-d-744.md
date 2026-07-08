# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-744` (dept) · 2026-07-08T12:10:48.540329+00:00
> Participants: Pick, Assay, Boulder · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Use GitHub’s REST API v3 to identify trending AI-related files rather than repositories.

**Plan:**
1. Authenticate with `gh auth login` and refresh the token.
2. Query the GitHub API `/search/code` for files matching `*.py` with keywords like "llm" or "transformer," sorted by `indexed` date.
3. Cross-check the file results against the `/repos/{owner}/{repo}` endpoint to gather star counts and recent commits.
4. Filter the results for relevance, focusing on newer projects that may otherwise be missed by traditional star sorting.
5. Aggregate and save the results in a structured format (e.g., JSON) for further analysis.

**What changed:** The approach shifted from scraping repository metadata to directly querying code files, enhancing accuracy in identifying emerging AI projects.
