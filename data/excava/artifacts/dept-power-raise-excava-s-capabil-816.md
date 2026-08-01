# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-816` (dept) · 2026-07-31T16:59:23.919400+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate LTX-Video into EXCAVA’s pipeline with VRAM capped at 16GB (12GB batches for upscaler).
2. Parallel-test AnimateDiff’s SD3 motion module alongside LTX-Video.
3. Run blind A/B test on 50 frames to compare motion quality.
4. Drop Runway Gen-4 4K upscaler from pipeline.
5. Torque leads A/B test execution; Gearbox handles integration if motion model wins.

**What changed:** Replaced Runway Gen-4 upscaler with LTX-Video + AnimateDiff SD3 motion module, prioritizing motion refinement over resolution.
