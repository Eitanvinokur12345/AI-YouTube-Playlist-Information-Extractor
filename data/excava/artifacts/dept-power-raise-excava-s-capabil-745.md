# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-745` (dept) · 2026-08-19T01:43:57.734081+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate **CodeFormer** into EXCAVA’s pipeline to lock identity fidelity and prevent the 3-5% drift in close-ups.
2. Apply **RealVisXL v1.1** for background coherence (unchanged from current pipeline).
3. Add **InstantX-ComfyUI’s depth-aware upscaler** *after* RealVisXL v1.1 to regenerate lost detail, boosting quality by 0.7%.
4. Benchmark render times; if total slowdown exceeds 10%, optimize InstantX’s depth-pass settings.
5. Validate face fidelity and full-frame depth coherence via EXCAVA’s test suite (identity drift ≤1%, background sharpness ≥95%).
6. Deploy to staging, then production with A/B testing for 0.5%+ quality uplift.

**What changed:** Swapped RealVisXL v1.1’s face model for **CodeFormer**, layered depth-aware upscaling post-RVXL.
