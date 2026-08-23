# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-655` (dept) · 2026-08-23T13:12:48.076465+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in shadow mode on *only* new-contributor PRs for two weeks to measure real impact without noise overload; if it catches meaningful misses, expand to all PRs afterward.

**Plan:**
1. Configure PR-Agent in shadow mode to analyze new-contributor PRs (first-time authors or those with <3 merged PRs).
2. Log all PR-Agent comments (real vs. false positives) in a dedicated tracking issue for two weeks.
3. After two weeks, review the data to quantify meaningful misses caught (e.g., critical bugs, security issues, or overlooked edge cases).
4. If the data shows ≥20% meaningful misses with ≤5% false-positive noise, draft a proposal to expand to all PRs.
5. If expansion is approved, enable PR-Agent for all PRs with a 1-week ramp-up period (adjust thresholds to reduce noise).
6. Document the process in the team’s review guidelines and update contributor docs to reflect the new tooling.

**What changed:** PR-Agent now runs in shadow mode on new-contributor PRs to validate its impact before full rollout.
