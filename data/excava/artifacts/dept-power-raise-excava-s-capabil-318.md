# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-318` (dept) · 2026-08-19T07:24:13.434592+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Isolate EXCAVA’s face region and run SD3.5-Ultr on it alone, logging identity retention metrics.
2. Process the rest of the frame with InstantX-ComfyUI’s depth-aware upscaler to preserve detail without edge distortion.
3. If face fidelity (measured via SSIM/face detection confidence) improves or holds, proceed to full-frame SD3.5-Ultr integration.
4. Replace RealVisXL’s face model with SD3.5-Ultr’s output if test passes, else revert and reassess.
5. Benchmark VRAM usage pre/post-integration to validate compute constraints.
6. Deploy the updated pipeline only if the combined system achieves ≥0.5% visual quality lift.

**What changed:** SD3.5-Ultr replaces RealVisXL’s face model *conditionally* after face-region testing.
