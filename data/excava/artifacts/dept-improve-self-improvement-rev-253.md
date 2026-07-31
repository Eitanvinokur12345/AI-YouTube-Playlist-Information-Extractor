# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-253` (dept) · 2026-07-31T16:44:33.368532+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent only for verifiable mechanical checks (linting, dependency scans) *after* human triage, not as a gatekeeper—humans own final judgment calls on design, UX, and trade-offs.

**Plan:**
1. Configure PR-Agent to run *only* on linting and dependency bump checks (e.g., `depguard`, `golangci-lint`).
2. Update PR templates to label human triage as the first step before automated checks.
3. Add a GitHub Action workflow that runs PR-Agent *after* the first human review (or label `triage:human-approved`).
4. Document in the team’s PR review guidelines that PR-Agent is advisory, not a gatekeeper.
5. Measure false positives/negatives monthly and adjust the set of verifiable checks.
6. Deprecate any existing PR-Agent gating rules in favor of this new workflow.

**What changed:**
PR-Agent now runs *after* human triage for mechanical checks only, preserving human ownership of design/UX decisions.
