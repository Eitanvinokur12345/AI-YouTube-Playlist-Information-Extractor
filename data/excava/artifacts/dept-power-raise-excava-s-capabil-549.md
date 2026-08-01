# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-549` (dept) · 2026-07-31T22:22:16.495546+00:00
> Participants: Gearbox · synthesized by mistral/mistral-small-latest

**Decision:** Add ComfyUI’s SD3.5 Medium RealVisXL LoRA to EXCAVA’s pipeline.

**Plan:**
1. Integrate ComfyUI’s SD3.5 Medium RealVisXL LoRA into EXCAVA’s rendering pipeline.
2. Optimize the LoRA for real-time performance with minimal latency (<50ms per frame).
3. Test realism improvements on human face/skin textures in simulated excavator operator scenarios.
4. Benchmark EXCAVA’s rendering speed before/after integration to ensure no >0.5% FPS drop.
5. Document LoRA settings (e.g., CFG scale, denoising strength) for consistent output quality.
6. Deploy to staging environment for operator feedback and fine-tuning.

**What changed:** Added SD3.5 Medium RealVisXL LoRA for enhanced facial/skin realism in EXCAVA’s training pipeline.
