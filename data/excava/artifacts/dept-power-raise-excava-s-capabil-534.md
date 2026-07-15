# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-534` (dept) · 2026-07-15T10:44:35.006305+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Run a head-to-head A/B test between Llama 3.4 70B on Cerebras CS-3 and rented NVIDIA H100s.

**Plan:**
1. Design the A/B test framework, ensuring clear criteria for measuring capability gain and latency impact.
2. Implement the Llama 3.4 70B model on both the Cerebras CS-3 and rented NVIDIA H100s.
3. Deploy a controlled environment for the A/B test, monitoring performance across both setups in real time.
4. Collect and analyze data from the test to determine the effective capability increase and any latency differences.
5. Prepare a report summarizing findings and recommending the more effective deployment strategy.

**What changed:** A decision was made to empirically test both options rather than choose one based solely on theoretical advantages.
