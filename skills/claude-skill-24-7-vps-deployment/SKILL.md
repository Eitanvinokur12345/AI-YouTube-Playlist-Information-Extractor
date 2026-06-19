---
name: claude-skill-24-7-vps-deployment
description: "Use when you need a Claude skill or automation to run continuously without your local machine — deploy it through Hermes on a VPS with a schedule trigger."
---

# Claude Skill 24/7 VPS Deployment via Hermes

## Overview
Claude Skills only run while your laptop is active. This technique breaks that limitation by deploying a skill through Hermes on a VPS and attaching a scheduled trigger, creating a true 24/7 agent.

## Key Techniques
- Port your Claude Skill to Hermes running on a cloud VPS
- Expose the skill through Hermes' MCP interface
- Set a schedule trigger (cron-style) so the agent runs on a defined interval

## How to Apply
1. Build and test your Claude Skill locally in Claude Code
2. Set up Hermes on a VPS (any cloud provider)
3. Copy the skill into the Hermes environment
4. Configure the MCP port so the skill can receive external triggers
5. Add a schedule trigger (time interval or cron expression)
6. Verify the agent fires and completes tasks when your laptop is off

## Examples
- A skill that monitors inbox and drafts replies → deployed on VPS → runs every 15 minutes overnight
- Content generation pipeline → VPS-hosted → fires every morning at 6am automatically

## Source
Extracted from: [The #1 Underrated Claude Skill Hack for 24/7 Agents](https://www.youtube.com/watch?v/o0NA6qyLUB4)
Channel: Charlie Automates
