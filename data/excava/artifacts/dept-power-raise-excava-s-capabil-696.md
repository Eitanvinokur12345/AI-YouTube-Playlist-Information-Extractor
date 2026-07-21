# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-696` (dept) · 2026-07-21T17:48:43.133252+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Design a controlled ablation test comparing DeepSeek-v3-671B and Llama-3.3-70B-Instruct on EXCAVA’s longest tasks.
2. Measure recall accuracy and throughput at 32K, 64K, and 96K context lengths.
3. Torque owns test design, metrics, and validation; Gearbox owns model deployment and cost tracking.
4. Run tests in a staged environment to isolate performance differences.
5. Report results within 72 hours, including failure modes and cost trade-offs.
6. Final model selection based on empirical gains, not benchmarks alone.

**What changed:** Ablation test replaces premature model adoption.
