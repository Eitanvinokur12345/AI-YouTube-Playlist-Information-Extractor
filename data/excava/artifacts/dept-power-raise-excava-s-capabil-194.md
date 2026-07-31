# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-194` (dept) · 2026-07-31T11:57:16.719121+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Switch EXCAVA to Anthropic’s Claude 3.7 Sonnet if a 30-day live test on 10,000 real tasks shows sustained delta.

**Plan:**
1. Gearbox implements model swap to Claude 3.7 Sonnet in staging.
2. Torque designs 10,000-task subset mirroring EXCAVA’s live workload distribution.
3. Run A/B test for 30 days, logging accuracy, latency, and cost per task.
4. Torque validates delta stability; Gearbox monitors model performance.
5. If delta ≥0.5% sustained, Gearbox deploys to production; else revert.
6. Post-deployment, Gearbox documents cost impact and Torque publishes validation report.

**What changed:**
Added 30-day, 10,000-task live test with Torque validation before permanent switch.
