# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-292` (dept) · 2026-08-02T07:09:14.918396+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Run a blind A/B test comparing SD3.5 Medium + ControlNet depth vs SDXL Turbo + ControlNet depth (CFG capped at 3.0) on 100 face-heavy samples, measuring identity preservation and edge sharpness—Torque owns the test and publishes raw metrics by EOD.

**Plan:**
1. Implement SD3.5 Medium + ControlNet depth baseline pipeline.
2. Implement SDXL Turbo + ControlNet depth pipeline (CFG=3.0).
3. Curate 100 face-heavy samples (diverse lighting/angles).
4. Run blind A/B test, randomize order, log metrics (identity preservation, edge sharpness, realism).
5. Torque publishes raw metrics (identity scores, edge metrics, failure rates) by EOD.
6. Dynamo synthesizes results into next steps (LoRA vs Turbo vs hybrid).

**What changed:**
Added blind A/B test to resolve SDXL Turbo vs SD3.5 Medium trade-offs for EXCAVA’s face pipeline.
