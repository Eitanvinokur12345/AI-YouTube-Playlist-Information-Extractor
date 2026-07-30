# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-354` (dept) · 2026-07-30T19:53:35.162508+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Navigate to GitHub’s "Trending" page ([github.com/trending](https://github.com/trending)).
2. Filter by "AI" in the language dropdown and select "This week" for the timeframe.
3. Extract the top 20 repos by stars gained, capturing their names, star counts, descriptions, and links.
4. Cross-reference each repo’s README for AI-related keywords (e.g., "LLM," "neural," "transformer") to ensure relevance.
5. Compile results into a GitHub-flavored markdown table with columns: **#**, **Repo Name**, **Stars Gained**, **Description**, **Link**.
6. Export the table as a `.md` file named `ai_trending_repos_weekly.md`.

**What changed:** Focus narrowed to GitHub’s trending AI repos (weekly) with star-based ranking and README validation.
