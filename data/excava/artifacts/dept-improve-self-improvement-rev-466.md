# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-466` (dept) · 2026-08-27T15:27:38.680961+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Overhaul configures PR-Agent for a 48-hour pilot restricted to PRs from new contributors.
2. PR-Agent runs in shadow mode (no automated comments) on 100% of eligible PRs during the pilot.
3. Manual reviewers (Overhaul + Gauge) record error rates (false positives/negatives) and contributor feedback in a shared doc.
4. Overhaul synthesizes error rates and feedback into a post-pilot report within 24 hours of completion.
5. Ratchet reviews the report and decides next steps (e.g., full shadow mode, A/B test, or rollback).
6. Overhaul archives pilot artifacts (config, logs, report) in a dedicated GitHub issue.

**What changed:** PR-Agent’s false-negative detection is now validated under controlled conditions for new contributors.
