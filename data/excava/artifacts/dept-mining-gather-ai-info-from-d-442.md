# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-442` (dept) · 2026-07-31T18:37:52.875615+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy a real-time scraper targeting GitHub, Hacker News, Product Hunt, Reddit (r/MachineLearning, r/artificial, r/learnmachinelearning), and Telegram AI channels for posts in the last 24 hours.
2. Filter results for AI-related keywords (e.g., "LLM", "diffusion", "neural", "AI", "ML") and exclude job postings/job boards.
3. Curate top 20-30 posts by engagement (upvotes, stars, comments) and novelty (unique tools/models).
4. Generate concise summaries (1-2 sentences) with direct links for each entry.
5. Output as a GitHub-flavored markdown table with columns: **Source**, **Title/Post**, **Summary**, **Link**, **Engagement Metric**.
6. Schedule automated runs every 6 hours and push to a dedicated repo.

**What changed:** Focus shifted from broad "AI info" to high-signal, diverse sources with exclusion of job spam and structured output.
