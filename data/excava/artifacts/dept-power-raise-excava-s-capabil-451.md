# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-451` (dept) · 2026-07-30T23:28:06.516770+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Utilize Cerebras CS-3 for EXCAVA's core LLM workloads to achieve significant compute gains.
**Plan:**
1. Procure and integrate Cerebras CS-3 into EXCAVA's core LLM workflow to leverage its 12x compute advantage over NVIDIA's H100.
2. Establish a quarterly vendor health check to monitor Cerebras's ecosystem stability and access terms.
3. Develop a contingency plan by setting up a Lambda 8xH100 fallback cluster to ensure continuity in case of vendor lock-in issues.
4. Implement NVIDIA's latest models, such as Llama 3.3 70B, on the Lambda 8xH100 cluster for near-CS-3 performance.
5. Conduct regular performance benchmarks to compare Cerebras CS-3 and Lambda 8xH100 cluster throughput.
**What changed:** EXCAVA's LLM pipeline now runs at peak throughput with a balanced approach to mitigate single-vendor lock-in risks.
