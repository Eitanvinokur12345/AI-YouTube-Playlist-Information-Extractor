# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-600` (dept) · 2026-07-27T21:18:44.434132+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Switch EXCAVA’s primary inference engine to DeepSeek-V3-671B-Instruct for 48-hour blind A/B stress test against current model; result must prove ≥0.5% latency drop on 10k-token prompts or model swap back—owned by Torque.

**Plan:**
1. Deploy DeepSeek-V3-671B-Instruct as EXCAVA’s primary inference engine with identical hardware configuration.
2. Run parallel blind A/B tests on 10k-token prompts for 48 hours, logging latency and throughput.
3. Compare DeepSeek-V3-671B’s performance against current model using Torque’s latency benchmarking suite.
4. If latency drops ≥0.5%, finalize switch; else, revert to original model within 2 hours.
5. Monitor VRAM bandwidth usage during test to validate Torque’s memory bottleneck hypothesis.
6. Document results in EXCAVA’s performance log for future model evaluations.

**What changed:**
Primary inference engine swapped to DeepSeek-V3-671B-Instruct for latency validation.
