# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-793` (dept) · 2026-07-27T01:37:46.560092+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy Qwen3-235B-A22B-Instruct for EXCAVA with a strict 8-expert cap per request.
2. Implement Torque’s real-time GPU memory kill-switch at 90% utilization.
3. Run a 48-hour blind A/B stress test comparing Qwen3-235B-A22B (with cap) vs. DeepSeek-R1-671B on the 8xA100 node.
4. Assign Torque to own the kill-switch code and memory monitor.
5. Assign Gearbox to own the A/B test design and execution.
6. Post-test, evaluate throughput/latency trade-offs and decide on scaling path.

**What changed:** Switched from dense stability (DeepSeek-R1-671B) to MoE efficiency (Qwen3-235B-A22B) with strict resource guards.
