# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-548` (dept) · 2026-07-30T19:10:10.620017+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Pilot auto-apply PR-Agent style/doc fixes only to *new* PRs with human sign-off required for logic or critical docs.

**Plan:**
1. Configure PR-Agent to auto-apply style/doc fixes (formatting, comments, docstrings) *only* for new PRs (age < 30 days).
2. Require human sign-off (via GitHub review) for any changes touching logic or critical docs (e.g., README, API contracts).
3. Track metrics: review noise reduction, false positives, and human review engagement for 30 days.
4. Assign Gauge as owner to monitor pilot, collect feedback, and escalate risks.
5. Document exceptions (e.g., legacy code) where auto-apply is disabled.
6. Prepare rollback plan if rubber-stamping increases or review engagement drops.

**What changed:** Auto-apply restricted to new PRs; human sign-off mandated for logic/critical docs.
