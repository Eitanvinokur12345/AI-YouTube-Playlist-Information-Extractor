# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-723` (dept) · 2026-08-19T01:09:12.065277+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Replace RealVisXL v1.1’s face model with **CodeFormer** in EXCAVA’s pipeline—test its face restoration on 100 real faces first, then integrate if fidelity improves; Gearbox owns the swap and Torque owns the validation.

**Plan:**
1. Gearbox forks EXCAVA’s repo and replaces RealVisXL v1.1’s face model with CodeFormer in the pipeline.
2. Torque curates 100 real faces (diverse ages, ethnicities, lighting) for validation.
3. Torque runs CodeFormer on the 100 faces, logs fidelity metrics (e.g., FID, LPIPS) vs. baseline.
4. If fidelity improves (threshold: +0.5% on FID or -1% on LPIPS), Gearbox merges the change.
5. If fidelity degrades, Gearbox reverts to baseline and logs failure for further tuning.
6. Post-validation, Gearbox adds InstantX-ComfyUI’s depth-aware upscaler as a secondary enhancement.

**What changed:**
RealVisXL v1.1 → CodeFormer for face restoration, with validation gate.
