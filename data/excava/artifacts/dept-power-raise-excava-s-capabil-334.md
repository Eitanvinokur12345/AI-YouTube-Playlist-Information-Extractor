# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-334` (dept) · 2026-08-18T14:17:48.531711+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Replace RealVisXL v1.1’s face model with **CodeFormer** in EXCAVA’s pipeline.
2. Integrate **InstantX-ComfyUI’s depth-aware upscaler** after face refinement to boost output sharpness.
3. Benchmark render time impact of both changes against baseline EXCAVA.
4. Fine-tune CodeFormer’s parameters for EXCAVA’s real-world face distribution.
5. Validate identity preservation and sharpness gains via automated perceptual metrics (e.g., LPIPS, FID).
6. Deploy changes to staging branch and iterate based on A/B test results.

**What changed:** Switched face model to CodeFormer + added depth-aware upscaler.
