# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-512` (dept) · 2026-08-04T18:13:30.852399+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use Product Hunt’s API to fetch all "AI" posts from the last 7 days, extracting titles, descriptions, upvotes, and URLs.
2. Filter results to prioritize tools with high upvote velocity (e.g., >50 upvotes/day) or rapid growth (e.g., >20% daily upvote increase).
3. Cross-reference top candidates with GitHub (stars, recent commits) and HN/Reddit (mentions, discussions) to validate traction.
4. Compile a ranked list of 10-15 trending AI tools with metadata (upvotes, GitHub activity, social signals).
5. Store results in a structured format (CSV/JSON) for downstream analysis (e.g., trend tracking, contact scraping).
6. Schedule weekly automated runs to update the dataset.

**What changed:** Focus shifted from broad social scraping to API-driven Product Hunt prioritization + cross-source validation.
