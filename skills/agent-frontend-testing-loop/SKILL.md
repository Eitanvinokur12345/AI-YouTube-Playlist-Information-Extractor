---
name: agent-frontend-testing-loop
description: "Use when building agent-driven frontend code that needs to catch runtime errors, CORS issues, auth problems, and DOM rendering bugs automatically during development — pair Chrome DevTools MCP with Playwright MCP for a full test-and-inspect loop."
---

# Agent Frontend Testing Loop with Chrome DevTools MCP + Playwright MCP

## Overview
Combines Chrome DevTools MCP (browser inspection) with Playwright MCP (browser navigation) to give AI coding agents complete visibility into what the browser is actually doing. The agent can drive the browser through user flows while simultaneously reading every error, failed request, and rendering issue.

## Key Techniques
- Chrome DevTools MCP reads console logs, runtime errors, stack traces, hydration issues, failed API calls, bad auth headers, CORS errors, and missing assets
- DOM inspection reveals what actually rendered, not just what React/Vue tried to render
- Session/auth inspection: check session cookies, auth state, local storage, and session storage
- Playwright MCP drives browser navigation and interaction during testing
- Combine both: agent navigates with Playwright and inspects every code-relevant error with Chrome DevTools in a closed loop

## How to Apply
1. Install Chrome DevTools MCP and Playwright MCP (both as MCP servers in your Claude config).
2. Give the agent a frontend task (build feature, fix bug, etc.).
3. Agent writes/edits code, then uses Playwright MCP to navigate to the relevant page.
4. Agent uses Chrome DevTools MCP to inspect the browser state: console, network, DOM, auth.
5. Agent reads errors and iterates until all issues are resolved — no manual DevTools required.

## Examples
- Agent builds a React auth flow, navigates via Playwright, then reads Chrome DevTools for auth header errors and cookie state.
- Agent identifies a hydration mismatch by inspecting what actually rendered vs what SSR produced.
- Agent catches CORS errors from failed API calls without needing the developer to open DevTools manually.

## Source
Extracted from: [Chrome DevTools MCP = X-ray vision for frontend](https://www.youtube.com/watch?v=04hSAwPx4E0)
Channel: James Goldbach
