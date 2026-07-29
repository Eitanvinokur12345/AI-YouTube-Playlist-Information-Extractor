# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-798` (dept) · 2026-07-29T17:50:53.257815+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Adopt **Qwen 2.5-72B-Instruct** as EXCAVA’s reasoning engine.

**Plan:**
1. Replace current reasoning engine with Qwen 2.5-72B-Instruct in EXCAVA’s core architecture.
2. Benchmark against prior model to verify ≥0.5% performance improvement in complex tasks.
3. Profile latency impact; optimize inference pipeline if real-time thresholds are exceeded.
4. Document cost-benefit analysis comparing Qwen 2.5-72B-Instruct to Claude Mythos 5.
5. Deploy staged rollout to mitigate risks, starting with non-critical modules.
6. Owner Gearbox to lead integration and validation.

**What changed:** Switched from Claude Mythos 5 to Qwen 2.5-72B-Instruct to balance performance gains with latency constraints.
