---
name: claude-code-github-full-team-setup
description: "Use when you want to configure Claude Code with a complete team of sub-agents, hooks, MCPs, and skills via a single GitHub repository — so every session starts fully loaded."
---

# Claude Code GitHub Full Team Setup

## Overview
A single open-source GitHub repository that pre-loads Claude Code with sub-agents, slash commands, hooks, MCP servers, security scanning, and skill files. Clone it once and Claude Code reads its configuration automatically on every session start, transforming a bare install into a full AI engineering team.

## Key Techniques
- Store all Claude Code configuration in a version-controlled GitHub repo
- Include sub-agent definitions, hook scripts, MCP server configs, and SKILL.md files in the repo
- Let Claude Code's auto-discovery load everything from the repo at session start
- Include security scanning rules to protect every session by default

## How to Apply
1. Clone or fork the setup repo into your project (or use it as a submodule)
2. The repo contains: `.claude/` config folder, `skills/` folder, hook scripts, MCP configs
3. Start a Claude Code session — it automatically reads sub-agent definitions, hooks, and MCPs
4. Use slash commands that are now pre-loaded and available immediately
5. Update the repo to roll out config changes across the whole team

## Examples
- A repo with a `/review` agent that runs a full code review pipeline
- Pre-loaded hooks that run security scans before every commit
- MCP servers for GitHub, Jira, and Slack pre-configured in the repo
- Memory files that persist key project context across sessions

## Source
Extracted from: [The GitHub setup that changes everything for Claude](https://www.youtube.com/watch?v=AaS-mursHKA)
Channel: Sebastian Hardy | AI Marketing
Guide: https://docs.google.com/document/d/1MOPeQ72bCdtNSJo9FGAmizYo7Aq7qYGQ/edit
