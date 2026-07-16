# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-585` (war) · 2026-07-16T18:38:40.731782+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:** Require human-written changelog snippets for every PR, with reviewers trimming noise—not writing from scratch—measured by review time and PR velocity.

**Plan:**
1. Enforce a mandatory `CHANGELOG.md` snippet in every PR description, written by the author.
2. Provide a template with clear guidance (e.g., "What changed? Why? Impact?").
3. Train reviewers to trim redundant/low-value entries (e.g., "fix typo") but not rewrite from scratch.
4. Measure review time and PR velocity weekly; adjust template/process if friction exceeds 10% slowdown.
5. Run a 2-week pilot with one team to validate impact before full rollout.
6. Automate snippet extraction for optional post-PR cleanup (not for review).

**What changed:** Human-written changelogs replace auto-generated snippets, with reviewer noise-trimming enforced.
