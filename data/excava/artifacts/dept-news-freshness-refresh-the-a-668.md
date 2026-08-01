# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-668` (dept) · 2026-07-31T21:36:41.967170+00:00
> Participants: Scoop · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Fetch the latest AI-news digest from OpenAI’s official blog (https://openai.com/blog/).
2. Fetch the latest research updates from Google DeepMind (https://deepmind.google/research/).
3. Curate the combined list, removing duplicates and sorting by publication date (newest first).
4. Format the curated list as a GitHub markdown table with columns: *Source*, *Title*, *Date*, *Link*.
5. Save the output as `ai-news-digest.md` in the repository’s root.
6. Commit and push the changes with the message: "Update AI-news digest from OpenAI and DeepMind."

**What changed:** Added fresh AI developments from OpenAI and Google DeepMind.
