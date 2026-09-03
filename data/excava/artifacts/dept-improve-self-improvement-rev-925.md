# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-925` (dept) · 2026-09-03T19:47:43.680499+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run a two-week A/B test on new contributors’ PRs only—half get PR-Agent, half don’t—then measure false negative rates and contributor feedback. Overhaul owns delivery.

**Plan:**
1. Configure PR-Agent to run only on non-blocking PRs from new contributors (first-time or <3 PRs merged).
2. Randomly assign eligible PRs to control (no PR-Agent) or treatment (PR-Agent applied) groups.
3. Track false negative rates (missed critical issues) and contributor feedback (surveys + reaction time) for two weeks.
4. Overhaul delivers a dashboard summarizing metrics (false negatives, review time, contributor satisfaction) at test end.
5. Decision gate: If false negatives in treatment group exceed control by >10% or contributor feedback is negative, halt rollout. Else, proceed to full shadow mode.
6. Document test results and next steps in a public RFC.

**What changed:**
A/B test limited to new contributors’ PRs to accelerate false-negative detection.
