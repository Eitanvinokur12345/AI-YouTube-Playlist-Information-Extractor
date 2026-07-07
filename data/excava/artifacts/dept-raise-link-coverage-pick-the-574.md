# Raise link coverage: pick the next 200 unlinked elements and the fastest resolution path

> Decision artifact · room `dept-raise-link-coverage-pick-the-574` (dept) · 2026-07-07T10:09:45.199435+00:00
> Participants: Fetch, Probe, Ledger · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Run a comprehensive verification of the `link-coverage-report.py` script on a broader sample of 100 varied files from the `docs` repository.

**Plan:**
1. Execute the command `python link-coverage-report.py -t 100 -o comprehensive-verification.csv` to analyze 100 files.
2. Thoroughly review the output generated from the script.
3. Cross-reference the findings with the latest repository layout to ensure accuracy.
4. Document any discrepancies and update the script if necessary to address identified issues.
5. Generate a new batch of the next 200 unlinked elements based on validated output.

**What changed:** The verification process was expanded from 20 to 100 files for more comprehensive results.
