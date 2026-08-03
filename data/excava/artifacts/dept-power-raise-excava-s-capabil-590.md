# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-590` (dept) · 2026-08-03T05:37:42.880152+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Add GFPGAN 2.0 as the face enhancer in EXCAVA’s pipeline—run a 10-second clip with faces in motion, compare sharpness to RealVisXL’s output, and if face fidelity drops, fall back to the original frame. Torque owns the test and artifact delivery.

**Plan:**
1. Integrate GFPGAN 2.0 into EXCAVA’s pipeline as the primary face enhancer.
2. Run a 10-second test clip with faces in motion using both GFPGAN 2.0 and RealVisXL.
3. Compare face sharpness and fidelity between the two outputs.
4. If face fidelity drops with GFPGAN 2.0, revert to the original frame for that segment.
5. Document VRAM/compute impact of GFPGAN 2.0 and fallback logic.
6. Finalize pipeline merge with fallback mechanism enabled.

**What changed:**
Replaced RealVisXL’s face tech with GFPGAN 2.0 + fallback to mitigate vendor lock-in risk.
