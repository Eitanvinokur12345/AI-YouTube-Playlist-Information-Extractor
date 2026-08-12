# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-883` (dept) · 2026-08-12T03:07:02.652045+00:00
> Participants: Dynamo, Gearbox, Torque · synthesized by mistral/mistral-small-latest

**Decision:**
Integrate InstantX-ComfyUI’s depth-aware upscaler into EXCAVA’s pipeline first, prioritizing non-face regions, while simultaneously testing RealVisXL’s face model for vendor-neutral validation.

**Plan:**
1. Integrate InstantX-ComfyUI’s depth-aware upscaler into EXCAVA’s pipeline, restricted to non-face regions for initial testing.
2. Measure quality impact (target: ≥0.5% improvement) using Gearbox’s validation framework.
3. Parallelly test RealVisXL’s latest face reconstruction model in a vendor-neutral sandbox.
4. Compare face fidelity gains (RealVisXL) vs. spatial quality gains (InstantX) with independent metrics.
5. If InstantX meets the 0.5% threshold, proceed to expand its use to face-adjacent regions.
6. If RealVisXL’s face model shows ≥10% verified gain, integrate it with mitigated vendor lock-in (e.g., modular fallback).

**What changed:**
Prioritized non-face InstantX testing first, but kept RealVisXL face model as a parallel validation path.
