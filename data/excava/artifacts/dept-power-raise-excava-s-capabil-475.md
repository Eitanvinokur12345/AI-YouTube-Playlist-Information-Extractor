# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-475` (dept) · 2026-08-30T03:16:25.375784+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Hybrid pipeline—run VFI-Flow only on keyframes with worst motion blur, measured by optical flow variance > threshold; rest use depth-aware upscaler for spatial sharpness. Owner: Gearbox.

**Plan:**
1. Integrate InstantX-ComfyUI’s depth-aware upscaler into EXCAVA’s spatial pipeline for all frames.
2. Add VFI-Flow to the motion pipeline, gated by optical flow variance > threshold (high-motion segments only).
3. Set threshold empirically via test runs on 100 sample frames, targeting 0.5%+ quality gain.
4. Benchmark compute overhead: ensure hybrid approach stays within 5% total runtime increase.
5. Validate output quality via PSNR/SSIM on 1000-frame test set; iterate threshold if needed.
6. Document integration steps in `/docs/pipeline_updates.md` with performance metrics.

**What changed:** Hybrid pipeline combining depth-aware upscaling (spatial) and VFI-Flow (temporal, gated).
