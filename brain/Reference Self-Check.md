---
tags: [system, self-check, quality, reference-spec]
aliases: [Reference Self-Check, Self-Check, 50 Questions]
---

# Reference Self-Check (the 50 questions)

The promise the owner cares about most: **every deep pass returns to the original reference
spec and checks it is all still there.** The spec is preserved verbatim in
`docs/REFERENCE_SPEC.md` (see [[Engines]] and the [[Reference Spec]]); Part C is the
**50 yes/no questions**, each annotated with the cloud file/field that proves it.

## The loop
1. **Answer** — [[Pipeline - Improve]] Step 7c re-answers all 50 against live data and writes
   `data/self_check.json`:
   `{ ran_at, score, total, improvements_logged, results:[{n, question, answer, evidence}] }`.
2. **Log gaps** — every `no` opens a task in `data/improvement_tasks.json`:
   `{ n, question, fix, kind, status, created_at }` where `kind` ∈
   `safe_auto` (a module fixes it) · `needs_approval` (write a suggestion) ·
   `engine_followup` (needs a CLAUDE.md/config change).
3. **Auto-fix next run** — Step 1b reads the open tasks and applies the `safe_auto` ones,
   turns `needs_approval` into suggestions, and notes `engine_followup` ones. Fixed questions
   are marked `status:"fixed"`. The loop closes: **no → task → fixed → re-verified.**
4. **Surface** — the dashboard shows `Self-check score: X/50 — Y improvements logged`.

## Always runs
Step 7c executes on **every** improve invocation — full pass, catch-up light mode, and idle
days — so `self_check.json` is never left empty. (This was the bug behind an early empty file;
fixed in `IMPROVE.md`.)

## Latest snapshot
Seeded at **45/50** with 5 open tasks: vague tool versions (Q10), a skill missing a tip
(Q12), 19 techniques missing `SKILL.md` (Q16), the improve deep pass not yet completing (Q21),
and an off-list general-tip topic (Q27). See [[Self-Improvement Loop]].
