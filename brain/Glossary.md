---
tags: [reference, glossary]
aliases: [Glossary, Terms]
---

# Glossary

One-line definitions of the project's terms. Follow a link for the full note.

- **Excavatortron** — the whole self-running, self-improving AI-playlist dashboard.
  See [[Excavatortron Brain]].
- **Skill** — a *technique* (something you DO). Lives in `skills.json` + `skills/<slug>/SKILL.md`.
  See [[Skills vs Tools]].
- **Tool** — a *product* (something that EXISTS). Lives in `tools.json`. See [[Skills vs Tools]].
- **Model** — a tool subset (an AI model w/ version) mirrored into `models.json`, ranked with a
  podium per category.
- **Connector / MCP server** — an integration Claude can use; tracked in `connectors.json`.
- **Ingest** — the high-frequency [[Pipeline - Analyze|analyze]] arm that adds new knowledge.
- **Deep pass** — the weekly [[Pipeline - Improve|improve]] curation run (+ first-week nightly).
- **Catch-up mode** — large newest-first batches drain a backlog after a surge, then auto-stop.
  See [[Cadence]].
- **Light mode** — during catch-up, improve does only safe modules + the self-check.
- **Idle early-exit** — a no-change improve run does only index + self-check + health + audit.
- **Self-check** — the 50-question [[Reference Self-Check]] → `self_check.json`.
- **Improvement task** — a logged `no` from the self-check, auto-fixed next run.
- **safe_auto / suggest_only** — operations applied automatically vs. proposed for approval.
- **Suggestion / approval** — risky change written to `improvement_suggestions.json`; the user
  approves ids in `approvals.json`.
- **Star / frozen** — a proven record locked from any auto-change. See [[Stars and Freezing]].
- **Dynamic tab** — a dashboard tab grown from recurring anecdotes. See [[Dynamic Tabs]].
- **Surroundings** — the non-transcript signals: description, links, stats, tags, duration,
  top comments. See [[Pipeline - Analyze]].
- **The surroundings rule** — extract everything the video *and its surroundings* offer,
  without ever editing the verbatim transcript. See [[Reference Spec]].
- **Three-agent review** — usability + cut-the-bullshit + deep-code-bugs, verified by a
  different engine. See [[Three-Agent Review]].
- **Frozen-slug set** — the set of slugs the engines must never modify (built each improve run).
