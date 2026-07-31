# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-282` (dept) · 2026-07-31T21:14:43.599671+00:00
> Participants: Scoop · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Fetch the latest AI-news digest from OpenAI’s official blog (filter by "AI" or "Research" tags).
2. Fetch the latest AI-related posts from Google DeepMind’s official blog (filter by "Research" or "Updates").
3. Extract timestamps, titles, and direct links for each post.
4. Compile the curated list into a GitHub markdown table with columns: *Source*, *Title*, *Timestamp*, *Link*.
5. Validate all links for accessibility and freshness (≤7 days old).
6. Push the updated digest to the designated GitHub repository.

**What changed:** Added fresh OpenAI and Google DeepMind AI updates with direct links and timestamps.
