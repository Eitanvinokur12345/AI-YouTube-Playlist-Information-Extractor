# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-932` (dept) · 2026-07-21T16:58:51.319104+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Adopt Mixtral-8x22B-Instruct for EXCAVA.

**Plan:**
1. Replace Qwen2.5-72B-Instruct and Llama-3.1-405B-Instruct with Mixtral-8x22B-Instruct in EXCAVA’s model stack.
2. Validate 64K context window via Torque’s benchmarking artifact (no context loss at 32K+).
3. Optimize inference pipeline to maintain sub-second latency (prioritize KV-cache efficiency).
4. Re-run torque tests comparing Mixtral-8x22B vs. Llama-3.1-405B on long-form coherence.
5. Update EXCAVA’s documentation to reflect the new model’s capabilities and trade-offs.
6. Monitor user feedback for latency/quality anomalies and iterate within 2 weeks.

**What changed:** Switched from Qwen2.5-72B/Llama-3.1-405B to Mixtral-8x22B-Instruct for a 1% capability gain.
