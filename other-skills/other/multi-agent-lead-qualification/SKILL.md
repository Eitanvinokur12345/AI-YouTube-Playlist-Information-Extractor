---
name: multi-agent-lead-qualification
description: "Use when building an automated intake pipeline where leads need scoring, data enrichment, and personalized outreach all in sequence without human steps."
---

# Multi-Agent Lead Qualification Pipeline

## Overview
A three-agent coordination pattern that runs automatically on trigger events. Each agent handles one specialized job — qualifying, enriching, and drafting — then passes results to the next.

## Key Techniques
- Trigger-based agent activation (form submission fires the pipeline)
- Specialized agent roles: qualifier, data fetcher, outreach drafter
- Parallel CRM updates throughout the pipeline
- Human review at end rather than at each step

## How to Apply
1. Define a trigger event (e.g., form submission, new CRM entry).
2. Agent 1: Score and qualify the lead based on their answers/criteria.
3. Agent 2: Pull matching data from an external source (listings, inventory, records).
4. Agent 3: Draft a personalized message including the matched data.
5. Auto-update the CRM at each stage.
6. Deliver results to human inbox for final review/approval before sending.

## Examples
Real estate pipeline: new buyer lead fills form → Agent 1 scores fit/budget → Agent 2 pulls matching MLS listings → Agent 3 drafts personalized email with those listings → CRM updated → human wakes up to a ready-to-act lead.

## Source
Extracted from: [Level 3: An AI Agent Team](https://www.youtube.com/watch?v=3yTmnB_KnLM)
Channel: The Paperless Agent
