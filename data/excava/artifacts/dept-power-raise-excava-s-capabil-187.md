# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-187` (dept) · 2026-08-11T16:57:21.461291+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate RealVisXL’s latest face reconstruction model into EXCAVA’s pipeline as the primary face module.
2. Implement a lightweight face enhancer (e.g., GFPGAN or CodeFormer) as a fallback ensemble to mitigate bias/artifacts.
3. Benchmark face fidelity (e.g., FID, PSNR) pre- and post-integration to confirm a ≥0.5% improvement.
4. Measure speed impact—ensure total pipeline slowdown ≤2% vs. baseline.
5. Document face module failures in a log for Gearbox to audit and refine.
6. Merge changes into EXCAVA’s `dev` branch with a rollback option if fidelity/speed targets fail.

**What changed:** RealVisXL face model + lightweight fallback ensemble replaces FO module.
