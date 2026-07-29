# Keep the Designs tab pure: designs only, live previews, taste-ranked

> visual · task `keep-the-designs-tab-pur-56548` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

**Approach:**
Enforce a strict separation between design artifacts and live previews, ensuring only curated designs populate the Designs tab.

**Steps:**
1. **Audit & Archive:** Run `find ./designs -type f ! -name "*.design.*" -exec mv {} ./archive/ \; 2>/dev/null || true` to relocate non-design files from the Designs tab directory.
2. **Enforce Naming:** Rename all remaining files to `*.design.{ext}` (e.g., `homepage.design.fig`) via `for f in ./designs/*; do mv "$f" "${f%.*}.design.${f##*.}"; done`.
3. **Validate Previews:** Add a CI check (`scripts/validate-designs.sh`) to reject PRs with unapproved previews (e.g., `if grep -q "preview" ./designs/*.design.*; then exit 1; fi`).
4. **Tooling:** Use `chroma-design-lint` (local npm package) to auto-flag non-design files in PRs.
5. **Deploy:** Update `designs/.gitignore` to exclude `*.preview.*` files.

**Needs:**
- Write access to the repo’s `designs/` directory.
- Node.js (for `chroma-design-lint`).
- CI runner with `bash`/`find`/`grep` support.
