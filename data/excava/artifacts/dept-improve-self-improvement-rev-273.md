# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-273` (dept) · 2026-08-03T01:43:50.236656+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in CI with a two-week dry-run phase logging violations without blocking, then enforce adjusted thresholds based on logged data.

**Plan:**
1. Configure PR-Agent in CI with `dry-run: true` for 14 days.
2. Log all violations to a dedicated channel/file for analysis.
3. After two weeks, review logs to identify false positives/misses.
4. Adjust PR-Agent thresholds based on logged data (e.g., severity, frequency).
5. Enable enforcement mode in CI with the new thresholds.
6. Document the final rules in the repo’s `CONTRIBUTING.md`.

**What changed:**
PR-Agent enforcement now uses data-driven thresholds from a dry-run phase.
