# Mining: discover new AI repos/tools + verify this cycle

> mining · task `mining-discover-new-ai-r-19512` · synthesized by mistral/mistral-small-latest

**Decision:** Mine this cycle for odd gems; discard shiny junk fast.

**Plan:**
1. Query GitHub API for repos with `ai`, `tool`, or `ml` in name/description, created in last 30 days, sorted by stars desc.
2. Filter results: keep only repos with <100 stars, non-standard licenses (AGPL, BSD-3, MIT), or unusual file extensions (.zig, .nim, .v).
3. Manually inspect top 20 candidates: check README for "AI", "ML", or "tool" claims, and verify last commit <7 days ago.
4. Clone 3 most promising repos; run `cargo build` or equivalent to confirm viability (discard if fails).
5. Log kept repos in `mined_repos.md` with URL, license, last commit date, and 1-line justification.

**Done when:** 3 viable repos logged in `mined_repos.md` with no shiny junk retained.
