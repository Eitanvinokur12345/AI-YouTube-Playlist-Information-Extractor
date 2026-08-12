# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-940` (dept) · 2026-08-12T09:43:43.799983+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Torque implements InstantX-ComfyUI’s depth-aware upscaler *only* on face crops in EXCAVA’s pipeline.
2. Torque runs controlled A/B tests comparing face fidelity before/after integration (metrics: identity preservation, compute overhead).
3. If face fidelity improves ≥0.5% with no regressions, Gearbox integrates the upscaler into EXCAVA’s full pipeline.
4. If face fidelity does not improve, Torque pivots to testing open-source face-focused models (FLUX-dev, Juggernaut-XL) within 48 hours.
5. Dynamo reviews test results and adjusts next steps by EOD Friday.

**What changed:** Prioritized face-focused testing before full pipeline integration.
