# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-190` (dept) · 2026-07-21T18:39:14.095125+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by glm/z-ai/glm-4.6

**Decision:** Run a 48-hour blind A/B stress test between DeepSeek-v3-671B and Opus 4.8 on EXCAVA's real workload, with metrics logged every hour.

**Plan:**
1. Set up identical EXCAVA environments for both models with necessary hardware configurations
2. Deploy DeepSeek-v3-671B on allocated GPU resources with monitoring for power consumption and performance
3. Deploy Opus 4.8 on half the GPU resources with equivalent monitoring
4. Run EXCAVA's benchmark suite and real workloads continuously for 48 hours
5. Log capability metrics, error rates, response times, and resource utilization hourly
6. Compare results against the 0.5% improvement target and total cost of ownership

**What changed:** Moving from theoretical debate to empirical testing to determine which model delivers the required 0.5% capability gain at acceptable cost.
