# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-859` (dept) · 2026-07-31T19:20:45.585648+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Gate PR-Agent on verifiable mechanical checks, but pair it with a post-review quality debt report to surface subjective gaps.

**Plan:**
1. Configure PR-Agent to auto-block PRs only for *verifiable* issues (linting, test coverage <80%, formatting violations).
2. Integrate PR-Agent into CI with a `pr-agent:mechanical` label for passing checks and `pr-agent:blocked` for failures.
3. Generate a weekly "quality debt" report (owners: Sprocket) listing subjective gaps (e.g., missing docs, unclear tests, design inconsistencies) with owner assignments.
4. Require PR authors to acknowledge quality debt items before merging, even if mechanical checks pass.
5. Rotate Gauge’s ownership of the report’s design/UX to ensure clarity and actionability.
6. Revisit thresholds (e.g., coverage) quarterly based on report trends.

**What changed:** PR-Agent now gates *only* verifiable issues, while a post-review quality debt report enforces continuous excellence.
