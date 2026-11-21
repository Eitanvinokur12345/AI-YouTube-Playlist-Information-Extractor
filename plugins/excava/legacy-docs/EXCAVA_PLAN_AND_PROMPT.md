# EXCAVA — Plan & Loop Prompt (paste into a fresh session) — 2026-07-15

## What EXCAVA is (canonical, corrected by Eitan)
**EXCAVATORTRON = the HUB** — mined AI knowledge + ~8,311 elements incl. ~1,883 free open-source GitHub repos, Chinese tools, free utilities. **EXCAVA = an AGENT ORCHESTRA that GENERATES tools/projects** from Eitan's parameters by **orchestrating OTHER free/existing tools** (OpenCode / Claude Code on his existing Claude Pro = frontier quality at zero marginal cost) and **integrating the free OSS in the hub**. **Purpose: GENERATE projects/tools and assist Eitan's work — NOT to be sold** ("sellable quality" is only the excellence bar). **Ultimate goal: every component integrates perfectly.**

## The reality this starts from (measured 2026-07-15 — do not repeat the past mistake of ignoring it)
- **97 Python modules, ~30 wired into the beat, 21 referenced by nothing (dead).**
- **The HUB is a card catalog, not a toolbox:** 8,311 elements, 61% with links, but only **16% enriched, 25% stubs, and 0.8% (68) with real run/install info.** "100% verified" is a facade flag.
- **The memory brain is fragmented:** 3 separate graph files + memory_index, 2 graph modules orphaned; memory + history (663KB) + requests (82KB) live in separate silos, never joined.
- **Diagnosis: this is an INTEGRATION + CAPTURE problem, not a building problem.** Things are mined-but-unusable and built-but-orphaned. Stop building new; connect and complete what exists.

## THE PLAN (integration-first; run it on the loop below)
**Phase 0 — ONE BRAIN.** Merge memory + history + requests + the 3 fragmented graphs into ONE queryable brain, and WIRE it so agents read it at every decision (not just store it). Deliver a visible in-app view of it. *(No owner input needed.)*
**Phase 1 — USABLE HUB.** Remove the "100% verified" facade. Enrich a curated set (~25–50 highest-quality mined OSS repos) with REAL run/install info so they are actually runnable; surface "usable vs stub" honestly in-app. *(No owner input needed.)*
**Phase 2 — ASSISTIVE GENERATOR.** The orchestra takes Eitan's parameters + the brain + the usable tools and scaffolds ONE real tool/project, assist-first, visible as it works. *(Needs a real always-on HOST: the free Oracle VPS or Eitan's PC — an orchestra running OpenCode/Claude Code cannot live on GitHub Actions.)*
**Phase 3+ — EXPAND from the backlog** (the 99-item audit in `EXCAVA_MASTER_AUDIT.md` is the sorted backlog; pull ONE wired+visible piece per loop).

## The loop protocol (each iteration)
1. Standing checks: git pull (quarantine-never-delete), engine canary, regression.
2. Advance the CURRENT phase by exactly ONE increment that ends **wired + visible** (runs in the beat AND shows in the cockpit). Never start a second thing before the first is visible.
3. Verify the READ side in a browser (a number/screenshot) — never claim done from input alone.
4. Log WHY; ship ONLY via `python -m src.git_safe ship`.
5. Report with harsh 100% criticism of BOTH Claude and Eitan.
**Progress is measured as "Eitan can do something new this week," never "a commit happened."**

## DECONSTRUCTION MANDATE (Eitan's order — do NOT be a yes-man)
Challenge his assumptions out loud, every step, with evidence. Keep re-raising: (a) "integrate countless tools" vs "everything fits perfectly" are in tension — force a small deeply-integrated set first; (b) "generate pro tools" is autonomous software generation, the hardest unsolved AI problem — insist assist-first; (c) "free/pro-grade via OSS" needs enrichment first (0.8% of the hub is runnable today); (d) "free" also leans on his Claude Pro sub + a real host. If evidence contradicts a preconception of his, say so plainly and show the number.

## Laws that hold
Free (via OSS + his existing Pro, never per-token billing). Everything operable IN THE APP (he doesn't use GitHub). Real-not-facade. Ship only via git_safe; quarantine-never-delete. Recall-before-change + log WHY. Teach as you go — Eitan wants to understand, not just receive. The old law "fulfill EVERY request before anything new" is RETIRED → "one core, integrated and visible, then expand from the backlog."

## What Eitan provides
Nothing to start (Phases 0–1 are pure integration of existing data). The ONE dependency is a **real always-on host (Oracle VPS or his PC)**, needed only at **Phase 2**. Optionally he can pick which OSS tools to enrich first, or approve a shortlist ranked by quality_score.

## First move for the fresh session
Give the management verdict → run the STEP-0 module inventory (tag 97 modules wired/orphaned, delete the 21 dead) → begin Phase 0 (One Brain), one wired+visible increment → verify in browser → ship → criticize both. Then loop.
