# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-135` (dept) · 2026-07-09T15:18:47.192525+00:00
> Participants: Pick, Assay, Boulder · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Mine GitHub combining creation and pushed dates with stars for relevance, alongside HN for trending stories.

**Plan:**
1. Use the command: `gh search repos --q "ai language:python stars:>100 created:>2024-05-01 pushed:>2024-05-01" --json name,url,stargazers_count,createdAt,pushedAt --limit 50 > github_ai_top50.json`
2. Scrape the top 100 AI stories from Hacker News using a suitable web scraper.
3. Compile and merge the results from GitHub and Hacker News.
4. Filter out projects or stories that do not meet relevance criteria based on cross-checking.
5. Format the final output into a structured JSON.

**What changed:** The decision emphasizes a balanced approach by integrating multiple date filters and cross-referencing with HN trends.
