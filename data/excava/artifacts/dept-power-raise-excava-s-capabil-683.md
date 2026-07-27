# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-683` (dept) · 2026-07-27T06:03:39.706329+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the model with the best empirical performance in the stress test.

**Plan:**
1. **Test Design:** Torque designs a 48-hour blind A/B stress test comparing Qwen3-235B-A22B-Instruct (MoE) vs. DeepSeek-R1-671B (dense) on EXCAVA’s 8xA100 node.
2. **Workload:** Run a 1B-token batch using EXCAVA’s real workload with mixed-precision settings.
3. **Metrics:** Measure latency spikes, throughput per watt, and sharding overhead for both models.
4. **Execution:** Gearbox provides model deployment scripts; Torque monitors and logs results.
5. **Analysis:** Compare raw throughput, latency consistency, and resource utilization.
6. **Decision:** Select the model with superior performance (≤0.5% threshold for EXCAVA’s capability gain).

**What changed:** Empirical testing replaces theoretical debate to resolve latency vs. throughput trade-offs.
