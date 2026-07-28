---
name: ai-model-fingerprinting
description: "Identifying the specific AI model being used when interacting through an abstracted application (e.g., Copilot, Slack) or an API aggregator."
---

# AI Model Fingerprinting

## Overview
A technique to identify the underlying AI model by analyzing its 'random' outputs, leveraging the fact that LLMs are word prediction engines and have statistical favorites for seemingly random requests.

**Use case:** Identifying the specific AI model being used when interacting through an abstracted application (e.g., Copilot, Slack) or an API aggregator.

## Key steps
1. Ask for a random number between 1 and 100 multiple times.
2. Ask for a random color.
3. Ask for a random animal.
4. Compare the statistical distribution of answers to known model fingerprints.

## Details
- **Category:** research
- **Tool:** various LLMs  ·  **Quality:** 5/10

## Source
Extracted from: https://www.youtube.com/watch?v=D6cBsAWwCd0
