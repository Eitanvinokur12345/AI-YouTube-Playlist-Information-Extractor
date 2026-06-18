---
name: function-calling-structured-output
description: "Use AI function calling / tool use to force models to return schema-defined structured data directly consumable in code, replacing brittle text parsing."
---

# Function Calling for Structured AI Output

## Overview
Function calling (also called tool use) allows you to define a schema for the data you want and have the AI model fill in the values according to that schema. Instead of parsing freeform text responses, your application receives a properly typed, structured object it can use directly.

## Key Techniques
- Define function schemas that match your application's data models
- Use function calling instead of asking the model to "return JSON" in plain text
- Validate returned structured data against the schema before use
- Combine with JSON mode for maximum output reliability

## How to Apply
1. Define the function/tool schema with the exact fields and types your application needs.
2. Register the function with the AI API (Claude tool_use, OpenAI function_calling, Gemini tools).
3. Call the model with the function definition — instruct it to call the function with extracted/generated values.
4. Parse the tool_use block from the model's response to extract the structured arguments.
5. Validate the returned data against your schema.
6. Use the structured data directly in your application logic.

## Examples
- Extracting structured information from documents: define a function with fields like `{company: string, revenue: number, date: string}` and the model fills them from the document
- AI-powered form filling: define a schema matching your database model and let the AI populate it from freeform user input
- Content classification: define categories as an enum in the function schema and the model always returns one of the valid categories

## Source
Extracted from: [Prompt Engineering Skills Real AI Engineers Need](https://www.youtube.com/watch?v=_WwfE5feS8w)
Channel: Tech With Tim
