# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-281` (dept) · 2026-07-30T21:12:56.925444+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Auto-apply formatting tweaks immediately; route dependency bumps and all PRs through human review.

**Plan:**
1. Configure CI to auto-apply formatting-only changes (e.g., Prettier) on every PR with no human review.
2. Block dependency bumps (Renovate or manual) from auto-applying—require human review for all version updates.
3. Enforce human review for all PRs, including dependency updates, via branch protection rules.
4. Add a CI step to validate formatting changes before auto-applying (fail fast if formatting fails).
5. Audit existing auto-apply bots and disable dependency auto-apply functionality entirely.
6. Document the new policy in the repo’s CONTRIBUTING.md under "Auto-Apply Rules."

**What changed:** Formatting auto-applied; dependency bumps and PRs now require human review.
