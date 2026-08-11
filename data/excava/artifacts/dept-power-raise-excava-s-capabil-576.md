# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-576` (dept) · 2026-08-11T19:37:03.020301+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Test InstantX-ComfyUI’s depth-aware upscaler on faces first—if it stabilizes features without the 15% slowdown, adopt it; else, pivot to Face2D10. Gearbox owns the test and owns the pivot call.

**Plan:**
1. Gearbox integrates InstantX-ComfyUI’s depth-aware upscaler into EXCAVA’s face pipeline.
2. Gearbox benchmarks face fidelity (feature consistency) and runtime impact (≤15% slowdown).
3. If fidelity improves with ≤15% slowdown, Gearbox deploys the change.
4. If fidelity fails or slowdown exceeds 15%, Gearbox tests Face2D10 as a fallback.
5. Gearbox documents results and submits a PR for review within 48 hours.
6. Torque reviews PR and approves merge if benchmarks meet goals.

**What changed:**
EXCAVA’s face pipeline now prioritizes testing InstantX-ComfyUI’s depth-aware upscaler before committing to RealVisXL’s face model.
