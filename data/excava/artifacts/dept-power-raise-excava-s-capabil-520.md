# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-520` (dept) · 2026-08-03T05:11:16.186688+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Test Flux-dev's face-detail branch in EXCAVA's pipeline to achieve a 0.5%+ face fidelity gain.
**Plan:**
1. Integrate Flux-dev's face-detail branch into EXCAVA's pipeline for testing.
2. Benchmark Flux-dev's face-detail branch against RealVisXL's face-preserving upscaler and InstantX-ComfyUI's depth-aware upscaler.
3. Evaluate the compute overhead of Flux-dev's face-detail branch and optimize if necessary.
4. Compare face fidelity gains from Flux-dev's face-detail branch with other upscaling methods.
5. Refine EXCAVA's pipeline to incorporate the chosen upscaling method for improved face fidelity.
**What changed:** Replaced consideration of vendor-locked RealVisXL with open-weight Flux-dev for face fidelity enhancement.
