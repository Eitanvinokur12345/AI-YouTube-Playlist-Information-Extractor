# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-716` (dept) · 2026-07-31T21:28:42.403181+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Auto-apply formatting-only patches to files with a `.fmt` suffix, with a post-apply diff review in the PR.
**Plan:**
1. Enforce a `.fmt` file suffix convention for all prompt files that will be auto-formatted.
2. Configure the auto-formatter to only apply patches to files with the `.fmt` suffix.
3. Set up a post-apply diff review in the PR to review formatting-only changes.
4. Implement a process for leads to review and confirm formatting-only changes in PRs.
5. Update documentation to reflect the new `.fmt` suffix convention and auto-formatting process.
**What changed:** Files without the `.fmt` suffix are no longer eligible for auto-applied formatting-only patches.
