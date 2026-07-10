# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-588` (dept) · 2026-07-10T17:35:38.130152+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Deploy TensorRT-LLM on A100 nodes only, pending ROCm-vLLM stability validation.

**Plan:**
1. Run 48-hour A/B test on A100 nodes comparing TensorRT-LLM vs baseline.
2. Measure latency/throughput; require ≥0.5% gain to proceed.
3. If gain confirmed, deploy TensorRT-LLM to all A100 nodes.
4. Leave V100 nodes on current stack to avoid regression.
5. Benchmark ROCm-vLLM on a single V100 node in staging for 24 hours.
6. If ROCm-vLLM passes stability test, evaluate cluster-wide rollout.

**What changed:** A100s optimized with TensorRT-LLM; V100s unchanged.
