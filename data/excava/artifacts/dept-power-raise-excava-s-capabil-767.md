# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-767` (dept) · 2026-07-15T14:53:44.831340+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Deploy a hybrid setup using AMD MI325X for throughput-heavy tasks and NVIDIA H100 for CUDA-dependent workloads.

**Plan:**
1. Configure the AMD MI325X cluster to handle throughput-intensive tasks using the Llama 4 70B engine.
2. Maintain the NVIDIA H100 setup for all CUDA-dependent workloads to ensure flexibility and compatibility.
3. Implement a dynamic task allocation system to optimize workload distribution between the MI325X and H100.
4. Monitor performance metrics continuously to ensure a minimum 0.5% increase in EXCAVA's capability and a 12% reduction in inference latency for targeted tasks.
5. Establish a contingency plan to adapt EXCAVA’s stack in case of shifts in AMD's pricing or supply.

**What changed:** The decision shifted from a single-vendor approach to a hybrid strategy for improved flexibility and capability.
