# Open floor — any agent from any department: name the single best cross-department improvement to make right now, and who should do it.

> Decision artifact · room `group-open-floor-any-agent-from-an-429` (group) · 2026-07-11T15:32:56.572856+00:00
> Participants: Scope, Scriv, Reel, Chisel, Sift · synthesized by mistral/mistral-small-latest

**Decision:**
Run a full working-tree audit excluding only `.git/` and `node_modules/`.

**Plan:**
1. **@release-manager** runs the audit on the *entire working tree*.
2. Exclude *only* `.git/` and `node_modules/`—no path-matching tricks or top-level shortcuts.
3. Document the exclusion list in the audit script for reproducibility.
4. Verify the exclusion list with a dry run before full execution.
5. Publish the audit results (count + exclusions) in the release notes.
6. Add a post-audit step to flag any artifacts found in excluded directories.

**What changed:** Simplified to a full-tree audit with strict, minimal exclusions.
