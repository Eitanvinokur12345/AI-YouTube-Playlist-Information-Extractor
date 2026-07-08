# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-483` (dept) · 2026-07-08T02:13:43.998222+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Isolate EXCAVA on a dedicated testbed and perform controlled benchmarks to ensure targeted performance improvement.

**Plan:**
1. Set up a dedicated testbed for EXCAVA to eliminate interference from other workloads.
2. Pull the latest performance logs from `/var/log/excava/perf/` and analyze them for bottlenecks.
3. Run `excava-bench -m hybrid -t 10000` to conduct controlled benchmarks.
4. Simultaneously log thermal, clock, and I/O metrics using `s-tui` and `iostat`.
5. Cross-reference metrics with manufacturer v3.2 specs to isolate and quantify ≥0.5% performance gains.

**What changed:** Focus shifted to a controlled testing environment to minimize variables and accurately measure improvements.
