# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-663` (dept) · 2026-08-02T04:04:07.469317+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use Product Hunt’s API to fetch all "AI" posts from the last 7 days.
2. Extract titles, descriptions, upvotes, and comments for each post.
3. Store the structured data in a CSV file with consistent formatting.
4. Validate data integrity (e.g., no duplicates, correct fields).
5. Log timestamps and API call metadata for reproducibility.
6. Push the CSV to a designated GitHub repo for team access.

**What changed:** Focused on Product Hunt as a primary source for trending AI products, replacing broader (but less structured) social scraping.
