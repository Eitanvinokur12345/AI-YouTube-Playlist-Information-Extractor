# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-235` (dept) · 2026-08-11T01:59:38.414159+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Prioritize face-specific fidelity in high-motion scenes by testing Real-ESRGAN’s face model over depth-aware upscaling or generic VFI.

**Plan:**
1. Integrate Real-ESRGAN’s face-specific model into EXCAVA’s pipeline as a replacement for the current upscaler.
2. Benchmark face fidelity in high-motion scenes against baseline (current pipeline) and alternatives (InstantX-ComfyUI depth-aware, Flowframes VFI).
3. Profile VRAM/compute overhead of Real-ESRGAN’s face model; optimize batch sizes or precision if needed.
4. If face fidelity improves by ≥0.5% with acceptable trade-offs, merge into main branch; otherwise, iterate with FILM-Face as fallback.
5. Document face-specific metrics (e.g., facial landmark stability, PSNR on faces) in the repo’s performance logs.
6. Freeze other pipeline changes until face fidelity is validated.

**What changed:**
Replaced generic upscaler/VFI debate with a targeted face-fidelity focus using Real-ESRGAN’s face model.
