---
name: ponytail-pre-build-reasoning
description: "Use before any Claude Code build task to force the agent to ask 'should we build this at all?' — applies a lazy senior developer decision tree to eliminate unnecessary code."
---

# Ponytail Pre-Build Reasoning Gate

## Overview
Ponytail is an open-source Claude Code plugin (7.5k GitHub stars) that makes AI agents adopt a "lazy senior developer" philosophy before writing any code. The best code is the code you never wrote — Ponytail enforces this as a first-class gate.

## Key Techniques
- **YAGNI gate**: "Does this need to exist?" — if not, skip it entirely
- **Standard library check**: Can the language's stdlib handle this without a new dependency?
- **Platform feature check**: Is there a native OS/framework feature that already does this?
- **Existing dependency check**: Is there a package already installed that solves this?
- **One-liner check**: Can this be a single expression instead of a function?
- **Minimal code fallback**: Only if all above fail, write the smallest working implementation

## How to Apply
Install Ponytail in Claude Code:
```
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```

Once installed, every time Claude Code is about to write code, it runs through the decision tree above before generating anything.

## Examples
- Request: "Add a function to format currency" → Ponytail: "Does this need to exist? → Check: `Intl.NumberFormat` in JS stdlib handles this in one line" → Returns a one-liner instead of a utility function
- Request: "Add date parsing" → Ponytail: "Is there a platform feature? → Check: `Date.parse()` already exists" → Uses native instead of adding a dependency
- Request: "Build user authentication" → Ponytail: "Is there an installed dependency? → Check: Auth library already in package.json" → Wires up existing auth instead of building from scratch

## Source
Extracted from: [Ponytail: a Claude Code skill that asks "should we build this at all?"](https://www.youtube.com/watch?v=bMfUtbD-EDU)
GitHub: https://github.com/DietrichGebert/ponytail
Channel: Github Awesome
