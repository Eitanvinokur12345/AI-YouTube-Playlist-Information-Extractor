# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-695` (dept) · 2026-08-22T10:52:50.334417+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Fork Depth Anything V2’s temporal consistency module from its GitHub repo.
2. Integrate the module into EXCAVA’s pipeline as a motion-blur correction node.
3. Benchmark against baseline (no correction) using EXCAVA’s sharpness metric on 100 noisy/fast-motion test frames.
4. Measure VRAM usage and runtime overhead; target ≤10% VRAM increase.
5. If sharpness gain ≥0.5%, merge into main pipeline; else, iterate with parameter tuning.
6. Document failure modes (e.g., flickering) in a GitHub issue for future fixes.

**What changed:** Prioritized Depth Anything V2’s temporal module over InstantX-ComfyUI/SD3.5-Ultra due to stability and local execution.
