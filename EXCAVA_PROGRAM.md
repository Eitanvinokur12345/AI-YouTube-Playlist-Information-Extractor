# EXCAVA — the complete program (multi-agent orchestrator + harness over Excavatortron)

## ⭐ EXCAVATORTRON & EXCAVA REHABILITATION PLAN — updated 2026-07-11 (this section IS the source of truth; below it = the original foundation)

**0. HISTORY MINING (owner 2026-07-11 — INTEGRAL):** src/history_mine.py mines the FULL owner history
(586 records, all sessions) for want-signals; repeated wants rank higher → data/excava/rehab_plan.json
(first run: 208 clusters; top: VPS/24h ×45, retrieval+new sources ×34, post-extraction verification ×31,
OpenSpec/visual-analysis…). Each loop round, a short QUESTION SEQUENCE confirms a few candidates with the
owner; confirmed gaps enter this plan. Don't follow only the recent requests — the history is the backlog.
**DONE-WHEN (owner 2026-07-11): the plan ends only when EVERY request he has EVER made is fulfilled as
he wanted — then new things. Frequency orders the queue but NEVER decides importance: a request raised
once counts fully. Scoreboard: rehab_plan.json coverage (now 208 total · 4 in-progress · 204 unreviewed);
every tick may move it, question sequences drain 'unreviewed'.**
**CONFIRMED ROUND 1 (owner order, 2026-07-11): R1 free-VPS 24/7 — READY, awaiting owner approve:
deploy/vps_setup.sh written (Oracle Always Free + systemd timer, 5-min beats forever); v2 pitch in the
in-app decide queue with the 10-min guide (signup + fine-grained token + one command) · R2 more retrieval sources — v1 DONE (HuggingFace trending models+spaces + arXiv cs.AI/CL/LG joined the hourly discovery sweep, keyless, live-verified; next: wire finds into element creation) · R3 EXCAVA external +
internal capabilities [study done: AGENTIC_OS_STUDY.md — 5 free-first adoption ideas] · R4 post-extraction verification · R5 visual data analysis. REMINDERS LEDGER lives at
data/excava/reminders.json (owner: nothing may be forgotten) — the loop re-reads it; miner refills it.**

**Standing laws (owner):** free-only forever · everything operable IN THE APP (no GitHub for the owner) ·
Ponytail law (reuse before build, minimal diffs, fewest tokens) · one item to VERIFIED-done per loop tick
(operate the real user path; captured ≠ built ≠ used) · recall-before-change + log WHY after · ship only via
`python -m src.git_safe ship` · harsh 100% criticism both ways every tick · memory-review opens each tick.

**Autonomy tiers (agreed 2026-07-10, data/excava/autonomy.json, enforced):** EXCAVA alone may tune
prompts/configs/tunings; change its OWN code only behind a sandbox test (auto-revert on fail); ADD AGENTS
(labeled "Added by EXCAVA"). New tools from scratch / new departments / completely new features → pitch.

**DONE + verified (July 10-11):** approvals decidable in-app (v94) · pitch system revived + PITCH V2
(who/need/importance/missing + own-hub candidate chips, v98) · creators assemble real packages · humanized
output + plain-language agent debates (VERIFIED live: 20/20 fresh turns, 0 bash) · Visualization ⁄
Accessibility split into two staffed departments (v96) · Proof files open in-app (v97) · SI-1 hub self-use ·
SI-2 hourly engine-benchmark canary + health-aware engine picking + 🔌 panel (v99, cerebras id fix pending CI
proof) · SI-3 autonomy enforced + tier-2.5 auto-staffing (sandbox-proven) + 🧪 experiments roster in-app (v100).

**R1 STATUS (2026-07-12): waiting on the owner's PARENTS' OK — Oracle requires address + card identity
verification and the owner is 17; he is asking first, which is exactly right. No pressure in reports;
the GitHub cron remains the runtime until they decide. ('Sonat' resolved = Claude Sonnet, the model.)**

**NOW → NEXT (approved order — self-improvement first):**
1. **SI-4a Golden-task regression suite** — ~6 fixed engine-free tasks (bus routing, package assembly,
   pitch v2 generation, humanize, hub-candidate search, pitch-survival in approvals) → `run_regression()` →
   `data/excava/regression.json`; beat-wired; roster flips to LIVE. This GATES tier-2 self-code for real.
2. **SI-4b Formation A/B** — LIVE: first real CI verdict 2026-07-11 — blind judge picked SOLO (tally solo 1 : debate 0). Daily cadence; 3 net wins flips formation_policy.json.
3. **SI-4c Huge-task splitting** — SHIPPED+verified: 'Close the link gap: 4060/7360 unlinked (G3)'
   split into 6 checkpoints; measure step executed immediately; 4 batch steps + final re-verify are
   REAL bus tasks the links lane consumes; daily cap; roster live with progress. NOTE 2026-07-11: the
   hub GREW (7764 els, unlinked 4431) — batch done-criteria use absolute counts; switch to PERCENT
   coverage criteria next touch.
3½. **AGENT REALNESS (owner 2026-07-11 — priority #2 after self-improvement):** rooms must be TRUE
   multi-model debates, not one engine talking to itself (owner caught 20/20 turns all-Mistral).
   Mechanics SHIPPED: healthy-pool round-robin per turn (consecutive speakers get different models),
   canary no-healthy reports never block a keyed re-run, supervisor flags single-engine rooms (11
   caught on real data, visible in its criticism). PLUS: complete() now falls through the HEALTHY
   pool only — a quota-dead engine used to eat a 60s timeout on every turn (why cycles crawled and
   Mistral answered everything). LIVE CI PROOF PENDING — check fresh transcripts for a real engine
   mix. ✅ LIVE PROOF 2026-07-11 ~10:00Z: 9 of 17 rooms show TWO models debating (gh-models + mistral in the same room; canary: groq/sambanova/mistral/gh-models all healthy — gh-models revived by the zero-setup GITHUB_TOKEN). Spread fix SHIPPED 2026-07-11: per-room OFFSET in the round-robin (before it, every room's first turn hit pool[0] — 17 rooms bursting one engine) + 2s pacing between turns; simulated cycle shows first-turn load 3-5 per engine instead of 17-on-one. LIVE spread proof next beats. Then per-agent memory/stance.
3¾. **POWER finds capacity itself (owner 2026-07-11):** DONE v1 — src/power_scan.py is Power's real
   executor: audits which engine families lack a live key (+ the exact free signup path), searches
   EXCAVA's OWN hub for free engines/gateways, files the best move as a v2 pitch. Plus a zero-setup
   win: the beat now passes the built-in Actions GITHUB_TOKEN with models:read → free gh-models
   capacity with NO owner key. (Power is no longer talk-only.)
4. **P1 Live refresh** — DONE+verified v102: the app polls the beat stamp every 60s while open; on new
   data it drops the cache, re-renders the ACTIVE tab, and pulses "🟢 live · new data HH:MM" next to the
   build badge; never refreshes while a modal is open or the tab is hidden (browser-verified end-to-end).
4½c. **DECISION-MAKING — STRUCTURALLY RESOLVED (owner's 3rd ask, 2026-07-12): rooms are now SHAPED
   by tier. Output-tier depts (creators/analysis/security/memory/mining/news/transcripts/visual/
   watch): 3-turn ACTION-shaped rooms — the doer states the act, the checker verifies it's mission
   work, the lead closes with 'ACTION:', and the close puts REAL work on the bus. Improvement-
   flavored conclusions REROUTE to improve (or power for EXCAVA-capability matters) — verified:
   mission→own queue, 'standardize our workflow'→IMPROVE, 'upgrade our EXCAVA engine'→POWER, all
   syscall-traced. Initiative restricted to the decision-heavy tier. Decision-heavy rooms
   (improve/power/visualization/accessibility + war/group) keep the debate shape — deciding IS
   their mission. LIVE PROOF pending: next beats' creators transcripts should read act-verify-ACT.**
4½b. **DECISION-VOLUME POLICY — CONFIRMED 2026-07-12:** decision-heavy tier =
   improve/power/visualization/accessibility (debate IS their job); everyone else must let
   decisions lead to ACTION (owner: 'the emphasis should be on action') — enforcement
   (every-room-ends-in-artifact vs case-by-case) decided per department over coming ticks.
   data/excava/dept_tiers.json is the record. AUDIT v2 (owner-requested upgrade): replaced
   pure vocabulary with GROUNDING — hallucinated_pct (foreign-tech-stack mentions; this repo
   is Python/JS/JSON only) + artifact_output_ratio (decisions referencing a REAL existing
   file). Result validates the owner's instinct exactly: CREATORS is worst on both new
   metrics — 17% hallucinated, 0.17 ratio (room debates a FICTIONAL Rust/cargo project,
   'excava-core'/'cargo build', with zero link to the real assemble_packages() builder).
   Owner explicitly DEFERRED the fix — folds into a bigger CREATORS OVERHAUL (queued in
   reminders.json, NOT a quick prompt patch — do not touch the room brief yet).
4½. **DECISION AUDIT — DONE+verified (priority-0 bus task completed):** 284 real decisions audited
   (src/decision_audit.py, mechanical): 13% are self-improvement — concentrated in WAR-ROOM (18/18),
   GROUP-CHAT (2/2) and legacy links rooms; the 13 departments themselves are 0-5% SI (they hold
   their missions). Supervisor flags DECISION DRIFT in its criticism. NEXT LAYER: SI liaison agent
   per dept (tier-2.5) + war/group SI decisions auto-route to improve. ORIGINAL ITEM: many department 'decisions' are actually SELF-IMPROVEMENT
   work, not the department's mission. Build: classify recent room decisions (mission vs self-improve);
   self-improve-type decisions route to the SI department's EXTERNAL ARMS (an SI liaison per dept);
   departments keep only mission decisions. Output data/excava/decision_audit.json + in-app view;
   supervisor gains a mission-vs-SI drift flag. (Bus task filed, priority 0.)
4¾. **TOKEN DIET (Caveman, found on the web — NOT in the hub; mining gap):** apply its no-filler law to
   AGENT prompts next _prompt touch (fewer output tokens per turn = more turns per quota). Owner-facing
   reports stay full sentences (his standing 'sentences not code' law outranks caveman-speak).
5. **P2 Item-6 rest** — (a) DONE+verified v103: creations ROUTE to their tabs (_plusCreations merges
   'Created by EXCAVA' items into Prompts/Tools/Designs — 11 prompt-creations visible under the
   'Creation' filter; packages already merged). (b) DONE+verified v104: Rooms rail flags 🗣 talk-only
   (accessibility, visualization) and ⛔ blocked (watch) from systemcheck's honest per-dept lists.
   (c) DONE+verified v104: global /blob/main/ interceptor — every repo-file link (current + future)
   opens IN-APP via the artifact modal; the modal's own GitHub fallback is the one escape hatch.
   → P2 COMPLETE.
6. **P5 Visual dept + Designs tab overhaul** — auto-ADD every design, quality-filter the junk, then tasks.
7. **P6 Department interconnection** — depts ↔ brain systems/protocols, surfaced in the Developer tab.
7½. **TUTORIAL SYSTEM OVERHAUL — WAVE 1 DONE+verified v109: four REHAB WAVE walkthroughs cover
   v94-v108 (decide+pitches+truth-chip · live refresh · engine-health/experiments/token-diet ·
   agents/history/honest-flags), each with an interactive tour; ROOT-CAUSE FIX: the walkthrough list
   showed the OLDEST 4 entries (slice(0,4)) so new tutorials could never appear — now newest-first.
   Tour verified live (navigates + highlights the decide button). WAVE 2 DONE+verified v110: pinned 'START HERE' 5-stop
   fundamentals tour (hub=product, EXCAVA=beat/bus/departments, rooms=staff+honest flags, proof=trust,
   approval-queue=you're the boss) — pinned-first sort so it always leads the walkthrough list.
   LIVE PROOFS harvested this tick: 19 agent memories in CI + 5 real initiative tasks on the bus
   (Lumen/Ratchet/Chroma/Root/…). REMAINING: per-tab help buttons. ORIGINAL:** 'so many things have been added that I'm
   starting to lose my bearings' — the walkthrough/tutorial system must catch up with everything
   shipped (v94-v108: decide modal, pitches, live refresh, diet card, agents card, history strips…).
   HIGH priority after the external-action spec.**
8. **P7 Rooms/Results HISTORY views** — PER-DEPT CONVERSATION HISTORY DONE+verified v108 (owner pulled
   it forward: each dept room shows a 📜 history strip of its earlier conversations — one click opens
   any past room's real transcript; window widened 4→14 days so older rooms actually load; verified:
   CREATORS shows 12 earlier rooms, older transcript loads). Remaining from the original ask: — per-department all-conversations view; war rooms sectioned above;
   group-chat tab inside Rooms (owner re-confirmed; deliberately after the items above).

**DECIDE-FLOW TRUTH FIX v105 (owner caught it: his VPS review never arrived):** a decision saved in the
app lives ONLY on the device until the cloud-dispatch click; the chip used to lie 'sent'. Now: orange
'NOT SENT — tap to send' chip until the dispatch link is actually clicked (verified both states in
browser). Real cure = one-click in-app decisions via a tiny receiver — folds into the VPS (R1) which
can host it. **KEYS EXIST (confirmed 2026-07-11 from owner's secrets screenshot):** GROQ_API_KEY(+_2), GEMINI_API_KEY_2..6,
OPENROUTER_API_KEY, CEREBRAS_API_KEY(+_2), MISTRAL, SAMBANOVA, NVIDIA, GH_MODELS, BRIGHTDATA, SUPADATA, YOUTUBE,
OMNIROUTE, CLAUDE_CODE_OAUTH — ALL present. So engine failures are NOT missing keys; they are engine-side.
CANARY VERDICTS 15:35: groq HEALTHY (UA fix VERIFIED beat Cloudflare); openrouter model valid (transient
429 only); cerebras past Cloudflare but model-404 → id swapped to llama3.1-8b (canary verifies next).
Debate pool now 3 healthy (groq+mistral+gh-models). REAL CODES ARRIVED 2026-07-11 14:04 + FIXES: groq/cerebras = Cloudflare 1010 bot-block → browser
User-Agent added (canary verifies next beat); gemini = GENUINE quota-429 (not project-access — analysis
pipeline drains all 7 keys; needs burn-rate control, not new keys); openrouter = deepseek-r1:free went
PAID (404) → switched to llama-3.3-70b:free; sambanova temp 429; nvidia timeout (parked). Mistral +
gh-models healthy = today's debate pair. Diagnosis layer: canary records the REAL HTTP status per engine (quota-429 / bad-model-404 / bad-key-401),
benchmarks each engine in ISOLATION (no fallthrough mislabel), and CHAT-gemini got its own plain-text path
(bulk_analyze.call_gemini forced JSON + json.loads -> crashed on any free-form reply — gemini rooms were doomed
regardless of quota; fixed + stub-verified). NEXT beat's canary reveals each engine's real reason -> fix precisely.

**R3 ORDER (owner 2026-07-12): context-paging DONE (v-code 2026-07-12: every room turn now carries a
≤200-char 'KNOWN FROM THE HUB' block — keyword recall over 7.9k elements, per-room cache, regression
gate passed; semantic recall upgrades it when Gemini quota returns; LIVE proof = agents citing hub
items in fresh transcripts) → temporal-validity DONE (v-code 2026-07-12: reuses elements_verified.json, no new store;
honest finding: 0 stale hub elements right now — verify lane runs too often for element-level
staleness to show; REAL staleness so far is at the CAPABILITY layer (openrouter/cerebras),
now durably logged in staleness_events.jsonl instead of one-off memory notes; Power/SI-type
room prompts get a live stale-capability warning, verified: fires for Power, silent for
Security) → impact-scheduler DONE (war > at-risk-goal depts > others > group-chat-last; verified) →
syscall-layer DONE (v-code 2026-07-12: _task_tool_fit gate in _work_generic REFUSES wrong-tool runs
with an honest fail→escalation instead of a fake done — verified against the EXACT historical facade
(mining 'completing' link-resolution checkpoints: now refused) + 3 controls; every generic tool call
logged to syscalls.jsonl so the supervisor can audit calls uniformly). **R3 COMPLETE — all four
owner-ranked upgrades live.** Next layers when due: TRUE-AGENT-PLATFORM spec (question sequence) +
SI agent-improvement experiments.**
**TRUE AGENT PLATFORM — SPEC LOCKED 2026-07-12 (owner build order): 1) per-agent persistent MEMORY — DONE+verified (each agent's argued positions persist to agent_memory/<id>.jsonl, capped 30; its own last 2 injected into its turns ≤220 chars; isolation verified: agents never see each other's memory; live proof = consistency across days in CI transcripts) →
2) visible TRACK RECORD — DONE+verified v107 (👥 Agents card in Rooms: per-agent turns/rooms/engines/
latest-held-position over 7 days from real transcripts — Scriv leads: 153 turns, 49 rooms, 5 brains;
hit-rate honestly deferred to the initiative layer's decision→outcome links) → 3) INITIATIVE — DONE+verified (when an agent converges a room's DECISION, it may put ONE follow-up
task on the bus, attributed 'agent:<id>', priority-2, capped at 2 open per agent, group-chat excluded;
outcome links from BIRTH: agent_record now counts proposed vs shipped = the real hit-rate; sandbox-
verified incl. cap + refusal + attribution, live bus untouched; LIVE proof = first real initiative
tasks in CI beats) →
3½) PROPOSAL-TIME GROUNDING — DONE+verified: an initiative whose decision mentions a foreign tech
stack is REFUSED before touching the bus (same detector as the audit — one law, two enforcement
points; refusals syscall-traced; sandbox-verified: cargo-decision refused, grounded decision passed) →
4) EXTERNAL ACTION — SPEC LOCKED 2026-07-12: allowed classes (all owner-gated) = repo actions, web
research (read-only), publishing to the hub site; outside-world posting = FUTURE (resource waste now).
PERMANENT PROHIBITIONS from history: NEVER a YouTube comment bot; never keys in output. Open tension
for a later question: 'comment-gated resources' want vs the no-comment-bot law. PILOT BUILT+sandbox-
proven: agent files a repo issue (evidence: >=5 twice-failed dead links -> full draft into the in-app
decide queue -> posts ONLY after owner approval, only from CI, once ever, syscall-traced). Currently
DORMANT honestly: 0 elements meet the dead-link threshold today. ORDER: tutorials overhaul NEXT
(comprehensive — everything essential to the owner's understanding). Explainer written into AGENTIC_OS_STUDY.md §6 per his ask. A/B LAW: DEBATE
STAYS regardless of the judge's tally (auto-flip disabled in code; experiment stays advisory). SI-CONTINUOUS
(owner): self-improvement runs continuously & independently, improving agents AND other agents over time —
a distinct SI branch, possibly its own tab; design next SI wave.** (original thread note:) 'we are using engines; I'm not certain they qualify as true
agents — the system must run on a genuine agent-based platform' → spec via question sequence (per-agent
memory/stance is layer 1; what else makes an agent 'true' — persistence? initiative? tools-of-its-own?).
**SI-ADVANCED (owner):** experiments specifically designed to drive AGENT improvement (not just system
health) — design next SI wave after R3 paging.
**TOKEN-DIET VISIBILITY — DONE+verified v106:** 🥗 card in the Effectiveness tab: both laws, the hard
caps as pills, and per-day turns + ≈tokens/turn from real transcripts (honest read: turns LENGTHENED
after the plain-language switch — the newly wired Caveman no-filler prompt law is the counterweight;
the card exists to watch that line fall). **OPEN-S resolved:** = open-source tools must be usable in-app; umbrella.

**Q-SEQUENCE 2026-07-12 (late): VISUAL/VISUALIZATION boundary HARDENED (owner: keep both) — Visual =
mine OTHER people's designs (action tier), Visualization = OUR screens (decision tier); both mandates
rewritten with explicit hand-over rules; new-room goals carry the boundary (old open rooms close out
naturally). QUEUED BY OWNER ANSWERS: (a) GUARDRAIL FIRING TEST — 'needs to be done firmly to check
everything is working': a test that each G-rule's enforcement point actually triggers; (b) GRAPH
EXPANSION — brain graph must include Q&A/problems/history, 'not all information is in it yet'.**

**Standing checks each tick:** newest room-turn timestamp (beat health) · engine_health.json real HTTP status per
engine · any tier-2.5 auto-added agents · supervisor real_pct + movement + systemcheck + proof.

---

_Original draft below (approved 2026-07-03; phases 0-3 built). Grounded in the 52 goals + James
Goldbach's cortextOS/m2c1/claude-remote-manager patterns + agent-harness research. All visual work =
Fable; the reserved-for-Opus-4.8 track is listed at the end._

## The core insight (why the order is what it is)
Goldbach's own line: **"without the hand-off layer between agents you don't have an OS, you have a tab
pile — and the biggest mistake is skipping shared memory."** EXCAVA today is a beautiful tab pile: a
cockpit + inbox + status, but no real inter-agent hand-off and no shared working memory. **So Phase 0
builds the spine (bus + shared memory + orchestrator) BEFORE any more visual polish.** Everything else
hangs off it.

## The one decision that shapes everything: how "24/7" runs, free
- **Recommended — CRON HEARTBEAT (free):** GitHub Actions cycles every N minutes/hours; agents hand off
  through a file bus; state persists in files; every run resumes where the last stopped. It never stops
  cycling → "always on" in the sense that matters, at zero cost, no machine required (Eitan's PC can't
  stay on). Not sub-second real-time, but continuous.
- **Alternative — ALWAYS-ON runner:** a machine/free-VPS running a daemon (cortexOS-style PM2/tmux) for
  live sub-second hand-offs. More "real" but needs an always-on host = conflicts with free-only + PC-off.
- **Plan assumes the cron heartbeat** unless Eitan says otherwise. Goal 52 (safe 24/7 at full capacity)
  is met on the heartbeat model via the safety mechanisms in Phase 2.

---

## PHASE 0 — THE OS SPINE  (hand-off + shared memory)  · Fable + Python · covers G1,2,6,7,8,13,14,17,18,27,29,30,40
The thing that turns the tab pile into an OS. Build first; everything depends on it.
- **0.1** `data/excava/` store: `bus.json` (task queue + events), `state.json` (shared world facts —
  "what we tried, outcome, decisions"), `agents.json` (registry: 3 tiers + departments, each with a
  scoped toolset), `guardrails.md` (self-extending rules), `handoffs/<task>.md` (per-task memory docs),
  `traces/<run>.json` (per-run decision logs).
- **0.2** `src/excava_bus.py` — bus API: `enqueue`, `claim(agent)`, `handoff(from,to,doc)`,
  `event(kind,payload)`, `read()`; atomic file writes so concurrent lanes can't corrupt it.
- **0.3** `src/excava_agents.py` — registry + a base Worker contract: `name, tier, tools_allowed,
  can_handle(task), run(task, ctx) -> result`. Specialists map to existing lanes (mining, links,
  memory, designs, security, quality); Creators added in Phase 3.
- **0.4** Rewrite `src/excava.py` into the **ORCHESTRATOR**: each cycle → load bus + state + resources +
  gate → route each open task to the best department (specialization + resources + load) → dispatch →
  record a trace → on success write a handoff doc + emit an event; on failure escalate (retry → other
  agent → hold for you). Gate + guardrails enforced on every outward step.
- **0.5** Shared memory wiring: the 900+ vector index is the READ layer every department queries (this
  is literally "uses Excavatortron as its database"); `state.json` is the cross-agent WRITE layer.
- **0.6** Per-task `done_criteria` + `max_steps` + termination — nothing runs away silently.
- **Done when:** two departments pass one task via the bus with a real handoff doc, visible in a trace,
  gate-enforced. Also builds goal 5 (graphify-style self-graph) as a stretch inside this phase.
- ✅ **SHIPPED 2026-07-03** (see SESSION_HANDOFF §3).

## PHASE 0.7 — PROJECT MEMORY MASTER  (added 2026-07-03, owner-directed)  · Python · serves EVERY later phase
**The rule: no AI tool — Claude, EXCAVA agents, Opus, anything — starts a change from scratch.** Every
change starts from what the project already knows about every prior change, however small. Token use
drops because context is RECALLED, not re-derived.
- **0.7.1** `src/project_memory.py` + `data/project_memory/`: an **episode ledger** (JSONL — one line per
  change: when/what/files/why/by-whom) + a **brain graph** (Obsidian/graphify-style nodes+links over
  files↔episodes↔topics, feeding the existing brain tab later).
- **0.7.2** **AUTO ingestion** (owner-chosen mode: auto + manual WHY): every EXCAVA beat ingests new git
  commits + bus traces into episodes — zero effort, never forgotten. Playwright is NOT needed for our own
  repo (it's the extraction engine for Phase 9 sources); the memory master is git+bus based.
- **0.7.3** **Manual WHY contract**: `PROJECT_MEMORY.md` at repo root instructs every AI tool: (a) BEFORE
  changing anything, run `python -m src.project_memory recall "<topic/files>"` and start from that; (b)
  AFTER a meaningful change, log one WHY line via `python -m src.project_memory log ...`. EXCAVA's own
  agents obey the same contract through the bus (hand-off docs double as episodes).
- **0.7.4** Recall returns a compact **context pack** (recent episodes touching those files/topics +
  linked graph nodes + the relevant hand-off docs) — small enough to paste anywhere, incl. non-Claude tools.
- **Done when:** `recall` answers "what happened around X?" correctly for the last 30 days of real
  history, and the beat auto-ingests without growing unbounded (pruning/rollup included).

## PHASE 1 — YOU DRIVE IT  (task intake + control)  · Fable UI + Python · covers G4(part),5,19,24,42,46,52g
- **1.1** Multi-channel task send (G46): keep the JSON inbox; add a cockpit **"Send EXCAVA a task"** form
  (writes to the bus); leave a clean seam for a future remote channel (G4).
- **1.2** **Priority-weights dial** (G42): `data/excava/weights.json` + cockpit sliders ("care more about
  links vs designs right now"); the orchestrator's routing respects them.
- **1.3** **Kill switch + safe-mode** (G52g): a flag file EXCAVA reads FIRST each cycle; safe-mode =
  internal-only; stops cleanly mid-task, no corruption.
- **1.4** **Approval queue + categories** (G5,19,24): `data/excava/approvals.json`; external + spend
  actions land here; one reusable cockpit approve/reject widget used everywhere.

## PHASE 2 — SAFE 24/7 AT FULL CAPACITY  (goal 52 + supports)  · Python + Fable readouts · covers G9,16,21,32,33,36,39,51,52a-h
- **2.1 Resource arbiter / leases** (G32,52a): an agent must acquire a lease on a key/quota before use;
  hard daily ceilings that hold over days/weeks; auto-release on done. No runaway spend, ever.
- **2.2 Cost/usage per department** (G39): each department logs quota use → state → cockpit.
- **2.3 Crash recovery + checkpointing** (G7,21,52d): tasks idempotent + resumable; an interrupted task
  is re-claimable; checkpoints in `handoffs/`.
- **2.4 Rate-limit/backpressure + self-healing** (G51,52f): on 429/block → backoff → switch engine →
  pause that lane; honors the residential-backfill rule (never burst → escalating IP block).
- **2.5 Continuous self-audit** (G52h): a cycle that verifies gate + guardrails are still intact; alerts
  on drift — autonomy can't silently widen at 3 AM.
- **2.6 Memory pruning/retention** (G16,52b): consolidation cycle + prune stale bus/trace entries so 24/7
  running never bloats/slows.
- **2.7 Rollback of EXCAVA's own code** (G33): tag last-known-good; a self-improvement that breaks a
  self-audit auto-reverts.

## PHASE 3 — CREATORS DEPARTMENT  (the big capability)  · Python + free-LLM + gated Claude · covers G10,11,15,28,34,47 + full Creators scope
- **3.1 Gap radar**: `data/excava/gaps.json` fed by inbox failures (your hits, weighted 2×), coverage
  holes, competitor deltas, trend scan, and "important capabilities no tool/skill/MCP/format covers."
- **3.2 Creator agents produce** (your full scope): new skills / prompts / formats / MCP scaffolds /
  design concepts **and** new information sources, new plans, faster self-improvement proposals, risk
  plans, upgrades to existing info, trend finds, tasks for linked projects — each a **DRAFT** into a
  review queue, never live. Bar: **fast AND high-quality** (small time, high quality; no day-long slogs).
- **3.3 Quality gate** (G15,34): self-test (skill runs / scaffold compiles / prompt hits its goal) →
  **canary** on one small real case → your **1-click review**.
- **3.4 Zero-touch shipping** (G47): an approved draft auto-commits + activates, no leftover manual steps.
- **3.5 DISCOVERY scoping step** (G28): a creator states its plan (a decisions file) before it executes.

## PHASE 4 — CONNECTORS MADE REAL  (your explicit complaint)  · Python + sandbox · covers connectors-fix, G13, G43
Audit already done: **1,065 of 1,133 connectors (94%) have an empty install field; the rest are the
placeholder string `activator: add "X"`** — almost nothing is truly wired. Fix:
- **4.1 Resolver**: for each connector, find the REAL install (repo `package.json` bin, npm name, MCP
  registry, README) → produce an actual `claude mcp add <slug> -- npx -y <pkg>` (or config block).
- **4.2 Verify + sandbox test-run** (G43): actually run it in an isolated box (no secrets, no data
  network), confirm it starts/responds; store `verified: true/false` + evidence. **This also delivers the
  real behavioral simulator from your original security ask.**
- **4.3 Shrink the tab** to verified/runnable (quality > quantity, like Designs); unverified become
  "candidates," not shown as real.
- **4.4 EXCAVA-as-MCP-server** (G13): expose the hub so Cursor/ChatGPT/etc. call INTO Excavatortron.

## PHASE 5 — THE LIVING OS  (crew v2 + cockpit)  · ALL FABLE · covers G3,10,20,22,23,29,38
- **5.1 Residents = real agents 1:1** (G22): each resident bound to a real department on the bus;
  click → its real task queue + last trace + status. No more mascots.
- **5.2 Interaction** (G38 + your ask): click → menu (run its lane now · show its report · **delegate a
  task to just this department**); optional typed delegate to one resident.
- **5.3 Work animations + maintenance mode + special visitors** — all driven by REAL bus events (a
  milestone, a draft approved, a lane hot with changes → sky-creatures repair), not random.
- **5.4 Fleet-health vs control** as two separate views (G20).
- **5.5 Bus-driven bubbles** (G29): one source of truth feeds cockpit + residents.
- **5.6 Trace viewer** (G10,38): "why did you pick X over Y" answered from the real trace.

## PHASE 6 — DIRECTION LOOP + THE 10 ALIGNMENT SYSTEMS  (keep it to YOUR will)  · Fable + memory · covers direction-loop(missed), 10-systems, G18,36
- **6.1 The Direction area** (the item I MISSED, now first-class): a cockpit panel where **you state
  direction**; EXCAVA **previews "here's what's about to be done" before major changes**; a real
  **back-and-forth** ("is this the direction? yes/no/adjust"); **after every major change, an in-dashboard
  TUTORIAL** of what changed (walkthrough, not a changelog line); **feature-activation toggles** (turn
  parts of the project on/off yourself).
- **6.2 The 10 systems** that continuously pull the project to your will — I propose, you confirm/swap:
  (1) direction-loop · (2) self-extending guardrails · (3) a DISCOVERY decisions-file per initiative ·
  (4) priority-weights dial · (5) goals-as-law re-score · (6) approval queue · (7) change-tutorials ·
  (8) proactive digest · (9) a memory-audit at session start · (10) source trust-scores.
  **→ You told me to build toward YOUR list: name 2-3 and I'll finalize the 10.**

## PHASE 7 — PORTABILITY + HARNESS-AS-PRODUCT  · Python · covers G25,26,31,35,41,44,45,48,49,50
Portable harness (G35 — run EXCAVA on Budoaris/FreeDup, not hardcoded paths) · trust scores per source
(G45) · scoped credentials (G31) · deprecation protocol (G41) · version-compatibility matrix (G44 —
**closes the P6 "version-tracking" leftover**) · recurring source-scan for new creator patterns (G26) ·
provider-agnostic runtime (G25) · event-condition-action rules (G48) · auto env/dependency provisioning
(G49) · automated recurring structured reports (G50).

## PHASE 8 — NORTH STAR + P/F CLEANUP  · Fable + Python
- **8.1** Add **G9 "Agency / Orchestration"** to the North Star (or reframe G4) and re-score all goals
  incl. 52; goals stay law, checked every cycle.
- **8.2** Close remaining **P6 leftovers**: version-tracking (via G44), weekly digest (via G50), public
  SDK (via G13 MCP), auto-test tools (via G15).
- **8.3** `formats.json` → a "Formats" filter inside the Designs tab; brain white-node + title-collision
  cleanup (known P-plan gaps).

## PHASE 9 — OMNI-SOURCE INTAKE  (added 2026-07-03, owner-directed)  · Python + Playwright/agent-reach · feeds G1
**Extract capability-knowledge from beyond the playlist**: YouTube-outside-playlist, Instagram, TikTok,
LinkedIn, X/Twitter, Reddit, Facebook, Telegram, AI WhatsApp groups, and general whole-internet search.
Owner decision 2026-07-03: **public-only, free** (no logins/cookies for now); toolkit assist =
**agent-reach** (MIT, ~26k★, keyless CLI for web/GitHub/YouTube/RSS/X-read; its Reddit/IG/FB paths need
logins → skipped). Every intake passes security_preflight + the trust-score gate before touching the hub.
- **TIER 1 (buildable now, keyless):** Reddit public JSON · Telegram public channels (t.me/s previews) ·
  DuckDuckGo/SearXNG whole-web search · YouTube-beyond-playlist (existing free API key, search quota) ·
  RSS (already live) · X/Twitter read-only via agent-reach/nitter mirrors (flaky, best-effort) ·
  arbitrary-page reading via agent-reach's Jina Reader.
- **TIER 2 (needs owner action, still free):** WhatsApp groups via manual chat export (.txt dropped in
  repo — no free API exists) · Exa search free signup (optional; DDG is the no-signup fallback).
- **TIER 3 (locked, declined for now):** Instagram/TikTok/Facebook/LinkedIn feeds need account
  cookies/sessions → revisit only if Eitan later opts in (D-source decision parked in QUESTIONS.md).
- **9.1** `src/mine_social.py` + `data/social_sources.json` (which subreddits/channels/queries — owner
  fills over time) → intake lane in the **mining department**, daily workflow, everything gated.
- **9.2** Playwright renders JS-heavy public pages in CI when plain HTTP fails (also the seed of the
  Phase-4 sandbox test-runs).
- **9.3** Source **trust-scores** (D2 pick) gate what intake may touch; per-source coverage shows on the
  Sources tab.
- **Done when:** ≥3 tier-1 sources feed real, gated items into the hub on a daily cadence.

---

## RESERVED FOR OPUS 4.8 (not Fable — data/logic accuracy)
- SKILL.md / activator actually functioning end-to-end (still broken).
- "Open code" (github.dev) button broken → fix.
- Dashboard preview loads in **<3s**, with **Arena images prioritized**.
- Data-retrieval quality/accuracy improvements + anything Fable built that's inaccurate.

## SEQUENCING (status 2026-07-03 evening — one-day sprint through the spine)
0 ✅ → 1+2 ✅ → 0.7 ✅ + 5 ✅ (job-menus/visitors open) + 9-tier-1 ✅ → **3 ✅ (creators live under
G-12: labeled + test-before-run; PACKAGES = owner's term for multi-element bundles) + 4 ✅ machinery
(sandbox test-run EVERYTHING per owner — 6-hourly CI batches walking all 1,142; tab shrinks as passes
land)** → **6 partial ✅ (direction-loop + change-tutorials LIVE — cockpit card, issue channel, beat
acknowledgment, tutorial audit; remaining 8 systems + HORSE fan-out open)** → 7 (harness documented
portable per owner "skip porting"; runtime/rules-engine/meta-brain open) + 8 partial (G9 ✅ scored;
formats-filter, brain-cleanup, token-split open) → 9 tiers 2-3 as unlocked. Link-coverage keeps
climbing the whole time. Every build ships a change-tutorial (data/tutorials.json — enforced by the
beat's tutorial audit).

## GOAL → PHASE MAP (traceability, all 52)
P0: 1,2,6,7,8,13(seed),14,17,18,27,29,30,40 · P1: 5(control),19,24,42,46,52g · P2: 9,16,21,32,33,36,39,51,52a-h ·
P3: 10,11,15,28,34,47 · P4: 13,43,connectors · P5: 3,10,20,22,23,29,38 · P6: 4,direction-loop,10-systems ·
P7: 25,26,31,35,41,44,45,48,49,50 · P8: North-Star/G9, P6-leftovers, formats, brain-cleanup. (5 = the
graphify self-graph, seeded P0, finished P4.)

## ASK-CHECKPOINTS (built into the plan — NON-BLOCKING; proceed on the default if no answer)
Eitan wants questions asked at the right moments but does NOT want to babysit. So each phase has a
checkpoint: ask (park in QUESTIONS.md), proceed on the stated default, adjust when he answers.
- **P0 start:** D1 — cron-heartbeat (default) vs always-on.
- **P1:** which action categories always require approval? _Default: external + spend._
- **P2:** the hard free ceilings (quota caps). _Default: current per-key free budgets._
- **P3:** Creators review-queue UX + what may auto-ship. _Default: self-test + canary + your 1-click; nothing auto-ships._
- **P4:** confirm the connectors tab shrinks to verified-only (D5). _Default: yes._
- **P5:** special-visitor triggers + per-department animation vocabulary. _Default: my picks, tune on feedback._
- **P6:** name 2-3 of your "10 systems" (D2). _Default: my proposed 10._
- **P7:** which linked project to make the harness portable to first. _Default: Budoaris._
- **P8:** the G9 goal name + whether to re-weight the North Star. _Default: "Agency/Orchestration", equal weight._

## OPEN DECISIONS
- **D1 ✅ ANSWERED 2026-07-03: cron heartbeat.** Phase 0 built on it same day.
- **D2 ✅ ANSWERED 2026-07-03: direction-loop + change-tutorials first**, delivered as DEEP integration
  ("like a daemon for the entire project, not something casual, like in cortexOS — a clean daemon part
  of the OS that connects, or full integration") + HORSE-style fan-out pulled into Phase 6 scope.
- **D3 (default: one program, per-phase ask-checkpoints running)** — proceeding on default.
- **D4 (default: spine-first, cleanup in P8)** — proceeding on default.
- **D5 (default: yes, shrink connectors to verified-only)** — proceeding on default.
- **D6 (new): locked social sources (IG/TikTok/FB/LinkedIn feeds) need your cookies — opt in ever?**
  _Default: no; public-only stands._

---

## GOALS 53-56 — added from the 2026-07-02 internet gap-audit (real, important, were missing)
Sourced from 2026 multi-agent production research (arxiv orchestration survey, Microsoft Agent Governance
Toolkit, futureagi/Galileo observability + A2A writeups). These are the failure modes that kill real
agentic systems — and they weren't in the 52:
- **G53 — Handoff state-validation (HIGH).** The single hardest multi-agent bug is the *silent partial
  completion*: an agent reports "success" but passes CORRUPT state downstream, and the error cascades
  silently. Every hand-off on the bus must VALIDATE the handed-off state against the task's contract
  before the next agent accepts it. Without this, 24/7 autonomy quietly rots the data. → **Phase 0** (bus
  contract) + **Phase 2** (self-audit catches drift). *Why it matters: this is exactly how an unattended
  system breaks without anyone noticing.*
- **G54 — Verifiable execution (HIGH).** Proof an agent actually DID the thing, not just claimed it
  (file really written / MCP really responds / links really resolve) — checked by the system, not taken
  on the agent's word. → **Phase 0** (every result carries evidence) + **Phase 4** (connector proof).
  *Why: pairs with G53 — "trust but verify" is the only safe basis for autonomy.*
- **G55 — Human-oversight ergonomics (HIGH, and personal to you).** Research names *alert fatigue* and
  *automation bias* as the top ways human oversight fails — you rubber-stamp approvals or drown in pings
  and stop really overseeing. Since you're "in and out a lot," EXCAVA must surface decisions BY RISK
  (batch the trivial, foreground the consequential), each with a one-line "why you're being asked," and
  never cry wolf. → **Phase 1** (approval queue design) + **Phase 6** (direction loop). *Why: without
  this, all the approval gates become theater.*
- **G56 — Immutable audit trail / governance log (MEDIUM, ties to G7).** A tamper-evident record of who/
  which-agent/when/why for every action — Gartner attributes ~40% of agentic-project cancellations partly
  to inadequate risk controls. → **Phase 2** (append-only log) + surfaced in **Phase 5** trace viewer.
  *Why: for a security-conscious owner, "what did it do while I was away, provably" is the trust backbone.*

## Considered but NOT adopted now (with reasons — so we're deliberate, not ignorant)
- **OpenTelemetry / GenAI semantic-convention tracing** — the enterprise standard for agent observability.
  *Not necessary now:* our custom traces + the Phase-5 trace viewer already give full legibility for a
  single-owner free system; OTel is interop plumbing for multi-team/multi-vendor stacks. Revisit only if
  EXCAVA ever needs to feed an external monitoring tool. (Low cost to add later.)
- **A2A (Agent2Agent) protocol** — Google's cross-vendor agent-interop standard (Apr 2025, still thin in
  production). *Not necessary now:* our internal file-bus handles our own agents, and **G13 (EXCAVA-as-
  MCP-server)** already lets outside tools reach in. Adopt A2A later IF you want EXCAVA to talk to
  third-party agent *systems* (not just tools). Watching it, not building on it yet.

## COVERAGE AUDIT — honest: what was under-placed, now fixed
Cross-checked the plan against all 52 goals, the P0-P7 plan, the F1-F4 plan, and the remember-later
roadmap. Gaps found and now closed:
- **G12 (12-phase brain-dump→deployed pattern)** — was in the goals list but missing from the phase map.
  → now **Phase 3/7**: it's the literal path for "build MY things" (Budoaris/FreeDup).
- **G37 (agent conflict resolution over shared files/resources)** — missing from map. → now **Phase 0**
  (bus locking) + **Phase 2** (lease arbiter).
- **HORSE** (named ~10-agent fan-out → merge-by-base-values → trigger word) — the mechanisms existed
  (G13 sharding, G19 debate) but the *named feature* wasn't a step. → now explicit in **Phase 3**.
- **Split token-reduction into 2 skills (heavy/light)** — discrete deferred task, was MISSING. → **Phase 8**.
- **Meta-brain of all Excavatortron history/conversations** — was MISSING. → **Phase 7** (ingest
  transcripts/commits/decisions → queryable store; extends the semantic memory).
- **Per-tab self-improvement (split self-improvement into per-tab sub-systems)** — was MISSING (only the
  source-hunting half, G26, was placed). → now **Phase 7**.
- **Unified personal preference model / taste beyond designs (G8 depth)** — G8 is a scored goal but had
  no BUILD step. → now **Phase 6** (extend Arena taste to tools/stacks/plans).
- **Activator 30-question overhaul + live examples** — the activator *fix* is Opus 4.8's; the 30-Q
  *overhaul process* wasn't placed. → **Phase 8**, run as the 30-MC-question step per your stated process,
  after the core program.
- **Run-a-repo-DIRECTLY (opensrc + pre-prepared ready-to-run env / "active mode" run link)** — was only
  partial via P4 sandbox. → now explicit **Phase 4** (pre-prepare env so a click OPENS a running thing).
- **LiteLLM routing / 429 waste** — its PURPOSE is fully covered by **G25 (provider-agnostic runtime) +
  G32 (resource-lease arbiter)**; noting explicitly so it's not seen as dropped.
- **Links → ~100%** — runs as an ongoing background track through ALL phases (not a discrete phase); the
  autonomous resolver keeps climbing while the rebuild happens.
- **F2 activation "actually does setup"** — its CORE (SKILL.md/activator working) is on the **Opus 4.8
  track**; EXCAVA's orchestration (Phase 3) drives it once Opus makes the activator function.

### Coverage audit — ROUND 2 (2026-07-02b): 3 more that were implicit, now explicit
- **Dynamic departments (FULLY AUTONOMOUS)** — your installment-2 answer; EXCAVA opens/closes departments
  itself within resource limits. → **P0** (agents registry supports spawn/retire) + **P3** (it decides
  when a new dept is needed, within the lease ceilings) + **P5** (visible birth/death on the floor).
- **Crystallize repeated patterns into skills** — roadmap behavior: any system/suggestion used a lot gets
  turned into an auto-running skill, and EXCAVA keeps producing+running such skills as it progresses. →
  **P3 Creators** (a standing generator, not just gap-filling).
- **Beyond-the-project capabilities** (installment-1: the OS does "a lot of other things") — **build MY
  things** (Budoaris/FreeDup/new ideas, via the G12 12-phase pattern) → **P7**; **research & briefs** →
  **P3**; **daily ops** (digests/monitoring/reminders) → **G50 + G36** (P2/P7). Content/publishing stays
  gated (not selected).

**Result: all 52 goals + G53-56 + the P/F plans + every remember-later item + all scattered requests now have an explicit home.**
The only intentionally-unbuilt items are the two above (OTel, A2A) with stated reasons, and anything
gated on decision **D1** (always-on) for full remote control (G4).
