# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-464` (dept) · 2026-08-20T04:06:09.131533+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Skip InstantX-ComfyUI’s depth-aware upscaler and SD3.5-Ultra’s motion-refiner; prioritize testing InstantX-ComfyUI’s temporal upscaler.

**Plan:**
1. Integrate InstantX-ComfyUI’s temporal upscaler into EXCAVA’s pipeline.
2. Test on a 10-second clip with heavy motion blur, comparing output to current baseline.
3. Measure VRAM usage, speed impact, and artifact reduction vs. depth-aware/motion-refiner nodes.
4. Benchmark against SD3.5-Ultra’s motion-refiner under identical conditions.
5. If temporal upscaler fails, evaluate hybrid approaches (e.g., temporal + depth-aware).
6. Document results in `/docs/EXCAVA_upgrade_log.md` with metrics.

**What changed:**
Prioritized temporal upscaler over spatial/depth-aware and motion-refiner nodes.
