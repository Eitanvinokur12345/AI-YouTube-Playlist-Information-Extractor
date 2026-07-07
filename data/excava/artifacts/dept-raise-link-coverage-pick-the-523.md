# Raise link coverage: pick the next 200 unlinked elements and the fastest resolution path

> Decision artifact · room `dept-raise-link-coverage-pick-the-523` (dept) · 2026-07-07T15:23:37.178157+00:00
> Participants: Fetch, Probe, Ledger · synthesized by gh-models/openai/gpt-4o-mini

**Decision:**  
Proceed with rerunning `./fetch-links.sh --batch 200 --mode probe` on the first 200 unlinked elements and include a comparative analysis of probe errors against past resolution failures in production within the final artifact.

**Plan:**  
1. Execute `./fetch-links.sh --batch 200 --mode probe` on the first 200 unlinked elements (lines 1-200 of `unlinked-elements.json`).
2. Gather and analyze error data logged in `probe-errors.log` after the probe run.
3. Compare the failure rates from this run against the previous resolution failures from Run 42 logs.
4. Document findings in a comprehensive report, including specific probe error counts and insights.
5. Share the report with the team and discuss potential action items based on the analysis.

**What changed:**  
The approach shifted to collecting empirical evidence of failures through a simulated resolution method before proceeding with actual resolution attempts.
