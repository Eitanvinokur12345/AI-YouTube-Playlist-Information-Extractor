# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-715` (dept) · 2026-08-20T02:02:52.200320+00:00
> Participants: Dynamo, Gearbox, Torque · synthesized by mistral/mistral-small-latest

**Decision:**
Prioritize temporal-sharpness over static refiners; test VRT/RVRT on worst face frames first.

**Plan:**
1. Isolate EXCAVA’s worst 10% face frames (highest motion blur).
2. Run baseline pipeline on these frames to establish motion-blur severity.
3. Apply VRT or RVRT temporal-sharpness model to the isolated frames.
4. Compare pre/post results using EXCAVA’s fidelity metrics (target: ≥0.5% gain).
5. If gain ≥0.5%, integrate VRT/RVRT into EXCAVA’s pipeline; else, test Gearbox’s InstantX depth-upscaler as fallback.
6. Document runtime impact and motion consistency improvements.

**What changed:**
Replaced SD3.5 face-refiner and InstantX depth-upscaler with temporal-sharpness model (VRT/RVRT) as primary fix.
