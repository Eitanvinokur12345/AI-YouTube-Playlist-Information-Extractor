# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-870` (dept) · 2026-07-16T02:19:03.247917+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Switch to Llama 4 Maverick 12B for EXCAVA prompts above 5K tokens after A/B testing.

**Plan:**
1. Run a 24-hour A/B test comparing Llama 4 Maverick 12B vs. Mistral Large 2 12.8B on EXCAVA’s 5K-token prompts.
2. Measure structured output accuracy and inference speed as primary metrics.
3. Torque owns the test and reports raw numbers (accuracy, speed) by EOD.
4. If Maverick’s speed advantage outweighs Mistral’s stability, adopt it for all >5K-token prompts.
5. Document prompt collapse risks (if any) and fallback to Mistral if accuracy drops below 95%.
6. Update EXCAVA’s model routing logic post-test based on results.

**What changed:**
Maverick 12B selected as default for >5K-token prompts pending test validation.
