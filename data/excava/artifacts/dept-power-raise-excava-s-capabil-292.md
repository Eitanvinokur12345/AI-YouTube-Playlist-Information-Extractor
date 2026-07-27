# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-292` (dept) · 2026-07-27T06:20:57.809360+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy Qwen3-235B-A22B-Instruct, DeepSeek-R1-671B, and Llama-3.3-70B-Instruct on EXCAVA’s 8xA100 node in a blind A/B stress test.
2. Measure real-time latency (per-token) and throughput (tokens/sec) for each model over 48 hours.
3. If any model achieves ≥0.5% capability improvement, adopt it as primary inference engine.
4. If no model clears the 0.5% bar, default to a distilled 32B model (e.g., Qwen3-32B-Instruct).
5. Log all raw metrics (latency, throughput, memory usage) for reproducibility.
6. Freeze EXCAVA’s current model during testing to isolate performance changes.

**What changed:** Blind A/B stress test replaces theoretical debate; default to distilled 32B if no model meets 0.5% bar.
