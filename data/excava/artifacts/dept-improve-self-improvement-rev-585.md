# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-585` (dept) · 2026-08-16T09:00:31.348508+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Configure PR-Agent to run in shadow mode exclusively on merged PRs for one week.
2. Log all autofeedback (including for open PRs) in a separate, non-review channel (e.g., `pr-agent-logs`).
3. Disable PR-Agent comments on open PRs during the trial to avoid review noise.
4. After one week, compare review quality metrics (e.g., review time, comment resolution rate) against a baseline.
5. Survey reviewers on perceived noise/value of autofeedback to validate trust erosion concerns.
6. Decide next steps (e.g., full rollout, adjustments, or termination) based on metrics and feedback.

**What changed:** PR-Agent autofeedback is now siloed to merged PRs and logs, preserving data while keeping active reviews clean.
