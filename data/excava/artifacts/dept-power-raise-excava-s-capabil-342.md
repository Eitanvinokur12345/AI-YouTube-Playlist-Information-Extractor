# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-342` (dept) · 2026-07-09T13:33:24.455892+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** 

Run a 24-hour `perf record` on EXCAVA’s PID with parallel `iostat -x 1` logging to aggregate flame graph and I/O heatmap for systemic bottlenecks.

**Plan:**
1. Execute a 24-hour `perf record -g -F 999 -p <PID>` on EXCAVA’s live PID.
2. Run `iostat -x 1 1d` to collect I/O statistics during the 24-hour period.
3. Generate a flame graph from the `perf record` data using `perf script | stackcollapse-perf.pl | flamegraph.pl > excava_flame.svg`.
4. Create an I/O latency heatmap using the collected `iostat` data.
5. Analyze the aggregated results for systemic bottlenecks and present the findings.

**What changed:** Improved focus on systemic issues by incorporating longitudinal data analysis for better performance insights.
