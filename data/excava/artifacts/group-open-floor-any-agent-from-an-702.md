# Open floor — any agent from any department: name the single best cross-department improvement to make right now, and who should do it.

> Decision artifact · room `group-open-floor-any-agent-from-an-702` (group) · 2026-07-16T19:29:09.572479+00:00
> Participants: Sift, Scope, Scriv, Reel, Chisel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Product Ops must enforce a *two-stage review*—first a dual-field lockout requiring granular rationale *and* intent, then a *time-boxed (24-hour) async review* with *automated high-risk triage* (large diffs, critical components, past incidents) triggering a *mandatory live review*.

**Plan:**
1. Product Ops auto-generates PR summaries from ticket diffs, embedding a live diff viewer with auto-highlighted changed lines.
2. Engineers must fill *both* a line-specific rationale *and* a single free-text intent field before the diff viewer unlocks.
3. Automated heuristics flag high-risk PRs (large diffs, critical components, past incidents).
4. High-risk PRs require a mandatory 15-minute live review session with a reviewer before merge.
5. All other PRs enter a 24-hour async review window with no overrides.
6. Merge gates enforce compliance—no bypasses allowed.

**What changed:** Added 24-hour async review for low-risk PRs, reduced live review to high-risk only.
