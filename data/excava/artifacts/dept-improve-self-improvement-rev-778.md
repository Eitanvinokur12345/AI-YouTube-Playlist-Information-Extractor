# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-778` (dept) · 2026-07-30T18:22:12.488040+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Auto-apply PR-Agent style/doc fixes only to files with recent human approval (last 30 days), blocking merges if PR-Agent score drops below 90%.

**Plan:**
1. Configure PR-Agent to auto-apply style/doc fixes only to files modified in PRs where all touched files were approved by humans in the last 30 days.
2. Set PR-Agent merge block if its score for a PR drops below 90%.
3. Document the rule in the team’s PR review guidelines and tooling docs.
4. Run a 2-week pilot on a non-critical repo to validate false positives/negatives.
5. Adjust the 30-day window or 90% threshold based on pilot feedback.
6. Roll out to all repos after pilot success.

**What changed:** Auto-apply scope restricted to recently human-approved files, with risk-based merge blocking.
