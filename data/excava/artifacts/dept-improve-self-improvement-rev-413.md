# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-413` (dept) · 2026-07-30T20:50:49.615330+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Auto-apply formatting tweaks immediately; route dependency bumps to human review—formatting is zero-risk, deps carry hidden breakage.

**Plan:**
1. Implement PR-Agent with formatting auto-apply layer (post-PR-Agent, pre-human review).
2. Exclude dependency bumps from auto-apply; flag them for human review.
3. Add a `safe-formatting` label to PRs where formatting changes are applied.
4. Require explicit human approval for dependency bumps (e.g., `needs-dep-review` label).
5. Log auto-applied formatting changes in PR comments for transparency.
6. Monitor build failures from dependency bumps to refine the process.

**What changed:**
PR-Agent + formatting auto-apply layer live; dependency bumps gated behind human review.
