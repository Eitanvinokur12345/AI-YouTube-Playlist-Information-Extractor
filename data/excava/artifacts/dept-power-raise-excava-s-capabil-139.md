# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-139` (dept) · 2026-08-22T14:36:32.694634+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
**Plan:**
1. Benchmark RVRT and FILM temporal denoisers on EXCAVA’s motion-blurred test clips.
2. Select the model with ≥0.5% motion blur reduction and near-zero compute overhead.
3. Integrate the chosen model into EXCAVA’s pipeline with minimal latency impact.
4. Validate quality gains via A/B testing against baseline EXCAVA outputs.
5. If successful, deprecate InstantX-ComfyUI’s depth-upscaler and SD3.5-Ultra’s motion-refiner nodes.
6. Document pipeline changes and compute cost trade-offs in EXCAVA’s repo.

**What changed:**
Replaced speculative high-cost/black-box fixes with a proven, low-overhead temporal denoiser.
