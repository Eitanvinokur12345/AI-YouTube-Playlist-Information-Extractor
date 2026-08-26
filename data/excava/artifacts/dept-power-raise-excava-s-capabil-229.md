# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-229` (dept) · 2026-08-26T05:08:40.282237+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Implement a controlled benchmark to select the optimal motion-compensation tool for EXCAVA’s pipeline.

**Plan:**
1. **Dataset Prep:** Select 5 representative EXCAVA inputs (mixed blur severity, motion types).
2. **Tool Setup:** Integrate FILM, XVFI++, and VFI-Flow into EXCAVA’s motion pipeline with identical pre/post-processing.
3. **Metrics:** Measure blur reduction (SSIM/PSNR delta vs. raw input) and throughput (FPS) for each tool.
4. **Baseline:** Run EXCAVA’s current pipeline (no motion tool) as control.
5. **Report:** Gearbox logs raw numbers (blur metrics, FPS) and ranks tools by (blur reduction / throughput).
6. **Decision Gate:** Dynamo reviews results by EOD; Gearbox implements the top-performing tool.

**What changed:** Motion-compensation tool selection now empirically validated via controlled benchmark.
