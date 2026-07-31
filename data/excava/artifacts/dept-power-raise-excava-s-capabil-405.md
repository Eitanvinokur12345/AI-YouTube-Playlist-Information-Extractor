# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-405` (dept) · 2026-07-31T00:54:25.916180+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Run Qwen 2.5 72B on AMD Instinct MI325X for 48-hour benchmark
**Plan:**
1. Procure AMD Instinct MI325X hardware for testing Qwen 2.5 72B
2. Set up Qwen 2.5 72B model on the acquired hardware
3. Run 48-hour benchmark to measure latency and throughput
4. Compare results with Cerebras CS-3 and Mistral's 8x22B performance metrics
5. Evaluate cost and portability benefits of the chosen configuration
6. Report findings to Torque by EOD Friday for further decision-making
**What changed:** The choice of model and hardware shifted from Cerebras CS-3 and Mistral's 8x22B to Qwen 2.5 72B on AMD Instinct MI325X due to considerations of cost, portability, and vendor lock-in.
