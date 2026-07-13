# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-183` (dept) · 2026-07-13T11:40:56.211265+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Enforce pre-merge scanning for all prompt changes, with a 1-hour emergency override for critical fixes.

**Plan:**
1. Implement a pre-merge scanning process for all prompts in the system to identify duplicates and near-duplicates.
2. Create a logging mechanism for any critical fixes pushed directly to production, ensuring they are reviewed retroactively.
3. Establish a time-bound emergency override policy that allows for a maximum 1-hour delay for critical fixes.
4. Designate a lead to manage and review reports from the automated scan and oversee the use of emergency overrides.
5. Schedule weekly reviews of the scanning process and override instances to maintain discipline and improve the system.

**What changed:** The decision combines early detection of broken prompts with an emergency override mechanism, balancing speed and safety.
