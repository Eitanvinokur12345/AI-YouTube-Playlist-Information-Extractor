---
name: send-to-user-tool-pattern
description: "Use when building long async Claude Fable 5 agents that need to surface verbatim content (deliverables, progress updates) to the user mid-task without ending the agent's turn."
---

# send_to_user Tool Pattern for Long Agents

## Overview
In long async agent runs, Claude Fable 5 summarizes its own narration — meaning critical content (deliverables, specific numbers, direct replies) can be paraphrased or lost before reaching the user. Adding a client-side send_to_user tool bypasses this: tool inputs are never summarized, so content arrives verbatim. The agent calls it mid-task without ending its turn.

## Key Techniques
- Tool inputs bypass the model's summarization — content arrives exactly as written
- The tool takes a single 'message' string input and returns a simple acknowledgement
- Requires both: (1) the tool definition and (2) a system prompt elicitation
- Use only for user-facing content — not narration or internal reasoning

## How to Apply

1. Define the tool in your API call:
```json
{
  "name": "send_to_user",
  "description": "Display a message directly to the user. Use for progress updates, partial results, or content the user must see exactly as written before the task finishes.",
  "input_schema": {
    "type": "object",
    "properties": {
      "message": {"type": "string", "description": "The content to display to the user."}
    },
    "required": ["message"]
  }
}
```

2. In your system prompt, add:
```
Between tool calls, when you have content the user must read verbatim (a partial deliverable,
a direct answer to their question), call the send_to_user tool with that content. Use
send_to_user only for user-facing content, not for narration or reasoning.
```

3. In your UI, when the model calls send_to_user, render the input['message'] directly and return {"result": "displayed"} as the tool result.

## Examples
- Generated code snippet: call send_to_user with the exact code
- "Here are the 3 files changed: [list]" — send verbatim
- Direct answer to a question asked mid-loop — send verbatim
- "I'm now running the tests..." — do NOT send (narration only)

## Source
Extracted from: [Before You Use Claude Fable 5, Watch This](https://www.youtube.com/watch?v=L2IBm6PZBDo)
Channel: GundeepAi
Official guide: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
