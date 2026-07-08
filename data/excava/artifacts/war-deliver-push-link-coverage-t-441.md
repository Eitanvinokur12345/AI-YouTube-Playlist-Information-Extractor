# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-441` (war) · 2026-07-08T17:42:04.818207+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Use multi-pass regex sweeps to ensure comprehensive link coverage validation.

**Plan:**
1. Execute `grep -rE '\[.*\]\(https?://[^)]*\)' --include="*.md" docs/` to count valid markdown links.
2. Run `grep -rE 'requests\.(get|post|put|delete|patch)\(["\'](https?|ftp|git|mailto):\/\/[^)"']*["\']\)' --include="*.py" src/` for Python link checks.
3. Implement `grep -rE '(fetch|axios|XMLHttpRequest)\(["\'](https?|ftp|git|mailto):\/\/[^)"']*["\']\)' --include="*.js" src/` for JavaScript links.
4. Conduct a sample audit of inline comments and raw URLs in HTML using `grep -rE 'http[s]?://[^ )]*' .` to capture missed links.
5. Consolidate findings into a delta report detailing coverage and gaps confirmed by sample audits.
6. Iterate based on audit results to refine regex patterns and ensure comprehensive coverage.

**What changed:** Focus was shifted to include a comprehensive validation of various protocol schemes and coverage across all relevant file types.
