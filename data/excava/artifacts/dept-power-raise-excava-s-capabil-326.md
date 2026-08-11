# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-326` (dept) · 2026-08-11T01:41:33.337142+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Prioritize Real-ESRGAN’s face-specific model for EXCAVA’s keyframes to recover lost facial details.

**Plan:**
1. Integrate Real-ESRGAN’s face model into EXCAVA’s keyframe processing pipeline.
2. Run A/B tests comparing Real-ESRGAN’s output against baseline EXCAVA outputs for face fidelity metrics.
3. Optimize Real-ESRGAN’s parameters (e.g., denoise strength, face enhancement scale) for EXCAVA’s use case.
4. Benchmark runtime impact and adjust pipeline to process only keyframes (skip non-critical frames).
5. Validate 0.5%+ face fidelity gain via human evaluation and automated metrics (e.g., PSNR, LPIPS).
6. Document integration steps and share results with the EXCAVA pipeline team.

**What changed:** Real-ESRGAN face model replaces Flowframes/InstantX in keyframe processing.
