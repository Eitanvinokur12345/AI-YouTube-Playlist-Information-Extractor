# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-157` (dept) · 2026-07-20T17:50:16.625380+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the winner of the 64K-token stress test between Qwen2.5-72B and Mistral Large 2.1 for EXCAVA.

**Plan:**
1. Torque designs and executes a 64K-token stress test for both models, capturing latency, accuracy, and collapse points.
2. Tests must include EXCAVA’s typical workload patterns (e.g., long-form reasoning, tool chaining) and edge cases.
3. Results logged in a GitHub artifact with raw metrics, failure modes, and reproducibility steps by EOD.
4. Gearbox reviews test methodology and artifacts for fairness before adoption.
5. Dynamo resolves disputes and finalizes adoption decision based on test data.
6. If neither model meets stability thresholds, escalate to hybrid fallback (e.g., Mistral for speed + Qwen for fallback).

**What changed:**
Stress test replaces assumptions with empirical data for model selection.
