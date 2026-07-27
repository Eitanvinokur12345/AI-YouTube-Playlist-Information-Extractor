# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-209` (dept) · 2026-07-27T05:09:10.147945+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt Qwen3-235B-A22B-Instruct for EXCAVA’s 8xA100 node after a 48-hour blind A/B stress test.

**Plan:**
1. Configure NVLink-enabled 8xA100 node with Qwen3-235B-A22B-Instruct (8-expert cap) and DeepSeek-R1-671B.
2. Torque designs a blind A/B stress test comparing latency, throughput per watt, and reasoning depth across both models.
3. Gearbox prepares optimized artifacts (Docker images, configs) for both models, ensuring fair comparison.
4. Run the 48-hour test, logging metrics (GPU utilization, memory usage, inference speed, accuracy).
5. Dynamo and team analyze results; if Qwen3-235B-A22B-Instruct meets or exceeds DeepSeek-R1-671B in key metrics, adopt it.
6. If Qwen3-235B-A22B-Instruct underperforms, fall back to DeepSeek-R1-671B.

**What changed:**
Blind A/B stress test replaces theoretical debate with empirical validation.
