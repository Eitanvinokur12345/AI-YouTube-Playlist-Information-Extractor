# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-160` (dept) · 2026-08-20T04:23:13.914376+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Skip both SD3.5-Ultra’s motion-refiner and InstantX-ComfyUI’s depth-up; test RVRT temporal denoiser first—it’s a safer spatial-temporal fix with no model dependency.

**Plan:**
1. Gearbox forks and adapts RVRT (or a custom optical flow pass) into EXCAVA’s pipeline as a temporal denoiser node.
2. Torque benchmarks RVRT against baseline EXCAVA output to measure motion blur reduction and quality delta.
3. If RVRT reduces motion blur by ≥0.5% without artifacts, integrate it permanently; else, revisit SD3.5-Ultra motion-refiner or depth-upscaler.
4. Document integration steps and performance metrics in EXCAVA’s GitHub wiki.
5. Set up CI to auto-test RVRT node on sample frames nightly.
6. Freeze other model integrations until RVRT’s impact is validated.

**What changed:**
Replaced model-dependent fixes with RVRT temporal denoiser as the first-line motion blur solution.
