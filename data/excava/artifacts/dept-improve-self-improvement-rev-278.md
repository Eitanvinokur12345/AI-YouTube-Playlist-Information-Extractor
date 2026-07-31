# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-278` (dept) · 2026-07-31T22:03:59.156555+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement a stratified evaluation harness that runs new prompts on:
   - 100 recycled tasks (from last 100 production inputs) for consistency checks.
   - 400 fresh diverse tasks (curated to cover edge cases and unseen distributions).
2. Compare outputs against baselines to flag regressions (accuracy drops >2%) or gains (improvements >1%).
3. Auto-apply safe changes (e.g., prompt tweaks with no regressions) via CI/CD pipeline.
4. Log all comparisons in a dashboard with diffs for manual review of edge cases.
5. Rotate recycled tasks weekly to prevent overfitting to stale data.
6. Enforce 24-hour hold on auto-applied changes, requiring manual approval for production.

**What changed:** Stratified evaluation replaces uniform batch testing.
