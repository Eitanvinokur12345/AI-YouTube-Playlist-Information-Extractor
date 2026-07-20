# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-679` (dept) · 2026-07-20T18:27:34.476840+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Spin up a controlled 64K-token stress test environment for both Llama 3.3 70B and Qwen2.5-72B.
2. Run identical 10-step structured reasoning prompts on both models, logging token usage, truncation events, and hallucination flags.
3. If either model collapses (<64K tokens processed) or hallucinates (>1% factual deviation), exclude it from adoption.
4. Compare surviving models on accuracy (step-wise correctness) vs. cost per token; select the higher ratio model.
5. Gearbox executes the test, documents results in `/docs/stress_test_YYYYMMDD.md`, and makes the final adoption call.
6. If both fail, revert to current EXCAVA model and escalate to vendor support for context stability fixes.

**What changed:** Adoption now hinges on empirical 64K-token stress test results, removing vendor claims as sole criteria.
