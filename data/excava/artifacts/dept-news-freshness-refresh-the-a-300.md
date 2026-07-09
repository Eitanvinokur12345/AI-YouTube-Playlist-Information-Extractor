# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-300` (dept) · 2026-07-09T23:49:50.311945+00:00
> Participants: Scoop, Factcheck, Wire · synthesized by gh-models/openai/gpt-4o-mini

**Decision:**  

1. Fetch the 50 newest v1+ arXiv cs.AI items with titles.
2. Pull 30 NVIDIA Developer Blog posts published in the last 30 days.
3. Retrieve the 20 latest effective entries from the EU AI Act registry.
4. Merge and deduplicate the items into a single markdown file.
5. Sort the final output by timestamp, with the newest items first.
6. Include the source, title, and URL for each entry in the markdown digest.

**What changed:** Incorporated a timestamp check for recency and ensured only effective entries from the EU AI Act registry are included.
