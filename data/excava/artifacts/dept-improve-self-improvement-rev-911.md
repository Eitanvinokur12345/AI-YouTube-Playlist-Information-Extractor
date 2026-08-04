# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-911` (dept) · 2026-08-04T09:38:36.440258+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Run PR-Agent in shadow mode on both the oldest merged PR and the newest open PR simultaneously to compare stable and unstable routing paths.
**Plan:**
1. Identify the oldest merged PR and the newest open PR in the repository.
2. Run PR-Agent in shadow mode on both identified PRs simultaneously to gather data on routing flaws.
3. Compare and analyze the results from both PRs to identify flaws and trade-offs in routing paths.
4. Report the findings, including routing flaws and compute cost trade-offs, to Overhaul for review.
5. Implement safe changes based on the analysis, ensuring data-driven decisions for self-improvement.
**What changed:** The approach to running PR-Agent in shadow mode now includes simultaneous testing of both the oldest merged PR and the newest open PR for comprehensive insight into routing flaws.
