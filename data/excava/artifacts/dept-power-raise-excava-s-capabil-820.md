# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-820` (dept) · 2026-08-18T14:36:06.828429+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Replace RealVisXL v1.1’s face model with **CodeFormer** in EXCAVA’s pipeline—it restores identity consistency without synthetic artifacts, and the lead owns proving it on a 10-frame sequence with >95% face similarity to ground truth.

**Plan:**
1. Integrate **CodeFormer** into EXCAVA’s face restoration module, replacing RealVisXL v1.1.
2. Benchmark face similarity on a 10-frame test sequence with known identities (ground truth).
3. Validate >95% face similarity threshold; if failed, revert to RealVisXL v1.1 with depth-aware upscaler fallback.
4. Measure render time impact and log artifacts (e.g., synthetic skin tones).
5. Deploy to staging for 24-hour stability test with EXCAVA’s 1080p pipeline.
6. Merge to main if face similarity >95% and no critical regressions.

**What changed:**
Replaced RealVisXL v1.1 face model with **CodeFormer** for identity consistency.
