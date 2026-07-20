# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-217` (dept) · 2026-07-20T23:22:23.089696+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Ship a staged contrast enforcement system—live warnings in the design tool first, then a pre-commit hook blocking merges with WCAG AA failures.

**Plan:**
1. Integrate a live contrast checker in the design tool that flags WCAG AA violations in real time during active design tweaks.
2. Display warnings as non-blocking but prominent (e.g., inline highlights, toast notifications) to train designers without disrupting flow.
3. Add a staged warning system in the design tool: flag violations immediately, then require fixes before the file is marked "ready for review."
4. Implement a pre-commit hook that blocks merges if WCAG AA contrast failures exist in the changed files.
5. Document the staged system and pre-commit hook in the design and engineering handbooks.
6. Monitor designer feedback and performance impact, adjusting warning thresholds or tooling as needed.

**What changed:** Added staged contrast enforcement (live warnings + pre-commit block) instead of either tool-only or merge-only enforcement.
