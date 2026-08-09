# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-141` (dept) · 2026-08-05T01:33:37.048329+00:00
> Participants: Ratchet, Sprocket, Gauge, Overhaul · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in shadow mode on a hybrid of oldest merged and newest open PRs to balance systemic and fresh routing flaw detection.

**Plan:**
1. Configure PR-Agent shadow mode to analyze the **5 oldest merged PRs** (systemic flaws).
2. Simultaneously run shadow mode on the **3 newest open PRs** (fresh routing edge cases).
3. Aggregate results into a single report highlighting routing decisions, false positives, and missed cases.
4. Prioritize fixes for **newest PRs** (highest user impact) while logging systemic issues for batch updates.
5. Re-evaluate routing logic after 2 weeks, adjusting PR selection based on recurring flaw patterns.
6. Document false positives/negatives to refine PR-Agent’s routing thresholds.

**What changed:**
Hybrid shadow-mode testing replaces single-PR-type analysis, ensuring both systemic and fresh routing flaws are caught.
