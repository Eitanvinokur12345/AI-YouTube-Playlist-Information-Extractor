# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-148` (dept) · 2026-08-27T14:32:25.000045+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate InstantX-ComfyUI’s depth-aware upscaler into EXCAVA’s pipeline.
2. Integrate VFI-Flow’s temporal super-resolution into EXCAVA’s motion pipeline.
3. Run a blind A/B test on EXCAVA’s worst 50 frames and 10 fastest cuts.
4. Use three independent reviewers for scoring, with Torque designing the test and scoring criteria.
5. Compare results: adopt the method with the highest net gain (quality vs. artifacts/compute).
6. If neither meets the 0.5% threshold, iterate with combined or alternative tools.

**What changed:** EXCAVA’s pipeline now includes both depth-aware upscaling and temporal super-resolution, tested head-to-head for optimal artifact reduction and quality gain.
