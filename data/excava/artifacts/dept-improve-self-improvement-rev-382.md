# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-382` (dept) · 2026-07-31T17:26:59.211840+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Gate PR-Agent on high-confidence mechanical checks only (linting, dependency hygiene), with human review mandatory for all other PRs—no gatekeeping.

**Plan:**
1. Configure PR-Agent to auto-run only on verifiable mechanical checks (e.g., linting, dependency hygiene).
2. Remove PR-Agent as a gatekeeper; it provides suggestions but does not block PRs.
3. Require human review for all PRs, regardless of PR-Agent output.
4. Train teams to treat PR-Agent as an assistive tool, not a final authority.
5. Audit PR-Agent’s false positive rate quarterly and adjust mechanical check thresholds.
6. Document the policy in the team’s PR review guidelines.

**What changed:**
PR-Agent no longer blocks PRs; humans retain full judgment for all reviews.
