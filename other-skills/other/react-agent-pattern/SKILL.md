---
name: react-agent-pattern
description: "Building, debugging, or optimizing any AI agent system — once you see the ReAct loop, you can instantly diagnose whether"
---

# ReAct Agent Loop: Reason → Act → Observe Cycle

## Overview
ReAct (Reasoning + Acting) is the core Reason → Act → Observe loop that underlies all modern AI agents. The agent reasons about what to do next, calls a tool (act), observes the result, then loops back to reasoning until the task is complete. Understanding this pattern makes debugging any agent immediate.

## Key Techniques
- Agent stuck in a loop = reasoning step is failing to progress; add stricter stopping criteria
- Agent taking wrong actions = act step is misinterpreting the reasoning; tighten the tool descriptions
- Agent ignoring results = observe step is broken; check tool output formatting

## How to Apply
Building, debugging, or optimizing any AI agent system — once you see the ReAct loop, you can instantly diagnose whether the reasoning, acting, or observing step is failing.

## Examples
A well-structured AI agent loop that predictably progresses toward task completion, plus a debugging framework when it stalls.

## Source
Extracted from: [The ReAct Pattern: How Your AI Agent Actually Thinks #techto](https://www.youtube.com/watch?v=sUdHyB5kChE)
Channel: Doby Lanete Highlights
