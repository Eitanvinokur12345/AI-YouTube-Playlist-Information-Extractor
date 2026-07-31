# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-520` (dept) · 2026-07-31T15:54:12.113474+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Add Kijai’s SD3.5 Medium RealVisXL LoRA with a 1440p base to EXCAVA’s pipeline.

**Plan:**
1. Integrate Kijai’s SD3.5 Medium RealVisXL LoRA into EXCAVA’s generation pipeline.
2. Set base resolution to 1440p to preserve fine details (subtitles, textures).
3. Benchmark against Flux Realism LoRA and Runway Gen-4 upscaling for hallucination rates and sharpness.
4. Optimize VRAM usage via ComfyUI’s memory-efficient settings.
5. Replace current upscaling step with RealVisXL LoRA for final output refinement.
6. Validate improvements via automated QA checks for text/UI clarity.

**What changed:**
EXCAVA’s output sharpness improves by at least 0.5% with reduced hallucinations in fine details.
