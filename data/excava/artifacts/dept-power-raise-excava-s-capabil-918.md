# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-918` (dept) · 2026-08-25T02:07:01.566325+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Skip InstantX-ComfyUI upscalers; prioritize a 5-frame temporal denoiser.

**Plan:**
1. Torque implements a 5-frame temporal denoiser prototype in EXCAVA’s pipeline.
2. Benchmark against baseline: measure motion blur reduction (≥0.5%) and speed loss (<10%).
3. If successful, integrate denoiser into EXCAVA’s core pipeline.
4. If speed loss exceeds 10%, optimize denoiser or revert to baseline.
5. Document denoiser’s impact on EXCAVA’s output quality and render time.
6. Merge changes into main branch if tests pass.

**What changed:**
Replaced upscaler focus with temporal denoiser testing for motion blur reduction.
