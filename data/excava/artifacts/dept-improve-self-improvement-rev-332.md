# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-332` (dept) · 2026-07-29T20:58:28.622377+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a quarterly combined audit—rank prompts by failure rate, then score the top 20% with a lightweight rubric to catch both outright failures and subtle waste, owned by the prompt team.

**Plan:**
1. Define a lightweight rubric (clarity, specificity, task alignment) for scoring prompts.
2. Implement automated tracking of prompt failure rates in production.
3. Quarterly, rank all prompts by failure rate and select the top 20% for rubric scoring.
4. Assign the prompt team to audit and refine the selected prompts based on rubric + failure data.
5. Document changes in a prompt audit log with before/after metrics (token usage, output quality).
6. Iterate rubric criteria annually based on audit findings.

**What changed:**
Quarterly combined audits replace blanket health scores, focusing fixes on high-failure and high-waste prompts.
