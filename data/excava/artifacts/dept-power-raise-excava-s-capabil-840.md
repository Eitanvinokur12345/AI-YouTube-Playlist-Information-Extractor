# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-840` (dept) · 2026-07-31T11:11:46.933473+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Switch EXCAVA to Anthropic’s latest Claude 3.7 Sonnet with a 30-day rolling accuracy check.
**Plan:**
1. Immediately integrate Anthropic's Claude 3.7 Sonnet into EXCAVA's system.
2. Torque will design and execute a 30-day rolling accuracy check against Haiku's current baseline.
3. Monitor the 30-day rolling accuracy to ensure Sonnet's 0.7% gain survives drift.
4. If the 30-day rolling accuracy check shows that drift erases the gain, roll back to Haiku.
5. Continuously review token costs and adjust as necessary to maintain cost-effectiveness.
**What changed:** The decision to switch to Claude 3.7 Sonnet with a condition to revert if its gain is erased by benchmark drift.
