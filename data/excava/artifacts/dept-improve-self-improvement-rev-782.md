# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-782` (dept) · 2026-07-31T17:06:21.333650+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Use PR-Agent for initial triage (high-confidence mechanical checks only) then route to human review—humans must justify dismissing any flagged issue in writing.

**Plan:**
1. Configure PR-Agent to run only high-confidence checks (e.g., linting, dependency vulnerabilities, syntax errors).
2. Set PR-Agent as a *non-blocking* initial triage step—PRs pass to humans even if checks fail.
3. Require written justifications (via PR comments) for any dismissed PR-Agent feedback.
4. Rotate PR-Agent’s role periodically to prevent over-reliance (e.g., alternate between triage and advisory modes).
5. Track false positives and adjust high-confidence thresholds quarterly.
6. Document the process in team onboarding and PR templates.

**What changed:** PR-Agent now flags only verifiable issues before human review, with mandatory written justifications for dismissals.
