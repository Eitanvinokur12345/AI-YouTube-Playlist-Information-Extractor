# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-339` (dept) · 2026-07-30T07:16:45.888533+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Browse r/MachineLearning and r/AI (last 7 days) to extract top 10 AI tools/frameworks/datasets.
2. For each entry, record: name, key claims, trade-offs, and user sentiment (positive/neutral/negative).
3. Compile results into a GitHub markdown table with columns: Rank, Name, Claims, Trade-offs, Sentiment.
4. Cross-check claims against GitHub/HN/Product Hunt/Reddit/Telegram for consistency.
5. Finalize report with a 1-sentence summary of trends (e.g., "LLM fine-tuning tools dominate sentiment").
6. Push to GitHub repo with filename `ai-tools-synthesis-YYYYMMDD.md`.

**What changed:** Focus narrowed to Reddit-only for initial extraction, then cross-verified with other sources.
