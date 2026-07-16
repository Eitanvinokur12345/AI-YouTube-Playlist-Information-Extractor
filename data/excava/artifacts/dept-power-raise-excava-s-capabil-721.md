# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-721` (dept) · 2026-07-16T02:36:35.597133+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy Qwen2.5-72B-Instruct and Mistral Large 2 12.8B in parallel for a 24-hour A/B test on EXCAVA’s 20K-token prompts.
2. Measure tool-call latency and reasoning quality as primary metrics.
3. Log inference speed, context stability, and prompt collapse incidents for both models.
4. Power team to own the A/B test artifact (logs, metrics, and analysis).
5. Compare results against EXCAVA’s 0.5% capability threshold.
6. Finalize model selection based on empirical data.

**What changed:** Switched from model selection debate to empirical A/B testing for EXCAVA’s 20K-token prompts.
