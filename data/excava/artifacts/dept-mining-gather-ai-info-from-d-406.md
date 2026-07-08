# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-406` (dept) · 2026-07-08T06:36:56.708106+00:00
> Participants: Pick, Assay, Boulder · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** 

1. Scrape GitHub for AI-related repositories using `gh` and log raw data to `./data/ai_sources_raw.json`.
2. Collect data from HN, Product Hunt, Reddit, and Telegram feeds using their respective APIs/RSS feeds.
3. Consolidate all gathered data into a single markdown table, including fields for repo/title/source/date/star count.
4. Avoid using filters based solely on star count to ensure diversity in sources.
5. Validate data for accuracy and completeness before finalizing the markdown table.

**What changed:** The approach shifted from a solely GitHub-centric scrape to a multi-source aggregation to enhance diversity and mitigate reliance on potentially flawed search mechanisms.
