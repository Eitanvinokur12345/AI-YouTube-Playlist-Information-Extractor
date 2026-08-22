# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-831` (dept) · 2026-08-22T14:51:53.695057+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Skip both InstantX-ComfyUI’s depth-aware upscaler and SD3.5-Ultra’s motion-refiner—test a frame-interpolation model like FILM or RIFE first to address motion blur directly, then integrate only if it delivers measurable clarity gain without artifacts.

**Plan:**
1. Benchmark FILM or RIFE on a 10-frame blurred clip from EXCAVA’s dataset, measuring PSNR/SSIM and manual artifact review.
2. If FILM/RIFE reduces blur without jitter/ghosting, integrate it into EXCAVA’s pipeline with a toggle for fallback.
3. If FILM/RIFE fails, test a hybrid approach: apply InstantX-ComfyUI’s upscaler *only* to non-blurred frames post-interpolation.
4. Document compute cost per frame for each tested model (FILM/RIFE vs. InstantX vs. SD3.5-Ultra).
5. Prioritize models with published benchmarks or EXCAVA-specific validation data.
6. Freeze pipeline changes until at least 0.5% visual fidelity improvement is confirmed via automated + human evaluation.

**What changed:** Motion blur addressed via frame interpolation first, with fallback to spatial/temporal refiners only if validated.
