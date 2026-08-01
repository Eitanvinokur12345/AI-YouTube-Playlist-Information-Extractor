# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-150` (dept) · 2026-07-31T16:16:29.035842+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate Runway Gen-4’s 4K upscaler into EXCAVA’s pipeline as the first post-processing step.
2. Test the 10% raw 1080p sample through the new pipeline to verify flicker reduction in 4K output.
3. If flicker is reduced by ≥50% in the test, proceed to layer Kijai’s SD3.5 Medium RealVisXL LoRA at 1440p base resolution.
4. Apply the LoRA with a strength of 0.75 to sharpen textures without exceeding the compute budget.
5. Validate the final output for both flicker stability and texture sharpness against the original pipeline.
6. Document compute cost per frame and inference time for both Gen-4 and LoRA steps.

**What changed:** EXCAVA now uses Runway Gen-4 upscaling first, with optional RealVisXL LoRA for texture enhancement if flicker is resolved.
