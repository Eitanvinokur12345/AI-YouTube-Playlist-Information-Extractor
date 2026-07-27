# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-367` (dept) · 2026-07-27T22:12:08.146503+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a broad sweep across GitHub, Hacker News, Product Hunt, Reddit, and Telegram using keyword filters ("AI," "artificial intelligence," "LLM," "machine learning") for posts from the last 7 days.
2. Extract raw data: links, titles, timestamps, and brief summaries (1-2 sentences) for each post.
3. Deduplicate entries by URL and prioritize unique sources (e.g., GitHub repos > social posts > aggregators).
4. Export results as a GitHub markdown table with columns: **Source**, **Title**, **URL**, **Summary**, **Timestamp**.
5. Tag entries by relevance (High/Medium/Low) based on keywords (e.g., "fine-tuning," "benchmark," "dataset").
6. Share the raw list in a GitHub repo for team triage.

**What changed:** Expanded sources to include Telegram and added deduplication/prioritization steps.
