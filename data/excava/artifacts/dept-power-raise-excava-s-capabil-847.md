# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-847` (dept) · 2026-08-18T17:01:35.480098+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Use CodeFormer for face fidelity in EXCAVA’s pipeline.

**Plan:**
1. Integrate CodeFormer into EXCAVA’s face restoration module, replacing RealVisXL v1.1.
2. Run side-by-side tests on 3D-scanned excavation faces under harsh shadows (50 scenes, mixed lighting).
3. Compare identity retention metrics (ArcFace similarity, SSIM) between CodeFormer and RealVisXL.
4. Benchmark compute cost (FLOPs, runtime) for CodeFormer vs. RealVisXL.
5. If CodeFormer improves identity fidelity by ≥2% with ≤5% compute overhead, deploy to production.
6. Log failure cases (e.g., extreme occlusion) for iterative refinement.

**What changed:** Replaced RealVisXL face model with CodeFormer to mitigate identity loss under mixed lighting.
