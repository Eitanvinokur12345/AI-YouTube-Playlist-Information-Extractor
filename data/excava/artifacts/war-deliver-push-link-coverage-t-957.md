# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-957` (war) · 2026-07-10T17:14:23.173161+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Generate a definitive list of all markdown files: `find . -type f -name "*.md" > /tmp/md_files.txt`.
2. Run a single `rg` pass with expanded regex to flag all unlinked patterns: `rg -l --no-filename '\[[^\]]+\]\([^)]*\)|\[[^\]]+\]\[\]|https?://[^\s)]+|`[^`]+`\([^)]*\)' --type md | tee /tmp/checked_files.txt`.
3. Log every file checked and unlinked pattern found in `/tmp/unlinked_refs.log`.
4. Validate coverage by cross-referencing `/tmp/md_files.txt` and `/tmp/checked_files.txt` to identify gaps.
5. Output a clean artifact (`/tmp/unlinked_refs.log`) for the next task owner.
6. Set a daily target of +5% link coverage, tracked via the logged gaps.

**What changed:** Expanded regex to include inline code links and added falsifiable file/pattern logging.
