# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-927` (dept) · 2026-07-31T18:31:03.731215+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy a real-time web scraper (e.g., Scrapy + Playwright) to monitor GitHub (new repos), Hacker News (front page + "Show HN"), Product Hunt (daily top posts), Reddit (r/MachineLearning, r/ArtificialIntelligence, r/learnmachinelearning), and Telegram (AI-focused channels).
2. Filter results for AI-related keywords (e.g., "LLM", "diffusion", "neural", "transformer") and exclude low-signal content (e.g., spam, outdated repos).
3. Rank items by GitHub stars (recent growth), HN upvotes, or Reddit engagement, prioritizing diversity of sources.
4. Manually curate a final list of 10-20 items, adding 1-sentence context for each (e.g., "New open-source diffusion model with 5K+ stars in 3 days").
5. Output as a GitHub markdown table with columns: **Source**, **Title/Link**, **Signal Summary**, **Impact Score** (1-5).
6. Schedule daily automated runs with Slack/email alerts for new high-impact items.

**What changed:** Switched from ad-hoc scraping to a systematic, real-time pipeline with ranked output and automated alerts.
