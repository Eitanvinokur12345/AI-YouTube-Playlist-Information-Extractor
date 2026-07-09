# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-760` (dept) · 2026-07-09T14:41:58.167556+00:00
> Participants: Scoop, Factcheck, Wire · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Parse NIST SP 800-22b PDFs via their GitHub repo (`https://github.com/usnistgov/SP-800-22b-Updates`) for official AI-related standards updates.
2. Fetch EU AI Act legal text via EUR-Lex API (`https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689`) for the latest AI Act regulations.
3. Scrape top-5 AI vendors’ official JSON feeds (e.g., NVIDIA’s `https://blogs.nvidia.com/feed/`, Google AI’s `https://ai.googleblog.com/feeds/posts/default`) for AI announcements.
4. Store raw artifacts in `./digest/2024-06-28-raw.{pdf,json,xml}` with parsed markdown in `./digest/2024-06-28.md` (top 20 AI-related items).
5. Apply a 3-step filter (`grep -E "AI|artificial intelligence|machine learning"`) to the parsed markdown for relevance.
6. Validate sources against official endpoints before finalizing the digest.

**What changed:** Shifted from scraping HTML to parsing official feeds/APIs and structured raw storage for completeness.
