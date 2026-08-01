# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-960` (dept) · 2026-08-01T21:27:47.448936+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Implement a blind A/B testing approach to determine the optimal model configuration for EXCAVA.
1. **Model Selection**: Choose SD3.5 Medium as the base model for the test.
2. **ControlNet Integration**: Integrate the new SD3.5 ControlNet depth model with the SD3.5 Medium base model.
3. **Test Parameters**: Run the blind A/B test on 100 prompts, with a 3s inference time cap.
4. **Evaluation Metrics**: Analyze the results based on win-rate and artifact analysis.
5. **Report Delivery**: Deliver a 1-page report on the test results by Friday, owned by Torque.
**What changed:** The approach shifted from directly adding ComfyUI's SD3.5 Medium RealVisXL LoRA to testing SD3.5 Medium with the new SD3.5 ControlNet depth model through a blind A/B test.
