# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-893` (dept) · 2026-07-26T23:31:01.067709+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 48-hour blind A/B stress test to empirically resolve the latency vs. redundancy trade-off.

**Plan:**
1. Deploy **DeepSeek-R1-671B** on **4xA100 nodes** in a distributed, redundant setup (sharding overhead ≤ MoE).
2. Deploy **Qwen3-235B-A22B-Instruct** on **4xA100 nodes** with MoE (latency target: 30-40% reduction).
3. Run identical **real-time power-task workloads** for 48 hours with blind monitoring (no model bias).
4. Measure **latency (P99/P95)** and **failure rate** (node crashes, task stalls).
5. Torque to publish raw metrics (no synthesis) within 24 hours post-test.
6. Dynamo to finalize model selection based on **latency ≤500ms** and **failure rate ≤0.1%** thresholds.

**What changed:**
Replaced theoretical trade-offs with a controlled empirical test to break the deadlock.
