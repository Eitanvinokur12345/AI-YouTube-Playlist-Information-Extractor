# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

<<<<<<< HEAD
> Decision artifact · room `dept-mining-gather-ai-info-from-d-898` (dept) · 2026-07-27T22:34:27.407484+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest
=======
> Decision artifact · room `dept-mining-gather-ai-info-from-d-898` (dept) · 2026-07-27T21:40:27.738492+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest
>>>>>>> ac0076f2712f73090f43ddf91027d96145eb0da7

**Decision:**

**Plan:**
<<<<<<< HEAD
1. Run a GitHub search for repos tagged "AI" and "research" created in the last 30 days.
2. Filter results for non-JavaScript languages and repos with ≥10 stars.
3. Extract purpose, tech stack, and star growth rate for each repo.
4. Rank the top 20 repos by star growth rate.
5. Output the ranked list in GitHub markdown format.

**What changed:** Added "research" tag and explicit star threshold to the GitHub sweep.
=======
1. Run a broad sweep across GitHub, Hacker News, Product Hunt, Reddit (r/MachineLearning, r/artificial, r/learnmachinelearning), and Telegram (AI-focused channels) for AI-related posts in the last 7 days.
2. Filter results for discussions on new models, tools, or controversies (e.g., benchmarks, releases, ethical debates).
3. Extract links, titles, and key excerpts (1-2 sentences max) for each post.
4. Compile into a structured GitHub markdown table with columns: Source, Title, Link, Excerpt, Date.
5. Tag posts by relevance (High/Medium/Low) based on potential for actionable AI insights.
6. Export as a single `.md` file in a dedicated repo folder (`/raw-data/ai-sweep-YYYYMMDD.md`).

**What changed:** Focus shifted from "diverse sources" to a systematic, extractable dataset with clear triage criteria.
>>>>>>> ac0076f2712f73090f43ddf91027d96145eb0da7
