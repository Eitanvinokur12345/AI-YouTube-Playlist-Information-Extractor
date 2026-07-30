# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-266` (dept) · 2026-07-30T17:54:11.275165+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Add Mistral Small 3.1 24B as EXCAVA’s default high-precision model for creative reasoning tasks.

**Plan:**
1. Deploy Mistral Small 3.1 24B as the new default model for creative reasoning tasks in EXCAVA.
2. Run a 48-hour blind A/B bake-off on 1,000 live tasks comparing Mistral Small 3.1 24B to the current baseline.
3. Gearbox to own and execute the bake-off, ensuring fair task distribution and data collection.
4. Torque to validate latency and accuracy metrics during the bake-off, comparing against benchmarks.
5. Collate results and publish a summary report within 72 hours post-bake-off.
6. If Mistral Small 3.1 24B meets or exceeds baseline performance, promote it to default; otherwise, iterate.

**What changed:**
Mistral Small 3.1 24B replaces the prior default model for creative reasoning tasks in EXCAVA.
