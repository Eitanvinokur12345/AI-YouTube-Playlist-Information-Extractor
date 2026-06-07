---
name: claude-code-usage-optimization
description: "Reducing API token spend when working with Claude Code on large or iterative coding tasks."
---

# Claude Code Usage Optimization

## Overview
Three-command workflow for reducing Claude Code token consumption: /model opus plan restricts Opus to planning only with Sonnet for execution; /compact compresses long context windows; /ultra-plan forces deep reasoning before big refactors to prevent hallucinated changes.

## Key Techniques
- Run /model opus plan to limit Opus to planning only — Sonnet 4.6 handles code execution at far lower token cost.
- Run /compact when conversations grow long — Claude rereads full history on every message, compressing saves significant tokens.
- Use /ultra-plan before large refactors to force deeper reasoning upfront, preventing hallucinated changes that waste correction cycles.

## How to Apply
Reducing API token spend when working with Claude Code on large or iterative coding tasks.

## Examples
From the source video: Lower token usage, fewer hallucinated code changes, and more efficient model tier usage.

## Compatibility
Claude Code (any)

## Source
Extracted from: [Stop Wasting Your Claude Code Usage Limits](https://www.youtube.com/watch?v=0-p-SuoHCoo)
Channel: Unknown
