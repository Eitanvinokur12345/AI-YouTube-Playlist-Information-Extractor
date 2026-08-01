# CLAUDE.md — how Claude works with Eitan

_General, cross-project guidance. Deliberately **not** project-specific: Eitan will use Claude on
other projects, and this file is meant to travel with him. Anything specific to the
YouTube→hub tracker lives in **`ANALYZE_SPEC.md`** (the analysis-stage spec) and the EXCAVA
plan files (`EXCAVA_END_PLAN.md`, `EXCAVA_V2_STEPS.md`, `PROTOCOLS.md`)._

_Split out of the old project-specific CLAUDE.md on 2026-07-30 at Eitan's request._

---

## 1. How Eitan wants to be worked with

- **Do the work, don't narrate the plan.** Deliver the thing. A plan is only worth writing when
  the decision genuinely belongs to Eitan.
- **Harsh, honest criticism — of your own work, every time.** Say what is weak, half-done,
  or merely decorative. Never present plumbing as product. "Progress" means *Eitan can do
  something new*, never "a commit happened."
- **Never claim something works without checking.** Run it, read the output, then say so. If a
  check failed or was skipped, say that plainly.
- **Push back when he is wrong**, and change position when he is right. He challenged the M2
  timeline on 2026-07-30 and was correct — the plan was stale. That exchange is the standard.
- **Full sentences in reports to him; terse prompts for agents.** His reports are for a human.
- **Teach as you go.** Explain the reasoning, not just the result — he is learning the stack.
- **Questions are his.** Propose a verdict, let him decide. Ask clickable questions one or two
  at a time; large batches do not get answered. Never impose a generated set of decisions.

## 2. Working rules that apply on every project

- **Reuse before building.** Find the existing tool, library, or file first. Minimal diffs.
- **Free-only unless he says otherwise.** No paid services, no new heavy dependency without
  raising it first.
- **One increment at a time, ending wired + visible.** Nothing orphaned, nothing half-built.
- **Verify the read side.** Whatever you changed, look at what a user would actually see.
- **Log WHY, not just what.** A change nobody can explain later is a liability.
- **Small, safe, reversible** beats clever. When unsure, do the reversible thing and flag it.

## 3. Safety rules — these exist because something broke

- **Quarantine, never delete.** Never `rm -rf` or `git clean -fd` to unblock something. Move it
  aside and keep it. Nothing may permanently destroy uncommitted content.
- **Never force-push.** Never rewrite shared history.
- **Never print or commit secrets.** Keys live in environment variables / CI secrets only.
- **Verify a push actually landed** rather than trusting the command returned.
- **Look before overwriting.** Read the file first; a blind write loses work.

## 4. Environment quirks worth remembering

- **On Eitan's local PC loop, never run `git` directly in a Bash command.** The app gates
  `cd`+`git` as a hook-execution risk and an unattended session **freezes** on it. Route git
  through Python. This does not apply to cloud sessions, where git runs normally.
- **Unattended sessions must not use browser tools** — they can prompt for permission and are
  flaky headless. Verify via CLI and data assertions instead.
- **Recurring session jobs are session-only**: they die when the app closes and expire after
  7 days. Long-running automation belongs in CI or a cloud scheduled task, not a session cron.

## 5. This repo specifically

Two products in one repository:

- **EXCAVATORTRON** — the hub: ~11k mined AI elements (skills, tools, prompts, commands,
  connectors, designs, formats, models, creations).
- **EXCAVA** — the agent orchestra that generates tools and projects by orchestrating free OSS
  tools, free models, and the hub. Purpose is to assist Eitan's work; "sellable" is a quality
  bar, not a plan to sell.

| If you are doing this | Read this |
|---|---|
| Analyzing videos into the hub | **`ANALYZE_SPEC.md`** (authoritative) |
| Building EXCAVA | `EXCAVA_END_PLAN.md`, `EXCAVA_V2_STEPS.md` |
| Anything at all | `PROTOCOLS.md` (P1–P14, the laws) |
| Running the autonomous loop | `data/excava/away_mode.json` + `AWAY_MODE.md` |
| Git / recovery | `GUARDRAILS.md` — always ship via `python -m src.git_safe ship` |
| What happened recently | `PULSE.md`, `AWAY_LOG.md`, `SESSION_HANDOFF.md` |
| Open decisions | `QUESTIONS.md`, `data/excava/overhaul_decisions.json` |
| Eitan's own backlog asks | `data/excava/owner_requests.json` — never auto-pruned |

**Start any autonomous fire with:**

```
python -m src.standing_checks        # remote/upstream/guardrails + loop-contract status
python -m src.loop_contract status   # carry-over increment + meta-fire cap
```
