# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-920` (dept) · 2026-07-31T16:23:35.881792+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent as a lightweight pre-filter *after* human triage to catch mechanical issues without gatekeeping.

**Plan:**
1. Configure PR-Agent to run *only* on PRs that pass human triage (e.g., labeled "ready-for-review").
2. Set PR-Agent to flag *only* mechanical issues (typos, formatting, missing docs) with auto-fix enabled.
3. Train teams to treat PR-Agent’s output as *suggestions*—not blockers—requiring human approval for fixes.
4. Audit PR-Agent’s false positives/misses monthly and adjust rules to reduce critical misses (e.g., security gaps).
5. Document the process in `CONTRIBUTING.md` and team onboarding.
6. Measure impact via PR cycle time and human review load (target: 20% reduction in trivial comments).

**What changed:** PR-Agent now runs post-triage as a cleanup tool, preserving human ownership of context-heavy decisions.
