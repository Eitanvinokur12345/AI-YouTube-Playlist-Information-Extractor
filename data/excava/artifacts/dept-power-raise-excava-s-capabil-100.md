# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-100` (dept) · 2026-07-27T19:01:18.536831+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy Qwen3-235B-A22B-Instruct and DeepSeek-R1-671B on EXCAVA’s 8xA100 node.
2. Run a 48-hour blind A/B stress test under real EXCAVA load, measuring latency, throughput, and cost per token.
3. Torque executes the test and logs raw metrics without bias.
4. Publish results by EOD Friday, including per-model breakdowns.
5. If Qwen3-235B-A22B’s latency spike is <20% vs DeepSeek-R1-671B, adopt it as primary; else default to DeepSeek-R1-671B.
6. Optimize routing/gating for Qwen3-235B-A22B post-test if selected.

**What changed:** Blind A/B test replaces debate with empirical validation.
