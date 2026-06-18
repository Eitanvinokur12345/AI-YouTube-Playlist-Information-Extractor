---
name: addy-osmani-agent-skills-library
description: "Use to install Addy Osmani's 23-file open-source agent-skills library into Claude Code, Gemini CLI, or OpenCode — a complete, battle-tested agent workflow with 51K GitHub stars."
---

# Addy Osmani Agent-Skills Library

## Overview
Google's Addy Osmani open-sourced his complete 23-file SKILL.md agent workflow at github.com/addyosmani/agent-skills (51K stars). The collection covers self-verification, context engineering, coding patterns, and more. It runs across Claude Code, Gemini CLI, and OpenCode via a single symlink.

## Key Techniques
- 23 SKILL.md files covering distinct aspects of an AI agent workflow
- Cross-agent portability: one symlink makes the full library available in any compatible agent
- Standout skill: doubt-driven self-checking before output delivery

## How to Apply
1. `git clone https://github.com/addyosmani/agent-skills` into your project or a shared location.
2. Reference the `skills/` folder in your `CLAUDE.md` or agent config.
3. For OpenCode: create a 10-byte symlink (`ln -s ../skills`) to avoid duplication.
4. For Gemini CLI: point the config to the same `skills/` directory.

## Examples
- Drop the entire 23-file library into a new Claude Code project to immediately have a full, proven agent skill set.

## Source
Extracted from: [A Google Director Open-Sourced His Claude Skills](https://www.youtube.com/watch?v=EXdBg_5ydV8)
Channel: Bitwise AI
Repo: https://github.com/addyosmani/agent-skills
