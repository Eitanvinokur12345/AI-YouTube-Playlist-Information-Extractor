---
name: claude-code-token-optimization
description: "Use when diagnosing and reducing high Claude Code API token costs by auditing what is sent to the model, not what comes back."
---

# Claude Code Token Cost Optimization

## Overview
Identify and eliminate token waste in Claude Code by auditing what you SEND (not what Claude responds with), focusing on tool-loading leaks. CC Glass provides a local dashboard of token spend per session to make waste visible, helping cut costs by up to 50%.

## Key Techniques
- Audit what is sent to Claude (the input tokens), not just what comes back
- Identify tool-loading leaks — forgotten tools that load with every prompt
- Use CC Glass for a local per-session token spend dashboard

## How to Apply
1. Install CC Glass (comment "glass" on the source video for the link).
2. Run CC Glass alongside Claude Code to track token spend per session.
3. Identify which tools are loaded on every prompt — look for forgotten integrations.
4. Remove or conditionally load tools that are not needed for your current workflow.
5. Monitor the dashboard to confirm cost reduction after changes.

## Examples
- One user found 538 tools loading per prompt, costing almost $12 for 10 requests with only 3,000 words of output
- Removing unused tool connections dropped per-session costs by up to 50%

## Source
Extracted from: [Reduce Your Claude Code Token Bill By 50%](https://www.youtube.com/watch?v=QtlMU6rn86g)
Channel: Charlie Automates
