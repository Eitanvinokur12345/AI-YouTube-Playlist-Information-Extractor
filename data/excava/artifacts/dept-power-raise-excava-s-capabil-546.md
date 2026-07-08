# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-546` (dept) · 2026-07-08T11:51:38.928949+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Run abrasion-weighted torque benchmarks on EXC-2024-07 with new 2024 CAT 349F pump (PN:105-4468) in mixed abrasive clay (30% moisture, 25% silica).

**Plan:**
1. Swap out EXCAVA’s current hydraulic pump for the new CAT 349F 2024 pump (PN: 105-4468).
2. Prepare the excavator arm (EXC-2024-07) for benchmarking in mixed abrasive clay.
3. Conduct 50 full-dig cycles while logging `ARM_TORQUE_REQ`, `PUMP_FLOW_ACT`, and linkage wear data via the CAN bus (DBC: `excava_v3.dbc`).
4. Analyze the logged data to quantify torque performance and identify any further improvements.
5. Share results with the team to assess capabilities and next steps for the EXCAVA system.

**What changed:** The focus shifted to benchmarking in mixed abrasive clay rather than dry clay, addressing real-world performance issues more effectively.
