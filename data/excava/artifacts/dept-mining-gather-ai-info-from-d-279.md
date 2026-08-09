# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-279` (dept) · 2026-08-04T23:36:34.579541+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use Product Hunt’s API to fetch all "AI" posts from the last 7 days, extracting titles, descriptions, upvotes, and comments.
2. Apply initial filtering to remove duplicates, non-English posts, and irrelevant content (e.g., job postings, non-AI tools).
3. Store raw data in a structured format (e.g., JSON/CSV) for further analysis.
4. Cross-reference filtered results with GitHub/HN/Reddit/Telegram to identify overlapping or complementary AI discussions.
5. Prioritize posts with high engagement (upvotes/comments) for deeper extraction of AI-related insights.
6. Document metadata (source, timestamp, engagement metrics) for traceability.

**What changed:** Focus shifted from broad social scraping to a targeted API-driven approach for Product Hunt, ensuring efficiency and scalability.
