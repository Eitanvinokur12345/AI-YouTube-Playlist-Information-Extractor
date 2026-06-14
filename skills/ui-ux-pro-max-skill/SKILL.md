---
name: ui-ux-pro-max-skill
description: "Use when building UI/UX interfaces in Claude Code and needing professional design intelligence — 161 reasoning rules, 67 UI styles, and stack-specific guidelines for React, Next.js, Vue, Flutter and more."
---

# UI UX Pro Max Design Intelligence Skill

## Overview
UI UX Pro Max is a Claude Code skill package that injects professional design intelligence into your AI coding workflow. It provides searchable databases of UI styles, color palettes, font pairings, chart types, and UX guidelines across 13+ frameworks and stacks.

## Key Techniques
- Search UI styles with domain flags: `--domain style/typography/color/landing/chart/ux`
- Target specific tech stacks: `--stack react/nextjs/tailwind/vue/flutter/shadcn/swiftui`
- Use the v2.0 Design System Generator to produce complete branded design systems from project descriptions
- Access 161 AI reasoning rules and 67 UI styles for consistent design decisions

## How to Apply
1. Install via npm CLI: `npx uipro-cli` or integrate the CLAUDE.md into your project
2. Use the search script: `python3 src/ui-ux-pro-max/scripts/search.py "<query>" --domain <domain>`
3. Specify your stack for framework-specific output: `--stack react` or `--stack nextjs`
4. For a complete design system: use the Design System Generator with your project name and target audience
5. Claude Code reads the installed skill's CLAUDE.md automatically for design intelligence context

## Examples
- "SaaS dashboard" → product type, color palettes, typography, and component layout recommendations
- "glassmorphism" → style definition, CSS keywords, Tailwind classes, and AI generation prompts
- "Serenity Spa" → complete custom design system with brand colors, fonts, and UI style rationale
- Stack-specific: `--stack swiftui` returns SwiftUI-native component patterns and Apple HIG guidelines

## Source
Extracted from: [Build Stunning Websites with Claude Code](https://www.youtube.com/watch?v=VDtJbeWlXEk)
Channel: Ben Kimball Ai
Resource: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (91k+ GitHub stars)
