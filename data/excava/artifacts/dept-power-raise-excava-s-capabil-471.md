# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-471` (dept) · 2026-07-28T13:04:11.245777+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Spin up a single-A100 rig with EXCAVA’s live workload slice.
2. Deploy **Claude Mythos 5** and **DeepSeek-V3-671B** in parallel for head-to-head A/B testing.
3. Enforce a strict 500ms response SLA on both models; log all latency and accuracy metrics.
4. Benchmark on complex reasoning tasks (prioritize the 0.5% capability jump metric).
5. If Mythos 5 meets/exceeds SLA and the 0.5% target, promote it to primary engine; else, lock in DeepSeek-V3-671B.
6. Publish a GitHub markdown report with latency distributions, accuracy deltas, and cost projections.

**What changed:** Replaced Qwen2.5-72B-Instruct with a live A/B test between Claude Mythos 5 and DeepSeek-V3-671B under 500ms SLA.
