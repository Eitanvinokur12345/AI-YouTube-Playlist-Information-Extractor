# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-152` (dept) · 2026-07-10T06:48:18.260538+00:00
> Participants: Scoop, Factcheck, Wire · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Fetch AI news exclusively from vetted official/national/company sources (NIST, EU AI Act portal, corporate press rooms) via direct API/HTML scraping—no GitHub topics/issues.

**Plan:**
1. Identify and list authoritative sources for AI news (e.g., NIST, EU AI Act portal, relevant corporate press rooms).
2. Develop a script to scrape or call APIs from these sources for recent AI news updates.
3. Ensure to filter news items by date, focusing on those published after May 20, 2024.
4. Collect and store only news items that include timestamped headlines and direct source links.
5. Verify each news item against at least two corroborating sources to confirm credibility.

**What changed:** The focus shifted to exclusively using verified official sources for refreshing the AI news digest.
