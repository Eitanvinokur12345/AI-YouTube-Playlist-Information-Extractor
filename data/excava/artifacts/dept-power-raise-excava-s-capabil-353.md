# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-353` (dept) · 2026-08-25T22:59:02.106024+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate RIFE v4.17 into EXCAVA’s motion pipeline for frame interpolation.
2. Layer MPRNet blind-deblurring on top of RIFE v4.17 for artifact reduction.
3. Conduct side-by-side A/B tests to measure the 0.5% clarity lift.
4. Assign Torque to monitor throughput impact and adjust real-time budget.
5. Assign Gearbox to validate artifact reduction and final quality.
6. Document performance metrics and rollback criteria for each component.

**What changed:** Motion pipeline now uses RIFE v4.17 + MPRNet instead of VFI-Flow or depth-aware upscaling.
