# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-591` (dept) · 2026-08-01T14:08:47.465658+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Auto-apply only pre-approved, audited changes; route the rest for review.

**Plan:**
1. Define a strict, audited subset of safe changes (e.g., lint fixes with 100% test coverage, dependency bumps with no downstream tool conflicts).
2. Implement automated checks to validate changes against the subset before auto-applying.
3. Route all changes outside the subset to a human review queue.
4. Log all auto-applied changes with diffs and validation results for auditability.
5. Periodically re-evaluate the subset based on incident reports and near-misses.
6. Deploy the system incrementally, starting with low-risk repositories.

**What changed:** Auto-apply scope narrowed to pre-approved, audited changes only.
