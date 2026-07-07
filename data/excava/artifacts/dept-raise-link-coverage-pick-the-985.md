# Raise link coverage: pick the next 200 unlinked elements and the fastest resolution path

> Decision artifact · room `dept-raise-link-coverage-pick-the-985` (dept) · 2026-07-07T15:27:00.755166+00:00
> Participants: Fetch, Probe, Ledger · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Validate the integrity and methodology before proceeding with the next 200 unlinked elements.

**Plan:**
1. Run `sha256sum ./data/unlinked.csv` to generate the hash of the file.
2. Execute `git diff HEAD -- ./data/unlinked.csv` to compare the CSV against the canonical source.
3. Manually audit and record the last 5 entries from `./output/last_5_audits.log` to verify the output of `find_fast_paths.sh`.
4. Assess the validation sample size and error margin for the edge weights used in `find_fast_paths.sh`.
5. Document the handling of cyclic dependencies or API timeouts by `find_fast_paths.sh`.

**What changed:** The need for validation of both the data source and the method used for pathfinding before moving forward.
