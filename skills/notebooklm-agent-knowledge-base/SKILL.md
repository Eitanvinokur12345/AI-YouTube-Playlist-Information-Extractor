---
name: notebooklm-agent-knowledge-base
description: "Use when setting up a knowledge base for AI agents — NotebookLM provides zero-setup document synthesis without RAG pipelines or vector DB configuration."
---

# NotebookLM as Zero-Setup Agent Knowledge Base

## Overview
Google NotebookLM is purpose-built for storing documents and letting AI synthesize across them — which is exactly what 99% of agent memory needs. Skip the RAG pipeline, the Supabase vector DB, the embeddings setup — upload your docs to NotebookLM and your agent has a working knowledge base immediately.

## Key Techniques
- **Direct document upload**: Upload PDFs, docs, notes directly to NotebookLM sources
- **Natural language retrieval**: Ask natural language questions and NotebookLM synthesizes across all uploaded sources
- **Multi-source synthesis**: Automatically finds connections across different documents in the same notebook

## How to Apply
1. Create a new notebook in NotebookLM (notebooklm.google.com)
2. Upload your agent's knowledge sources: PDFs, Google Docs, web pages, text files
3. Test retrieval by asking cross-document questions
4. Give your agent access to the NotebookLM notebook for knowledge retrieval
5. For Claude Code: add the NotebookLM URL to your agent's resource list

## Examples
- Documentation agent: Upload all product docs → agent queries NotebookLM for accurate answers
- Research agent: Upload 20 research papers → NotebookLM synthesizes findings across them
- Support agent: Upload FAQ + knowledge base articles → NotebookLM retrieves relevant answers
- Code agent: Upload architecture docs + style guides → agent references them during builds

## Source
Extracted from: [Easiest vector-DB knowledge base: NotebookLM](https://www.youtube.com/watch?v=yPMpOpy0Yhs)
Channel: James Goldbach
