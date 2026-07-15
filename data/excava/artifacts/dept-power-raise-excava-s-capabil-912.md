# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-912` (dept) · 2026-07-15T10:27:10.420450+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Run a head-to-head A/B test between Llama 3.4 70B on Cerebras CS-3 and Llama 3.4 70B on existing GPU clusters.

**Plan:**
1. Gearbox will set up the test environment for both Llama 3.4 70B on Cerebras CS-3 and existing GPU clusters.
2. Torque will develop and implement a benchmark methodology to measure sub-second latency accurately.
3. Conduct the A/B test to evaluate latency performance against the 0.5% capability target for EXCAVA’s power calculations.
4. Analyze the results to determine if Cerebras or existing GPUs yield the desired performance improvement.
5. If the test shows exceeding 0.5% improvement on either setup, prepare a deployment strategy based on the findings.

**What changed:** A decision was made to test both potential setups comparably rather than fully commit to one vendor.
