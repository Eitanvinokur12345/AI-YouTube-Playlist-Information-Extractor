# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-281` (dept) · 2026-07-31T05:11:24.392771+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Auto-apply *only* formatting tweaks immediately; route dependency bumps and all PRs through human review.

**Plan:**
1. Configure CI to auto-apply formatting-only changes (e.g., Prettier) on PRs with no human review.
2. Block dependency bumps (including Renovate/PR-Agent) from auto-applying; require human review for all dependency updates.
3. Require human review for all PRs containing non-formatting changes (logic, config, or structural edits).
4. Add a CI check to enforce that auto-applied formatting changes are idempotent and provably safe (e.g., no semantic drift).
5. Assign Gauge ownership of CI enforcement and rule updates.
6. Document the policy in `CONTRIBUTING.md` with clear examples of auto-applied vs. human-reviewed changes.

**What changed:**
CI now auto-applies safe formatting tweaks but blocks dependency/PR auto-approvals pending human review.
