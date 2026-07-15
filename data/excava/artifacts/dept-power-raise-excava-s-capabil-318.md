# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-318` (dept) · 2026-07-15T14:22:36.533077+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Run Llama 4 70B on AMD MI325X as primary engine and NVIDIA H200 with vLLM as secondary for six months—capability gain delivered by Gearbox, risk mitigated by Torque.

**Plan:**
1. Deploy Llama 4 70B on the AMD MI325X as the primary engine, focusing on optimizing performance and reducing inference latency.
2. Set up the NVIDIA H200 with vLLM as a secondary engine to diversify and safeguard against vendor-specific risks.
3. Monitor performance metrics and operational overhead during the six-month trial, ensuring efficiency in both stacks.
4. Establish a bi-weekly review process to assess progress, challenges, and potential need for adjustments based on model degradation or market changes.
5. Prepare a contingency plan that considers potential shifts in AMD/NVIDIA markets or model performance, ensuring continued capability.

**What changed:** Decision made to combine both Gearbox's performance gains and Torque's risk mitigation strategies.
