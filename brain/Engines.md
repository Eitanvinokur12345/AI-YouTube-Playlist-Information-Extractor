---
tags: [architecture, engines, spec]
---

# Engines

The "brains" of each Claude-driven stage are **Markdown spec files** at the repo
root. The GitHub Action passes the file to `claude-code-action`, and Claude follows
it exactly. These files — not the Python in `src/` — are what actually run the
analysis, curation, and review.

| File | Stage | Governs |
|------|-------|---------|
| `CLAUDE.md` | [[Pipeline - Analyze]] | How to read each video and extract every section. |
| `IMPROVE.md` | [[Pipeline - Improve]] | The weekly deep pass: tidy, calibrate, self-check, dynamic tabs. |
| `REVIEW.md` | [[Pipeline - Review]] | The 3-agent quality gate (Claude-first). |
| `REFERENCE_SPEC.md` | (read by improve) | The user's original "System Prompt" spec + the 50 self-check questions. |

Each engine is **governed by a block in `config.json`** (see [[Config Reference]]),
so behavior can be tuned without rewriting the spec.

## `CLAUDE.md` — the analyze engine
Defines the per-video flow: relevance gate → video-quality review (Step 2b) →
follow AI-relevant description links with WebFetch (Step 2c) → extract into the
right sections, keeping [[Skills vs Tools|skills and tools separate]] → capture
off-tab anecdotes to `data/tab_candidates.json` for [[Dynamic Tabs]] → move the
file to `data/processed` → commit **and push** before the next video.

## `IMPROVE.md` — the deep-pass engine
Modules for dedup, schema repair, ratings calibration (suggest-only), starring the
best ([[Stars and Freezing]]), a dashboard/UX review, **skills-folder learning**
(reads `./skills` + `./other-skills`), [[Dynamic Tabs|dynamic-tab discovery]], the
[[Reference Self-Check]] (Module 9), token optimization, and a health report. It
**auto-applies only "safe" operations**; risky ones become suggestions to approve.

## `REVIEW.md` — the review engine
Three reviewers across three dimensions (usability vs competitors, "cut the
bullshit", deep code bugs). Claude runs first and writes `data/review_findings.json`;
then a **different external engine** verifies. See [[Three-Agent Review]].

## `REFERENCE_SPEC.md` — the source of truth for "are we still on-spec?"
Part A preserves the user's original system prompt verbatim. Part B maps it to the
cloud architecture (what changed and why). Part C lists the **50 questions** the
[[Reference Self-Check]] re-answers every run.

## Related
- [[Architecture]] · [[Self-Improvement Loop]] · [[Cadence]]
