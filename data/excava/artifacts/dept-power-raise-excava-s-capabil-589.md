# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-589` (dept) · 2026-08-13T14:01:40.157660+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt InstantX-ComfyUI’s depth-aware upscaler for face crops first, with fallback to RealVisXL v1.0 if gains <0.5%.

**Plan:**
1. Isolate face crops from EXCAVA’s pipeline and run InstantX-ComfyUI’s depth-aware upscaler on them.
2. Measure face detail retention (target ≥0.3% gain) and inspect metal texture integrity post-upscale.
3. If gains ≥0.5% net (face detail + no corruption), integrate the upscaler into EXCAVA’s full pipeline.
4. If gains <0.5%, test RealVisXL v1.0’s face model on face crops with metal texture validation.
5. If RealVisXL v1.0 passes (≥0.5% net gain, no corruption), adopt it; else reject both tools.
6. Document render time impact and quality metrics for each test.

**What changed:**
Prioritized InstantX-ComfyUI’s face upscaler with RealVisXL v1.0 as fallback, enforcing ≥0.5% net gain threshold.
