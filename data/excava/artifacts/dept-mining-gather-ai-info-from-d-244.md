# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-244` (dept) · 2026-07-31T20:53:26.020483+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**
Run a targeted sweep across GitHub, Hacker News, Product Hunt, Reddit, and Telegram for AI-related content from the last 7 days, outputting a curated list of links, titles, and summaries.

**Plan:**
1. **GitHub:** Search for AI-related repos created in the last 7 days, extract links, names, and one-sentence summaries.
2. **Hacker News:** Scrape top AI-related posts from the last 7 days, including titles, links, and summaries.
3. **Product Hunt:** Gather AI-related products launched in the last 7 days, with titles, links, and summaries.
4. **Reddit:** Collect AI-related posts from r/MachineLearning, r/artificial, and r/learnmachinelearning from the last 7 days, with titles, links, and summaries.
5. **Telegram:** Scan AI-related channels (e.g., AI News, Future of AI) for recent posts, extracting titles, links, and summaries.
6. **Compile:** Merge all sources into a single curated list, ensuring diversity and avoiding duplicates.

**What changed:**
Expanded from GitHub-only sweep to a multi-source approach across GitHub, HN, Product Hunt, Reddit, and Telegram.
