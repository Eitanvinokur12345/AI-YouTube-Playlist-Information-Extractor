# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-760` (dept) · 2026-09-01T04:00:30.639494+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement VFI-Flow in EXCAVA’s motion pipeline to target temporal artifacts.
2. Apply VFI-Flow *only* to keyframes with the worst motion blur (prioritize aerial footage).
3. Use EXCAVA’s default interpolation for non-keyframes to minimize runtime.
4. Torque tests the 100-frame aerial clip, logging artifacts (jitter/ghosting) and runtime impact.
5. If artifacts exceed tolerance, revert to depth-aware upscaling for those frames.
6. Measure quality gain (target ≥0.5%) and runtime impact (<10% net increase).

**What changed:** VFI-Flow selectively applied to keyframes, replacing full-pipeline depth-aware upscaling.
