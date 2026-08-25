# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-470` (dept) · 2026-08-25T01:25:14.378114+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Skip SD3.5-Ultra’s motion-refiner and InstantX-ComfyUI’s depth-aware upscaler—neither guarantees a provable 0.5% EXCAVA quality gain.

**Plan:**
1. **Baseline Validation:** Run a 100-frame clip through EXCAVA’s current pipeline to establish a PSNR baseline.
2. **Depth-Aware Test:** Integrate InstantX-ComfyUI’s depth-aware upscaler, measure PSNR vs. baseline—abort if gain <0.5%.
3. **Motion-Refiner Test:** Integrate SD3.5-Ultra’s motion-refiner, measure PSNR vs. baseline—abort if gain <0.5% or latency >0.5%.
4. **Hybrid Test:** If either passes, combine the winning model with EXCAVA’s core pipeline for a final 100-frame validation.
5. **Rollback Clause:** If both fail, revert to baseline and log failure reasons for future iteration.

**What changed:** Rejected both proposed models due to unproven gains.
