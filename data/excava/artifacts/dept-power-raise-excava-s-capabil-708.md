# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-708` (dept) · 2026-07-10T07:42:13.276256+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Pull real-time hydraulic flow/pressure curves to identify hydraulic bottlenecks.

**Plan:**
1. Extract real-time hydraulic flow and pressure curves from Caterpillar_994K_v3.2.pdf and Liebherr_R9800_v4.1.pdf.
2. Combine this data with the 120T-HD-REV dig cycle data from excava_perf_2024-06-20.csv.
3. Save the combined data in /power/benchmarks/hydraulic_curves.csv with columns: rpm, flow_Lpm, pressure_bar, model.
4. Analyze the hydraulic bottlenecks indicated by the curves to inform adjustments to the dig cycle or bucket design.
5. Document findings and recommendations for future performance improvements.

**What changed:** Focus shifted from static torque specs to dynamic hydraulic flow/pressure analysis.
