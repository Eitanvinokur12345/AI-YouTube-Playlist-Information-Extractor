# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-416` (war) · 2026-07-09T03:59:11.992497+00:00
> Participants: Echo, Reel, Scriv, Chisel, Sift, Scope · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Prioritize `export.py` for runtime-coverage testing while evaluating `parser.py` based on its impact on the bus task.

**Plan:**
1. Run a coverage scan on the last 7 days of commits to identify gaps in `export.py` coverage.
2. Execute the command `coverage report --show-missing --include="src/**"` to capture coverage metrics.
3. Instrument the bus task by running the CLI export command with a realistic payload to obtain runtime coverage data.
4. Compare runtime coverage results against static coverage data to identify any indirect call paths.
5. If `parser.py` shows indirect calls impacting the bus task, backfill tests; otherwise, focus resources on `export.py`.

**What changed:** The focus shifted from merely addressing 0% coverage to evaluating the impact of files on the bus task before deciding on testing priorities.
