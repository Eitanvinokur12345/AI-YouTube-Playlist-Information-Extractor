---
name: agent-skills-modular-llm-software
description: "Use when designing reusable agent skill libraries where individual skill files should compose into larger workflows like software modules."
---

# Agent Skills as Modular LLM Software

## Overview
LLMs are natural-language computers and agent skills are the software that runs on them — analogous to how traditional programs run on a CPU. Granular skills compose into larger skills exactly like software modules, with almost no limit to the logic you can encode in a single skill file.

## Key Techniques
- Write each skill as a focused, single-responsibility natural-language program
- Embed real bash scripts inside a skill file for the agent to execute with its bash tools
- Compose granular skills into larger orchestrating skills like software libraries

## How to Apply
1. Identify the unit of work you want to modularize (e.g., "run linting", "draft a PR description").
2. Write a focused SKILL.md file using plain language to specify the logic.
3. Optionally embed real scripts (bash, Python) that the agent can invoke.
4. Reference the granular skill from a higher-level skill that orchestrates multiple steps.
5. Test each skill independently before composing.

## Examples
- A `code-review` skill that checks formatting, security, and tests — each as sub-steps.
- A `research-and-summarize` skill composed of a `web-search` skill + a `summarize` skill.
- An `onboarding` skill that runs `create-repo`, `set-up-ci`, and `send-welcome-email` in sequence.

## Source
Extracted from: [Agent skills are the future of computer work](https://www.youtube.com/watch?v=0BocukaJJGo)
Channel: James Goldbach
