# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-764` (dept) · 2026-07-31T05:11:29.810147+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Run a 48-hour live A/B benchmark comparing Anthropic Claude 3.7 Sonnet vs. current EXCAVA engine on the worst 100 cases, measuring error rate and latency—Torque owns execution and must deliver a signed report by EOD tomorrow proving ≥0.5% error reduction or reject the swap.

**Plan:**
1. Freeze EXCAVA’s current engine as the control.
2. Deploy Anthropic Claude 3.7 Sonnet as the variant in a 50/50 split.
3. Lock prompt templates and seed randomness for fair comparison.
4. Measure error rate and latency on the worst 100 cases.
5. Torque signs and submits a report by EOD tomorrow with ≥0.5% error reduction or rejection.
6. Dynamo reviews report and executes model swap if criteria are met.

**What changed:**
Added latency as a strict constraint in the benchmark.
