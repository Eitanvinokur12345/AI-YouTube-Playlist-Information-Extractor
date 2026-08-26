# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-220` (dept) · 2026-08-26T09:25:17.261989+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
**Plan:**
1. Integrate RIFE v4.17 into EXCAVA’s motion pipeline for motion interpolation.
2. Layer MPRNet (blind-deblurring) post-RIFE to refine temporal artifacts.
3. Benchmark blur reduction vs. render-time cost on a 10-second clip by EOD.
4. If SLA breach occurs, fallback to Gearbox’s depth-aware upscaler for static frames.
5. Document throughput metrics and quality delta in `/docs/perf/blur_analysis.md`.
6. Freeze pipeline changes pending Dynamo’s final sign-off.

**What changed:**
RIFE v4.17 + MPRNet stacked in motion pipeline; depth-aware upscaler retained for statics.
