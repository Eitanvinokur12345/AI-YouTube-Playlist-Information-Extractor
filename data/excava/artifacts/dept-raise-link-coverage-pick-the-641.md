# Raise link coverage: pick the next 200 unlinked elements and the fastest resolution path

> Decision artifact · room `dept-raise-link-coverage-pick-the-641` (dept) · 2026-07-06T19:35:00.729615+00:00
> Participants: Fetch, Probe, Ledger · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** We will proceed with running the `link-coverage-report.py` script on the entire `docs` repository to generate a comprehensive list of unlinked elements.

**Plan:**  
1. Execute the `link-coverage-report.py` script on the entire `docs` repository.  
2. Save the output to `unlinked-elements.csv` for documentation.  
3. Include the list of 200 identified unlinked elements for further action.  
4. Document any file revisions and checks made during the reporting process.  
5. Review the generated report for coverage accuracy and potential edge cases.

**What changed:** We decided to run the script on the entire repository instead of a smaller subset to ensure comprehensive link coverage.
