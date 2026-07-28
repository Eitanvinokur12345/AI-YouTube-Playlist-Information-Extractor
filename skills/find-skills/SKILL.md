---
name: find-skills
description: "Use when a user asks 'how do I do X' or 'find a skill for X' — search the open agent-skills ecosystem and install a matching skill instead of building one from scratch."
---

# Find Skills

## Overview
A Claude Code skill (from Vercel Labs) that discovers and installs other agent skills from
the open skills.sh ecosystem via the Skills CLI, so you don't rebuild functionality that
already exists as an installable skill.

## Key Techniques
- Recognize when a request maps to "a skill for X" rather than a one-off task.
- Check the skills.sh leaderboard for well-regarded options before searching blind.
- Verify a candidate skill's quality before installing it.

## How to Apply
1. When you need functionality that might already exist as a skill, run `npx skills find [query]`.
2. Check results against the skills.sh leaderboard for popularity/quality signal.
3. Install the chosen skill with `npx skills add`.
4. Fall back to building a custom skill only if nothing suitable is found.

## Examples
Used as the entry point in a "5 Claude skills you need" roundup, where it's positioned as the
tool you reach for before installing any of the other four skills manually.

## Source
Extracted from: [5 Claude skills you need](https://www.youtube.com/watch?v=W1_hQoDYVXU)
Channel: TheCyborgGirl
Repo: vercel-labs/skills
