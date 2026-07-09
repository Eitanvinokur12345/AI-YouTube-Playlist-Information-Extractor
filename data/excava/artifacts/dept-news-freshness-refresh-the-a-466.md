# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-466` (dept) · 2026-07-09T04:00:45.859292+00:00
> Participants: Wire, Scoop, Factcheck · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Scrape structured AI feeds from arXiv, EU AI Act portal, and NIST AI RMF updates to ensure official and real-time sources for AI news.

**Plan:**
1. Access arXiv's API to retrieve the latest papers on AI using their structured feed.
2. Monitor the EU AI Act portal for any updates via their RSS feed.
3. Scrape the NIST AI RMF updates through their official API to gather relevant news.
4. Compile the gathered information into a JSON file named `ai-news-digest.json`, ensuring it includes timestamp, headline, URL, source, and relevance score.
5. Ensure a minimum of 50 fresh AI-related articles are captured from the official sources.
6. Validate the accuracy and relevance of the information before finalizing the digest.

**What changed:** Focus shifted to exclusively use structured feeds from official sources to avoid inaccuracies.
