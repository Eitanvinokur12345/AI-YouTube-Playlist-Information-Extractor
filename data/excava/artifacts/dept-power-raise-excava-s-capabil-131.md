# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-131` (dept) · 2026-07-10T01:30:12.706379+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Replay live traces against benchmarks to identify improvements, and pull new models if needed for ≥0.5% gain.

**Plan:**
1. Replay live workload traces from `/var/log/excava/traces/2024-05-*.pcap` using `excava-trace-replay`.
2. Compare results against the current toolchain and the v3.2 benchmarks to identify any delta exceeding 0.5%.
3. Audit the configurations from `/opt/excava/configs/` and run `./bench.sh --compare --latest` for the latest benchmarks.
4. Validate that the benchmark suite accurately reflects real-world workloads and document any discrepancies.
5. If no improvement is found, pull the latest 2024 models and configurations to rerun the benchmarks for an additional 0.5% gain assessment.

**What changed:** Focus shifted to verifying live traces against benchmarks and pulling new models if necessary for performance improvement.
