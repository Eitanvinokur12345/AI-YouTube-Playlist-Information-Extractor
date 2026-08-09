# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-605` (dept) · 2026-08-03T04:20:23.788607+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Run a controlled A/B test—InstantX-ComfyUI’s depth-aware upscaler for the whole frame vs. RealVisXL face model only on faces—measure face fidelity gain and compute cost per frame; Gearbox owns the test and delivers the numbers by EOD.

**Plan:**
1. Implement InstantX-ComfyUI’s depth-aware upscaler as baseline for full-frame processing.
2. Integrate RealVisXL’s face model into EXCAVA’s pipeline, applying it only to detected faces.
3. Configure identical test conditions (A100 GPU, same input dataset) for both pipelines.
4. Measure face fidelity (PSNR/SSIM) and compute cost (time/frame, VRAM usage) per variant.
5. Log edge cases (occlusions, extreme motion) and failure modes for each approach.
6. Deliver comparative report (metrics + qualitative analysis) to Dynamo by EOD.

**What changed:**
Hybrid pipeline (depth-aware upscaler + face-specific RealVisXL) will be tested against full-frame depth-aware baseline to validate 0.5%+ power gains.
