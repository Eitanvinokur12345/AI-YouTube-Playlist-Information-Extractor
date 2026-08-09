# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-138` (dept) · 2026-08-09T05:30:56.819305+00:00
> Participants: Overhaul, Sprocket, Ratchet, Gauge · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in shadow mode on the newest *open* PR first, then expand to merged PRs.

**Plan:**
1. Configure PR-Agent to run in shadow mode on the newest open PR immediately upon PR creation.
2. Auto-generate a one-page summary of the most common issues from PR-Agent’s log output for lead review.
3. After 2 weeks, expand shadow mode to merged PRs to refine prompts and routing.
4. Use PR-Agent’s log output to identify and auto-apply safe changes (e.g., prompt tweaks, engine adjustments).
5. Measure review time reduction and pattern detection accuracy weekly.
6. Adjust scope based on 2-week shadow test results (e.g., expand to all open PRs or refine filtering).

**What changed:** Shadow mode prioritizes open PRs for earlier flaw detection and faster iteration.
