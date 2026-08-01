---
name: opencode-plan-build-workflow
description: "Use when exploring an unfamiliar codebase with OpenCode before making changes — start in the read-only 'plan' agent, then switch to the full-access 'build' agent once you're ready to edit."
---

# OpenCode Plan/Build Agent Workflow

## Overview
OpenCode is an open-source AI coding agent (terminal and desktop) that ships with two
built-in agents you switch between with the Tab key. This skill covers the safe pattern
of exploring first, editing second.

## Key Techniques
- Start in the **"plan"** agent: read-only, denies file edits by default, and asks
  permission before running bash commands — ideal for exploring unfamiliar codebases.
- Switch to the **"build"** agent (Tab key) once you understand the codebase and are
  ready to make full-access changes.
- Invoke the **"general"** subagent with `@general` for complex searches or multistep
  tasks that don't fit cleanly into plan/build.

## How to Apply
1. Open OpenCode in the target repository (CLI or desktop app).
2. Stay in the default read-only "plan" agent while you ask it to explain structure,
   locate relevant files, and outline a change — nothing gets edited yet.
3. When the plan looks right, press Tab to switch to the "build" agent and let it apply
   the edits, running bash commands as needed (now permitted).
4. For a broad or multi-step search across the codebase, mention `@general` instead of
   trying to do it manually in plan/build.

## Examples
- Exploring a new open-source repo you just cloned: ask "plan" to map out the module
  structure and propose where a bug fix belongs, then Tab into "build" to apply it.
- Debugging: use "plan" to read logs/tests read-only, confirm root cause, then switch to
  "build" only to write the fix.

## Source
Extracted from: [OpenCode: The Open Source AI Coding Agent for Your Terminal (and Desktop)](https://www.youtube.com/watch?v=sR6E9COyDaU)
Channel: Nico Decodes AI
Repository: https://github.com/anomalyco/opencode
