---
name: agent-tool-calling-methods
description: "Use when deciding how to wire an AI agent up to an external capability — pick from CLI, MCP, browser automation, computer use, or programmatic tool calling based on the task's constraints."
---

# Agent Tool-Calling Methods Taxonomy (5 Approaches)

## Overview
There are five common ways to give an AI agent access to tools or actions, each with different reliability, speed, and setup tradeoffs. Choosing the right one per task beats defaulting to a single style everywhere.

## Key Techniques
- **CLI invocation** — the agent shells out to a command-line tool; simple and scriptable when a CLI already exists.
- **MCP (Model Context Protocol)** — the agent talks to a standardized server exposing tools/resources; most reusable across different agents and clients.
- **Browser automation** — the agent drives a real browser (clicks, forms, navigation) when no API exists.
- **Computer use** — the agent controls the screen/mouse/keyboard directly, for GUI-only tasks with no browser or CLI path.
- **Programmatic tool calling** — structured function-calling APIs where the model emits typed calls the host executes directly.

## How to Apply
1. Check whether the target capability already has a CLI or API — if so, prefer CLI or programmatic tool calling for determinism and speed.
2. If the capability should be reusable across multiple agents/tools, wrap it as an MCP server instead of a one-off integration.
3. Fall back to browser automation or computer use only when no programmatic path exists (legacy web apps, GUI-only software).

## Examples
The source video frames this as a quick 5-way comparison for anyone wiring up agent tools in Claude Code / Codex-style workflows, without picking one method as universally best.

## Source
Extracted from: [5 methods for agent tools: CLI, MCP, browser automation, computer use, programmatic tool calling](https://www.youtube.com/watch?v=c8mTYJK7_oY)
Channel: James Goldbach
