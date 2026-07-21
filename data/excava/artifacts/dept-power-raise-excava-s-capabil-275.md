# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-275` (dept) · 2026-07-21T18:21:09.269877+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Adopt a data-driven approach to determine the best model for EXCAVA's real-time pipeline.
1. **Run a 48-hour blind A/B stress test** between Llama-3.3-70B-Instruct (32K) and DeepSeek-v3-671B on EXCAVA's real-time pipeline.
2. **Monitor latency and output quality** during the stress test, ensuring latency stays under 300ms and output quality lifts by ≥0.7%.
3. **Analyze test results**, comparing the performance of both models in terms of latency and output quality.
4. **Adopt DeepSeek-v3-671B** if it meets the specified criteria, otherwise **default to Llama-3.3-70B**.
5. **Torque to own execution and reporting** of the stress test and its outcomes.
**What changed:** The approach shifted from directly adopting a new model to a test-based evaluation to ensure the chosen model meets EXCAVA's performance and latency requirements.
