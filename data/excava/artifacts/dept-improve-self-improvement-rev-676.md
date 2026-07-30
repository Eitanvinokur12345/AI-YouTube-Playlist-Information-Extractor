# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-676` (dept) · 2026-07-30T19:52:47.707894+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Auto-apply *only* non-trivial fixes via PR-Agent—style/doc tweaks like trailing whitespace stay manual.

**Plan:**
1. Configure PR-Agent to auto-apply *only* non-trivial fixes (e.g., logic, performance, or structural changes).
2. Exclude trivial style/doc fixes (e.g., trailing whitespace, basic formatting) from auto-application.
3. Run PR-Agent on a sample of PRs for 2 weeks to measure human review engagement.
4. Track false positives and noise levels in automated feedback.
5. Adjust thresholds or exclusions based on engagement metrics.
6. Owner: Gauge.

**What changed:**
Non-trivial fixes auto-applied; trivial style/doc fixes remain manual.
