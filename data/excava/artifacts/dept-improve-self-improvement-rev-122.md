# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-122` (dept) · 2026-07-31T18:30:11.966855+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent as a gatekeeper for *only* mechanical, verifiable issues (linting, test failures, docs gaps) and auto-apply safe fixes—humans handle everything else.

**Plan:**
1. Configure PR-Agent to enforce linting, test failures, and docs gaps as gatekeepers.
2. Auto-apply safe fixes (e.g., formatting) for mechanical issues.
3. Route subjective decisions (design, trade-offs) to humans with clear criteria.
4. Measure PR-Agent’s impact on PR velocity and issue resolution rates.
5. Review gatekeeping criteria quarterly to ensure alignment with team goals.
6. Document the process in the team’s engineering handbook.

**What changed:**
PR-Agent now enforces mechanical checks while deferring subjective decisions to humans.
