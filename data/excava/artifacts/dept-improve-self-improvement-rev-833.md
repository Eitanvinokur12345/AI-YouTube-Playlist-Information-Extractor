# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-833` (dept) · 2026-07-30T21:33:47.064068+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Auto-apply *only* formatting tweaks immediately; route all dependency updates—including patch-level—to human review after full-suite + integration tests.

**Plan:**
1. Configure PR-Agent to strip whitespace/style noise in real-time (no logic changes).
2. Add a pre-commit hook to reject PRs with formatting violations before review.
3. Route all dependency updates (patch/minor/major) to a dedicated "deps-review" label.
4. Require full-suite + integration tests to pass before deps-review label is removed.
5. Auto-assign dependency PRs to a human reviewer for final approval.
6. Log all auto-applied formatting tweaks in a public changelog.

**What changed:**
Dependency updates now require human review; formatting is auto-cleaned.
