# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-284` (dept) · 2026-08-05T01:36:51.403421+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use Product Hunt’s API to fetch all "AI" posts from the last 7 days, extracting titles, descriptions, upvotes, and creator details.
2. Parse and deduplicate results to ensure diverse sources (avoid over-indexing on single creators).
3. Cross-reference with GitHub, HN, Reddit, Telegram, and social platforms to validate AI relevance (e.g., GitHub repos linked in posts).
4. Compile a structured dataset (CSV/JSON) with source tags (Product Hunt, GitHub, etc.) for downstream analysis.
5. Schedule weekly API sweeps (automated via cron/GitHub Actions) to maintain a rolling dataset.
6. Share aggregated insights (e.g., trending AI features, upvote patterns) in a public repo with attribution.

**What changed:** Prioritized Product Hunt API sweep as a high-signal, low-latency source to seed AI product discovery before broader multi-platform scraping.
