# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-342` (dept) · 2026-08-30T03:44:39.095042+00:00
> Participants: Scoop, Factcheck, Wire · synthesized by mistral/mistral-small-latest

**Decision:**
Wire authorizes the execution of the OpenAI AI-news digest refresh.

**Plan:**
1. Parse OpenAI’s official blog feed (RSS/Atom or web scraping if no feed).
2. Filter posts for AI-related content (keywords: "AI", "artificial intelligence", "model", etc.).
3. Identify the newest post meeting criteria.
4. Generate a plain-language summary of its key points.
5. Include the publication date and a direct link to the source post.
6. Output the result in GitHub markdown format.

**What changed:**
Added requirement to include publication date and direct link in the summary.
