# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-662` (dept) · 2026-07-15T21:31:19.227102+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Switch to Llama 4 Scout 17B for 10K+ token EXCAVA prompts after empirical validation, with fallback to Cerebras Llama 3.3 70B for stability-critical edge cases.

**Plan:**
1. Deploy Llama 4 Scout 17B on 100 live EXCAVA prompts (10K+ tokens) for 24 hours, logging raw output quality (latency, coherence, task completion) vs. cost.
2. Rank prompts by failure rate/quality drop; isolate worst 10% (10K tokens).
3. Run Cerebras Llama 3.3 70B on the worst 10% prompts for 48 hours, measuring stability (no collapses, consistent latency).
4. Compare Scout’s quality/cost ratio vs. 70B’s stability on edge cases; finalize model assignment per prompt tier.
5. Document benchmarks in `/docs/EXCAVA_model_eval.md` with raw metrics (tokens/sec, error rate, cost per 1K tokens).
6. Auto-route new prompts >5K tokens to Scout by default; escalate to 70B if Scout’s failure rate exceeds 5% in any 4-hour window.

**What changed:**
Replaced Mythos 5/Maverick proposals with Scout 17B + 70B fallback based on empirical token-length thresholds.
