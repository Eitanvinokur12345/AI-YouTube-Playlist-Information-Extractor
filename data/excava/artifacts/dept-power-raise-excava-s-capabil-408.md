# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-408` (dept) · 2026-07-15T15:27:24.694259+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Lock in Llama 4 Maverick 12B for EXCAVA’s worst-case 10K-token prompts after blind A/B testing
1. **Run a blind A/B test**: on 50 live worst-case EXCAVA prompts to compare Llama 4 Maverick 12B and Mythos 5 performance
2. **Evaluate test results**: if Maverick 12B drops below 90% accuracy vs Mythos 5, revert to Mythos 5; otherwise, proceed with rollout
3. **Lock in Maverick 12B for 30 days**: if it meets the 90%+ accuracy threshold, assign Gearbox to own the rollout and monitor performance
4. **Monitor and adjust**: track EXCAVA’s performance with Maverick 12B and reassess after 30 days to determine if further adjustments are needed
5. **Revert to Mythos 5 if necessary**: if Maverick 12B underperforms during the 30-day period, switch back to Mythos 5 to maintain EXCAVA’s capabilities
**What changed:** EXCAVA’s primary model for worst-case 10K-token prompts will be Llama 4 Maverick 12B, pending successful blind A/B testing.
