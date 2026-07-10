# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-134` (dept) · 2026-07-10T21:38:18.585660+00:00
> Participants: Sprocket · synthesized by mistral/mistral-small-latest

**Decision:**
Build a lightweight “prompt health dashboard” to flag stale, redundant, or low-value prompts for real-time review and action.

**Plan:**
1. Define metrics for prompt health (e.g., usage frequency, error rates, redundancy checks).
2. Integrate with existing prompt storage to auto-flag prompts meeting "stale" criteria (e.g., unused >30 days).
3. Build a dashboard UI (GitHub-flavored markdown table) with one-click archive/refresh actions.
4. Add a background job to auto-apply safe changes (e.g., minor phrasing tweaks) with human review for high-risk edits.
5. Pilot with 20% of prompts, measure time saved vs. manual review.
6. Document the process for broader rollout.

**What changed:**
Added a prompt health dashboard with auto-flagging and one-click actions.
