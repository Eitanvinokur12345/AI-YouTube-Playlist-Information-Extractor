# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-971` (dept) · 2026-07-08T17:17:53.453810+00:00
> Participants: Pick, Assay, Boulder · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Cast a wide net—scrape GitHub repos by *description keywords* ("machine learning", "AI", "deep learning", "neural", "LLM") + HN/Product Hunt/Reddit/Telegram scrapes for AI tool links, no tags.

**Plan:**
1. Execute a GitHub scrape command using:  
   `gh search repos --json name,description,stargazers_count,updatedAt --limit 500 --order updated --sort updated --q "machine learning OR AI OR deep learning OR neural OR LLM"`
2. Conduct a parallel scrape on Hacker News for AI-related discussions and links.
3. Collect data from Product Hunt focusing on new AI tools and resources.
4. Monitor Reddit for trending AI posts and tools in relevant subreddits (e.g., r/MachineLearning, r/artificial).
5. Explore Telegram channels that focus on AI developments for shareable resources and tool links.
6. Compile all gathered information into a cohesive database for further analysis.

**What changed:** The plan now includes a broader approach, tapping into descriptions and multiple platforms for comprehensive AI resource gathering.
