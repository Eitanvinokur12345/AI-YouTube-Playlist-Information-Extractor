# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-599` (dept) · 2026-07-30T19:39:16.035925+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a focused sweep on GitHub for trending AI repos this week using the GitHub API, filtering by stars and forks from the past 7 days.
2. Extract metadata (repo name, description, stars, forks, URL, primary language) for each result.
3. Deduplicate entries and exclude repos with <10 stars or no clear AI focus.
4. Format results into a GitHub-flavored markdown table with columns: **Repo**, **Description**, **Stars**, **Forks**, **Language**, **URL**.
5. Append a "Sources" section listing all queried endpoints (e.g., `/search/repositories?q=ai+created:>2023-11-01&sort=stars&order=desc`).
6. Save as `trending-ai-repos-YYYY-MM-DD.md` in a dedicated `/data` directory.

**What changed:** Shifted from broad social scraping to a high-signal GitHub API sweep for AI repos.
