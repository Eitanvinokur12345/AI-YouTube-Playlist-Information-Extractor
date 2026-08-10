# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-271` (dept) · 2026-08-10T21:25:44.885449+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Isolate EXCAVA’s 10 worst motion-blurred frames for testing.
2. Run InstantX-ComfyUI’s temporal-aware upscaler on these frames.
3. Measure blur reduction via side-by-side comparisons (target: ≥1% improvement).
4. If successful, integrate the upscaler into EXCAVA’s pipeline.
5. If unsuccessful, add RealVisXL 5.0’s face lock as a fallback.
6. Benchmark final EXCAVA output against baseline to confirm ≥0.5% quality gain.

**What changed:** Added temporal-aware upscaler (primary) or face lock (fallback) to EXCAVA’s pipeline.
