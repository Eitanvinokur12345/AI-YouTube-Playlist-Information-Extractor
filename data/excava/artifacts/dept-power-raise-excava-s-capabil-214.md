# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-214` (dept) · 2026-07-21T17:32:21.719142+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Adopt Llama-3.3-70B-Instruct for EXCAVA with a controlled 24K prompt cap and comparative analysis against DeepSeek-v3-671B.
**Plan:**
1. Integrate Llama-3.3-70B-Instruct into EXCAVA with a 24K prompt cap to ensure reliability and accuracy.
2. Design a controlled ablation study to compare Llama-3.3-70B-Instruct and DeepSeek-v3-671B on identical tasks with 24K prompts.
3. Measure and publish side-by-side hallucination rates and latency results for both models by EOD.
4. Assign Torque to own and execute the controlled ablation study and testing.
5. Assign Gearbox to own the integration of Llama-3.3-70B-Instruct into EXCAVA.
**What changed:** The model selection for EXCAVA shifted from DeepSeek-v3-671B to Llama-3.3-70B-Instruct due to reliability and verification concerns.
