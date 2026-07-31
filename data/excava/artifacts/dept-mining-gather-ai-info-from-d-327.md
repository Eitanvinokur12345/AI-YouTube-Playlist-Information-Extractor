# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-327` (dept) · 2026-07-31T14:36:03.052421+00:00
> Participants: Pick, Boulder · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Sweep diverse sources for AI information
1. **Sweep Reddit**: Collect AI posts from the last 7 days with at least 10 upvotes, outputting top 10 threads with titles, upvotes, and subreddit names.
2. **Sweep GitHub**: Collect AI repositories created in the last 7 days with at least 10 stars, outputting top 10 with names, stars, and brief descriptions.
3. **Sweep Product Hunt**: Collect AI products launched in the last 7 days, outputting top 10 with launch dates and upvotes.
4. **Broad Sweep**: Run a broad sweep across Hacker News, Telegram, and social media for AI-related posts with at least 10 upvotes or 50 views.
5. **Refine Dataset**: Refine the collected datasets to identify trending AI discussions, tools, and pain points.
**What changed:** Added a broad sweep across multiple platforms to gather more comprehensive AI information.
