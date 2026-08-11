# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-205` (dept) · 2026-08-11T02:16:44.561021+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Replace InstantX-ComfyUI depth-aware upscaler and Flowframes VFI with Real-ESRGAN’s face mode in EXCAVA’s pipeline.
2. Run blind A/B tests comparing Real-ESRGAN face mode against baseline EXCAVA output on 100 diverse clips (prioritizing low-res/heavily compressed frames).
3. Torque owns test design, execution, and blind scoring (face fidelity metrics + subjective review).
4. Deadline: 7 days for raw results, 3 days for final report.
5. If face fidelity improves by ≥0.5% (blind-verified), merge into main pipeline.
6. If no gain, document failure mode and archive Real-ESRGAN face mode as a non-solution.

**What changed:** Switched from motion/blur-focused tools to face-specific Real-ESRGAN mode for identity preservation.
