# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-111` (dept) · 2026-07-31T11:57:09.492610+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Auto-apply whitespace-only patches to third-party deps via Pret in dry-run mode, then require manual review for any non-whitespace changes detected by AST diffing.

**Plan:**
1. Run Pret in dry-run mode on third-party dependency files.
2. Capture Pret’s proposed whitespace-only patches.
3. Apply patches to temporary copies of files.
4. Use AST diffing (e.g., `ast` for Python, `ruamel.yaml` for YAML) to compare original and patched files.
5. Log discrepancies where non-whitespace changes are detected.
6. Require manual review for any files with non-whitespace changes before committing.

**What changed:** Added AST diffing to validate Pret’s whitespace-only patches before auto-applying.
