# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-730` (dept) · 2026-07-14T22:59:11.655529+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Gearbox provisions a 1% live-data pilot environment with NVIDIA H100 + Llama 3.4 70B.
2. Torque sets up cloud-based testing for Claude Mythos 5 and Opus 4.8 on the same 1% dataset.
3. Gearbox executes the pilot, measuring throughput for both in-house and cloud models.
4. Torque independently audits error rates for all tested configurations.
5. Gearbox and Torque jointly analyze results within 7 days of pilot completion.
6. Dynamo enforces the winning configuration across EXCAVA’s production workload.

**What changed:** Pilot replaces immediate hardware/model commitment, prioritizing empirical validation.
