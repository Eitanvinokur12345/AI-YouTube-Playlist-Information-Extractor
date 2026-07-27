# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-586` (dept) · 2026-07-27T04:51:04.351243+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt Qwen3-235B-A22B-Instruct for EXCAVA if it outperforms DeepSeek-R1-671B in the 48-hour blind A/B test.

**Plan:**
1. Torque designs a 48-hour blind A/B stress test on EXCAVA’s 8xA100 with NVLink, measuring latency, throughput, and output quality under full load.
2. Gearbox and Torque jointly define output quality scoring criteria for the blind evaluation.
3. Run the test with Qwen3-235B-A22B-Instruct (8-expert cap) vs DeepSeek-R1-671B.
4. Torque collects raw performance data; Gearbox scores output quality.
5. If Qwen3’s latency/throughput gains outweigh DeepSeek’s stability, adopt Qwen3.
6. Document results in a GitHub issue with raw data and analysis.

**What changed:**
Replaced 24-hour test with a 48-hour blind A/B stress test to resolve sharding bottlenecks and validate Qwen3’s MoE claims.
