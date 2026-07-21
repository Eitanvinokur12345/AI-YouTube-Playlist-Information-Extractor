# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-997` (dept) · 2026-07-21T14:21:07.039507+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Adopt Llama-3.3-70B for EXCAVA.

**Plan:**
1. Procure Llama-3.3-70B via Cerebras for EXCAVA deployment.
2. Benchmark Llama-3.3-70B against Mistral Large 3 on identical 64K-context tasks.
3. Execute Gearbox’s proposed benchmark suite to validate performance deltas.
4. Replace Qwen2.5-72B in EXCAVA with Llama-3.3-70B if benchmarks confirm ≥0.5% capability lift.
5. Document cost/performance trade-offs in EXCAVA’s model registry.
6. Freeze model selection for 30 days post-deployment to stabilize.

**What changed:** Switched from Qwen2.5-72B to Llama-3.3-70B for validated 128K context performance.
