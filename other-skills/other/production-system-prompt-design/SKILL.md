---
name: production-system-prompt-design
description: "Write system prompts that reliably constrain AI model behavior in production codebases — not just chat, but consistent, predictable output at scale."
---

# Production System Prompt Design

## Overview
Getting reliable output from AI models in production is fundamentally different from getting decent chat responses. This skill covers writing system prompts that genuinely constrain model behavior so outputs are consistent and predictable every single time, across all requests.

## Key Techniques
- Constrain model behavior explicitly — don't just describe what you want, restrict what the model cannot do
- Include output format requirements directly in the system prompt
- Test system prompts against adversarial and edge-case inputs before deploying
- Version control your system prompts like code

## How to Apply
1. Identify the exact output format and behavioral constraints your production system needs.
2. Write the system prompt to explicitly prohibit unwanted behaviors (not just encourage wanted ones).
3. Specify the output format in the system prompt (JSON schema, list format, etc.).
4. Test with a diverse set of inputs including adversarial cases.
5. Version control the prompt and review changes as you would code changes.
6. Monitor production outputs for drift and update the prompt when needed.

## Examples
- A customer support bot system prompt that explicitly prohibits discussing competitors, pricing beyond a set range, or making promises
- A data extraction prompt that constrains the model to only return values present in the input, never to invent data
- A code review assistant that is constrained to output only in a specific structured format

## Source
Extracted from: [Prompt Engineering Skills Real AI Engineers Need](https://www.youtube.com/watch?v=_WwfE5feS8w)
Channel: Tech With Tim
