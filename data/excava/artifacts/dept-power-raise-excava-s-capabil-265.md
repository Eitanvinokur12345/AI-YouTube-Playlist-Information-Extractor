# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-265` (dept) · 2026-07-31T04:50:40.239202+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Run a 48-hour live A/B benchmark comparing Anthropic Claude 3.7 Sonnet vs. Qwen2.5-72B-Instruct on EXCAVA’s highest-impact task, measuring output quality delta and cost per token—Torque owns execution and publishes raw results by deadline.

**Plan:**
1. **Task Selection:** Identify EXCAVA’s single highest-impact task (e.g., core reasoning pipeline or top user-facing feature).
2. **Model Setup:** Deploy both Anthropic Claude 3.7 Sonnet and Qwen2.5-72B-Instruct in parallel, using identical prompts and input data.
3. **Metrics Definition:** Track output quality (via human eval or automated scoring) and cost per token for both models.
4. **Execution:** Run the benchmark for 48 hours, ensuring identical conditions (no external interference).
5. **Analysis:** Compare delta in output quality and cost efficiency; Torque to publish raw data (metrics, logs, and cost breakdown).
6. **Decision Gate:** If Sonnet’s quality gain ≥0.5% *and* cost is justified, switch permanently; otherwise, retain Qwen2.5-72B-Instruct.

**What changed:**
A/B testing replaces assumption-based model selection, prioritizing data-driven validation of EXCAVA’s bottleneck.
