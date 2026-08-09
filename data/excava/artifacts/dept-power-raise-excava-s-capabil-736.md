# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-736` (dept) · 2026-08-03T03:52:35.639660+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate GFPGAN 2.0 GPU face enhancer into EXCAVA’s pipeline for face regions ≤20% of frame.
2. Reserve RealVisXL CPU face model for face regions >20% of frame.
3. Benchmark against 1080p face video baseline; target ≥0.5% FID improvement.
4. Measure latency impact; ensure real-time feasibility for ≤20% face regions.
5. Document trade-offs (latency vs. quality) in EXCAVA’s model registry.
6. Merge changes into `dev` branch with Torque as reviewer.

**What changed:** GFPGAN 2.0 GPU face enhancer replaces depth-aware upscaling for small faces; RealVisXL CPU model reserved for large faces.
