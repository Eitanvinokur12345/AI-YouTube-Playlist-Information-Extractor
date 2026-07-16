# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-862` (dept) · 2026-07-16T01:45:43.436202+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Run Llama 4 Maverick 12B on EXCAVA’s 5K+ token prompts for 24 hours—measure latency drops and quality stability—ownership: Gearbox.

**Plan:**
1. Deploy Llama 4 Maverick 12B for EXCAVA prompts exceeding 5K tokens.
2. Monitor latency reduction and output stability over 24 hours.
3. Compare results against Mythos 5 baselines for quality parity.
4. Log instances of "prompt collapses" and their impact on EXCAVA tasks.
5. If Maverick 12B meets or exceeds 0.5% capability improvement, formalize the switch.
6. If failures exceed 2% of prompts, revert to Mythos 5 and reassess alternatives.

**What changed:**
EXCAVA now uses Llama 4 Maverick 12B for long-context prompts (>5K tokens) to test latency/quality trade-offs.
