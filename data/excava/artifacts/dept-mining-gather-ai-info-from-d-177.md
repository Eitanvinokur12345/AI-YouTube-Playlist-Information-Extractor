# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-177` (dept) · 2026-07-27T22:25:55.438271+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a broad sweep across GitHub, Hacker News, Product Hunt, Reddit, and Telegram for AI-related posts from the last 7 days.
2. Extract raw links, titles, and brief summaries for each source.
3. Compile findings into a structured GitHub markdown table with columns: Source, Link, Title, Summary, and Date.
4. Tag posts by relevance (High/Medium/Low) based on keywords (e.g., "AI," "LLM," "neural network").
5. Export the table to a CSV for further analysis.
6. Schedule a follow-up review to refine the dataset and remove duplicates.

**What changed:** Focus expanded to include Telegram and structured output for scalability.
