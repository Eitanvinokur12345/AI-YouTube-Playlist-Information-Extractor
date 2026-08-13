# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-720` (dept) · 2026-08-13T16:50:29.303267+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
**Plan:**
1. Integrate InstantX-ComfyUI’s depth-aware upscaler into EXCAVA’s texture pipeline.
2. Run blind A/B tests comparing texture fidelity (PSNR/SSIM) against baseline EXCAVA outputs.
3. If texture sharpness improves by ≥0.5%, adopt the upscaler; else, discard.
4. If discarded, test RealVisXL v1.0’s face model on facial fidelity (same metrics).
5. Benchmark render time impact (15% max tolerance) for adopted tools.
6. Document results in GitHub repo with artifacts.

**What changed:** Prioritized texture fidelity testing before face model adoption.
