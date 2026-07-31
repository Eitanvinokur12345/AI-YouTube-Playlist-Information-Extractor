# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-101` (dept) · 2026-07-31T18:51:31.307383+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Configure PR-Agent to auto-block PRs on verifiable issues (linting, test coverage <80%, style violations).
2. Require PR authors to add a `## Why These Metrics Matter` section in PR descriptions, justifying each blocked metric.
3. Lead updates the team’s workflow doc to enforce this policy by EOD.
4. Run a 2-week pilot, tracking PR cycle time and post-merge defect rates.
5. After pilot, re-evaluate the `Why These Metrics Matter` requirement—drop it if it adds noise without improving impact.

**What changed:** PR-Agent now gates only verifiable quality metrics, with justification required for each blocked issue.
