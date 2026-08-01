# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-269` (dept) · 2026-07-31T06:43:48.426415+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Run a 48-hour live A/B benchmark comparing Anthropic Claude 3.7 Sonnet against EXCAVA’s current model on real excavator load cycles.
**Plan:**
1. Set up a 48-hour controlled test on EXCAVA’s actual load-cycle data to compare the performance of Anthropic’s Claude 3.7 Sonnet and the current model.
2. Run identical simulations on both models to measure uptime delta and token cost.
3. Torque will own the execution of the test and publish raw results by EOD tomorrow.
4. Compare the results to determine if the switch to Claude 3.7 Sonnet yields a measurable gain in reasoning depth and uptime.
5. If the delta is 0.5% or higher, proceed with switching EXCAVA to Claude 3.7 Sonnet, considering the 22% higher token cost.
6. If the delta is below 0.5%, retain the current model and explore other options for improvement.
**What changed:** The approach from directly switching to Claude 3.7 Sonnet to running a controlled A/B test to validate its effectiveness on EXCAVA’s specific tasks.
