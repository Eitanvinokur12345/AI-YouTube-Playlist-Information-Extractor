---
name: claude-code-codex-orchestration-pattern
description: "Use when you want to reduce token costs in multi-step coding tasks by routing planning and orchestration to Claude Code while delegating actual code execution to OpenAI Codex via a plugin connection."
---

# Claude Code + Codex Orchestration Pattern

## Overview
A multi-agent coding pattern that uses Claude Code for orchestration and multi-agent planning while routing actual code execution to OpenAI Codex via a direct plugin. Each model covers the other's gaps: Claude is stronger at reasoning and orchestration, Codex provides more token runway and writes surgical production-ready code. Cost per good output drops because the expensive model only plans.

## Key Techniques
- Install the Claude Code → Codex plugin to enable direct model-to-model handoff
- Assign all orchestration, planning, and multi-agent coordination to Claude Code
- Route actual code writing and execution tasks to Codex (more tokens, less tech debt)
- Use the heavy model (Claude) for high-level reasoning; use the efficient model (Codex) for building
- Monitor cost by tracking which tasks go to which model

## How to Apply
1. Install the plugin that lets Claude Code call Codex directly (search Claude Code plugins for Codex integration)
2. Structure your prompt to ask Claude Code to plan and orchestrate, not to write the code itself
3. Have Claude Code delegate code generation subtasks to Codex via the plugin
4. Review Codex output for production-readiness; use Claude Code to synthesize final output
5. Iterate: complex decisions → Claude Code; precise code generation → Codex

## Examples
- Claude Code decomposes a feature into 5 tasks, then calls Codex to implement each one
- Multi-file refactoring: Claude Code orchestrates the order and dependencies, Codex writes the changes
- Tech debt reduction: let Codex write the surgical implementation, Claude Code validates correctness

## Source
Extracted from: [Use Claude Code to control Codex and save tokens](https://www.youtube.com/watch?v=szGK-RYFVOQ)
Channel: James Goldbach
