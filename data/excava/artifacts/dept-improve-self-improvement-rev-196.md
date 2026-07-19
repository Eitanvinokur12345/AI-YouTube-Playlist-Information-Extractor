# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-196` (dept) · 2026-07-19T19:43:16.753881+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a hybrid system—auto-apply regression-tested, low-risk changes with a one-line rationale in the shared log; all other edits require human sign-off.

**Plan:**
1. Implement a shared log (e.g., Git-backed) to record all changes to prompts, engines, and routing rules with timestamps, authors, and one-line rationales.
2. Develop a regression test suite that gates auto-applied changes, covering core functionality and past behavior deviations.
3. Configure the system to auto-apply changes that pass regression tests and are flagged as low-risk (e.g., minor prompt tweaks, engine parameter adjustments).
4. Require human sign-off for high-risk edits (e.g., routing rule changes, engine swaps) or any deviation from past behavior not covered by regression tests.
5. Add a lightweight review step for auto-applied changes, summarizing them in the shared log for visibility.
6. Monitor adoption for 30 days, measuring auto-apply success rate, human intervention frequency, and log readability.

**What changed:**
Hybrid auto-apply system with regression-gated changes and shared log for all decisions.
