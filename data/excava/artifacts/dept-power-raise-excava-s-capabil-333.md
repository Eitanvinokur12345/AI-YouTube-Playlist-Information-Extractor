# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-333` (dept) · 2026-08-20T03:49:03.369326+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
**Plan:**
1. Integrate ComfyUI’s TemporalNet node into EXCAVA’s pipeline via Cerebras’ llama-3.3-70b temporal model.
2. Replace SD3.5-Ultra motion-refiner and InstantX-ComfyUI depth-upscaler with TemporalNet for motion blur reduction.
3. Benchmark TemporalNet against baseline EXCAVA output to measure motion blur reduction (target: ≥0.5% quality gain).
4. Optimize TemporalNet node for EXCAVA’s compute constraints (e.g., batch processing, precision tuning).
5. Validate temporal consistency and edge sharpness in output frames.
6. Merge changes into EXCAVA’s main branch post-validation.

**What changed:** Replaced proposed upscaler/motion-refiner with Cerebras’ temporal model for lower-cost motion blur reduction.
