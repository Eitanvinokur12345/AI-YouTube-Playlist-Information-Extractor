# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-978` (dept) · 2026-07-27T17:58:27.974342+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Run a 5% canary rollout for 48 hours with dual-prompt A/B logging, auto-applying only routing tweaks via the Skill Pack’s safe-change rules while manually validating prompt changes in shadow mode before full adoption.  

**Plan:**  
1. Implement the Skill Pack’s safe-change rules to auto-apply routing tweaks.  
2. Begin a 48-hour canary deployment for 5% of users.  
3. Set up dual-prompt A/B logging to monitor the performance of prompts.  
4. Conduct manual validation of prompt changes in shadow mode during the deployment.  
5. Analyze the data from the canary report post-deployment to evaluate the impact.  

**What changed:** The decision blends Sprocket's automation with Gauge's cautious manual validation for a balanced approach.
