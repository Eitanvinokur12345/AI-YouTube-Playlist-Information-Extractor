# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-781` (dept) · 2026-07-31T03:12:40.110859+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Run a 48-hour head-to-head benchmark between Qwen2.5-72B-Instruct (local) and Claude Mythos 5 (API) to resolve the core LLM selection for EXCAVA.

**Plan:**
1. Deploy Qwen2.5-72B-Instruct locally on EXCAVA’s hardware with optimized inference settings (e.g., vLLM, 4xA100-80GB).
2. Configure Claude Mythos 5 via Anthropic’s API with identical prompts and batch sizes (500 tokens).
3. Measure runtime, cost per 1K tokens, and EXCAVA task success rate for both models over 48 hours.
4. Publish raw benchmark data (Torque to GitHub) by EOD, including hardware specs and API call logs.
5. Analyze results to determine if Mythos 5’s agentic benefits outweigh Qwen2.5’s efficiency or if a hybrid approach is viable.
6. Finalize LLM selection based on empirical data, with a 0.5% capability threshold as the minimum bar.

**What changed:**
A structured 48-hour benchmark replaces theoretical debate, forcing data-driven resolution.
