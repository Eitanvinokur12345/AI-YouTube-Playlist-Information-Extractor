# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-872` (dept) · 2026-07-10T10:04:55.169316+00:00
> Participants: Scoop, Factcheck, Wire · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Fetch arXiv AI papers via API v2 (`http://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&sortOrder=descending&max_results=100`) with `start=0` and `max_results=100`.
2. Pull NVIDIA dev blog posts via JSON feed (`https://blogs.nvidia.com/blog/category/ai/feed/json`) filtered to last 24h.
3. Query EU AI Act registry API (`https://ai-act-registry.ec.europa.eu/api/updates?limit=50&since=24h`) for structured updates.
4. Scrape MIT Tech Review AI vertical via JSON endpoint (`https://www.technologyreview.com/api/v1/articles/?tag=ai&limit=50&since=24h`).
5. Deduplicate entries by URL and timestamp, keeping the newest per source.
6. Output to `ai-news-digest.json` with fields: `source`, `title`, `url`, `timestamp`, `summary` (truncated to 150 chars).

**What changed:** Excluded HTML/RSS; enforced API-only, 24h max age, and structured JSON output.
