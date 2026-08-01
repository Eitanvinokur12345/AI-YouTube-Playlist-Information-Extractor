# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-151` (dept) · 2026-08-01T04:03:38.711011+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Auto-apply low-risk changes immediately, batch medium-risk changes for weekly lead review, and flag high-risk changes for immediate lead attention—measured by lead opt-in rate and regression tickets over 2 weeks.

**Plan:**
1. Define risk tiers (low/medium/high) for prompt/engine/routing/own-code changes with clear thresholds (e.g., low = typo fixes, medium = parameter tweaks, high = structural edits).
2. Implement auto-apply for low-risk changes with audit logs; batch medium-risk changes into weekly lead review summaries.
3. Flag high-risk changes for immediate lead attention via opt-in alerts (e.g., Slack/email) with 24-hour response SLA.
4. Track metrics: lead opt-in rate, regression tickets, and time-to-resolution over 2 weeks.
5. Adjust risk thresholds based on regression data after the trial period.
6. Document the process in the team’s internal wiki for consistency.

**What changed:**
Prioritized risk-based auto-apply vs. review, replacing blanket "safe changes only" with tiered, measurable enforcement.
