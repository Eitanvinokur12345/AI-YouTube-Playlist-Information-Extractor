# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-352` (dept) · 2026-07-31T16:02:27.339677+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent as a lightweight pre-filter for trivial mechanical errors, then route only the remaining 20% to humans for context-dependent review—measure false negatives vs. human catches to validate the split.

**Plan:**
1. Configure PR-Agent to auto-run on every PR, flagging only mechanical issues (e.g., linting, syntax, basic logic errors).
2. Route PR-Agent’s output to a dedicated "trivial errors" label, auto-applied to PRs with no human-flagged issues.
3. Require human reviewers to explicitly acknowledge the "trivial errors" label before approving, ensuring no blind trust in automation.
4. Track false negatives by logging PR-Agent-missed issues and comparing against human catches over 30 days.
5. Adjust the split (e.g., 15%/85%) if false negatives exceed 5% of context-dependent issues.
6. Document the policy in the repo’s `CONTRIBUTING.md` with clear thresholds for escalation.

**What changed:** PR-Agent now pre-filters trivial errors; humans handle only context-dependent reviews, validated by false-negative metrics.
