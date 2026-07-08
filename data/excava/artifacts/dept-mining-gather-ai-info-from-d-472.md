# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-472` (dept) · 2026-07-08T20:08:02.338311+00:00
> Participants: Pick, Assay, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run `gh search repos --q "ai language:python stars:>100" --json name,url,stargazers_count --limit 100 > github_ai_top100.json` to fetch 100+ star AI repos (Python).
2. For each repo in `github_ai_top100.json`, fetch recent commits via `gh api repos/{owner}/{repo}/commits?since=2024-05-01`.
3. Filter results to retain only repos with ≥1 commit in the last 30 days.
4. Cross-check top candidates against HN’s "Show HN" posts and Reddit’s r/MachineLearning.
5. Export final list to `active_ai_repos.json` with metadata (name, url, stars, last commit date).

**What changed:** Replaced date-filtered scrape with star-only filter + commit activity check.
