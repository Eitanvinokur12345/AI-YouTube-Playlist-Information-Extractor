---
name: prompt-contract-framework
description: "Use when writing prompts for AI agents to prevent off-rails execution — structure every agent prompt with Goal, Constraints, Format, and Failure sections."
---

# Prompt Contract Framework

## Overview
A four-section agent prompt structure that converts vague instructions into precise contracts. Unlike chatbot prompts that describe what you want, agent prompts must tell the agent what 'done' looks like, what it cannot do, what format to produce, and what to do when stuck.

## Key Techniques
- **Goal**: State the outcome with a clear finish line, not just an action
- **Constraints**: List everything the agent must NOT do (prevents disasters, grows over time as you learn)
- **Format**: Specify the exact shape/structure of the deliverable before the agent starts
- **Failure**: Instruct what to do when stuck — ask one question, stop and report, or flag an assumption

## How to Apply
1. Before writing a prompt, answer four questions: What does finished look like? What must not happen? What is the exact output shape? What should the agent do when stuck?
2. Write each section explicitly, even if brief.
3. Keep Constraints growing: after every agent mistake, add that mistake as a permanent constraint in future prompts.
4. Test the Format section by asking: "Can I describe this in one sentence?" If not, clarify first.

## Examples
Landing page agent contract:
- **Goal**: "Build a single-page landing site for my SaaS launch, optimized for email sign-ups above the fold, ready to review locally before deploying."
- **Constraints**: "Single index.html with inline CSS, no JS frameworks, no CDN scripts, light theme, mobile responsive, don't touch files outside /landing, don't deploy."
- **Format**: "landing/ folder with index.html + brief.md listing every section with the headline copy used."
- **Failure**: "If target audience or value prop is unclear, stop and ask one consolidated question rather than guessing."

## Source
Extracted from: [AI Agents Explained: How to Create and Use AI Agents in 2026](https://www.youtube.com/watch?v=4TvH-OZhwxI)
Channel: AI Master
