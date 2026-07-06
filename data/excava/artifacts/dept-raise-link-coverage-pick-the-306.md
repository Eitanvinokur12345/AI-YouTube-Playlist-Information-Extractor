# Raise link coverage: pick the next 200 unlinked elements and the fastest resolution path

> Decision artifact · room `dept-raise-link-coverage-pick-the-306` (dept) · 2026-07-06T22:39:16.442167+00:00
> Participants: Fetch, Probe, Ledger · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** We will conduct a comprehensive verification test by running the `link-coverage-report.py` script on the entire `docs` repository.

**Plan:**
1. Execute the command `python link-coverage-report.py` on the `docs` repository to generate a complete report of unlinked elements.
2. Save the output file containing the list of unlinked elements as `unlinked-elements.csv`.
3. Review and validate the output against the actual repository structure to ensure accuracy.
4. Identify the next 200 unlinked elements from the report for resolution.
5. Develop a timeline for addressing the unlinked elements based on their relevance and ease of linking.

**What changed:** The decision shifted to a more comprehensive and thorough approach in verifying the accuracy of the link coverage report.
