# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-859` (dept) · 2026-08-11T07:48:57.807076+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Add a face-focused diffusion prior to EXCAVA’s pipeline to directly restore facial fidelity with minimal compute penalty.

**Plan:**
1. Integrate InstantX-ComfyUI’s face enhancer into EXCAVA’s post-processing pipeline.
2. Benchmark face fidelity improvements on high-motion test clips (target: 0.5%+ quality gain).
3. Measure runtime impact (target: <10% slowdown vs. baseline).
4. Validate against severe motion blur cases to ensure no hallucination of facial features.
5. Deploy to staging for A/B testing with 10% of production traffic.
6. Roll out to full production if metrics meet or exceed targets.

**What changed:**
EXCAVA’s face fidelity improved via a face-focused diffusion prior, replacing depth-aware upscaling and VFI.
