# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-758` (dept) · 2026-08-21T22:32:31.521515+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 7 days.

**Plan:**
1. Call Product Hunt’s API endpoint `/posts` with query parameters:
   - `tag=AI`
   - `newer_than=7d`
   - `fields=title,description,upvotes,launch_date`
2. Parse the JSON response to extract raw product data (titles, descriptions, upvotes, dates).
3. Store the results in a structured format (e.g., CSV/JSON) for downstream processing.
4. Deduplicate entries by `title` and `launch_date` to avoid duplicates.
5. Enrich each entry with metadata (e.g., `source=ProductHunt`, `category=AI`).
6. Pass the cleaned dataset to the next stage (e.g., LLM summarization or cross-referencing with other sources).

**What changed:**
Focused on Product Hunt’s API as the first step to gather AI product data, prioritizing diversity of sources over immediate breadth.
