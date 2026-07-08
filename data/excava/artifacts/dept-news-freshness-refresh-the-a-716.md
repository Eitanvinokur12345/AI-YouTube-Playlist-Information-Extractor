# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-716` (dept) · 2026-07-08T17:17:59.490467+00:00
> Participants: Scoop, Factcheck, Wire · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Fetch raw XMLs from primary RSS feeds, validate schema/structure, and cross-check truncated content via secondary HTML scrape before JSON extraction.

**Plan:**
1. Fetch raw XMLs from NVIDIA, Google, Microsoft, and OSTP RSS feeds, saving to `/tmp/ai-news-raw/` with timestamps.
2. Validate the schema and structure of each XML feed using `xmllint`.
3. Implement a fallback by scraping the corresponding HTML pages for each source to capture full titles/descriptions.
4. Extract clean JSON summaries from the validated XMLs and HTML backups into `/tmp/ai-news-digest.json`.
5. Schedule regular updates to ensure freshness of the AI-news digest, with alerts for any feed errors or content truncation.

**What changed:** The approach now includes validation of content structure and potential fallback mechanisms to ensure accuracy and completeness of news items.
