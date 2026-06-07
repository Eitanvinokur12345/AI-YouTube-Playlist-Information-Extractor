---
name: deepseek-v4-pro-claude-code-backend
description: "Use when you want to cut Claude Code API costs by ~90% by redirecting it to DeepSeek V4 Pro via two environment variables, keeping the full Claude Code interface."
---

# DeepSeek V4 Pro Backend for Claude Code

## Overview
By setting two environment variables, Claude Code can use DeepSeek V4 Pro as its underlying model instead of Anthropic's own models. This cuts inference costs from $15/M tokens to $1.74/M while keeping the full Claude Code agent interface, same file edits, and same workflow.

## Key Techniques
- Set `ANTHROPIC_BASE_URL` to DeepSeek's Anthropic-compatible endpoint
- Add your DeepSeek API key as `ANTHROPIC_API_KEY`
- Launch Claude Code as normal — same interface, same agent behavior

## How to Apply
1. Get a DeepSeek API key from DeepSeek's developer portal.
2. In your terminal profile or `.env`, set:
   ```
   export ANTHROPIC_BASE_URL=https://api.deepseek.com
   export ANTHROPIC_API_KEY=<your-deepseek-key>
   ```
3. Launch Claude Code normally — it will route all requests to DeepSeek V4 Pro.
4. Verify by running a simple task and checking your DeepSeek usage dashboard.

## Examples
- A developer running 10+ hour coding sessions cuts their monthly Claude bill from $200 to ~$7 using DeepSeek V4 Pro.
- A team doing CI/CD agent runs uses DeepSeek as the default model and reserves Claude Opus for critical review tasks only.

## Source
Extracted from: [DeepSeek V4 Pro Cuts Claude Costs by 97%](https://www.youtube.com/watch?v=L9tfZjqtn2U)
Channel: Sebastian Hardy | AI Marketing
