---
name: chrome-devtools-mcp-frontend-testing
description: "Use when building or debugging frontend apps with Claude Code to create an autonomous testing loop that navigates the app and inspects every browser error simultaneously."
---

# Chrome DevTools MCP + Playwright MCP Agentic Frontend Testing Loop

## Overview
This technique pairs two MCP servers — Chrome DevTools MCP for browser inspection and Playwright MCP for browser control — so Claude Code can both navigate the app and read every runtime error without human intervention. The result is a closed-loop agentic testing workflow where the agent acts and diagnoses at the same time.

## Key Techniques
- **Chrome DevTools MCP** reads console logs, stack traces, hydration issues, failed API calls, CORS errors, DOM state, auth headers, and local/session storage.
- **Playwright MCP** navigates the browser, clicks elements, fills forms, and triggers state changes.
- **Combined loop**: Playwright acts → DevTools reads errors → agent diagnoses and fixes → repeat.

## How to Apply
1. Install Chrome DevTools MCP and Playwright MCP in Claude Code's MCP config.
2. Give Claude Code a frontend task (e.g., "test the login flow and fix any errors").
3. Claude uses Playwright to navigate to the page and interact with it.
4. Simultaneously, Claude uses Chrome DevTools MCP to read console logs, check failed API calls, and inspect DOM state.
5. Any errors found are diagnosed and fixed in the same agentic session without switching to manual browser inspection.

## Examples
- Agent navigates to a React app, Playwright detects a blank screen, DevTools MCP reveals a hydration mismatch in console — agent fixes the SSR/CSR inconsistency.
- Agent uses Playwright to log in, DevTools MCP finds an incorrect auth header in the network tab — agent corrects the API call.
- Agent checks local storage state after a form submission to validate persistence.

## Source
Extracted from: [Chrome DevTools MCP = X-ray vision for frontend](https://www.youtube.com/watch?v=04hSAwPx4E0)
Channel: James Goldbach
