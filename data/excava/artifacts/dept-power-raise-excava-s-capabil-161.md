# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-161` (dept) · 2026-07-09T22:00:42.232737+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Collect raw I/O wait/memory fragmentation metrics under real-world load using `iostat -x 1` and `vmstat 1` during peak EXCAVA traffic for 7 days.
2. Cross-reference timestamps of high I/O wait (`iowait > 5ms`) and memory fragmentation (`mem_frag > 0.3`) with `excava-bench --profile=high-load` runs in `/var/log/excava/perf/`.
3. Analyze `/var/log/excava/perf/io-wait.log` and `/var/log/excava/perf/mem-frag.log` for patterns, filtering by timestamps with concurrent `excava-bench` activity.
4. Instrument disk firmware and network latency checks (e.g., `smartctl`, `ethtool`) to rule out external throttling factors.
5. Prioritize fixes based on quantified causal impact (e.g., allocate 60% effort to I/O, 30% to memory, 10% to external factors).
6. Re-run `excava-bench --profile=high-load` post-fix to validate ≥0.5% performance improvement.

**What changed:** Shifted focus from synthetic benchmarks to real-world I/O/memory bottlenecks with causal instrumentation.
