# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-168` (dept) · 2026-07-09T04:00:40.770698+00:00
> Participants: Boulder, Pick, Assay · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Mine raw GitHub commits and diffs, then cross-check with unfiltered Telegram and Reddit commentary for true AI innovation.  
**Plan:**  
1. Execute a GitHub scrape for raw commits and diffs from AI repositories to capture live innovation.  
2. Use `telethon` to scrape multiple Telegram AI channels for raw links and metadata, saving output as `telegram_ai_links.json`.  
3. Gather unvoted Reddit comments from relevant threads (r/MachineLearning, r/StableDiffusion) for insights, filtered for relevance to emerging trends.  
4. Analyze and aggregate data from GitHub commits, Telegram links, and Reddit comments to identify novel AI concepts/providers.  
5. Document findings in a comprehensive report, emphasizing uncurated, diverse insights into AI advancements.  
**What changed:** The focus shifted from curated sources to raw data collection for a genuine representation of AI innovation.
