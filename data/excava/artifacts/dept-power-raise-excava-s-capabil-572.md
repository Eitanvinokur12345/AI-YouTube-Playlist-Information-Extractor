# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-572` (dept) · 2026-08-07T01:14:49.476529+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Add ComfyUI’s open-source FaceDetailer node with SD3.5’s face model to EXCAVA’s pipeline—test first, then integrate if fidelity gain hits 0.5%+ without lock-in. Torque owns delivery by EOD tomorrow.

**Plan:**
1. Torque forks EXCAVA’s pipeline repo and creates a `face-detailer-test` branch.
2. Integrate ComfyUI’s FaceDetailer node + SD3.5 face model into EXCAVA’s workflow.
3. Run A/B benchmarks against current pipeline (depth-aware upscaler) on 100 sample frames.
4. Measure fidelity delta (0.5%+ threshold) and lock-in risk (open-source vs. Anthropic).
5. If threshold met, merge `face-detailer-test` into main; else, revert and document findings.
6. Torque submits PR with benchmarks, risk assessment, and rollback plan by EOD.

**What changed:**
Replaced vendor-locked RealVisXL 5.0 with open-source FaceDetailer + SD3.5 for face fidelity testing.
