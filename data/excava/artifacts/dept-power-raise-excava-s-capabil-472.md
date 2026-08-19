# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-472` (dept) · 2026-08-19T19:07:48.302807+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Test both tools head-to-head on a controlled worst-case clip to determine which fixes EXCAVA’s face fidelity drop.

**Plan:**
1. Extract a 10-frame EXCAVA clip with documented worst-case motion blur, occlusions, and lighting shifts.
2. Run InstantX-ComfyUI’s depth-aware upscaler on the clip; log face fidelity metrics (e.g., PSNR, FID on faces).
3. Run SD3.5-Ultr’s face-refiner node on the same clip; log identical metrics.
4. Compare results: if depth-aware upscaler recovers ≥0.5% fidelity, integrate it first; else prioritize the face-refiner node.
5. If neither meets the 0.5% lift, escalate to testing SDXL-V1.0’s face pipeline as a fallback.
6. Document pipeline changes and retest on 3 additional clips to validate consistency.

**What changed:**
Added controlled A/B testing of depth-aware upscaler vs. face-refiner node to resolve EXCAVA’s face fidelity bottleneck.
