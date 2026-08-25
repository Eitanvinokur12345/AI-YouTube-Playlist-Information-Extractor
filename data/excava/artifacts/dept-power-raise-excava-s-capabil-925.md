# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-925` (dept) · 2026-08-25T06:38:59.565488+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Add RIFE to EXCAVA’s motion pipeline first—test it against FILM on a high-motion clip; if clarity drops <0.5% and no ghosting appears, integrate it. Own it: Torque.

**Plan:**
1. Replace EXCAVA’s current motion compensation with RIFE in the pipeline.
2. Test RIFE vs. FILM on a 10-frame high-motion clip with EXCAVA’s depth-aware upscaler disabled.
3. Measure clarity drop (target <0.5%) and check for ghosting/artifacts.
4. If passed, integrate RIFE into EXCAVA’s motion pipeline.
5. Benchmark VRAM usage and runtime impact; adjust batching if needed.
6. Document RIFE’s integration in EXCAVA’s repo with performance metrics.

**What changed:**
RIFE replaces FILM in EXCAVA’s motion pipeline pending validation.
