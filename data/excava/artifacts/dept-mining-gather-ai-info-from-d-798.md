# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-798` (dept) · 2026-07-31T17:27:12.653574+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use a web scraper (e.g., Python + `requests`/`BeautifulSoup`) to fetch Product Hunt’s "AI" launches from the last 7 days.
2. Parse each launch’s title, upvotes, core value proposition, launch date, and maker handle.
3. Rank projects by upvotes and select the top 10.
4. Format results into a GitHub markdown table with columns: Rank, Project Name, Core Value Prop, Launch Date, Maker Handle.
5. Store the output in a dedicated repo file (e.g., `trending_ai_product_hunt.md`).
6. Share the file with the team for evaluation.

**What changed:** Focus narrowed to Product Hunt’s AI launches (last 7 days) for a concise, high-signal dataset.
