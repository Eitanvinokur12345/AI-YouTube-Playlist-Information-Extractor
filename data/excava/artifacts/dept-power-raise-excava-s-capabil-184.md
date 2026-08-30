# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-184` (dept) · 2026-08-30T02:40:17.692559+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate VFI-Flow into EXCAVA’s motion pipeline for keyframes with worst motion blur.
2. Apply InstantX-ComfyUI’s depth-aware upscaler to all frames for spatial detail.
3. Benchmark render time impact (target: <15% overhead).
4. Validate quality gain on high-motion test scenes (target: ≥1.3% improvement).
5. Document fallback to depth-aware upscaler if VFI-Flow fails on edge cases.
6. Merge changes into EXCAVA’s main branch post-validation.

**What changed:** Hybrid pipeline combining temporal (VFI-Flow) and spatial (InstantX-ComfyUI) upscaling.
