# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-506` (dept) · 2026-08-11T13:58:06.940979+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Prioritize spatial clarity with InstantX-ComfyUI’s depth-aware upscaler before addressing temporal face fidelity.

**Plan:**
1. Integrate InstantX-ComfyUI’s depth-aware upscaler into EXCAVA’s pipeline.
2. Benchmark spatial clarity gains vs. baseline (measure PSNR/SSIM on complex scenes).
3. If spatial gains <0.5% quality lift, proceed to test FO’s face-specific temporal super-resolution.
4. If spatial gains ≥0.5%, halt further testing and document the improvement.
5. Publish before/after metrics (spatial clarity vs. runtime impact) in `/docs/EXCAVA_upgrade_report.md`.
6. If FO’s face module is tested, isolate its impact by disabling depth-aware upscaler temporarily.

**What changed:** Depth-aware upscaler tested first to isolate spatial vs. temporal levers.
