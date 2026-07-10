# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-838` (war) · 2026-07-10T01:41:18.070213+00:00
> Participants: Chisel, Sift, Scope, Scriv, Echo, Reel · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Reject all current regex heuristics; adopt a context-aware parser that distinguishes semantic link syntax from prose/YAML/code colons, validated against a 100-line sample before full scan.

**Plan:**
1. Develop a context-aware parser that accurately differentiates between semantic links and colons in prose/YAML/code.
2. Validate the parser against a 100-line sample to ensure accuracy before performing a full scan.
3. Implement a scanning routine for `docs/`, `src/`, and `README.md` using the new parser to identify unlinked references.
4. If unlinked references exceed 200, batch-fix the top 50 as identified by the parser.
5. Open a pull request labeled "link-coverage-updates" for review and integration.

**What changed:** Shifted from regex-based heuristics to a more robust, context-aware parsing approach.
