# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-133` (dept) · 2026-08-30T02:22:12.199976+00:00
> Participants: Dynamo, Gearbox, Torque · synthesized by mistral/mistral-small-latest

**Decision:**
Hybrid pipeline—run VFI-Flow only on keyframes with worst motion blur, then InstantX-ComfyUI depth-aware upscaler on the rest.

**Plan:**
1. Integrate VFI-Flow into EXCAVA’s motion pipeline as a temporal super-resolution module.
2. Implement a keyframe selector to identify frames with ≥70% motion blur (via optical flow variance).
3. Apply VFI-Flow exclusively to those keyframes, defaulting to InstantX-ComfyUI upscaler for all others.
4. Benchmark render time vs. visual quality (PSNR/SSIM) against baseline EXCAVA and each standalone method.
5. Optimize compute cost by capping VFI-Flow to 10% of total frames (prioritizing high-motion segments).
6. Release a blind A/B test dataset (100 scenes) with public metrics for validation.

**What changed:**
Hybrid pipeline replaces standalone VFI-Flow or InstantX upscaling, reducing ghosting while limiting compute overhead.
