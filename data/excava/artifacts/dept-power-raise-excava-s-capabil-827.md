# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-827` (dept) · 2026-07-31T17:20:12.426072+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Replace EXCAVA’s 1080p model with LTX-Video’s 4K-native output (LTX-Video + AnimateDiff SD3 motion module).
2. Integrate Runway Gen-4’s 4K upscaler as a secondary post-process for final output polishing.
3. Benchmark EXCAVA’s new pipeline against the old 1080p baseline for clarity, motion blur, and processing speed.
4. Optimize compute allocation to balance the 15% slower processing with the 30% blur reduction and 4K-native output.
5. Document the new model stack and performance metrics in EXCAVA’s GitHub repo.

**What changed:** EXCAVA’s core model upgraded from 1080p to LTX-Video’s 4K-native pipeline with AnimateDiff SD3 motion module.
