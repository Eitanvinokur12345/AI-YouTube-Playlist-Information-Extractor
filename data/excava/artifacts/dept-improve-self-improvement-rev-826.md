# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-826` (dept) · 2026-09-03T20:04:47.455969+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in parallel mode only on new contributors’ PRs for two weeks—it flags issues but lets humans override, exposing false negatives where they hurt most while keeping manual review costs low.

**Plan:**
1. Configure PR-Agent to run in parallel mode (flagging only) on PRs from contributors with <3 merged PRs in the last 6 months.
2. Log all PR-Agent flagged issues (false positives/negatives) in a dedicated tracking issue for analysis.
3. Require human override for all PR-Agent suggestions (no auto-apply) during the test period.
4. Assign a rotating reviewer to audit flagged issues and document manual overrides weekly.
5. After two weeks, compile false positive/negative rates and manual override frequency into a report.
6. Present findings to the team for a go/no-go decision on broader adoption.

**What changed:**
PR-Agent now runs in parallel mode exclusively on new contributors’ PRs for two weeks, with all flags requiring human review.
