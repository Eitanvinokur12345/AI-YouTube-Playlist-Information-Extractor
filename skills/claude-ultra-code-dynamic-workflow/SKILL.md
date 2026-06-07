---
name: claude-ultra-code-dynamic-workflow
description: "Use when you need Claude Code to tackle complex research or multi-faceted coding tasks by spawning up to 100 parallel worker agents that split, verify, and synthesize results."
---

# Claude Ultra Code Dynamic Workflow

## Overview
Ultra Code is Claude Code's parallel agent mode, combining xhigh thinking with dynamic workflows to spin up to 100 worker agents on a single task. Each worker handles a sub-task independently, they verify each other's work, and the results are synthesized before returning to you.

## Key Techniques
- Enable via Claude Code Settings → toggle Ultra Code (requires xhigh thinking + dynamic workflows)
- Use for research tasks, complex multi-module codebases, or adversarial verification workflows
- Budget for high token usage: a 22-agent food truck research run used ~983k tokens (~$9 on Opus 4.8)

## How to Apply
1. Open Claude Code and go to Settings.
2. Enable "Ultra Code" toggle (this enables both xhigh thinking and dynamic workflows simultaneously).
3. State your task clearly — the more decomposable the task, the more Ultra Code helps.
4. Claude will spawn workers, assign sub-tasks, have them verify each other, and return synthesized output.
5. For cost control: use on API tier and monitor token usage per run.

## Examples
- Research an entire food truck business: market, competitors, suppliers, financials — 22 parallel agents, 20 minutes.
- Multi-module codebase refactor where each agent handles one module and a supervisor verifies consistency.

## Source
Extracted from: [Claude Just Dropped ULTRA CODE. (Everything You Need to Know in 5 min).](https://www.youtube.com/watch?v=IgIlIWqeT-I)
Channel: Tristen O'Brien
