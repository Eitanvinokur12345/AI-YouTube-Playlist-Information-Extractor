# EXCAVA — the complete program (multi-agent orchestrator + harness over Excavatortron)

_Draft for approval. Nothing here is executed until Eitan approves. Grounded in the 52 goals + James
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

---

## RESERVED FOR OPUS 4.8 (not Fable — data/logic accuracy)
- SKILL.md / activator actually functioning end-to-end (still broken).
- "Open code" (github.dev) button broken → fix.
- Dashboard preview loads in **<3s**, with **Arena images prioritized**.
- Data-retrieval quality/accuracy improvements + anything Fable built that's inaccurate.

## SEQUENCING
0 (spine) → then 1 (control) + 2 (safe 24/7) together → **5 early** (so you SEE the spine working) →
3 + 4 (capabilities) → 6 (alignment) → 7 + 8 (breadth + cleanup). P0 link-coverage keeps climbing the
whole time. Each phase ends with a change-tutorial (Phase 6 mechanism) so you always know what shifted.

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

## OPEN DECISIONS (answer any; work can start on P0 regardless)
- **D1 (biggest):** cron-heartbeat 24/7 (free, recommended) or pursue an always-on runner?
- **D2:** name 2-3 of your "10 systems" so I finalize the set (Phase 6.2).
- **D3:** approve as ONE program, or ship it in the sequenced sub-programs above (approve each)?
- **D4:** should this whole rebuild jump ahead of P6-leftovers/formats/brain-cleanup, or after? (Plan
  currently interleaves; P8 does cleanup last.)
- **D5:** connectors — after Phase 4 the tab likely SHRINKS a lot (only verified ones shown). OK?

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

**Result: all 52 goals + G53-56 + the P/F plans + every remember-later item now have an explicit home.**
The only intentionally-unbuilt items are the two above (OTel, A2A) with stated reasons, and anything
gated on decision **D1** (always-on) for full remote control (G4).
