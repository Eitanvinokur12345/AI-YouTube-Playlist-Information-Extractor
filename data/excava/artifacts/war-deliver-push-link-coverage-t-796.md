# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-796` (war) · 2026-07-08T12:26:59.114139+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Run a symbol-usage sweep that cross-references live markdown links against actual symbol invocations in code.

**Plan:**
1. Execute a command to list all symbols in `/src` along with their respective line numbers and instances of use.
2. Capture live markdown links from all markdown files in the project, ensuring coverage includes the relevant context.
3. Cross-reference the symbol usage output against the live markdown links to identify symbols that lack documentation links.
4. Generate a report containing file path, symbol name, and line number for every symbol missing a link.
5. Review and prioritize fixing gaps based on the report, aiming for incremental improvement toward the 100% coverage goal.

**What changed:** Focus shifted from merely counting symbols and unlinked files to a more precise symbol-usage analysis to identify specific gaps in documentation.
