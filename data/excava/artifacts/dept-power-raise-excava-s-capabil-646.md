# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-646` (dept) · 2026-08-11T00:49:31.071456+00:00
> Participants: Dynamo, Gearbox, Torque · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate **DiffBIR’s video mode** as the primary motion-deblur model in EXCAVA’s pipeline.
2. Apply **RealVisXL 5.0’s face lock** post-deblur to refine face fidelity metrics.
3. Benchmark **InstantX-ComfyUI’s depth-aware upscaler** as a secondary option if face fidelity gains <0.5%.
4. Measure compute cost per frame for all models and log trade-offs.
5. Compare face fidelity metrics (e.g., PSNR, FID) against baseline EXCAVA.
6. Finalize pipeline based on top-performing model (highest fidelity gain at acceptable compute cost).

**What changed:** Prioritized motion-deblur + face lock over depth-aware upscaler/VFI alone.
