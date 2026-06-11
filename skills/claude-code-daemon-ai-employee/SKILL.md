---
name: claude-code-daemon-ai-employee
description: "Use when you want Claude Code agents to work 24/7 — managing sessions, processing tasks, optimizing skills overnight, and reporting via Telegram or Slack."
---

# Claude Code 24/7 Daemon + AI Employee Setup

## Overview
A system daemon architecture that manages multiple Claude Code and Codex sessions automatically — spinning them up and down as needed, connecting them to messaging apps for remote control, and running overnight skill optimization loops that improve agent quality from daily experience.

## Key Techniques
- System service manages Claude Code session lifecycle (start/stop/monitor)
- Telegram or Slack integration for remote task assignment and status updates
- Overnight skill optimization: process transcripts → extract failures → update CLAUDE.md/skills
- Shared observability logs for auditing agent work quality
- Scheduled workflows for GitHub scraping, PR review, trending repo testing

## How to Apply
1. Write a system daemon (systemd service, launchd plist, or similar) that manages Claude Code processes
2. Connect sessions to Telegram bot or Slack webhook for remote messaging
3. Set up an overnight cron that reads the day's session transcripts and extracts learnings
4. Have the optimization loop update the shared knowledge base and relevant SKILL.md files
5. Add observability logging so every agent action and output is auditable
6. Configure PR review, GitHub scraping, and package testing as scheduled overnight jobs

## Examples
- Evening: Telegram message "review all open PRs" → daemon spawns session → reviews 12 PRs → posts summaries → shuts down
- Overnight: transcript optimizer runs, finds 3 recurring Claude errors, updates skills to avoid them, updates shared knowledge base
- Continuous: a GitHub trending scraper runs hourly, tests new AI tools against your stack, notifies via Telegram if useful

## Source
Extracted from: [The 5 levels of Claude Code mastery](https://www.youtube.com/watch?v=1ZlkHLx37V0)
Channel: James Goldbach
