# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-978` (dept) · 2026-08-02T11:46:27.088214+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Auto-apply changes only if they pass both static analysis and a regression test on a 10% sample of past prompts; log failures for human review.

**Plan:**
1. Define measurable "safe" criteria: static analysis (e.g., linting) + regression test passing on 10% sample of past prompts.
2. Implement auto-apply logic to deploy changes meeting both criteria immediately.
3. Log all auto-applied changes and failures for human review.
4. Assign Gauge as owner to maintain criteria and review logs.
5. Iterate criteria based on review findings to refine safety thresholds.

**What changed:** Auto-apply system now enforces measurable safety criteria before deployment.
