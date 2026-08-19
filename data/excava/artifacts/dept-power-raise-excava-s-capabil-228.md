# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-228` (dept) · 2026-08-19T22:27:50.372908+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Prioritize face fidelity recovery in EXCAVA’s worst motion-blur cases by testing SD3.5-Ultr’s face-refiner node first, with fallback to MGMamba/Stripformer.

**Plan:**
1. Isolate EXCAVA’s worst 10% of frames (highest motion blur) using blur-detection metrics (e.g., Laplacian variance < threshold).
2. Integrate SD3.5-Ultr’s face-refiner node into EXCAVA’s pipeline *only* for these frames, logging VRAM/latency impact.
3. Benchmark face fidelity (e.g., FaceQNet score, landmark stability) vs. baseline; flag drops >0.5%.
4. If fidelity fails, switch to MGMamba or Stripformer for those frames, measuring GPU cost vs. gain.
5. Deploy the refined pipeline to a 1% A/B test on excavator footage, monitoring real-world performance.
6. Document VRAM/latency trade-offs and final face-fidelity delta for owner review.

**What changed:**
Added targeted face-refiner node (SD3.5-Ultr) for worst frames, with fallback to motion-deblur models.
