---
name: claude-agent-loop
description: "Use when you want to let claude code run long autonomous build-and-review loops without manual babysitting."
---

# Claude Code Agent-Loop Command Stack

## Overview
A set of Claude Code slash commands that let agents plan and work autonomously: /ultra-plan has sub-agents draft a plan, /goal loops the agent until a goal is met (it can run for hours), /agents launches background/parallel sessions and /ultra-review audits the code. Looping avoids constant re-prompting, which saves credits.

## Key Techniques
- Use /goal to loop the agent until a written goal is met.
- Run /ultra-plan first so sub-agents design the plan before coding.
- Use /agents to run parallel background sessions.

## How to Apply
A set of Claude Code slash commands that let agents plan and work autonomously: /ultra-plan has sub-agents draft a plan, /goal loops the agent until a goal is met (it can run for hours), /agents launches background/parallel sessions and /ultra-review audits the code. Looping avoids constant re-prompting, which saves credits.

## Examples
Let Claude Code run long autonomous build-and-review loops without manual babysitting. Completed multi-step work plus a self-review, produced autonomously.

## Source
Extracted from: [This Claude Code Trick Saves Thousands in Credits](https://www.youtube.com/watch?v=SOUg5EHGOaM)
Channel: Sebastian Hardy | AI Marketing
