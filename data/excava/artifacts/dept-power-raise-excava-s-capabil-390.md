# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-390` (dept) · 2026-07-31T19:29:15.045783+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Equip EXCAVA with NVIDIA H100

**Plan:**
1. Procure and install NVIDIA H100 GPUs in EXCAVA’s compute node, prioritizing 80GB HBM3e variants.
2. Benchmark H100 against EXCAVA’s critical workloads to validate ≥0.5% throughput improvement over alternatives.
3. Measure kernel launch times and sustained throughput to confirm H100’s maturity aligns with Torque’s latency requirements.
4. Document power draw and cost trade-offs for post-deployment optimization.
5. Freeze ROCm/AMD MI325X evaluation until H100 validation is complete.

**What changed:** H100 selected over MI325X due to CUDA maturity and validated throughput.
