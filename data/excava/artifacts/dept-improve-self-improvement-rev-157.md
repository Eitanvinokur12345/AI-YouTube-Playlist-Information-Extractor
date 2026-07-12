# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-157` (dept) · 2026-07-12T23:28:43.471187+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run continuous lightweight checks on every prompt edit, auto-blocking only syntax/references while batching human review for semantic drift—pilot for 2 weeks with false-positive tracking.

**Plan:**
1. Implement a real-time linter for prompt edits, auto-blocking syntax errors and broken references (e.g., via regex/parser checks).
2. Log all flagged issues (including false positives) in a dedicated dashboard for the 2-week pilot.
3. Batch human review for semantic drift (e.g., weak phrasing, outdated references) into weekly 30-minute sessions.
4. Integrate the linter into the prompt editing UI with clear error messages and quick-fix suggestions.
5. Track false-positive rates and review fatigue metrics (e.g., time-to-resolution, reviewer comments).
6. After 2 weeks, evaluate pilot data and adjust thresholds/processes (e.g., expand auto-blocking or refine batch review scope).

**What changed:**
Continuous lightweight checks replaced weekly scans, shifting from reactive to proactive prompt quality control.
