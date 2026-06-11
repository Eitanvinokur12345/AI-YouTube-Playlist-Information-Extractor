---
name: parallel-multi-agent-decomposition
description: "Use when tackling complex multi-step tasks by spinning up specialized Claude agents that run in parallel with shared memory to reduce both time and cost."
---

# Parallel Multi-Agent Task Decomposition

## Overview
Spin up 50+ specialized Claude agents running in parallel — one plans, one codes, one tests, one checks security, all sharing memory — to complete complex tasks dramatically faster than a single agent. This reduces both time and token costs compared to sequential single-agent approaches.

## Key Techniques
- Assign distinct roles to each agent (planner, coder, tester, security reviewer, etc.)
- Run all agents simultaneously rather than sequentially
- Use shared memory so each agent can read the outputs of others

## How to Apply
1. Define the complex task and break it into distinct specialist functions.
2. Create an agent for each function with a focused system prompt and role.
3. Share a memory/context store that all agents can read and write.
4. Launch all agents simultaneously in parallel.
5. Have a coordinator agent aggregate the outputs into the final result.

## Examples
- A 50-agent code project: planner drafts spec → 20 coders implement modules → 10 testers write tests → 10 reviewers check quality → 10 security agents scan for vulnerabilities
- Parallel research agents each analyzing different aspects of a topic then synthesizing findings

## Source
Extracted from: [This Claude Hack Can Cut Your AI Costs in Half](https://www.youtube.com/watch?v=akg9L65DnaA)
Channel: EMPIRES Digital Inc.
