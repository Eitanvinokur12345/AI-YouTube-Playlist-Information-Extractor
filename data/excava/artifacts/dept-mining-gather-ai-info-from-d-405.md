# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-405` (dept) · 2026-07-31T11:22:01.630905+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. **Telegram sweep (immediate):** Extract AI-related posts from the last 7 days in "AI Tools" and "AI News" channels, compiling titles, sources, and relevance notes.
2. **GitHub sweep (next 24h):** Query AI-related repositories created/updated in the last 7 days, capturing titles, links, and brief relevance summaries.
3. **Hacker News sweep (next 24h):** Scrape top AI-related posts from the last 7 days, including titles, URLs, and relevance notes.
4. **Product Hunt sweep (next 24h):** Pull AI-related launches from the last 7 days, with titles, sources, and relevance notes.
5. **Reddit sweep (next 48h):** Aggregate AI posts from r/MachineLearning, r/artificial, and r/learnmachinelearning (last 7 days), with titles, subreddit links, and relevance notes.
6. **Curate & merge:** Combine all sources into a single markdown table with columns: Title | Source | Relevance | Date.

**What changed:** Expanded scope to include all debated platforms (GitHub/HN/Product Hunt/Reddit/Telegram) with staggered execution over 48 hours.
