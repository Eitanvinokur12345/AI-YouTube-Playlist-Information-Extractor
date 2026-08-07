# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-837` (dept) · 2026-08-07T13:52:29.411475+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Replace EXCAVA’s face upscaler with ComfyUI’s FaceDetailer (SD3.5 face mode) for fidelity fixes.

**Plan:**
1. Integrate ComfyUI’s FaceDetailer node into EXCAVA’s post-processing pipeline.
2. Configure FaceDetailer to run in SD3.5 face mode for high-fidelity face preservation.
3. Remove RealVisXL 5.0’s face-preserving upscaler from the pipeline.
4. Benchmark face fidelity metrics pre/post-integration to validate improvements.
5. Document pipeline changes and trade-offs (speed vs. quality) in EXCAVA’s repo.
6. Torque to own implementation and testing, with Gearbox supporting pipeline integration.

**What changed:**
EXCAVA’s face upscaler replaced with ComfyUI FaceDetailer (SD3.5 face mode).
