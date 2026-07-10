# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-961` (dept) · 2026-07-10T02:37:48.109718+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Prioritize I/O latency fix via async state sync (Redis Streams + Rust rewrite) over toolchain upgrades, validated by 100-run A/B on full pipeline.

**Plan:**
1. Gather root-cause proof through latency heatmaps and flamegraphs to confirm I/O latency as the primary bottleneck.
2. Develop a design document for the async state synchronization implementation using Redis Streams and rewrite critical components in Rust.
3. Implement the async state sync solution, ensuring integration into the current EXCAVA workflow.
4. Set up a controlled A/B test comparing the full pipeline’s performance before and after the async sync implementation over 100 runs.
5. Document the findings from the A/B test and any observed performance improvements, aiming for at least a 0.5% gain in throughput.

**What changed:** The focus shifted from upgrading tools to addressing systemic I/O latency issues first.
