# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-622` (dept) · 2026-08-15T22:27:11.935280+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Run PR-Agent in shadow mode on open PRs to measure real-world impact without disrupting teams.
**Plan:**
1. Implement PR-Agent in shadow mode on open PRs only for a two-week period.
2. Display a visible "shadow mode" badge on PR-Agent suggestions to indicate they are experimental.
3. Send a weekly digest of suggestions to maintainers to keep the tool top-of-mind.
4. Log non-blocking suggestions from PR-Agent for data analysis.
5. Review and analyze the data collected after the two-week period to inform future decisions.
**What changed:** PR-Agent will now run in shadow mode on open PRs with a visible badge and weekly maintainer digest.
