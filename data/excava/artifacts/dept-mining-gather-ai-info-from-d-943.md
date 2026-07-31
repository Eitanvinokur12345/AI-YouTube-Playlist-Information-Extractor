# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-943` (dept) · 2026-07-31T16:24:04.404999+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep Reddit’s AI-related subreddits (r/MachineLearning, r/artificial, r/singularity, r/StableDiffusion, r/LocalLLaMA) for the last 7 days and extract 60 high-signal items with titles, engagement metrics, and key takeaways.
2. Sweep Product Hunt’s AI-related launches from the last 7 days and extract the top 10 most promising ones by upvotes and engagement, including launch date, upvotes, and a short description.
3. Combine both datasets into a unified ranked list prioritizing Reddit’s high-signal items (60) and supplementing with Product Hunt’s top 10.
4. Clean and deduplicate entries, then format into a structured GitHub markdown table with columns: Source, Title, Engagement, Key Takeaways, and Launch Date.
5. Validate top 20 entries for accuracy and relevance, then export as a final ranked list.

**What changed:** Combined Reddit’s high-signal breadth with Product Hunt’s trending focus to maximize diversity and quality.
