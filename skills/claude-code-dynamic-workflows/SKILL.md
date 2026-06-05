---
name: claude-code-dynamic-workflows
description: "Use when orchestrating complex, multi-step coding tasks in Claude Code that require independent sub-agents, verification loops, or parallel worktree execution."
---

# Claude Code Dynamic Workflows

## Overview
Dynamic workflows allow Claude Code to write a JavaScript control program that spawns and coordinates multiple focused sub-agents for a single complex task. Each sub-agent can use a different model, work in an isolated worktree, and verify other agents' outputs.

## Key Techniques
- Write a JavaScript workflow that defines task order, agent assignments, and synthesis logic
- Assign each sub-agent a single focused job (e.g., write tests, verify claims, merge results)
- Use one agent to verify another agent's output for adversarial or accuracy-critical work
- Choose a cost-effective model per sub-agent rather than using Opus for every step

## How to Apply
1. Identify a task that is too long or complex for a single agent context (flaky tests, large refactor, research)
2. Ask Claude Code to generate a dynamic workflow for the task
3. Claude writes a JavaScript file that orchestrates sub-agents with defined roles
4. Sub-agents run in parallel or sequentially across worktrees and merge results
5. Review the synthesized output and iterate on the workflow if needed

## Examples
- Fixing flaky tests: one agent rewrites the test, another verifies determinism, a third runs the suite
- Big refactors: sub-agents handle separate modules; a supervisor agent merges and checks consistency
- Source-heavy research: multiple agents gather sources in parallel; a synthesis agent ranks and summarizes
- Claim verification: one agent makes a claim, another adversarially checks it

## Source
Extracted from: [Dynamic Workflows in Claude Code](https://www.youtube.com/watch?v=PTpKj5t7xI8)
Channel: Arnitly