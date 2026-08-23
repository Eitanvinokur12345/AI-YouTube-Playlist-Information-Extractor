# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-790` (dept) · 2026-08-23T07:14:21.454580+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in shadow mode on all PRs—open and merged—for two weeks to validate routing/prompts without compute risk, then reassess.

**Plan:**
1. Enable PR-Agent in shadow mode for all PRs (open and merged) for 14 days.
2. Log feedback hit rate (useful feedback per PR) and reviewer noise levels (ignored autofeedback frequency).
3. Collect routing/prompt edge cases identified during the trial.
4. Lead synthesizes data into a summary report with hit rate vs. noise analysis.
5. Lead proposes next steps (e.g., full rollout, sampling, or heuristic-based filtering).
6. Team approves final path forward based on report.

**What changed:** PR-Agent now runs in shadow mode on all PRs for validation.
