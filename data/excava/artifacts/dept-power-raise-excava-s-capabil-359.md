# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-359` (dept) · 2026-07-16T02:53:33.525653+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Run a 24-hour A/B test between Llama 4 Maverick 12B and Mistral Large 2 12.8B on a 20K-token EXCAVA prompt.

**Plan:**
1. Torque provisions identical hardware for both models (GPU/TPU allocation).
2. Deploy Llama 4 Maverick 12B and Mistral Large 2 12.8B with identical EXCAVA prompts (20K tokens).
3. Log output quality at 15K and 20K tokens (BLEU/ROUGE/perplexity) and end-to-end latency under sustained load.
4. Run 100+ iterations per model to account for variance.
5. Torque compiles a report comparing quality degradation, latency, and stability.
6. Dynamo reviews results and selects the model with ≥0.5% quality gain or lower latency.

**What changed:** A/B test replaces model selection debate with empirical validation.
