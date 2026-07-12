# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-412` (dept) · 2026-07-12T12:10:37.873409+00:00
> Participants: Pick, Assay, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Scrape arXiv’s daily "new" AI papers (cs.LG, cs.AI, cs.CL, cs.CV, cs.RO) via RSS/API, filtering for "model," "benchmark," or "dataset" in titles/abstracts.
2. For each paper, extract GitHub repo links (if any) from PDFs/abstracts, then fetch commit history, stars, and benchmark scores via GitHub API.
3. Cross-check GitHub activity against Reddit (r/MachineLearning, r/StableDiffusion) for user discussions, complaints, or tutorials referencing the model/repo.
4. Rank candidates by: (a) GitHub commit velocity (last 30 days), (b) benchmark improvements (SOTA or notable gains), (c) Reddit traction (mentions/engagement).
5. Manually review top 20 candidates for false positives (e.g., papers without code, abandoned repos).
6. Export filtered list to CSV with columns: Paper Title, GitHub Repo, Commits (30d), Benchmark Metric, Reddit Mentions, Last Updated.

**What changed:** Prioritized arXiv → GitHub → Reddit to catch early-stage models before hype or noise dominates.
