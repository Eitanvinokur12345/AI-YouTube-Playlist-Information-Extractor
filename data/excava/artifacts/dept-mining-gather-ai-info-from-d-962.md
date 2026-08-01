# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-962` (dept) · 2026-08-01T04:04:24.425618+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use HN’s API to fetch all "AI" posts from the last 7 days, extracting titles, URLs, and upvotes.
2. Filter and sort posts by upvotes to identify the top 10 most-upvoted.
3. For each post, extract key themes (e.g., "LLM," "fine-tuning," "ethics") from titles/URLs.
4. Compile results into a concise GitHub markdown table with columns: Rank | Title | URL | Upvotes | Key Themes.
5. Store the dataset in a new repo branch (`hn-ai-mining-raw`) for downstream analysis.
6. Log execution time and post count in a `README.md` metadata section.

**What changed:** Focus shifted from broad social mining to a targeted HN sweep for high-signal AI content.
