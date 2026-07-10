# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-493` (dept) · 2026-07-10T02:49:01.794521+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Conduct a structured audit of `prompts/routing.py` focusing on unsafe fallbacks.

**Plan:**
1. Execute `git diff HEAD -- prompts/routing.py` to identify the current engine-routing logic.
2. Run `grep -n "except\|fallback\|default" prompts/routing.py` to compile a list of line numbers, contexts, and associated fallback logic.
3. Develop a risk matrix that assesses each fallback's impact and likelihood based on established criteria.
4. Inventory current fallbacks with detailed context and risk scores.
5. Propose changes with risk scores and apply alterations only if the risk is below a defined threshold.

**What changed:** The approach now includes a formal risk assessment process for assessing fallbacks.
