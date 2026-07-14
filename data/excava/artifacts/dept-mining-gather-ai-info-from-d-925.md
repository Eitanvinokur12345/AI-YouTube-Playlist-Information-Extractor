# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-925` (dept) · 2026-07-14T23:05:51.179748+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub API to fetch AI repos created/updated in last 30 days, sorted by stars.
2. Scrape Hacker News (top posts in "AI" tag), Product Hunt (trending AI products), and Reddit (r/MachineLearning, r/artificial) for high-engagement posts.
3. Manually check Telegram channels (e.g., AI/ML groups) for recent AI tool announcements with high reactions.
4. Cross-reference results to filter duplicates and prioritize projects with >50 stars/upvotes/comments.
5. Compile a curated list with direct links, engagement metrics, and brief descriptions.
6. Export as GitHub-flavored markdown table with columns: Name, Source, Link, Metrics, Description.

**What changed:** Focused on high-engagement metrics across 5 diverse sources, replacing vague "curated list" with explicit API/scraping steps and a structured output format.
