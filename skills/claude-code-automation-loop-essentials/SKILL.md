---
name: claude-code-automation-loop-essentials
description: "Use when designing a Claude Code workflow that needs to run unattended, with parallel agents, shared knowledge, and real data access — the 5-component loop architecture."
---

# Claude Code Automation Loop: 5 Essentials

## Overview
An AI automation loop in Claude Code requires five components working together: a schedule trigger, git worktrees for parallel isolation, a skills library for reuse, plugins/connectors for data, and sub-agents for parallelism. Without all five, loops either collide, forget, or stall.

## Key Techniques
- **Schedule** — a cron or event trigger that starts the loop without human action
- **Git worktrees** — each parallel agent gets its own isolated branch so they never overwrite each other
- **Skills library** — a shared pool of SKILL.md files so every agent starts with proven knowledge, not a blank slate
- **Plugins & connectors** — MCP servers or API connectors that give agents access to real databases, tools, and services
- **Sub-agents & agent teams** — nested agents that allow hundreds of concurrent workers inside one loop

## How to Apply
1. Set up a schedule (cron, GitHub Actions, or a timer) to trigger the loop automatically.
2. For each parallel task, create a separate git worktree (`git worktree add`) so agents have isolated working copies.
3. Point every agent at your `skills/` directory so they load relevant SKILL.md files at the start of each session.
4. Wire connectors (MCP servers) so agents can read/write real data without manual file passing.
5. Spawn sub-agents for subtasks; collect their outputs with an orchestrator agent that coordinates the team.

## Examples
- An overnight content pipeline where one agent writes, one reviews, one publishes — each in its own worktree.
- A bulk analysis run where 50 sub-agents each analyze one video in parallel and write results to separate branches.

## Source
Extracted from: [Everyone Talks About Loops, Nobody Explains This](https://www.youtube.com/watch?v=BSK5_zdrxbs)
Channel: Sebastian Hardy | AI Marketing
