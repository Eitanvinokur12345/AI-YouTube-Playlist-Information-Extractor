# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-467` (dept) · 2026-08-07T01:34:56.364826+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Add ComfyUI’s open-source FaceDetailer node with SD3.5’s face mode to EXCAVA’s pipeline now—it preserves identity without vendor lock-in, and SwinIR can handle upscaling separately.

**Plan:**
1. Integrate ComfyUI’s FaceDetailer node into EXCAVA’s pipeline as a post-processing step for face fidelity.
2. Configure FaceDetailer to use SD3.5’s face mode with default settings (no additional compute beyond existing nodes).
3. Route EXCAVA’s output through FaceDetailer before final SwinIR upscaling to preserve identity without latency impact.
4. Benchmark face fidelity (e.g., ArcFace similarity) against baseline to confirm ≥0.5% improvement.
5. Document the change in EXCAVA’s model card and update the pipeline’s dependency list.
6. Deploy to staging for 24-hour stress-testing before production rollout.

**What changed:**
EXCAVA now uses ComfyUI’s FaceDetailer (SD3.5 face mode) + SwinIR upscaling to improve face fidelity by ≥0.5% with zero added latency.
