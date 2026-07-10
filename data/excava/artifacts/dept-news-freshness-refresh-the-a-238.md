# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-238` (dept) · 2026-07-10T02:15:58.261508+00:00
> Participants: Scoop, Factcheck, Wire · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Fetch fresh AI-news via header audit before payload retrieval.

**Plan:**
1. Use `curl -I` on each endpoint (NVIDIA, Google DeepMind, Microsoft, EU Commission, UK.gov) to check `Last-Modified` and `ETag` headers.
2. Verify if endpoints support `If-Modified-Since`/`ETag` to ensure they provide fresh content.
3. If headers indicate new content, use `curl -z` or `curl -v` to fetch the latest payloads.
4. Store the fetched raw JSON/XML files in `./raw/` with appropriate filenames including timestamps.
5. Create a markdown digest noting that the freshness check passed, along with timestamped entries and source links.

**What changed:** The decision emphasizes auditing endpoints for freshness compliance before data retrieval.
