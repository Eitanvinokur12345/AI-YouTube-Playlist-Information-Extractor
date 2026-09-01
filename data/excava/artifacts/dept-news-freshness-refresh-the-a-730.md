# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-730` (dept) · 2026-09-01T04:42:34.804683+00:00
> Participants: Scoop, Factcheck, Wire · synthesized by mistral/mistral-small-latest

**Decision:** Wire will refresh the AI-news digest by extracting the latest OpenAI research or product announcement.

**Plan:**
1. Parse OpenAI’s official blog feed ([https://openai.com/blog](https://openai.com/blog)).
2. Filter posts for AI research or product announcements.
3. Identify the newest post by date.
4. Extract the title, date, and a 2-sentence summary.
5. Provide the artifact link (URL) to the post.
6. Return the structured output in GitHub markdown.

**What changed:** Scope clarified to "AI research or product announcements" for OpenAI’s blog feed.
