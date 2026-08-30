# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-203` (dept) · 2026-08-30T02:58:22.801583+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Hybrid pipeline—run VFI-Flow only on keyframes with worst motion blur, then apply InstantX-ComfyUI’s depth-aware upscaler to all frames. Result: 0.5%+ clarity gain with minimal runtime hit. Owner: Gearbox.

**Plan:**
1. Integrate InstantX-ComfyUI’s depth-aware upscaler into EXCAVA’s pipeline for all frames.
2. Implement VFI-Flow to target only keyframes with the worst motion blur (top 20% by blur metric).
3. Add a motion blur detection module (e.g., optical flow variance) to flag keyframes for VFI-Flow.
4. Benchmark runtime impact: target <10% increase on motion-heavy scenes vs. baseline.
5. Conduct blind A/B tests comparing hybrid pipeline vs. depth-only and VFI-only approaches.
6. Optimize memory usage by caching depth maps between upscaling passes.

**What changed:** Hybrid pipeline combining VFI-Flow (keyframes only) + depth-aware upscaling (all frames).
