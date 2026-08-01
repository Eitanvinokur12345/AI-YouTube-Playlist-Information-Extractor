# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-583` (dept) · 2026-07-31T21:14:38.854701+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy a real-time scraper (e.g., Python + `requests`/`BeautifulSoup`/`Scrapy`) to sweep GitHub, Hacker News, Product Hunt, Reddit (r/MachineLearning, r/artificial), and Telegram AI channels for posts in the last 7 days.
2. Filter results for AI relevance using keyword matching (e.g., "LLM", "diffusion", "neural", "AI", "ML") and exclude spam/low-signal items.
3. Curate a list of 15–30 high-signal items, extracting titles, sources, and one-line relevance notes (e.g., "New open-source diffusion model for 3D generation").
4. Format output as GitHub-flavored markdown with headers: `## AI Sweep [YYYY-MM-DD]` → `### Curated Items` → numbered list with `**Title** (Source) - Relevance note`.
5. Schedule daily automated runs (e.g., GitHub Actions) to maintain freshness.
6. Add a `## Archive` section for historical sweeps, linked in the header.

**What changed:** Switched from "j" (ambiguous) to a focused, automated sweep across diverse sources with clear curation criteria.
