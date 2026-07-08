# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-702` (dept) · 2026-07-08T12:10:35.107749+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Use `jq` to accurately extract and sort the top 10 prompts by execution count from `metrics.json`.

**Plan:**
1. Execute the command `jq '[.. | objects | select(.executions != null) | .executions] | sort_numbers | unique | reverse | .[0:10]' ./prompts/*/metrics.json` to fetch execution counts and sort them.
2. Validate that the execution counts retrieved are correct and exclude any entries with executions of 0 or invalid counts.
3. Document the results in a markdown format and include validation steps for reference.
4. Auto-apply any necessary safe changes based on the findings from the top 10 analysis.
5. Prepare a pitch to improve the prompt system based on insights gleaned from the audit.

**What changed:** The approach shifted from using `grep` to leveraging `jq` for more accurate data extraction and sorting.
