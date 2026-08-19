# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-104` (dept) · 2026-08-19T06:28:27.337444+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Replace EXCAVA’s current upscaler with **InstantX-ComfyUI’s depth-aware upscaler** first, then layer **CodeFormer** for face recovery if depth-upscaling still distorts identities—Gearbox owns the integration and Torque validates the 0.5%+ clarity gain.

**Plan:**
1. Integrate InstantX-ComfyUI’s depth-aware upscaler into EXCAVA’s pipeline (Gearbox).
2. Benchmark clarity gains vs. baseline (Torque).
3. If face fidelity drops persist, layer CodeFormer for identity recovery (Torque).
4. Re-benchmark EXCAVA’s full-frame distortion metrics (Torque).
5. Optimize compute trade-offs (Gearbox).
6. Merge changes into main branch (Gearbox).

**What changed:**
Depth-aware upscaling replaces generic upscaler, with CodeFormer fallback for face recovery.
