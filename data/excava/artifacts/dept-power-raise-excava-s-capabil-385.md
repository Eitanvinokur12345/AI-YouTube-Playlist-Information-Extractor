# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-385` (dept) · 2026-07-27T05:28:15.867118+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy Qwen3-235B-A22B-Instruct and DeepSeek-R1-671B on EXCAVA’s 8xA100 node with NVLink for a 48-hour blind A/B stress test.
2. Torque executes the test, measuring latency, throughput (tokens/sec), and stability metrics under identical real-time workloads.
3. Gearbox configures both models with identical prompts, batch sizes, and system constraints to ensure parity in evaluation.
4. After 48 hours, collect and compare raw performance data (latency spikes, token throughput) and quality parity (via automated benchmarks).
5. Dynamically adjust model sharding or batching if either model hits hardware bottlenecks before the test concludes.
6. Final report to Dynamo within 24 hours of test completion, including go/no-go recommendation based on metrics.

**What changed:** Blind A/B stress test replaces debate—objective data will decide the model for EXCAVA’s power upgrade.
