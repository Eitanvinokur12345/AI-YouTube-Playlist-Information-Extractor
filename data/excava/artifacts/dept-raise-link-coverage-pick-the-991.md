# Raise link coverage: pick the next 200 unlinked elements and the fastest resolution path

> Decision artifact · room `dept-raise-link-coverage-pick-the-991` (dept) · 2026-07-07T04:35:48.162559+00:00
> Participants: Fetch, Probe, Ledger · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Fetch will provide a comprehensive changelog and metrics for measuring link coverage while executing the `link-coverage-report.py` script.

**Plan:**
1. Fetch will compile a detailed changelog of the `link-coverage-report.py` script.
2. Fetch will conduct a verification test using a subset of 20 recently updated files from the `docs` repository.
3. Fetch will generate metrics for measuring link coverage.
4. Fetch will execute the `link-coverage-report.py` script on the `docs` repository to generate a list of 200 unlinked elements.
5. All findings will be saved in an output file for review.

**What changed:** Fetch agreed to provide additional evidence and metrics to validate the accuracy of the reporting script.
