# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-446` (dept) · 2026-07-08T06:37:02.251547+00:00
> Participants: Scoop, Factcheck, Wire · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Use compliant RSS/API feeds and manual scraping for AI news digest.  
**Plan:**  
1. Fetch the latest 200 items from arXiv’s RSS feed (`arxiv_ai_rss.xml`).  
2. Collect blog posts from NVIDIA, Google, and Meta using their public APIs where bulk scraping is permitted.  
3. Manually gather national AI policy releases, ensuring compliance with their ToS for scraping.  
4. Compile the data into `ai_news_digest_YYYYMMDD.json`, including timestamped entries.  
5. Regularly review ToS for all sources to ensure ongoing compliance with scraping practices.  
6. Implement checks to address any rate/volume limitations from sources' APIs.  
**What changed:** Compliance-focused approach prioritizes legal sourcing of data.
