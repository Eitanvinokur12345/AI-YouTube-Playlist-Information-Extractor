# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-305` (dept) · 2026-07-31T11:43:25.458490+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a 48-hour automated sweep across GitHub, Hacker News, Product Hunt, Reddit (r/MachineLearning, r/artificial, r/learnmachinelearning), and Telegram (AI-focused channels) for AI tools released in the last 7 days.
2. Extract project names, links, one-line summaries, and metadata (e.g., stars, upvotes, launch date).
3. Deduplicate entries and filter for relevance (exclude non-AI tools, spam, or duplicates).
4. Curate a final list prioritizing diversity (tools, discussions, launches) and freshness.
5. Format output as GitHub-flavored markdown with headers, links, and summaries.
6. Publish the list in a public repo with a README explaining methodology and update cadence.

**What changed:** Expanded scope to include Telegram and stricter deduplication, with a 48-hour window for thoroughness.
