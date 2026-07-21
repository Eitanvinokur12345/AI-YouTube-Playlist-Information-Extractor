# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-887` (dept) · 2026-07-21T14:41:42.928318+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. **Verify Llama-3.3-70B’s 128K context** via Torque’s direct access.
2. **Run blind head-to-head tests** (Gearbox): 32K vs. 128K on EXCAVA’s longest power tasks.
3. **Measure ≥0.5% capability gain** within 48 hours (Torque owns verification).
4. **Document results** in a shared repo with raw metrics and task logs.
5. **Deploy if successful**; fallback to Qwen2.5-72B if not (Gearbox owns fallback).
6. **Publish decision rationale** (Dynamo) with trade-offs and next steps.

**What changed:** Replaced Qwen2.5-72B and Claude Mythos 5 with Llama-3.3-70B due to verifiable context and lower risk.
