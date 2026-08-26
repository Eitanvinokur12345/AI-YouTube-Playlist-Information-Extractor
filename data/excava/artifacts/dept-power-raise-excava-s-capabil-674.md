# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-674` (dept) · 2026-08-26T09:43:42.164778+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Prepare a 10-second test clip with heavy motion blur.
2. Implement InstantX-ComfyUI’s depth-aware upscaler in EXCAVA’s pipeline.
3. Integrate VFI-Flow into EXCAVA’s motion pipeline.
4. Test Real-ESRGAN’s motion-aware mode as a baseline.
5. Measure clarity gain (PSNR/SSIM) and throughput drop (FPS) for each method.
6. Document results in a GitHub issue for review.

**What changed:** Added head-to-head testing for depth-aware upscaling, motion reconstruction, and motion-aware upscaling to resolve EXCAVA’s quality bottleneck.
