# SESSION HANDOFF — start here (new-session continuation format)

_Everything a fresh session needs to continue Excavatortron/EXCAVA with zero context loss.
Last updated: 2026-07-02. Keep this current at the end of every working session._

## 0. FIRST ACTIONS (do before anything)
1. **PROJECT MEMORY MASTER (Phase 0.7, owner law):** before touching ANYTHING run
   `python -m src.project_memory recall "<topic>"` and start from it; after meaningful changes
   `python -m src.project_memory log --what ... --why ...`. Full contract: `PROJECT_MEMORY.md`.
2. **Load memory** (re-read specifically): `project_excavatortron`, `project-excava-makeit-work`, `project-excava-roadmap`, `project-excava-direction-loop` (⚠ missed once before), `feedback-fable-workflow`, `feedback-nosg`, `feedback-ship-visible-progress`, `feedback-consistency-check`.
3. **Read the plan**: `EXCAVA_PROGRAM.md` (now phases 0–9 incl. 0.7 memory-master + 9 omni-source), `PLAN.md` (P/F history), `QUESTIONS.md` (open, non-blocking).
4. **Run the consistency check** (§6) and keep running it after every task.
5. **Decisions:** D1 ✅ cron heartbeat · D2 ✅ direction-loop + change-tutorials, DAEMON-GRADE integration (see QUESTIONS #18/#25) · D3–D5 on defaults · D6 (locked social feeds) default no.

## 0b. SHIPPED 2026-07-03 (second arc): 0.7 + 5 + 9-tier-1, dashboard v64
- **Phase 0.7 memory master**: `src/project_memory.py` + `data/project_memory/` + root
  `PROJECT_MEMORY.md`; auto-ingests commits+bus traces every beat; `recall`/`log` CLI; rollup at 90d.
- **Phase 5 living OS (v64)**: fleet-health card (11 depts, real counters, cooldowns), live bus
  queue with per-task TRACE VIEWER (real "chose X over Y" routing), 📡 OS-events daemon feed,
  floor bots = real registered agents carrying their actual bus task, maintenance overlay on
  safe/kill. Special visitors + job menus still open (P5 leftovers).
- **Daemon step 1 (D2)**: every beat converts pipeline-lane runs into bus events — the OS sees
  all 16 lanes, not just its own ticks.
- **Phase 9 tier-1**: `src/mine_social.py` + `data/social_sources.json` + daily
  `mine_social.yml` → `data/social_intake.json` (intake QUEUE, gated before hub). Reddit=RSS
  (json is 403-blocked), DDG needs the Chrome UA, Jina Reader verified as universal fallback;
  agent-reach (MIT, keyless parts) endorsed by owner — deeper integration next arc.

## 0c. SHIPPED 2026-07-03 (third arc): 3 + 4 + 6-core + G9, dashboard v65
- **Phase 3 creators LIVE** (`src/excava_creators.py`, daily creators.yml): discovery gap-radar →
  data-grounded drafts → independent self-test → publish INTO the project, always labeled
  **"Created by EXCAVA"** (owner rule → guardrail **G-12**); `--test-before-run "<name>"` re-tests
  before first use. **PACKAGES** = owner's term for multi-element bundles. Creators dept staffed.
- **Phase 4 sandbox verify LIVE** (`src/verify_connectors.py`, 6-hourly connectors_verify.yml):
  owner chose test-run EVERYTHING — resolve real install (npm/PyPI keyless) → run in clean-env
  sandbox (no secrets, temp dir, timeout) → `data/connectors_verified.json`; tab shows progress +
  shrinks to verified-only at ≥25 passes (D5). ~10 days of batches for all 1,142.
- **Phase 6 core LIVE**: direction loop ("EXCAVA: direction …" issue command + cockpit 🧭 card +
  beat acknowledgment with EXCAVA's reading) + change tutorials (`data/tutorials.json`, v62-v65
  walkthroughs; the beat NAGS when a build ships without one). Remaining: other 8 systems, HORSE.
- **G9 "Agency/Orchestration"** on the North Star (born at 80/100). PORTABLE_HARNESS.md documents
  the spine as a package (owner: port nothing yet). Source trust-scores seeded
  (`data/source_trust.json`), intake items now carry trust.

## 0a2. GUARDRAILS — READ THIS, information-loss protection (v84, owner law 2026-07-06)
The project must never topple or lose committed work. **Two enforcers, run every beat:**
- **`src/git_safe.py`** — the ONLY safe way to commit/push. Use it: `python -m src.git_safe ship -m
  "msg" -a <files>` (commit via UTF-8 message-file → no PowerShell mangling; then backup → sync →
  push → **verify origin==HEAD**). `sync` QUARANTINES colliding untracked files into `_ATTIC/` (NEVER
  `git clean -fd` — that deletes). `backup` bundles all history to `_ATTIC/backups/`.
- **`src/guardrails.py`** — 12 checks (G-A…G-L) → `data/guardrails_status.json` (shown on the cockpit's
  🛡 Guardrails card) + append-only `data/guardrails_log.jsonl` (git-ignored, per-machine). Full contract
  + recovery steps: **`GUARDRAILS.md`**. Fixes the two mechanical failures that risked the repo.
- **Recovery:** lost file → `_ATTIC/quarantine/<ts>/`; wrecked repo → clone `_ATTIC/backups/repo-*.bundle`.
- **Never again:** no blind `git clean -fd`/`rm -rf` on untracked content; no inline quoted commit
  messages in PowerShell; no unverified push. `_ATTIC/`, `*.bundle`, `data/horse/` are git-ignored.

## 0b. RESUME HERE (autonomous /loop 2026-07-07 — owner away, "carry on")
Movement now WORKS: order bug fixed + 8-cycle beat → 124 done, 10/11 depts active (G-M movement guardrail).
BUT the work is HOLLOW: `_work_generic` wrote LLM *plans* and false-stamped them DONE (0 real videos/
connectors done); now honestly labelled "EXECUTION PLAN — not executed" (`planned_only`).
**TWO TOP PRIORITIES NEXT:** (1) **wire REAL per-department executors** — each dept runs its actual tool
(security→`src.safety_check`, watch→pending processor…) and reports REAL output, not a plan. (2) **build
the POWER department** — mine the ~13k index (`data/excava/power_findings.md`) → auto-apply safe self-
improvements (token trims, routing) + pitch owner-gated ones (Modal/pinger/PAT for true 10-min cron; more
free keys). Also: dept-fairness under the tick cap; deferred capabilities-extent review (owner request).
_(historical stall notes below — mostly resolved:)_ **Fix these IN ORDER when resuming:**
1. **ORDER BUG (fast, do first):** in `src/excava.py` the backlog refresh runs AFTER the step-4
   worker-tick, so freshly-queued per-department tasks always wait a full beat. **Move the backlog
   refresh to BEFORE the worker-tick step.** This alone should let the other 6 departments execute.
2. **CRON UNRELIABLE:** `excava_beat.yml` `*/10` is throttled by GitHub — it actually ran ~hourly to
   every-4h (10:18, 10:01, 08:56, 04:17, 22:39), NOT every 10 min. Owner's "10 min" is **not
   achievable on free GH cron**. Options to raise with owner: accept sporadic timing · self-re-trigger
   workflow (a run dispatches the next) · external uptime pinger via repository_dispatch.
3. **FAIRNESS:** `busiest_first` + `MAX_TICKS_PER_BEAT=10` may starve a low-queue dept; add round-robin.
Verify each with the movement check (`data/excava/movement.json` / guardrail G-M) — it must actually rise.
Proven working: engines (5 live), real convos, decision.md artifacts, `_work_generic`, backlog+judgment,
capabilities.json (37), guardrails (13 incl G-M), safe-git. Ship via `python -m src.git_safe ship`.

## 0c. REAL-VERTICAL STATUS (2026-07-06 Opus — the agentic core is now GENUINELY real, not theater)
The M2 "agents conversing → artifact" layer was a FACADE (0 turns/33 beats: every engine call 429'd
because the beat only had exhausted Gemini). Fixed + PROVEN end-to-end:
- **Part 1 (engines answer) ✅** — selftest run 28817002526: groq×2/gh-models/sambanova/mistral live;
  all Gemini keys 429-exhausted, cerebras 404 (bad id). CATALOG reordered so proven engines lead.
- **Part 2 (real turns) ✅** — `excava_beat.yml` (NEW: decoupled heartbeat, dispatch + every 3h, full
  pool). Real debate committed: Fetch↔Probe, Reel↔Scriv via sambanova.
- **Part 3 (real artifact) ✅** — rooms write a committed `decision.md` on convergence
  (`data/excava/artifacts/<room>.md`, lead-synthesized). First one: dept-raise-link-coverage (Ledger).
- **Honesty ladder** in `goals_check.py`: G4/G9 = 30 (dead) → 50 (talk) → 65 (1-2 artifacts) →
  uncapped (3+). Now 65; overall 70. Score rises ONLY on real evidence.
- **NEXT PARTS (owner order, vertical-first):** 4 floor/rooms show ONLY real activity · 5 console fully
  in-app (kill the GitHub-issue send) · 6 monster+animation cast via a REAL image/video tool (legs, on
  the acted-on object) · THEN 7 Visualization+Power depts + 2 pitch conditions + pitch-monster (§J/§K/§M
  of EXCAVA_V2_ADDITIONS.md) · 8 M5 + breadth. Rule: "done" = a real artifact shown, never a rendered card.

## 0d. THE END PLAN LOOP (2026-07-25, Opus fire — live build v128; AWAY-WEEK, continue HERE)
**⭐ REPO NOW ON D:\AI-YouTube-Skills** (migrated 2026-07-23 off the chronically-full C:; D: has 458 GB
free). Fresh clone from GitHub, allowlist recreated, drain re-pointed to D:, `git_safe sync` verified
from D:. The C:\Users\eitan\AI-YouTube-Skills copy is a STALE BACKUP. This commit was shipped FROM D:
as end-to-end proof. When Claude opens on D:, re-arm the away CronCreate hourly job.
**AWAY-WEEK (from 2026-07-23):** Eitan is away ~1 week; loop runs via a **CronCreate hourly job
(session-only, app must stay open)** — NOT ScheduleWakeup (that died on usage caps).
Away rules in data/excava/away_mode.json: non-brain increments only, CLI-verify (no browser), stay
in .claude/settings.json allowlist, batch questions to QUESTIONS.md, never AskUserQuestion. The
GitHub beat is the 24/7 cloud floor regardless. ⚠ **C: DISK CRITICAL (~380 MB free, 99.8% full with
Eitan's own files)** — the cloud beat is unaffected, but the LOCAL drain + this cron loop ship from
C: and will FAIL if it hits 0. Eitan must free several GB. Since v120: brains reworked to LEAD+SUPPORT
peers with complementary pairing (v122-124), spoke_today usage tally, phantom 'openrouter' engine
removed (it's a transport not a model). **NEXT (non-brain):** M1/M3 polish, Hub, self-improve dept,
deterministic enrichment, audit-backlog machinery, cleanup.

**LOOP FIRE v125 (2026-07-24, Opus — type-aware Activate: a HUB usability win, deliberately NOT more
meta-machinery.)** The prior 3 away fires shipped observability (logger→digest→pulse), which their own
criticism flagged as "meta-machinery, not product." This one is real product per items 14/16 "6 element
types USABLE, not links": `elActivate` dumped one generic blob for every element; now the pure
`activationRecipe(e)` (docs/dashboard.js, marked `/*<<ACTIVATION>>*/`) hands back the ONE paste-ready
thing per type — prompt/command → the raw text (594/594 prompts verbatim, 759 commands via `name` since
0 carry a body); connector → a paste-ready **MCP-server JSON config** + the repo holding the exact
command (1,370/1,370 valid JSON, 928 cite their repo, `_mcpCmd` strips "(open-source)"-style prose so 0
polluted args); skill/tool/model/design/format → a clean setup card. Verified headless over ALL 10,133
elements via scratchpad/test_activation.mjs (ALL PASS), not the browser (away-rule). **Still stalled
(brain-gated → for Eitan's return):** the local drain enriches 0 (G-O) because deep_retrieve rides the
brains subsystem away-mode won't touch.
**v126 (next fire, Opus):** shipped the **"▶ ready to use" hub filter + count** — one click narrows the
10,133-element pile to the **6,505 (64%)** that are actionable NOW (paste-text for prompt/command, or a
real link/install anchor), hiding 3,628 stubs. Reuses v125's readiness via a shared pure `elReady(e)`
(Ponytail); node-verified over all elements (fp/fn = 0). Composes with Activate: filter → paste.
**v127 (this fire, Opus):** the element DETAIL view now SHOWS the ready-to-use payload inline
(`activationRecipe(e)` in a readable, copyable block) instead of hiding it behind the Activate clipboard
button; de-duped the old body `<pre>`. Reuses v125/v126 (Ponytail), node --check + unit test green.
**NEXT (non-brain):** per-type readiness hints on cards; a Hub default-sort that floats ready-to-use up;
M3 polish. **Real hub problem ESCALATED to QUESTIONS.md (brain-gated):** local drain enriches 0 (G-O); I
proposed a deterministic (no-LLM) GitHub-metadata enricher for Eitan's approval — these fires keep
producing browse-polish of diminishing value until the enrichment/brain front is unblocked. THREE
browse-layer fires in a row (v125/126/127) is the honest signal that away-mode has run its useful course
on the Hub read-side.
**v128 (Opus, 2026-07-25 — PIVOTED off the hub as promised):** wired the DEAD pulse tool to run every beat
(`python -m src.pulse` added to excava_beat.yml → refreshes data/excava/pulse.json; PULSE.md at root is
deliberately NOT auto-committed — a churny non-data file would be a git_safe source-conflict and could break
an unattended ship) and gave it an in-app consumer: a 🫀 **Program pulse** card on the self-improve tab
(guardrails/drain/open-Qs + the done-counter DELTA in RED when negative). It exposes a real ongoing
regression the all-green guardrails hide: done has fallen **1566→1256→1130 (delta −128)** over days while 12
depts still read "moving." **NEXT: DIAGNOSE that decline** (re-scoping vs real loss — the done-counter
semantics in movement.json / state.json usage), don't just display it. **Correction to my v125–127 claims:**
the drain is NOT "stalled at 0" — it enriches ~1–20/batch, just slowly vs 2,027 stubs; the
deterministic-enricher escalation in QUESTIONS.md stands to ACCELERATE it, not revive a corpse.

**v129 (away fire 7, unattended, cloud PR-branch session, 2026-07-26 — landed the stranded `links`
department fix):** registered `departments.links` + agents Anchor/Tether in `data/excava/agents.json`
(the fix QUESTIONS.md flagged as stranded on the unmerged `origin/claude/kind-shannon-ae4swi` branch,
PR #3) so link-coverage tasks route to a staffed worker instead of "no department specialization
matched". Verified via `pick_department()` + `python -m src.guardrails` (14/15, 0 critical, unchanged)
+ `python -m src.excava_systemcheck` (11/11). **Escalated to QUESTIONS.md: this scheduled task has now
produced 10 branches / 9 open draft PRs, none merged — needs a triage/merge pass, not another fire
re-deriving the same fixes.**

**v129 (away fire 6, unattended, 2026-07-26 — live build v129, DIAGNOSED v128's decline):** the "falling
done-counter" was a metric bug, not real loss: `g_movement()` in src/guardrails.py recounted "done" LIVE
from `data/excava/bus.json`, but `excava_bus.prune()` deliberately archives finished tasks out of the bus
after 7 days — so the live count falls as pruning runs, unrelated to whether work is happening. Switched it
to sum the monotonic `state.json['usage'][dept]['done']` tally instead (bumped once per completion, never
pruned) — now reads **4520 cumulative**, correctly only-rises. Reworded pulse.py's Movement section to match
(cumulative-only-rises framing; a genuine flat->0 warns separately from a numeric fall, which should now be
impossible). Also found + fixed **why guardrails read 13/15 instead of 15/15** since v128: (a) this v128
change made the CI beat run `src/guardrails.py` on its OWN ephemeral runner every 10 min — but the beat
commits/pushes with RAW git (not `src.git_safe`), so it never calls `backup_bundle()`, and `_ATTIC/backups`
(gitignored, per-machine) is permanently empty there; G-C now recognizes `GITHUB_ACTIONS=true` and reports
`info`/pass instead of a permanent false "warn" (local/interactive runs are unaffected — they still need a
real bundle). (b) This handoff hadn't mentioned the live build since v128 shipped — that's this paragraph.
**Honest side-note:** while diagnosing, found an UNMERGED branch (`origin/claude/kind-shannon-ae4swi`,
diverged after beat #17) already containing this exact G-M fix plus a routing fix for the `links` department
— a parallel away-fire session did this work first but it never reached `main`. Flagged in QUESTIONS.md:
away-fire sessions need a rule against silently orphaning work on divergent branches.

**(prior, v120) M2 UNDERWAY.** Sessions 8-10: 4 brain families in the engine CATALOG (GLM/DeepSeek/Kimi via
OpenRouter free + local Qwen/Llama); OpenRouter key VERIFIED (Eitan's secret OPENROUTER_API_KEY_REAL,
workflows repointed, selftest 11/11, glm/deepseek/kimi all PASS); `engines.debate_engines(n)` dedups
by model LINEAGE so a room debate crosses DISTINCT families (the 4 llama providers were correlated-
error same-model — now collapsed to 1), wired into excava_chat; 🧠 Brains card shows it. Drain
WATCHDOG added (daemon os._exit at deadline+90s — a 180-min run happened when one enrich() blocked).
**NEXT M2:** rooms PRODUCE committed artifacts across families in CI (verify a real multi-lineage
debate runs on the beat now the key is live); then the 5-class layer (Router/Agent/Tool/Room/Element)
+ leases/budgets + named roster. bulk_analyze still uses the RETIRED openrouter llama slug (cosmetic).

## 0d-v118. (2026-07-21, v118 — one-brain memory)
**Session 7 (v118):** M1 unify-memory READ SIDE — `src/memory_brain.py` federates all 5 memory
stores behind ONE deterministic `recall()` + `census()`; 🧠 One-Brain card on excava tab (8,579
records/4 stores), wired into the links beat. Confirmed sandbox-verify-all-types is correctly wired
(designs/skills NOT join-suppressed — genuinely thin/dead-link). **M1 core now essentially complete;
NEXT: semantic re-rank (layer memory_index vectors onto recall), make agents actually CALL
memory_brain.recall at decision time (write side of unify-memory), then M2 (engine layer + 5 classes).**


**Session 5 (v117):** shipped 🛢 **The Hub** — one browsable/searchable library across ALL 9,573
elements (type + verification filters, global-search box), reusing the element layer (eidx/elBadge/
elementActions). Nav button + `renderHub()` + route. Browser-verified: type-filter and search both
correct. This is item 13/21 (the usable hub browser). Trust-gate dead-prune is MOOT (0 dead elements).
Also: drain proven bounded (2.7-min scheduled run under the new 12-min in-loop deadline); PC set to
never-sleep on AC + task WakeToRun (owner's call, until VPS — revert values in memory end-plan-loop).
Next: audit batch 5-8; M1 remaining = sandbox-verify-all-types / unify-memory; then M2.

**(prior)** 
EXCAVA_END_PLAN.md (now IN the repo, with MASTER_AUDIT/FUNDAMENTALS/the rest) is the definitive plan;
an hourly /loop session advances it one wired increment at a time. **State after loop session 1:**
- **M1.C1 drain is KILL-PROOF**: local_worker.py does RECOVERY-FIRST shipping (a killed run's work
  ships seconds into the next start — proven live, b47988f6d), holds the machine awake mid-batch,
  takes a run lock; git_safe sync rebases with --autostash; task EXCAVA-LocalDrain survives battery
  + catches up missed runs. The WHY chain (project_memory files) ships with the drain.
- **Batch selection is honest**: fresh-fusable pool 677 (fusable = link OR transcript ON DISK —
  1,307 was counting ~500 transcript-less phantoms; 24 slots burned at 0 before the fix, 4/8
  enriched after). Failed elements cool down 3 days (attempts log in deep_retrieve_state.json).
- **NEXT (in order):** (1) check G-O + git log that the hourly scheduled run enriches >0 and
  self-ships with the fusable fix; (2) transcript backfill feeds the ~500 video-only stubs (gentle,
  residential); (3) M1 continues per EXCAVA_V2_STEPS.md — enrichment-at-scale, then trust gate /
  detail view / RELATE. The 122-item MASTER_AUDIT awaits Eitan's verdicts (clickable, 4/batch).

## 0d-old. EXCAVA v2 BUILD STATE (2026-07-06, Fable executing EXCAVA_V2_STEPS.md; was live build v84)
- **M1 ✅ COMPLETE (v66, dd665b39):** element model (6,422 els, schema+index+set_field) · deep_retrieve
  (full-source enrichment, stubs-first) · discovery_agent (hourly; GitHub/HN/PH/social; live-tested 58 new)
  · verify_elements (2-source+live, rolling+on-access, conflicts noted) · relate (4,796 with related) ·
  prewarm (52 targets) · badges+action-row on all list tabs · #element/<id> detail view · core_spoton.yml.
- **M2 ✅ COMPLETE (v67→fixed in v68, 988f6b1b):** PROTOCOLS.md P1-P14 + SAFE-tripping audit (proven) ·
  excava_engines (9 families, Hermes/OmniRoute optional, fall-through) · excava_leases (dept budgets,
  RPM, Claude-cap) · 38 NAMED agents (Echo/Marrow/Iris/Ledger/Root/Boulder/Chroma/Wire/Ratchet/Bastion/
  Nova + doers/checkers/improvers; --roster) · excava_chat rooms (debate→converge→ARTIFACT:
  package/bus-task/creation; day archives) · workers dispatch/dissolve · rooms advance每 beat ·
  excava_selfimprove (auto budget-shift, room-retire, PITCH filing). Rooms speak on CI beats (engines
  live in secrets; local runs degrade honestly).
- **M3 ✅ COMPLETE (v79, d6e13e0b):** shipped 2026-07-06 (Fable). Slice-1 (v68) = tokens.css + sidebar
  shell + 🗣 Rooms + console hero. Then: **M3.2** monster cast (`src/make_monsters.py`, 11 species ×3
  variants SVG in docs/assets/monsters/, wired into Rooms bubbles + floor stations + bus bots) · **M3.3**
  isometric factory floor + side cutaways (`docs/floor/floor.js`: ground+buildings+cutaway; monster at
  each door; floor clock=M2.7 timing) · **M3.4** animation catalog (11 props, `animForEvent` grounds each
  in a real bus/beat event) · **M3.6** final card visual (refined-neobrutalist, actions on hover/focus) ·
  **M3.7** 📦 Results feed (attributed, day/dept/maker filters, inline artifact bubble, new-badge) ·
  **M3.8** North-Star constellation (9 orbiting goal-stars, size=score, click→goal) · **M3.9** brain
  graph click→explore→"make cluster a package" · **M3.11** steering (header bell+count, dismissible
  approval banner, walk-up herald monster, pitches-as-conversations modal) · **M3.11b** 🎛 Taste tab
  (editable design-taste vs work-taste, feeds HORSE) · **M3.12** mobile pass (read/review/approve/send;
  run buttons off ≤640px; fixed a real [hidden]-override bug on modal/banner/walkup) · **M3.13** ship:
  interactive walkthrough RUNNER (E7 — navigates tabs, spotlights the new thing, Next/Back) + M3 tutorial
  + m3-podcast.wav (System.Speech).
- **⚠ LESSON (cost us v67):** NEVER bump builds/edit utf-8 files via PowerShell Get/Set-Content —
  python utf-8 only. Also: **commit -m messages must NOT contain embedded double-quotes** (PowerShell
  mangles native-exe args → git treats trailing words as pathspecs; use a simple single-line message).
  And: `git stash pop` can OOM on the huge untracked skill trees — extract just your files with
  `git checkout stash@{0} -- <paths>` instead of a full pop, and `git clean -fd skills other-skills
  data/excava/traces data/excava/handoffs backups` before a rebase (untracked CI/agent files block it).
- **M4 ✅ COMPLETE (v83, bc8d6970):** shipped 2026-07-06 (Fable). **M4.2** HORSE (`src/horse.py` — 10
  runners each fully execute the goal on varied free engines, scored vs work-taste, top-3 merged;
  console `/horse` → `excava_channel` HORSE handler → `run_horse`, runs in CI; merged artifact in the
  Results feed) · **M4.3** 🧰 Packages tab (`data/packages.json` 3 seeded kits; assemble w/ loose-name→id
  resolution, pin, edit, Run-all/Run-each, Save-to-EXCAVA; merges server + creations + localStorage) ·
  **M4.4** parent launcher (`launcher/` = **ORBIT**, its OWN calm minimal brand, project-cube grid, full
  context switch, EXCAVA-made projects auto-appear) · **M4.5** hub-as-database (`src/build_hub_api.py` →
  `docs/hub_api.json` public endpoint, packages resolved to element install+url + compact real-element
  index; **wired into the excava beat** so it refreshes every cycle; Packages tab shows endpoint+copy) ·
  **M4.6** ship: "Proof it's real" cockpit card (unattended CI artifact + goal→package path) + M4 tutorial
  + m4-podcast.wav.
- **M4.1 portable activator = [OPUS]-RESERVED** (compressed-hub SKILL.md + live fetch, obeys triggers,
  offline). Fable did NOT build it — it's on the Opus track. This is the ONLY unbuilt core-program step.
- **NEXT (per program): M5 is DEFERRED behind the core; BREADTH is next — B1/B3/B6 FIRST** (expand each
  to full steps, then build), then B2/B4/B5, alongside M5. B1 finish the 52 goals (§9 order) · B3 per-tab
  self-improvement + meta-brain · B6 EXCAVA-as-MCP-server · B2 omni-source tiers 2-3 · B4 portability
  (Budoaris first if asked) · B5 cleanup (formats filter, brain white-nodes, token-split). M5 (external
  actions) stays gated/deferred. Plan files: EXCAVA_V2_STEPS.md (+ADDITIONS §I) — the whole program is
  now complete through M4 except OPUS M4.1; only AFTER the whole program may Fable ask questions / suggest
  adding OpenClaw/Hermes/other tools.
- **Push mechanics learned this session:** commit -m must be a SIMPLE single-line string (NO embedded
  double-quotes — PowerShell mangles native args → git treats words as pathspecs). Before every rebase:
  `git checkout -- data backups` + `git clean -fd data/horse data/excava/traces data/excava/handoffs
  backups skills other-skills` (untracked CI/agent trees block rebase and can OOM `git stash pop` — use
  `git checkout stash@{0} -- <paths>` to extract, never a full pop). git's stderr progress trips
  PowerShell's NativeCommandError but the ref-update line confirms success.
- Gate note: internal gate was CLOSED this session by a REAL data_guard restore (designs.json 242→670)
  — correct behavior; it self-clears on the next clean guard pass.

## 1. WHAT THIS IS
A **personal build-leverage system** for Eitan — a hub of every AI capability (tools/skills/models/MCP/
prompts/commands/designs) mined from ONE YouTube playlist, used with all his tools to build things fast.
**EXCAVA** = the agentic-OS layer orchestrating it (multi-agent orchestrator + harness, using
Excavatortron as its database). Free on GitHub Actions. "LIV" = *live, together* (him + me), not a person.

## 2. CURRENT STATE (2026-07-02)
- Dashboard build **v62** (docs/, GitHub Pages). Theme = "Heavy Machinery" (hazard-yellow + ink neobrutalism, Archivo Black).
- Link coverage **~39%**, climbing (+5%/day target in `data/coverage_log.json`, shown on the 🔋 card).
- EXCAVA cockpit = **home tab**: living floor + task inbox (`data/excava_inbox.json`) + resources card + 8-goal North-Star bars. **Residents** wander every tab (bubbles = real dept status; click → cockpit).
- Activator: portable SKILL.md in `~/.claude/skills/excavatortron-activator/` + Desktop + `docs/activator-skill.md`. **KNOWN BROKEN → Opus 4.8 track (§5).**
- Connectors are **~94% fake** (empty/placeholder install) — Phase 4 fixes.

## 3. PHASE 0 — SHIPPED 2026-07-03 (the OS spine is LIVE)
- **File bus** `src/excava_bus.py`: enqueue → route → claim → hand-off/complete/fail; atomic writes;
  per-task traces (`data/excava/traces/*.jsonl`, incl. "why X over Y" routing events).
- **Hand-off gate (G-4)**: a hand-off missing what_was_done/artifacts/what_remains/context_for_next is
  REJECTED + traced. Docs land in `data/excava/handoffs/` as readable markdown.
- **Registry** `data/excava/agents.json`: 3 tiers, 11 departments mapped 1:1 to the real lanes, scoped
  tools (G-7); `creators` defined but unstaffed = mechanically gated until Phase 3.
- **Orchestrator** `src/excava.py` (same CI entry, same status schema + new `os` section): gate → inbox
  outranks (G-8) → priorities → specialization routing → ≤4 worker ticks/beat → 3-tier escalation → owner.
- **Shared memory**: vector index = read side; `data/excava/state.json` = write side (`bus.remember`).
- **Guardrails**: `data/excava/guardrails.md` (G-1…G-11), enforced in code.
- **Done-criterion PROVEN on real work**: owner inbox task t1 (link coverage) crossed links → memory via a
  real hand-off doc (`data/excava/handoffs/push-link-coverage-towar-31649--01--…`), completed next beat.
  Repeatable proof: `python -m src.excava --selftest` (scratch bus; asserts the doc-less hand-off is rejected).
- Phase-0 workers are ASSESSORS (read their dept's real data, move tasks with grounded docs); heavy work
  still lives in the CI lanes — later phases add execution muscle, the Worker contract stays.

## 3a. PHASES 1+2 — SHIPPED 2026-07-03 (you drive it + safe 24/7), dashboard v63
- **Multi-channel task send**: cockpit send-box → prefilled GitHub issue "EXCAVA: <task>" →
  `excava_inbox.yml` workflow applies it via `src/excava_channel.py`, commits, replies a receipt,
  closes the issue (phone-friendly). Channels: issue / tell Claude / edit inbox file.
- **Kill switch + safe-mode**: `excava_config.json mode` = run|safe|kill (issue "EXCAVA: kill|safe|run"
  or cockpit links). kill = bus untouched; safe = sync+route, no worker acts. Mode chip on cockpit + strip.
- **Priority-weights dial**: `excava_config.json priority_weights` orders which auto-priorities reach
  the bus ("EXCAVA: weight access 95"). Owner inbox always outranks (G-8).
- **Approval queue**: `data/excava_approvals.json` — everything owner-blocked, categorized
  (escalated/outward/unroutable/missing-resource); cockpit widget with per-item approve links
  ("EXCAVA: approve <id>" → re-queued next beat).
- **Phase 2 safety**: lease recovery (claims >6h = crashed worker → re-queued, traced) · bus pruning
  (done >7d → data/excava/archive/) · per-dept usage accounting (state.json) · fail-streak backpressure
  (3 straight fails → 6h cooldown, self-heals) · **continuous self-audit** (guardrails-vs-code + bus
  invariants each beat; problems force AUTO SAFE-MODE).
- **Cockpit v63 shows the spine**: "You drive it" card (send box, mode, weights), OS spine board
  (beat #, per-dept bus counts, beat log, last hand-off link), approval queue. Verified via DOM checks
  (screenshots still time out on the crew animation — known).

## 3b. THE PLAN (full steps in EXCAVA_PROGRAM.md)
9 phases: **P0 OS spine** (bus + shared-memory + orchestrator — build FIRST) → P1 you-drive-it → P2 safe
24/7 → P3 Creators dept → P4 connectors made real → P5 living OS (crew v2) → P6 direction-loop + 10
systems → P7 portability + breadth → P8 North-Star G9 + cleanup. **56 goals** (52 + G53-56 gap-audit),
each mapped to a phase. Core insight: EXCAVA today is a "tab pile," not an OS — build the hand-off +
shared-memory layer before more visual polish. **D1-D5 gate the start.**
Explicitly covered (were implicit, added 2026-07-02b): **dynamic departments** (fully autonomous — P0/P3/P5),
**crystallize repeated patterns into skills** (P3), **beyond-project capabilities** (build MY things=P7,
research & briefs=P3, daily ops/digests=G50/G36). Full coverage audit is in EXCAVA_PROGRAM.md.

## 4. STANDING RULES (non-negotiable)
- **Free only, forever** — "free tier that needs a card on file" = PAID → skip (Bright Data proxy declined).
- **Fable = 60-100%, ALL visuals**; Opus 4.8 = reserved track (§5) + accuracy fixes.
- **Every forward step deepens EXCAVA's integration.**
- **Quality over quantity** (300 verified > 3000 dead).
- **Ask questions, never block** — park in QUESTIONS.md, proceed with defaults, his later answers adjust. Avoid AskUserQuestion for big batches (token cost); use plain text / QUESTIONS.md. **He does NOT want to babysit.**
- **NOSG**: message ends with NOSG → skip options/advice, do the best thing, one-line report.
- **Resource-check before tasks**; **security-first** (untrusted creators); **token-reduction** before heavy work.
- **Ship visible committed progress each session.** Bump `APP_BUILD` + `sw.js` version on every dashboard change.
- **Drain transcripts gently** each session (residential; don't burst → IP block).

## 5. RESERVED FOR OPUS 4.8 (NOT Fable)
SKILL.md/activator working end-to-end · "Open code" (github.dev) button fix · preview <3s + Arena images
prioritized · data-retrieval accuracy + fixing anything Fable built inaccurately.

## 6. CONSISTENCY CHECK (after EVERY task — memory `feedback-consistency-check`)
After each task, before moving on, verify + state in ONE line: (a) it advances a specific
EXCAVA_PROGRAM phase/goal; (b) it contradicts NO decision/answer Eitan gave; (c) it respects §4. If
inconsistent → flag + fix before proceeding.

## 7. REPO MECHANICS
- Repo `C:\Users\eitan\AI-YouTube-Skills` · remote `Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor` · branch `main` · Pages: `.../AI-YouTube-Playlist-Information-Extractor/docs/`.
- **Push pattern** (dirty generated files block otherwise): add → commit → `git stash -u` → `git pull --rebase` → `git push` → `git stash drop`.
- `data/*.json` update in CI hourly — don't commit local test copies; revert them.
- Preview: launch config `dashboard` (python http.server 8787, root=repo). Crew animation makes screenshots time out → verify via `preview_eval` DOM queries.
- Commit trailer: `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>` (Opus on that track).

## 8. NEXT SESSION
1. **Phases 3+4** per sequencing (creators dept behind the gate; connectors made real + sandbox
test-runs). 2. P5 leftovers: job menus on residents, special visitors, per-dept animation vocabulary.
3. **Phase 9 deepening**: wire `social_intake.json` consumption into the mining lane's verify+security
gate (intake → hub); integrate agent-reach's keyless tools; Eitan's channel/subreddit list (Q22).
4. **Phase 6 start (D2)**: direction-loop + change-tutorials, daemon-grade (see QUESTIONS #25).
5. Transcript drain: 2026-07-03 run hit a pre-existing IP block after 4 videos (auto-stopped correctly);
1,389 still lack real transcripts — next residential session, retry gentler (`--sleep 6 --limit 60`).
6. Keep the consistency check + ask-checkpoints + PROJECT_MEMORY contract running. 7. Update this
handoff at session end.
