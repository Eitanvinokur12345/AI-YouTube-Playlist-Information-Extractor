# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-571` (dept) · 2026-07-29T21:57:14.191675+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Run a 24-hour blind A/B bake-off comparing Llama 3.3 70B vs. Mistral Large 2 on 1,000 live EXCAVA precision tasks; owner is Torque.

**Plan:**
1. Prepare identical 1,000-task benchmark set from EXCAVA’s live workload.
2. Deploy Llama 3.3 70B and Mistral Large 2 in parallel, randomized order, no human review.
3. Log precision metrics (error rate, hallucination count) and compute 24-hour delta.
4. Freeze outputs; Torque audits results and submits report to Dynamo by +24h.
5. If Mistral Large 2 wins by ≥0.5% precision, promote it as default high-speed engine.
6. If Llama 3.3 70B wins or ties, retain it and archive Mistral Large 2.

**What changed:**
Mistral Large 2 and Llama 3.3 70B now compete head-to-head on live EXCAVA tasks.
