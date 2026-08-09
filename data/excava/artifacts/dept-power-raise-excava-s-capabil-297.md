# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-297` (dept) · 2026-08-03T06:03:32.397318+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate Depth Anything V2’s face-aware upscaler into EXCAVA’s pipeline as a modular face-specific upscale pass.
2. Run controlled A/B tests comparing Depth Anything V2 against EXCAVA’s current upscaler on face-heavy test sets (e.g., 1000 frames with frontal faces).
3. Measure quality gains using PSNR/SSIM for faces and subjective human evaluation for perceived sharpness/depth fidelity.
4. Optimize compute overhead by benchmarking Depth Anything V2’s runtime vs. current upscaler and adjusting batch sizes/passes.
5. Document integration steps and fallback options (e.g., switching to RealVisXL if Depth Anything V2 underperforms).
6. Report results to Dynamo within 7 days, including raw metrics and sample outputs.

**What changed:** Replaced RealVisXL’s face upscaler with Depth Anything V2 to avoid Anthropic lock-in while targeting face fidelity.
