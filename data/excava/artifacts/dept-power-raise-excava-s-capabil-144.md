# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-144` (dept) · 2026-07-30T19:52:54.197808+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Run Llama 3.4 405B Instruct on a 10-second live pipeline slice with a curated prompt set of EXCAVA’s hardest edge cases, caching the top 20% outputs to control latency while testing adaptability.

**Plan:**
1. Replace the distilled 70B fine-tuned model with Llama 3.4 405B Instruct in the EXCAVA pipeline.
2. Curate a prompt set targeting EXCAVA’s hardest 0.5% edge cases (prioritizing adaptability over broad coverage).
3. Implement a 10-second live inference slice with caching for the top 20% most frequent/high-confidence outputs.
4. Benchmark against the current 70B fine-tuned baseline using a 1000-sample test set measuring quality (accuracy/precision) and latency.
5. Log model drift metrics (e.g., output variance, error rates) over 72 hours to assess adaptability.
6. If latency exceeds 10s for uncached cases, trigger fallback to cached outputs or smaller model (e.g., 70B) for those queries.

**What changed:**
Switched from a fine-tuned 70B to a raw 405B with edge-case prompting and caching to balance capability and latency while testing adaptability.
