---
name: react-rag-agent-architecture
description: "Use when building an AI agent that needs to reason step-by-step, retrieve external knowledge, and take real actions — the foundational ReAct + RAG architecture pattern."
---

# ReAct + RAG Agent Architecture

## Overview
The combination of ReAct (Reasoning + Acting) and RAG (Retrieval-Augmented Generation) forms the foundational architecture for true AI agents. ReAct structures agent reasoning as alternating Thought/Action cycles; RAG ensures the agent retrieves relevant up-to-date context rather than relying purely on its training.

## Key Techniques
- **ReAct loop**: Thought → Action → Observation → Thought → Action... until the task is complete
- **RAG retrieval**: Before generating, retrieve semantically relevant documents/data from a knowledge store
- **Tool routing**: Agent dynamically decides which tool to call based on reasoning — unlike a fixed workflow

## How to Apply
1. Define your agent's available tools (search, calculator, code runner, database, etc.)
2. Set up a vector store or knowledge base for RAG retrieval
3. Use a system prompt that instructs the model to alternate between Thought and Action steps
4. On each Action step, execute the tool and feed the result back as an Observation
5. Continue until the model produces a final Answer

## Examples
- Customer support agent: retrieves product docs via RAG, then calls order-status API via ReAct
- Research agent: retrieves recent papers, reasons about them, then runs data analysis tools
- Coding agent: retrieves project context, reasons about the bug, edits files, runs tests

## Source
Extracted from: [AI Agents, Clearly Explained](https://www.youtube.com/watch?v=FwOTs4UxQS4)
Channel: Jeff Su
