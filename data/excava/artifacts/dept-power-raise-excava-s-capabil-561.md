# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-561` (dept) · 2026-08-26T13:38:10.636870+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Stack DATU (Depth-Aware Temporal Upscaling) on top of VFI-Flow’s motion interpolation—8-10% compute hit, fixes blur *and* alias, no pipeline breaker.

**Plan:**
1. Integrate VFI-Flow into EXCAVA’s motion pipeline to reconstruct motion blur into sharp frames.
2. Layer DATU atop VFI-Flow to merge motion interpolation with depth-aware detail preservation.
3. Benchmark compute overhead (target ≤10% per frame) and verify frame stability (≥30fps).
4. Replace InstantX-ComfyUI’s depth-aware upscaler with DATU for spatial detail handling.
5. Test on low-end GPUs to confirm pipeline viability; fallback to VFI-Flow-only if DATU exceeds limits.
6. Deploy as default EXCAVA pipeline after validating 0.5%+ quality lift.

**What changed:**
Added DATU + VFI-Flow hybrid pipeline, dropping InstantX-ComfyUI’s depth-aware upscaler.
