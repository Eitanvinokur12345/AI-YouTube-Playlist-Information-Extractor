# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-797` (dept) · 2026-08-01T19:47:26.835200+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use HN’s API to fetch all "AI" posts from the last 7 days, capturing titles, URLs, upvotes, and submission times.
2. Store the raw JSON response in a dated file (e.g., `hn_ai_YYYYMMDD.json`) for downstream processing.
3. Validate the dataset for completeness (e.g., no missing fields, correct date range).
4. Log the operation (timestamp, file path, record count) for reproducibility.
5. Schedule daily execution (e.g., via GitHub Actions or cron) to maintain a rolling dataset.
6. Document the process in a `README.md` for future contributors.

**What changed:** Focus shifted from broad social scraping to a targeted HN API sweep for structured, trending AI discussions.
