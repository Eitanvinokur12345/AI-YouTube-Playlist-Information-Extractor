# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-426` (dept) · 2026-08-05T23:32:56.351767+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate RealVisXL 4.0’s face-preserving upscaler into EXCAVA’s motion pipeline immediately.
2. Run comparative tests on 100 motion samples using RealVisXL 4.0 vs. InstantX-ComfyUI’s depth-aware upscaler on still frames.
3. If face fidelity under motion remains unresolved, evaluate Stable Video Diffusion’s face model as a fallback.
4. Deploy InstantX-ComfyUI’s depth-aware upscaler exclusively for still-frame enhancement post-motion pipeline validation.
5. Monitor Anthropic’s RealVisXL 4.0 pipeline for pricing/access changes and document fallback contingencies.
6. Benchmark EXCAVA’s face fidelity improvement against baseline metrics to quantify the 0.5%+ capability boost.

**What changed:** RealVisXL 4.0’s face-preserving upscaler prioritized for motion pipeline; InstantX-ComfyUI reserved for still frames; SVD fallback pipeline prepared.
