---
name: task-observer
description: "Use when you want your skill library to keep improving on its own — Task Observer watches work sessions for corrections and repeating patterns and suggests new or improved skills."
---

# Task Observer

## Overview
A meta-skill that monitors an agent's work sessions to automatically identify corrections,
gaps, and repeating patterns, then generates structured recommendations for new or improved
skills, for human review before implementation.

## Key Techniques
- Capture work-session observations rather than requiring manual note-taking.
- Detect repeating correction patterns as signal for a missing or weak skill.
- Track cross-cutting principles across an entire skill library, not just one skill at a time.
- Produce a structured, reviewable log instead of silently auto-modifying skills.

## How to Apply
1. Download the repo and place `SKILL.md` plus its `references/` folder together.
2. For Claude Code: place at `.claude/skills/task-observer/`. For Claude.ai (web/mobile/
   desktop): upload via Settings -> Capabilities.
3. Let it run alongside normal work sessions.
4. Periodically review its generated observation logs and decide which suggested skill
   changes to actually implement.

## Examples
Recommended as one of "5 Claude skills you need," positioned as the skill that keeps the
other four (and any future ones) improving based on real usage instead of guesswork.

## Source
Extracted from: [5 Claude skills you need](https://www.youtube.com/watch?v=W1_hQoDYVXU)
Channel: TheCyborgGirl
Repo: rebelytics/one-skill-to-rule-them-all (1.3k stars)
