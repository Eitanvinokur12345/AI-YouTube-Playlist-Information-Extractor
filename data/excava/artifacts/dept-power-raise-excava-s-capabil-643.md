# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-643` (dept) · 2026-08-10T21:44:40.981220+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Combine InstantX-ComfyUI’s depth-aware upscaler with a motion-deblur model to address EXCAVA’s worst-case 10-frame burst with 30° camera pan, ensuring ≥0.5% fidelity gain.

**Plan:**
1. Integrate InstantX-ComfyUI’s depth-aware upscaler into EXCAVA’s pipeline as baseline.
2. Implement RestoreFormer++ (or custom LoRA) for motion deblurring on high-motion frames.
3. Run side-by-side tests on 10-frame bursts with 30° camera pan, comparing:
   - Depth-aware upscaler alone
   - Motion-deblur model alone
   - Combined pipeline
4. Measure fidelity gains via artifact side-by-side metrics (faces + fine details).
5. Optimize compute trade-offs (render time vs. quality) for high-res outputs.
6. Merge the top-performing combo into EXCAVA’s default pipeline.

**What changed:**
Added motion-deblur model (RestoreFormer++/LoRA) alongside InstantX-ComfyUI’s depth-aware upscaler to target motion blur and fine-detail loss.
