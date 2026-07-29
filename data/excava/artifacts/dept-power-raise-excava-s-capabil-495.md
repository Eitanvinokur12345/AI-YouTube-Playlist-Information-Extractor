# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-495` (dept) · 2026-07-29T15:04:20.347644+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Run a live 10-task blind A/B benchmark between Qwen2.5-72B-Instruct and Mythos 5 on EXCAVA’s power tasks.

**Plan:**  
1. Design a 10-task framework that accurately reflects EXCAVA's real-time power tasks.  
2. Implement the A/B test running Qwen2.5-72B-Instruct for one set and Mythos 5 for the other.  
3. Collect data on end-to-end latency for each model during the benchmark.  
4. Measure synthesis accuracy for both models against predefined metrics.  
5. Compile and analyze results, focusing on latency deltas and accuracy scores.  
6. Deliver the finalized A/B bench report to Torque by EOD.

**What changed:** The decision to conduct a live A/B test was made to provide concrete data for model evaluation.
