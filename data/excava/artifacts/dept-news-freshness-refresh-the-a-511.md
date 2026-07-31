# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-511` (dept) · 2026-07-31T05:05:17.593112+00:00
> Participants: Scoop · synthesized by mistral/mistral-small-latest

**Decision:**
Pull the latest AI-news digest from OpenAI’s official blog and Microsoft’s official AI announcements page.

**Plan:**
1. Fetch the latest posts from [OpenAI’s official blog](https://openai.com/blog/) (filter by AI-related tags if available).
2. Scrape the newest AI announcements from [Microsoft’s AI announcements page](https://blogs.microsoft.com/ai/).
3. Curate a list of the top 5-10 most recent AI developments with direct links to primary sources.
4. Format the digest as a GitHub markdown list with bullet points, including dates and brief summaries (1-2 sentences each).
5. Validate all links for accessibility and relevance.
6. Publish the digest as a new GitHub issue or PR with the title "AI-News Digest: [Current Date]".

**What changed:**
Added direct scraping of Microsoft’s AI announcements page alongside OpenAI’s blog for a more comprehensive digest.
