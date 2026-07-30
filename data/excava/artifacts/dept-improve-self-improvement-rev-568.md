# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-568` (dept) · 2026-07-30T23:57:08.510403+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Auto-apply only trivial, reversible formatting tweaks (typos, spacing) immediately; route all other prompt/routing changes through weekly human review with a changelog tracking the *why*.

**Plan:**
1. Implement a CI check to auto-apply and commit trivial formatting tweaks (typos, spacing) to non-critical prompts/routing rules.
2. For all other prompt/routing changes, require a GitHub PR with a standardized template capturing the *why* (context, impact, reversibility).
3. Schedule weekly human review of batched PRs by the prompt/routing team, with a changelog auto-generated from PR descriptions.
4. Tag non-critical paths in the codebase with a `// RISK: LOW` comment to clarify auto-apply boundaries.
5. Add a dashboard showing pending changes, applied changes, and reversibility status for transparency.
6. Conduct a quarterly audit to reassess "trivial" vs. "non-trivial" thresholds based on incident data.

**What changed:**
Non-critical paths now auto-apply only trivial formatting tweaks; all other prompt/routing changes require weekly human review with tracked rationale.
