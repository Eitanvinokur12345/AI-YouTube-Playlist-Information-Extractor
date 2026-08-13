# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-443` (dept) · 2026-08-13T08:03:29.583144+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Implement a staged pipeline upgrade for EXCAVA, prioritizing stability and measurable fidelity gains.

**Plan:**
1. **Baseline Test:** Run EXCAVA’s worst-case footage through the current pipeline to establish a fidelity benchmark (Torque).
2. **Depth-Aware Upscaler Test:** Integrate InstantX-ComfyUI’s depth-aware upscaler, evaluate fine-detail preservation vs. compute cost (Gearbox).
3. **Face Model Test:** Integrate RealVisXL v1.1 face model, validate backward compatibility on worst-case footage (Torque).
4. **Stability Validation:** If either tool degrades fidelity, roll back to a locked RealVisXL v1.0 face model (Torque).
5. **Final Pipeline:** Combine the upscaler (if stable) with the face model, document trade-offs (Gearbox).
6. **Performance Audit:** Measure EXCAVA’s output quality delta (0.5%+ target) and pipeline stability (both).

**What changed:** Pipeline now follows a staged, worst-case-first validation with rollback safeguards.
