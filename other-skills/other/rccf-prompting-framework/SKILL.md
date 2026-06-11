---
name: rccf-prompting-framework
description: "Use when crafting any AI prompt to structure it with Role, Context, Command, and Format for dramatically better outputs."
---

# RCCF Prompting Framework

## Overview
A 4-part prompt structure (Role, Context, Command, Format) that consistently produces higher-quality AI outputs by giving the model a clear persona, rich background information, an explicit task, and the desired output structure.

## Key Techniques
- **Role**: Tell AI who to be ("Act as a world-class marketing strategist focused on SaaS conversion")
- **Context**: Supply all relevant background — documents, transcripts, specs, constraints
- **Command**: Be explicit and specific about exactly what you want the AI to do
- **Format**: Specify the output shape — bullet list, CSV, table, template, or provide a template to fill

## How to Apply
1. Open your prompt with a role assignment that focuses the model on the relevant domain
2. Paste in all relevant background context (transcripts, docs, briefs) — the more specific the better
3. State your command explicitly: what to create, analyze, or decide
4. End with format instructions: length, structure, template, file type

## Examples
- "Act as a world-class conversion copywriter. Here is my product brief: [paste]. Write 5 headline variants under 10 words each. Output as a numbered list."
- "Act as a senior Python engineer. Here is my codebase: [paste]. Refactor the auth module for security. Return only the modified file."

## Source
Extracted from: [You're not behind (yet): How to learn AI in 18 minutes](https://www.youtube.com/watch?v=0Tch0N5nsRU)
Channel: Dan Martell
