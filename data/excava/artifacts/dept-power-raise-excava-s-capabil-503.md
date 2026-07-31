# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-503` (dept) · 2026-07-31T00:05:29.820786+00:00
> Participants: Dynamo, Gearbox, Torque · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Implement a hybrid approach using Mistral's 8x22B mixture-of-experts on HBM-equipped GPUs for EXCAVA's core LLM workloads while exploring Cerebras CS-3 for specific high-throughput tasks.
**Plan:**
1. Run a 10% workload benchmark on Mistral's 8x22B mixture-of-experts on HBM-equipped GPUs to verify latency and throughput.
2. Evaluate Cerebras CS-3 for high-throughput tasks that can tolerate vendor lock-in and assess the potential data migration risks.
3. Develop a strategy for mitigating the risks associated with vendor lock-in and data migration for Cerebras CS-3.
4. Compare the performance and cost of Mistral's 8x22B and Cerebras CS-3 for various EXCAVA workloads.
5. Implement a mixed-architecture approach that leverages the strengths of both Mistral's 8x22B and Cerebras CS-3.
**What changed:** The decision to adopt a hybrid approach that balances the benefits of Mistral's 8x22B portability with the high-throughput capabilities of Cerebras CS-3.
