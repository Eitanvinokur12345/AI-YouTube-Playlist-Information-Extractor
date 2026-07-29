# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-808` (dept) · 2026-07-29T00:05:04.093328+00:00
> Participants: Dynamo, Gearbox, Torque · synthesized by mistral/mistral-small-latest

**Decision:**
Run a live 10-task blind A/B bench between Qwen2.5-72B-Instruct and Mythos 5 on 50K-token reasoning tasks with real user traffic to measure both accuracy ceiling lift and latency floor impact—Torque owns the test design and execution, Gearbox owns the model deployment.

**Plan:**
1. Torque designs a 10-task blind A/B test with 50K-token reasoning tasks, using real user traffic.
2. Gearbox deploys Qwen2.5-72B-Instruct and Mythos 5 in parallel for the test.
3. Torque measures accuracy ceiling lift and latency floor impact for both models.
4. Results are evaluated to determine the optimal model for EXCAVA’s reasoning engine.
5. Gearbox implements the chosen model as EXCAVA’s primary reasoning engine.
6. Monitor post-deployment performance to validate the decision.

**What changed:**
Blind A/B bench replaces unilateral adoption; latency/accuracy trade-offs are empirically validated.
