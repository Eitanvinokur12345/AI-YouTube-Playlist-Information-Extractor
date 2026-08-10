# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-980` (dept) · 2026-08-10T10:01:02.969972+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Prioritize motion deblurring to address EXCAVA’s core face fidelity issue before layering specialized upscalers.

**Plan:**
1. Extract 10 representative motion-blurred samples from EXCAVA’s test suite.
2. Run DiffusionBeasts’ *Deblur* on each sample at default settings; log PSNR/SSIM and face fidelity (eyes, teeth, skin).
3. If face fidelity improves by ≥0.5% vs. baseline, integrate *Deblur* into EXCAVA’s pipeline.
4. Swap in RealVisXL 5.0’s face-preserving upscaler *only* if deblurring succeeds.
5. Benchmark combined pipeline (Deblur → RealVisXL) against InstantX-ComfyUI’s depth-aware upscaler.
6. If combined pipeline yields ≥0.5% face fidelity gain, merge changes; else, revert and test Topaz *Video AI* deblurring.

**What changed:**
Motion deblurring now precedes face-focused upscaling to target EXCAVA’s root flaw.
