# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-871` (dept) · 2026-09-01T04:19:08.904856+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate RIFE’s clean mode temporal denoiser into EXCAVA’s pipeline and benchmark against baseline to confirm temporal artifacts (ghosting/strobing) are the primary bottleneck.
2. If RIFE clean mode reduces artifacts by ≥0.5% without significant compute overhead, proceed to step 3; else, skip to step 4.
3. Deploy lightweight temporal denoiser as default for all frames, reserving VFI-Flow for keyframes with worst motion blur (prioritizing compute efficiency).
4. If RIFE fails, test VFI-Flow’s temporal interpolation on a 10% sample of clips to measure motion blur reduction vs. compute cost.
5. If VFI-Flow passes (≥0.5% motion clarity gain), integrate it selectively (keyframes only) with a 20-30% compute budget cap per clip.
6. Add InstantX-ComfyUI’s depth-aware upscaler to non-motion-critical frames (e.g., static shots) to enhance detail without impacting temporal pipeline.

**What changed:** Hybrid pipeline prioritizes temporal artifact reduction first (RIFE/VFI-Flow), then selective depth-aware upscaling for quality gains.
