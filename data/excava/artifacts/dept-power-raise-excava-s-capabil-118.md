# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-118` (dept) · 2026-07-28T17:53:52.322076+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy Qwen2.5-72B-Instruct as EXCAVA’s primary reasoning engine on the 5% test slice.
2. Deploy Claude Mythos 5 as a secondary reasoning engine on the same 5% slice.
3. Implement Torque’s test design to measure reasoning quality (human eval on 100 samples) and p95 latency.
4. Enforce the 95th-percentile SLA as the kill-switch threshold for both models.
5. Run the A/B test for 7 days, with daily monitoring for stability and performance.
6. Dynamo retains final approval for model rollout based on test results.

**What changed:** Live A/B test between Qwen2.5-72B-Instruct and Claude Mythos 5 on a 5% traffic slice.
