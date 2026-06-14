---
name: agent-memory-file-pattern
description: "Use when you want AI agents to remember your preferences and avoid repeating mistakes across sessions — create a plain-text memory file in the project root."
---

# Agent Memory File Pattern

## Overview
A plain-text file (claude.md, agents.md, or platform equivalent) placed in the project root that the agent reads at the start of every session. Whatever rules are in this file become permanent behaviors the agent follows without being re-told.

## Key Techniques
- One memory file per project in the root directory
- Platform-specific file names: `claude.md` (Claude Code), `agents.md` (OpenClaw), Antigravity has its own variant
- Self-modifying memory: instruct the agent to append new rules when corrected
- Graduated growth: start with 3 rules, let the agent expand it session by session

## How to Apply
1. Create a memory file in the project root (`claude.md` for Claude Code, `agents.md` for OpenClaw, etc.).
2. Add your initial rules: style preferences, constraints, known gotchas.
3. Add a self-modification instruction: "If I correct you or you hit a bug from a wrong assumption, append a new rule to the 'Learned Rules' section at the bottom of this file."
4. Let the agent run. When it makes a mistake and you correct it, it writes a new rule before finishing.
5. Each session the agent starts with the full accumulated ruleset — no repetition needed.

## Examples
Bug that triggered memory: agent kept inserting emojis in customer-facing copy of a B2B dashboard. Fix: told the agent to create claude.md with one rule: "Never use emojis in customer-facing copy unless explicitly asked. This is a B2B product." Bug never appeared again in any project.

## Source
Extracted from: [AI Agents Explained: How to Create and Use AI Agents in 2026](https://www.youtube.com/watch?v=4TvH-OZhwxI)
Channel: AI Master
