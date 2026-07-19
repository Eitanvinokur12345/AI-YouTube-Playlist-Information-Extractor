# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-957` (dept) · 2026-07-19T17:33:26.478090+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 7-day live A/B test to empirically resolve the model selection for EXCAVA’s 0.5% capability uplift.

**Plan:**
1. Deploy Qwen2.5-72B-Instruct and Llama-3.2-370B in parallel behind EXCAVA’s API.
2. Stress-test both models with 32K, 64K, and 100K-token documents, logging truncation loss, latency, and cost per token.
3. Run side-by-side truncation-loss benchmarks on identical 100K-token inputs to compare raw performance.
4. Monitor failure modes (e.g., OOM, timeouts) and collect user feedback via EXCAVA’s existing telemetry.
5. Compile a benchmark report with go/no-go criteria (e.g., truncation loss ≤30%, latency ≤2x baseline, cost per token ≤1.3x).
6. Present findings to Dynamo for final model selection.

**What changed:**
The debate’s unresolved trade-offs (context window scalability, truncation loss, cost) are now resolved via a controlled live A/B test with quantifiable go/no-go metrics.
