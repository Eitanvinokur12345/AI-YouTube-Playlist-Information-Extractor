---
name: claude-code-routines-scheduled-automation
description: "Use when you want a small, hands-off recurring automation (e.g. a daily report) without standing up an external scheduler — Claude Code's built-in Routines tab can run a prompt on a schedule."
---

# Claude Code Routines: Scheduled Sub-Agent Automation

## Overview
Uses Claude Code's built-in Routines tab to schedule a prompt to fire automatically at a set
time against a folder on your machine, turning Claude Code into a lightweight cron-style
automation platform for simple recurring agent tasks.

## Key Techniques
- Drop reference resources into the routine's working folder so the agent has a knowledge
  base to read, rather than relying only on the prompt text.
- Enable bypass permissions only for routines you trust to run fully unattended.
- Deploy a swarm of sub-agents from within a single routine (e.g. one per research task) that
  write their output into a shared deliverables folder.

## How to Apply
1. Open Claude Code's Routines tab and create a new routine.
2. Point it at a folder; drop in the resources/context the agent needs as a knowledge base.
3. Write the prompt for the workflow you want run.
4. Enable bypass permissions so it can run fully autonomously.
5. Pick the schedule (time of day / cadence) and let it run unattended, dropping output into
   a deliverables folder.

## Examples
The source video's routine deploys a swarm of sub-agents to research trending products, run
sourcing math, and drop a full report into a deliverables folder every day, unattended.

## Source
Extracted from: [Easiest agentic automation for your business](https://www.youtube.com/watch?v=nCLkryY8PXg)
Channel: James Goldbach
