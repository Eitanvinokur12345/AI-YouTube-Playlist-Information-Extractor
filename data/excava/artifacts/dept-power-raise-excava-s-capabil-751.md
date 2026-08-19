# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-751` (dept) · 2026-08-19T01:26:25.559213+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Add **InstantX-ComfyUI’s depth-aware upscaler AFTER RealVisXL v1.1’s face model** in EXCAVA’s pipeline.

**Plan:**
1. Integrate RealVisXL v1.1’s face model as the first stage in EXCAVA’s pipeline to lock facial fidelity.
2. Insert InstantX-ComfyUI’s depth-aware upscaler as the second stage to enhance backgrounds/depth cues.
3. Benchmark 100 frames with the new pipeline vs. baseline to validate a ≥0.5% quality gain.
4. Measure render time impact (target: ≤15% slowdown).
5. Document compute cost per frame (target: ≤8% increase).
6. Merge changes into EXCAVA’s main branch post-validation.

**What changed:**
Depth-aware upscaling now follows RealVisXL’s face model to preserve fidelity while improving frame quality.
