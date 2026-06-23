---
name: claude-code-context-efficiency
description: "Claude Code users experiencing high token costs, context limit errors, or slow iterative development."
---

# Claude Code Context Efficiency: Opus Plans, Sonnet Codes, /compact, ultrathink

## Overview
Three concrete tricks to prevent Claude Code from hitting context and usage limits: (1) set model so Opus handles planning and Sonnet handles coding to optimize cost/quality, (2) use /compact to compress long conversation contexts, (3) add "ultrathink" to complex prompts for deeper pre-coding analysis that reduces iteration.

## Key Techniques
- Opus plans, Sonnet codes: set /model to Opus for architecture planning, switch to Sonnet for implementation to balance cost and quality
- Use /compact to compress long conversation histories into a summary before continuing — reduces re-reading overhead
- Add "ultrathink" to prompts for complex problems so Claude reasons deeply before writing code, reducing back-and-forth

## How to Apply
Claude Code users experiencing high token costs, context limit errors, or slow iterative development.

## Examples
Significantly reduced token consumption per session while maintaining code quality — avoids usage limits and cuts per-task cost.

## Source
Extracted from: [3 Tricks So Claude Code Never Hits Its Limit](https://www.youtube.com/watch?v=wRdyvEOaOgA)
Channel: Sebastian Hardy | AI Marketing
