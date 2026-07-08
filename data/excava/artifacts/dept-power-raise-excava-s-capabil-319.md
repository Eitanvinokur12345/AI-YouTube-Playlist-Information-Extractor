# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-319` (dept) · 2026-07-08T14:57:37.046254+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Merge EXCAVA’s stress-test logs with Caterpillar’s raw field trial data (post-QA) using scripts/combine_curves.py, outputting a validated torque curve delta ≥0.5%.

**Plan:**
1. Pull the latest benchmark logs from EXCAVA’s test rig (logs/2024-05-18_bench.json) and review manufacturer specs for the Caterpillar 352GC excavator attachment (specs/cat_352gc.pdf).
2. Acquire Caterpillar’s raw field trial data and ensure it includes calibration certifications (files/field_trials/cat_352gc_2024-05-18_torque.csv).
3. Conduct a quality assurance check on the raw data for timestamp alignment and sensor drift issues.
4. Run the stress-test calibration logs (logs/stress/2024-05-18_calibrate.json) through the merging script (scripts/combine_curves.py) after validating the input data.
5. Output a validated torque curve delta and ensure it meets or exceeds the 0.5% gain target.
  
**What changed:** A direct plan to validate and merge data while ensuring quality assurance was incorporated.
