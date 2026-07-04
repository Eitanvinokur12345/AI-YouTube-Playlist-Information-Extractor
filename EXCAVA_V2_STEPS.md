# EXCAVA v2 — STEP-BY-STEP EXECUTION PLAN (the "do" doc)

_Companion to `EXCAVA_V2_PLAN.md` (why) + `EXCAVA_V2_ADDITIONS.md` (the finalized interview answers,
which this doc now folds in). Every task = **Build** (files/what) + **Done when** (acceptance). Order
is strict within a milestone. Fable does everything except **[OPUS]**; **[OWNER]** = an action from
Eitan (never blocks). Every task: recall-before-change, log the WHY, obey `PROTOCOLS.md`, free-only._

**Global rules folded in from the interview:**
- **CORE = SPOT-ON is priority #1** (the M1.C block below); retrieval depth is the single biggest fix.
- **Claude runs autonomously on Eitan's Pro** via `CLAUDE_CODE_OAUTH_TOKEN_REAL` (already wired), so
  **[OPUS] tasks can run in CI too** — budgeted to highest-value work, premium-marked.
- **Designs have NO approval gate** — Fable creates, Eitan reviews the result (samples shown, not pre-approved).
- **Every milestone ships an INTERACTIVE tutorial + an explainer video + podcast**, bumps `APP_BUILD`+`sw.js`,
  verifies in preview, commits.

---

## M1 — REAL / VERIFIED ELEMENTS + ACCESS  (+ the SPOT-ON core)
Nothing on any tab is dead or fake, everything is deep + accurate, and you can open/run/use it.

### CORE (priority #1 — runs continuously, folds through M1)
**M1.C1 — Retrieval depth (THE #1 fix).** Build: `src/deep_retrieve.py` — re-analyze every element from
its **FULL source** (whole transcript / repo README + docs) **+ enrich from ≥1 other source**; explicitly
recover things currently **missed from the playlist or unfindable online**. Done when: every kept element
has full-source + ≥1 enrichment source; stub-rate ≈ 0.
**M1.C2 — The discovery agent (hourly, everywhere).** Build: `src/discovery_agent.py` + hourly workflow —
scan GitHub trending/new + release feeds · HN/Reddit/X · Product Hunt/awesome-lists · official + company +
national releases · **every social network via agent-reach** · the playlist. New items → the gated intake
queue; inclusion = **AI-relevant + a quality signal** (stars/activity/real README). Done when: a brand-new
notable tool/repo lands in the hub **same-day**; the agent runs hourly.
**M1.C3 — Verify, re-verify, reconcile.** Build: verification = **cross-check ≥2 sources + a live link/
install test**; **rolling re-check (weekly) + on-access**; conflicts → **reconcile, keep best-supported,
note the conflict**; a **minimum enrichment + verification bar** — below it an item is **"unverified",
never shown as real**. Done when: real items carry 2-source proof; stale/changed items get caught; conflicts flagged.

### Access
**M1.0 — Unified element model.** Build: `data/schema/element.json` (id, type, name, what, source_videos,
links{website,github,open_code}, install, verified{status,method,at,log}, trust, related, video_bundle,
created_by); `src/element_model.py` normalizes every per-type file → read-only `data/elements_index.json`;
`set_field()` writes back to the owning file only. Done when: `--count` prints per-type totals + a sample;
no source file mutated except via `set_field`.
**M1.1 — Finish connector sandbox verification (all 1,142).** Build: keep `verify_connectors.yml` (6-hourly,
30/batch, tree-kill fix); add `--catchup 60`; npm+pip preflight. Done when: `connectors_verified.json.summary.checked == total`.
**M1.2 — Verify ALL element types.** Build: `src/verify_elements.py` — URL/repo → parallel HEAD liveness;
MCP/repo → sandbox runner; skills/prompts/formats → schema + `security_preflight`; **feeds the ≥2-source +
live-test standard from M1.C3** → `data/elements_verified.json`; `verify_elements.yml`. Done when: every
element carries `verified{status,at}` at the M1.C3 standard.
**M1.3 — Trust gate + "dead only" pruning (P3).** Build: join `source_trust.json`; status ∈
verified|unverified|niche|dead; **only dead (link+install+sandbox all fail) is hidden**; **never delete for
low rating** (keep niche); items under the M1.C3 min-bar show as **unverified**, not real. Done when: a
low-rated-but-working niche element stays visible; only dead ones hide.
**M1.4 — The per-card ACTION ROW.** Build: `elementActions(el)` → **Activate** (recipe+copy now, real setup
in M4), **Open** (github.dev/Codespaces/hosted MCP — a real runnable target), **Use for a task** (opens the
console prefilled), **Video**, **Video bundle**, **Source**. Done when: every card shows the row; Open opens
a runnable target; Video plays.
**M1.5 — The <10s pre-warm / open.** Build: `src/prewarm.py` keeps top-N repos/MCP warm (`data/prewarm.json`);
Open = instant if warm, else the **pancake-warming** animation + progress <10s. Done when: warm = instant;
cold resolves <10s (timed in preview).
**M1.6 — Element DETAIL view.** Build: `renderElement(id)` at `#element/<id>` — what it is, embedded
video/bundle, how-to, verified status, action row, related, use-for-task. Done when: any element opens a full page.
**M1.7 — RELATE (related rows).** Build: `src/relate.py` — related from memory-graph topics + same source
video + co-occurrence → `related[]`. Done when: each detail shows 3–8 real related elements.
**M1.8 — Dashboard reads the unified index.** Done when: all tabs render from `elements_index.json` with
verified/trust badges; no console errors.
**M1.9 — Ship M1.** Done when: interactive tutorial + explainer video/podcast + build bump + preview-verified + committed.

---

## M2 — REAL AGENTS CONVERSING + PRODUCING
Agents get real engines; their work is a visible conversation that produces artifacts.

**M2.0 — `PROTOCOLS.md` + self-audit.** Build: write P1–P14; extend the beat `_audit_spine()` to check it;
drift → SAFE mode. Done when: beat prints "audit OK vs PROTOCOLS.md"; deleting a rule trips SAFE.
**M2.1 — The engine layer (existing engines KEPT first-class; OmniRoute ADDED as a central option, not a
replacement or sole path).** Build: `src/excava_engines.py` keeps the **9 already-wired free families**
(Gemini ×6 · Groq ×2 · Cerebras ×2 · OpenRouter incl. **free DeepSeek R1 / Qwen3 Coder** · NVIDIA Nemotron ·
SambaNova · Mistral · GH-Models) as **first-class, directly-callable** engines, **+ self-hosted Hermes**
(Ollama/Pi) **+ Claude via the Pro OAuth token** (budgeted, premium-marked). **OmniRoute is ADDED alongside
them as an additional, central routing option** (never replacing them, never the only path): a free
self-hosted OpenAI-compatible gateway that fronts 160+ providers with **4-tier fallback (Subscription →
API-key → cheap → free)** + **token compression (15–95%)** + **90+ free tiers (~1.6B free tokens/mo)**.
`pick_engine(dept,difficulty)` may route **via OmniRoute** (central smart-routing + compression + widest free
reach) **or call an engine directly** — configurable per department; **direct calls always work if OmniRoute
is off or down**. Done when: `--selftest` returns real completions **both directly AND via OmniRoute**, and
turning OmniRoute off still works.
**M2.1a — [OWNER] Confirm keys (already added).** Eitan's ~20 secrets are already in the repo; run
`engine_selftest.yml` to confirm which families answer. **No new purchase.** Done when: the selftest report
shows the live set.
**M2.1b — External free tools (OPTIONAL — Fable/EXCAVA self-configures; no manual owner step required).**
**OmniRoute** — OPTIONAL central gateway (`npm install`, port 20128; per-CI-run or on a host). Eitan
installed it locally 2026-07-05 (it runs) but left the provider-key step; **Fable wires it up autonomously
later**, so no owner action now. **OpenClaw** (channels/browse/shell), **agent-reach** (M1.C2 discovery
reach), optional **Ollama/Hermes** + **Raspberry Pi** — all likewise Fable-set-up, deferred until needed.
Done when: each is reachable from a run whenever Fable brings it online; nothing here blocks M1–M4.
**M2.2 — Lease arbiter + budgets.** Build: `src/excava_leases.py` — per-dept daily token budget, hard
ceilings, per-engine RPM caps, **+ a tight Claude/Pro budget** so automation never eats Eitan's Desktop quota.
Done when: a department at budget is held+traced; Claude usage stays within its daily cap.
**M2.3 — The agent roster (named leads + workers).** Build: rewrite `agents.json` — per department 3–5 agents
`{name,engine,specialty,role∈doer|checker|improver,tier}`; **~11 distinct NAMED leads** with personas
(suit-and-tie), generic workers; **personality matches the department** (security = paranoid guard, creators =
eccentric inventor, links = meticulous librarian) and **affects tone AND behavior** (a cautious agent verifies
more); tone = characterful-but-competent; **EXCAVA proposes the cast, Eitan tweaks**. Borrow SOUL.md /
agency-agents patterns. Done when: `--roster` prints the named cast with engines+roles+personas.
**M2.3b — OpenClaw as a tool.** Build: expose OpenClaw's channels (WhatsApp/Telegram/…), browse/forms/shell,
and Canvas as scoped tools agents may call. Done when: an agent completes a task using an OpenClaw capability, traced.
**M2.4 — Agents vs workers.** Build: persistent AGENTS spawn ephemeral WORKERS (temp id → one unit → report →
dissolve); `state.json` tracks live workers. Done when: a task shows an agent dispatching workers that finish
and vanish, traced.
**M2.5 — The conversation engine.** Build: `src/excava_chat.py` — `Room(kind∈dept|cross|group|war, goal,
max_turns, done_criteria)`; agents take turns via real engine calls, with **productive debate then converge**
(a checker can push back on a doer before the room decides); messages → `data/excava/chats/<YYYY-MM-DD>/<room>.jsonl`.
**War rooms are the showpiece.** Done when: a room runs a real multi-turn debate ending on its done-criteria;
archived by day; replayable.
**M2.6 — Conversations produce artifacts.** Build: a room ends by calling a scoped tool (resolve-links / draft
an element / assemble a package); artifact committed + linked from the transcript. Done when: one war room
produces a real committed artifact you can open.
**M2.7 — Wire into the beat (24/7 + live, parity).** Build: each beat advances top rooms (bounded turns);
dashboard-open runs more turns in-browser via the same engines; identical code path. **Fully parallel, NO
concurrency cap** (it stays legible because it's organized by agent/department/room with drill-down); a
**visible timing readout** on the floor; **creations may take a while but never > ~1 hour (target < 30 min)**,
while **anything Eitan-facing responds fast**. Done when: rooms progress every CI beat unattended; opening the
dashboard accelerates them; output identical either way; timings visible.
**M2.8 — Self-improvement department (real).** Build: `src/excava_selfimprove.py` — agents review
prompts/engines/routing/hub/own-code; safe changes auto-apply+test; overhaul/new-tool/deeper-access → a PITCH.
The **strict quality bar applies to things EXCAVA CREATES** (small prompts/commands may be light). Done when:
≥1 real safe self-improvement + ≥1 pitch, both visible.
**M2.9 — Ship M2.**

---

## M3 — NEW SHELL + LAUNCHER + FULL DESIGN  (all Fable · NO approval gate)
It looks and feels like a real, professional product; the living workshop is real.

**M3.0 — Design system (direction DECIDED — build it, show samples, don't gate).** Build: `docs/design/tokens.css`
+ primitives + gallery, to this direction (ADDITIONS §I): **refined Heavy-Machinery + playful + clean-tech
touches**; **yellow + warm ink, real metal framing, pockets of greenery**; **light default, dark optional**;
**spacious**; **bold industrial** display + clean body; **refined-neobrutalist ≈ textured-industrial** finish;
**rounded, organic, characterful shapes** (no plain circles/squares); **bespoke line icons**. Done when: tokens
+ gallery render in that look; **Eitan sees it, no pre-approval blocks the build**.
**M3.1 — The app shell.** Build: new `index.html` — left sidebar + top bar (search, EXCAVA, account/settings/
shortcuts); migrate tabs in. Done when: sidebar+topbar+search work; feels like a real product; zero console errors.
**M3.2 — Monster art (samples first, no pre-approval).** Build: 11 species + agent/lead(suit-and-tie)/worker(small)
variants via image-gen (free-first) → `docs/assets/monsters/`; **friendly-but-distinctive with a cool/edgy edge**,
each **matched to its department**. Fable **shows Eitan a sample set** to judge quality, then proceeds. Done when:
11 distinct species; leads/workers distinct.
**M3.3 — Isometric factory floor (+ side cutaways).** Build: `docs/floor/` — **isometric** stations/buildings,
monsters walking, wired to real bus/room state, with **side-view cutaway moments** when you enter a department.
Done when: floor reflects real activity; stations open departments; cutaway on entry.
**M3.4 — Animation catalog.** Build: ~11 animations (fix=weld, build=hammer, test=magnifier, verify=stamp,
deliver=celebrate, research=dig, make-media=film, hand-off=carry parcel, pitch=wave, idle=rest, open=pancake-flip),
each from the real action; overall **lively but purposeful** (floor alive, elsewhere event-driven). Done when:
every action type plays its distinct animation from real events.
**M3.5 — Messenger chat UI.** Build: department channels rail; bubbles with monster avatars + "agent · engine"
badges + day dividers; **war-room round-table** (showpiece); open-room hall. Done when: you read any room's real
conversation, scroll by day, see who+engine per message.
**M3.6 — Element card + detail (final visual).** Build: apply the design system; compact card, actions on hover,
badges. Done when: cards match the system; actions on hover.
**M3.7 — Results feed.** Build: filterable by day/department/sub-agent; result card = what/preview/open/use/
send-to-project; also inline in the making-chat + "new" badge on the tab. Done when: real artifacts appear,
attributed, openable, in all three places.
**M3.8 — North-Star constellation.** Build: Excavatortron centered; **9 goal-stars** orbit (rotating), each
distinct, meaning below; live scores. Done when: shows live scores; each star opens its goal.
**M3.9 — Brain graph (relate, full).** Build: interactive element+link graph; click to explore; cluster → a
package. Done when: navigable; a cluster becomes a package.
**M3.10 — Direct EXCAVA console (full bar + floating).** Build: `#excava` **hero console like the screenshot** —
engine/agent selector · mic · attach file/task · "+" context · slash-commands for triggers (NOSG/HORSE/PLAN/
RESEARCH/WATCH); opens with the away-digest; **streams like a chat and dispatches** to departments; plus a
context-aware **floating quick-ask on every tab**. Done when: typing a task dispatches it and EXCAVA replies;
floating ask works on any tab.
**M3.11 — Steering (direction, pitches, notifications).** Build: direction card (state → EXCAVA's reading);
dismissible "needs your approval in ___" banner; bell+count; a monster walks up on new approvals; pitches as
conversations. Done when: a pitch shows the banner, opens as a conversation, approve/decline works.
**M3.11b — Editable taste panel.** Build: a visible, editable taste profile — **separate design-taste vs
work-taste**, learned + explicit; feeds HORSE merges + designs. Done when: you can view/tune your taste weights.
**M3.12 — Mobile pass.** Build: responsive shell — read/review/approve/send on phone; execution disabled on
phone. Done when: phone shows chats/results/approvals + send; no run buttons.
**M3.13 — Ship M3.**

---

## M4 — ACTIVATOR END-TO-END + LAUNCHER
Know→do works anywhere; EXCAVA proven real by agency + goal→package.

**M4.1 — [OPUS] Portable activator.** Build: `src/build_activator.py` → `activator/SKILL.md` — compressed hub
snapshot (elements + package recipes + PROTOCOLS + triggers) AND a live-EXCAVA fetch path; obeys NOSG/HORSE/
PLAN/RESEARCH/WATCH; runs an uploaded task offline; daily rebuild. Done when: uploaded to a second tool, it
finds/builds a package and runs a task; triggers behave; works offline.
**M4.2 — HORSE execution.** Build: `src/horse.py` — 10 agents (varied engines) each fully execute the goal;
merge best-of-**results** to your **work-taste**. Done when: `HORSE <goal>` returns one merged artifact from
10 real executions.
**M4.3 — Packages: build/edit/save/reuse.** Build: `data/packages.json` — on-request + editable + auto-suggested;
pin frequent; kit UI (open → run each/all). Done when: assemble → pin → reuse in one click.
**M4.4 — Parent launcher (its OWN brand).** Build: `launcher/` — a **distinct clean minimal brand with its own
identity** (not Excavatortron's look, not reused as a default frame); centered project-cube grid; each cube opens
the project's own app in a **full context switch**; EXCAVA-created projects auto-appear. Done when: it lists
Excavatortron + your projects; each opens its full app; a new EXCAVA-made project shows.
**M4.5 — Hub-as-database.** Build: `hub_api.json` / endpoint + activator as carrier so Budoaris/FreeDup pull
elements/packages. Done when: another project pulls a package via the activator or endpoint.
**M4.6 — Ship M4 + prove "real".** Done when: (a) agents build a real artifact overnight unattended, AND (b)
you type a goal → get a working package you use — both demonstrated.

---

## M5 — EXCAVA ACTS ON THE WORLD  (DEFERRED behind CORE + M1–M4)
The significant external reach — built only once the core is spot-on.
**M5.1** Manage Eitan's projects' tasks. **M5.2** Post to / monitor his channels (OpenClaw + agent-reach) +
alert. **M5.3** Build + deploy sites/tools. **M5.4** **Find ways to make money** for Eitan. **M5.5** Interact
with **systems Eitan adds later** + **spin up whole projects independently**. Gate = **hybrid**: low-risk/
read-only auto, **anything risky or money-related pitches first**. Done when: ≥1 external action runs end-to-end
under the gate, traced + tutorialized.

---

## BREADTH (after M1–M4, alongside M5)
B1 finish the 52 goals per §9 order · B2 omni-source tiers 2–3 · B3 per-tab self-improvement + meta-brain ·
B4 portability (Budoaris first if you ask) · B5 cleanup (formats filter, brain white-nodes, token-split) ·
B6 EXCAVA-as-MCP-server. _(Expand B1/B3/B6 to full steps first, then the rest.)_

## OPEN DECISIONS → fold into the build (Fable creates, you review — NO pre-approval)
O1 palette (direction already set §I) · O2 the 11-monster cast (samples shown) · O3 fonts · O4 first-run tour
(default: empty states, tour optional) · O5 war-room scene (default: illustrate) · O6 notification sound
(default: off) · O7 Cmd-K (default: add) · O8 floor station shapes. _These come after the program is finalized
in build; Fable mocks and you see the result._
