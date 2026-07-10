# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-990` (dept) · 2026-07-10T03:44:07.184464+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Validate EXCAVA’s baseline via raw telemetry and third-party audits, then benchmark with appropriate models.

**Plan:**
1. Obtain a raw telemetry dump from `/var/log/excava/perf/` without any filtering.
2. Conduct a third-party audit of the telemetry data to ensure accuracy and completeness.
3. Collect 2024 spec sheets for the Caterpillar 621XE and Volvo EC950E for comparison.
4. Gather field data for 621XE and EC950E models to support benchmarking.
5. Run the `excava-bench` tool to compare EXCAVA's performance against the benchmarks using validated data.

**What changed:** The approach shifted to ensure data integrity through third-party validation before benchmarking EXCAVA's performance.
