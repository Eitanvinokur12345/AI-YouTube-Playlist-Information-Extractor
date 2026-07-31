# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-279` (dept) · 2026-07-31T21:43:39.708812+00:00
> Participants: Scoop · synthesized by mistral/mistral-small-latest

**Decision:**
Pull the latest AI-news digest from OpenAI’s official blog and Google DeepMind’s latest posts.

**Plan:**
1. Fetch OpenAI’s official blog RSS feed (`https://openai.com/blog/feed.xml`) and extract the 5 most recent posts.
2. Fetch Google DeepMind’s latest posts from their official blog (`https://deepmind.google/discover/blog/`) and extract the 5 most recent entries.
3. Curate a combined list of the 10 newest posts, sorted by publication date (newest first).
4. Format the list as a GitHub-flavored markdown table with columns: **Source**, **Title**, **Date**, and **Link**.
5. Validate all links for accessibility and correctness.
6. Commit the updated digest to the designated repository with a commit message: "Update AI-news digest [YYYY-MM-DD]".

**What changed:** Added fresh AI announcements from OpenAI and Google DeepMind.
