# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-685` (dept) · 2026-07-30T19:10:16.104721+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Run Llama 3.4 405B Instruct on a 10-second live pipeline slice with strict 50ms latency gates; if it clears, swap it in as EXCAVA’s default high-precision model—else keep Sonnet 3.7 with its 0.7% gain.

**Plan:**
1. Deploy Llama 3.4 405B Instruct in a controlled 10-second pipeline slice.
2. Measure latency against a hard 50ms gate; reject if exceeded.
3. If latency passes, benchmark capability uplift vs. Sonnet 3.7 (target ≥0.5%).
4. If uplift confirmed, promote 405B to default high-precision model.
5. If failed, retain Sonnet 3.7 with its 0.7% gain.
6. Document results in EXCAVA’s model registry.

**What changed:**
Latency-gated trial replaces assumption-based model selection.
