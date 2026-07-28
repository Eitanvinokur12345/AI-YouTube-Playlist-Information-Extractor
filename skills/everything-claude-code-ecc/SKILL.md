---
name: everything-claude-code-ecc
description: "Use when you want to upgrade a bare Claude Code setup into a full disciplined development system — structured workflows, delegated sub-agents, and security scanning — instead of ad-hoc prompting."
---

# Everything Claude Code (ECC)

## Overview
An agent-harness performance-optimization system by Anthropic Hackathon winner Affaan
Mustafa: a structured plan -> test -> implement -> review -> verify -> remember -> improve
workflow, delivered as specialized agents, reusable skills, a security scanner, and
cross-session memory.

## Key Techniques
- Follow the fixed pipeline (plan, test, implement, review, verify, remember, improve)
  instead of one-shot prompting.
- Delegate specific work to specialized agents (planning, code review, security analysis,
  language-specific development) rather than doing everything in one context.
- Run AgentShield to scan agent configurations for secrets exposure, permission issues, hook
  injection risk, and risky MCP server profiles before trusting a new setup.
- Keep rules (standards), skills (workflows), agents (delegated workers), and hooks
  (automated enforcement) conceptually separate.

## How to Apply
1. Install via the Claude Code plugin path (also works with Codex, Cursor, OpenCode, GitHub
   Copilot, and emerging harnesses).
2. Run AgentShield first to scan your existing agent configuration for risk before adopting
   the rest of the system.
3. Use the specialized agents for delegated work (planning, review, security, per-language dev).
4. Draw on the reusable skills for TDD, security review, documentation, and domain-specific
   patterns (backend, frontend, ML, data engineering) instead of writing new prompts each time.
5. Let cross-session memory build confidence-scored "instincts" over repeated use.

## Examples
Refined over 10 months of daily use by its creator before winning an Anthropic Hackathon,
then open-sourced (MIT) with 67 specialized agents and 281 reusable skills.

## Source
Extracted from: [Anthropic Hackathon Winner Leaked His Entire AI Coding Setup!](https://www.youtube.com/watch?v=nKsMeNgqI1U)
Channel: AI Made Easy
Repo: affaan-m/ECC (234k+ stars, MIT)
