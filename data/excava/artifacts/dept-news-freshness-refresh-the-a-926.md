# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-926` (dept) · 2026-07-08T12:10:54.591729+00:00
> Participants: Scoop, Factcheck, Wire · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Pull *live* preprint (arXiv/bioRxiv) + *real-time* conference feeds (NeurIPS/ICML RSS + OpenReview API) with timestamped hashes to guarantee freshness and verifiable sourcing.

**Plan:**
1. Scrape the latest 10 AI papers from arXiv using a command that avoids stale data.
2. Collect the most recent papers from bioRxiv related to AI.
3. Fetch the latest conference papers via NeurIPS RSS feeds, ensuring no critical papers are missed.
4. Access ICML RSS feeds for additional updates on AI research.
5. Utilize the OpenReview API to gather any timely submissions relevant to AI.
6. Compile the gathered information into `AI-news-digest-YYYYMMDD_HHMMSS.txt` for distribution.

**What changed:** The approach evolved to prioritize live data and eliminate reliance on potentially stale cached sources.
