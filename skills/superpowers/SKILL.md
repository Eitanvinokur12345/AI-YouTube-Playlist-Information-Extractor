---
name: superpowers
description: "Use when you want a coding agent to follow a full, disciplined software development methodology — brainstorm, TDD, subagent code review, and systematic debugging — instead of one-shot ad-hoc coding."
---

# Superpowers

## Overview
A complete software development methodology for coding agents, built from composable skills:
structured brainstorming, strict test-driven development, two-stage subagent code review,
git worktree management for parallel work, and systematic, evidence-based debugging.

## Key Techniques
- Brainstorm and refine the design before writing any code.
- Enforce RED-GREEN-REFACTOR test-driven development cycles.
- Run a two-stage subagent code review instead of a single pass.
- Use git worktrees to isolate parallel development streams.
- Debug systematically with plan-based checkpoints and verification, not guessing.

## How to Apply
1. Install for your coding agent (Claude Code, Cursor, GitHub Copilot CLI, Gemini CLI, Kimi
   Code, and others are supported) via the platform-specific plugin marketplace or repo
   installation method.
2. Start any non-trivial task with the brainstorming/design-refinement step before coding.
3. Write the failing test first (RED), implement the minimum to pass (GREEN), then refactor.
4. Route finished changes through the two-stage subagent review before merging.
5. Use git worktrees when running multiple development streams in parallel.

## Examples
Recommended as one of "5 Claude skills you need," positioned as giving an agent a repeatable,
disciplined dev process instead of ad-hoc one-shot code generation.

## Source
Extracted from: [5 Claude skills you need](https://www.youtube.com/watch?v=W1_hQoDYVXU)
Channel: TheCyborgGirl
Repo: obra/superpowers (262.2k stars)
