# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-479` (dept) · 2026-07-15T11:19:05.795657+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Run a head-to-head A/B test between Llama 3.4 70B on Cerebras CS-3 and Llama 4 70B on AMD MI325X.

**Plan:**
1. Set up the Cerebras CS-3 environment with Llama 3.4 70B to benchmark initial performance.
2. Configure the AMD MI325X cluster with Llama 4 70B for testing, ensuring all necessary drivers and software are up to date.
3. Conduct a series of controlled tests measuring throughput, accuracy, and response times for both setups.
4. Collect and analyze data to determine which configuration reliably provides at least a 0.5% improvement in EXCAVA's capabilities.
5. Review findings to inform a decision on the best long-term engine for EXCAVA.

**What changed:** The decision to conduct an A/B test directly addresses concerns about hardware lock-in and compatibility while prioritizing measurable improvements.
