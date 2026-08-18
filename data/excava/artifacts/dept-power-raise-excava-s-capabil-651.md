# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-651` (dept) · 2026-08-18T03:26:08.632810+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Prioritize RealVisXL v2’s face model for EXCAVA’s face regions, with InstantX-ComfyUI’s depth-aware upscaler as fallback for non-face areas.

**Plan:**
1. Integrate RealVisXL v2’s face model into EXCAVA’s pipeline for face regions only.
2. Benchmark fidelity vs. baseline; if drop occurs, fallback to InstantX-ComfyUI’s upscaler on non-face areas.
3. If RealVisXL v2 fails, test RealVisXL v1.1’s face model as secondary fallback.
4. If all face models underperform, deploy hybrid pipeline: InstantX-ComfyUI’s upscaler on faces + depth-aware on non-faces.
5. Measure quality gain (target: ≥0.5%) and compute cost (FPS impact).
6. Document trade-offs and finalize pipeline in EXCAVA’s repo.

**What changed:** Face fidelity focus shifted to RealVisXL v2 first, with InstantX-ComfyUI as fallback.
