---
name: modular-rule-definition-ai-agents
description: "Providing structured and manageable guidelines to AI agents, allowing for dynamic loading of relevant rules based on the current task or file path."
---

# Modular Rule Definition for AI Agents

## Overview
Capability to break down complex instructions and guidelines into smaller, concern-specific rule files (e.g., code style, testing standards, API conventions) for an AI agent.

**Use case:** Providing structured and manageable guidelines to AI agents, allowing for dynamic loading of relevant rules based on the current task or file path.

## Key steps
1. Split rules by concern (e.g., code style, testing, API patterns) into separate files within a 'rules/' folder.
2. Utilize file path scoping to ensure Claude only loads relevant rules for the specific files or folders it's working on.

## Details
- **Category:** agents
- **Tool:** claude  ·  **Quality:** 5/10

## Source
Extracted from: https://www.youtube.com/watch?v=JvOvObgaQlU
