---
name: skillsmith-claude-skill-scaffolding
description: "Use when you need to rapidly build structured Claude Code skills — run /skillsmith to get a guided interview that scaffolds a complete skill directory with entry points, tasks, templates, frameworks, context files, checklists, and rules."
---

# SkillSmith Claude Skill Scaffolding

## Overview
SkillSmith is a Claude Code plugin that turns any idea into a properly structured skill in ~10 minutes using a guided interview-then-scaffold workflow. Each skill it creates is a named worker with its own tools, routing, and plain-text brain — making skills portable and installable across environments.

## Key Techniques
- Run `/skillsmith discover` for a guided interview that converts your idea into a skill specification
- Run `/skillsmith scaffold` to build a compliant skill directory from the specification
- Run `/skillsmith distill` to convert long-form videos or SOPs into framework components
- Run `/skillsmith audit` to review and improve existing skills over time
- Seven standardized file types per skill: entry point (skill.md), tasks, templates, frameworks, context files, checklists, rules

## How to Apply
1. Install: `npx @chrisai/skillsmith` (installs to `~/.claude/commands/skillsmith/`, available globally; use `--local` for project-specific)
2. In Claude Code, run `/skillsmith discover` — answer the interview questions about the skill you want
3. Run `/skillsmith scaffold` — SkillSmith generates the full directory structure
4. Review and customize the generated files, especially the entry `skill.md`
5. Reference the skill from your CLAUDE.md trunk file for progressive loading

## Examples
- Building a UGC Factory skill for social content creation in 10 minutes
- Converting an SOP document into a structured Claude Code skill via `/skillsmith distill`
- Creating 40+ skills across a workspace using repeated discover → scaffold cycles
- Integrating with Apify MCP for data layer or Hermes for autonomous skill running

## Source
Extracted from: [I Built 40+ Claude Skills With This 1 Simple Plugin](https://www.youtube.com/watch?v=splB_5Poawo)
Channel: Charlie Automates
Resources: https://charlieautomates.com/free-resources/#skillsmith
GitHub: https://github.com/ChristopherKahler/skillsmith
