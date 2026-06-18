---
name: doubt-driven-agent-development
description: "Use when you want your AI agent to actively doubt and re-check its own work before shipping output — adds a self-verification gate to prevent confident agent errors."
---

# Doubt-Driven Agent Development

## Overview
One of Addy Osmani's 23 open-source SKILL.md files instructs the AI agent to deliberately doubt its own output and re-verify before delivering. This counters the common failure mode of agents that ship wrong answers confidently. The skill is part of a library at github.com/addyosmani/agent-skills with 51K stars.

## Key Techniques
- **Self-doubt gate** — agent explicitly questions whether its answer is correct before finalizing
- **Re-check loop** — agent runs a verification pass (re-reads sources, rechecks logic) before output
- **Cross-agent portability** — works in Claude Code, Gemini CLI, and OpenCode via a 10-byte symlink

## How to Apply
1. Clone `github.com/addyosmani/agent-skills` into your project's `skills/` directory.
2. The doubt-driven skill file instructs Claude (or Gemini CLI / OpenCode) to re-examine its reasoning before every response.
3. Wire it via CLAUDE.md: `@skills/doubt-driven-development.md`.
4. For OpenCode, create a symlink: `ln -s ../skills opencode-skills` — the whole library ports instantly.

## Examples
- Code review agent: before outputting "looks good", agent re-reads the diff and asks itself "did I miss anything?"
- Analysis agent: before submitting findings, agent re-checks each data point against the source.

## Source
Extracted from: [A Google Director Open-Sourced His Claude Skills](https://www.youtube.com/watch?v=EXdBg_5ydV8)
Channel: Bitwise AI
Repo: https://github.com/addyosmani/agent-skills (Addy Osmani, Google)
