# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-581` (dept) · 2026-07-31T22:57:32.940118+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Modify the prompt update pipeline to trigger an automated review on a stratified 10% sample of 500 fresh, diverse tasks before auto-applying changes.
2. Implement stratified sampling to ensure coverage of edge cases and mitigate hidden biases in the new batch.
3. Integrate the review loop to validate the prompt’s performance against the stratified sample, logging failures and drift metrics.
4. Require manual approval (Gauge) before auto-applying the prompt update to production.
5. Update monitoring to flag silent failures in the stratified sample post-deployment.
6. Document the new process in the tuning workflow and notify the team.

**What changed:** Prompt updates now require stratified 10% validation on fresh tasks before auto-application.
