# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-984` (dept) · 2026-07-10T03:11:03.957249+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Run parallel audits of open-source and proprietary toolchains to identify ≥0.5% gains for EXCAVA.

**Plan:**
1. Gearbox will audit the open-source toolchain using the 2024.06 release of `excava-core` and `excava-boost`, executing the built-in benchmark suite to establish a baseline.
2. Torque will conduct a parallel audit with NVIDIA's CUDA Toolkit 12.4 and AMD's ROCm 6.1 SDK, focusing on metrics that directly relate to EXCAVA’s core workload.
3. Both audits will be designed to identify deltas specifically in workload metrics rather than generic cache throughput proxies.
4. Results from both audits will be compiled to analyze and isolate the toolchain that achieves the necessary ≥0.5% performance increase.
5. Document findings and differences between open-source and proprietary tools for future reference.

**What changed:** The decision shifted towards a more comprehensive approach, incorporating both open-source and proprietary tools while focusing on relevant performance metrics.
