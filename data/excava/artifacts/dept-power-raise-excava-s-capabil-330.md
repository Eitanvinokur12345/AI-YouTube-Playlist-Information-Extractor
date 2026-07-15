# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-330` (dept) · 2026-07-15T10:07:36.440462+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Run a head-to-head test between Llama 3.4 70B on NVIDIA H100s and Cerebras CS-3 with Llama 3.3 70B.  

**Plan:**  
1. Set up a testing environment for Llama 3.4 70B on NVIDIA H100s.  
2. Configure Cerebras CS-3 with Llama 3.3 70B.  
3. Define metrics for evaluation: latency, cost per token, and throughput based on EXCAVA's real workload.  
4. Execute the tests under similar conditions for fair comparison.  
5. Analyze results; if Cerebras CS-3 shows ≥0.5% improvement, proceed with vendor lock-in; if not, adopt Llama 3.4 on existing GPUs.  

**What changed:** A decision was made to test both configurations to ensure data-driven choices.
