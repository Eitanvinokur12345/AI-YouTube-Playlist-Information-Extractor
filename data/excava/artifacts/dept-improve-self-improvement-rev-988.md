# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-988` (dept) · 2026-07-10T17:39:09.907268+00:00
> Participants: Sprocket · synthesized by mistral/mistral-small-latest

**Decision:** Build a lightweight "prompt review bot" that runs after every prompt edit, checks for common issues, and suggests plain-language fixes.

**Plan:**
1. Implement a post-edit hook in the prompt editor to trigger the bot.
2. Define a checklist of common prompt issues (e.g., vague instructions, missing constraints).
3. Generate a yes/no + short reason for each issue detected.
4. Display suggestions inline without code or file paths.
5. Log reviews for later analysis and improvement.
6. Deploy to staging, then production with gradual rollout.

**What changed:** Added automated prompt quality checks with plain-language feedback.
