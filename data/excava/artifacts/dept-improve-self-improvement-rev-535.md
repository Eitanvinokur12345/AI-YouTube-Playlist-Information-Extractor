# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-535` (dept) · 2026-08-03T02:03:00.039513+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in CI with a staged dry-run—start with a single, low-risk rule (e.g., "require a description") enforced only on maintainer PRs for one week, then expand to all contributors and additional rules if the first passes without real-work blocks.

**Plan:**
1. Configure PR-Agent in CI with dry-run mode disabled (enforce rules) for the "require a description" rule.
2. Apply the rule only to PRs from the maintainer team for one week.
3. Monitor for false positives/blocks and gather reviewer feedback.
4. If no real-work blocks occur, expand enforcement to all contributors for the same rule.
5. After one week of clean enforcement, add the next least controversial rule (e.g., "no trailing whitespace") and repeat.
6. Once 3+ rules pass without issues, enable dry-run mode for broader validation before finalizing rules.

**What changed:** Enforced PR-Agent rules in CI with staged rollout, starting with maintainers and a single rule.
