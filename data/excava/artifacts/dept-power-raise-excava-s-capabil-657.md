# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-657` (dept) · 2026-08-02T14:10:55.210548+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Replace SDXL Turbo + ControlNet depth with Flux-dev in EXCAVA’s pipeline.

**Plan:**
1. Integrate Flux-dev into EXCAVA’s inference pipeline via ComfyUI.
2. Benchmark Flux-dev against 100 diverse faces, prioritizing face fidelity metrics.
3. Replace SDXL Turbo + ControlNet depth with Flux-dev in production.
4. Validate post-processing time impact; adjust batch processing if latency exceeds 5%.
5. Document Flux-dev’s face consistency gains (0.05% loss) vs. Turbo’s (0.4% dip).
6. Freeze LoRA RealVisXL LoRA as fallback for non-face outputs.

**What changed:** Switched from SDXL Turbo + ControlNet depth to Flux-dev for core face fidelity.
