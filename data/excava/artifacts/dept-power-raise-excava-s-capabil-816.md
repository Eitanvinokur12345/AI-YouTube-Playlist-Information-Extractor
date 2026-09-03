# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-816` (dept) · 2026-09-03T19:24:40.626125+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate InstantX-ComfyUI’s depth-aware upscaler into EXCAVA’s pipeline for all frames.
2. Log processing time deltas for upscaling vs. baseline.
3. Apply VFI-Flow *only* to keyframes flagged by motion blur detection (threshold: blind A/B test sharpness drop ≥15%).
4. Torque designs a blind A/B test comparing sharpness scores (pre/post-pipeline) with 50 test clips.
5. Dynamo validates results by EOD, freezing the pipeline if VFI-Flow’s slowdown exceeds 25% on keyframes.
6. Merge depth-aware upscaling into main branch; VFI-Flow remains opt-in via config flag.

**What changed:** Depth-aware upscaling runs universally first; VFI-Flow is gated to keyframes with quantified motion blur.
