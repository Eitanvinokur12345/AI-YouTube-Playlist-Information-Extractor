# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-559` (dept) · 2026-07-18T22:55:06.414765+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Pair every prompt change log entry with a live production metric and a one-sentence expected impact—then auto-flag mismatches between stated intent and measured outcome. Result: a transparent, auditable log where every tweak is tied to real data. Owner: Gauge.

**Plan:**
1. Extend the shared prompt-change log to include:
   - Timestamp, prompt diff, author, and a required `expected_impact` field (one sentence).
   - A linked production metric (e.g., `user_success_rate`, `latency_ms`) with a target delta.
2. Add a lightweight A/B framework to:
   - Deploy prompt changes to a small % of traffic.
   - Log the metric delta vs. `expected_impact` in real-time.
3. Implement an auto-flagging system:
   - Alert if the metric delta deviates from `expected_impact` by >20% (configurable).
   - Surface mismatches in the log with a `⚠️ MISMATCH` tag.
4. Enforce the workflow:
   - Block prompt merges if `expected_impact` or metric link is missing.
   - Require a post-mortem comment if flagged (even if change is rolled back).
5. Add a dashboard:
   - Show log entries with metric deltas, flags, and rollback history.
   - Include a "confidence score" (e.g., % of flagged vs. unflagged changes).
6. Document the process:
   - Update the prompt-review SOP with the new fields, A/B rules, and flagging logic.

**What changed:**
Prompt changes now require a one-sentence expected impact, a linked production metric, and auto-flagging for mismatches—turning the log into a data-driven audit trail.
