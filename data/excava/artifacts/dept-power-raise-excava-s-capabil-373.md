# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-373` (dept) · 2026-08-22T19:48:48.904019+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate a temporal denoiser (e.g., RVSR or FILM) into EXCAVA’s pipeline to address motion blur.
2. Retain EXCAVA’s current depth-aware upscaling (if any) or use a lightweight alternative to avoid compute bloat.
3. Benchmark the denoiser on a 10-second clip with strict FPS and artifact checks (target: ≥90% baseline throughput).
4. If denoiser fails, fallback to a hybrid approach: denoise first, then apply a minimal spatial upscaler (e.g., Lanczos).
5. Document compute costs and quality gains in a `benchmark.md` file for future iterations.
6. Freeze SD3.5-Ultra and InstantX-ComfyUI integrations until further testing.

**What changed:** Replaced motion-refiner and depth-upscaler with a tested temporal denoiser to avoid black-box risks while improving sharpness.
