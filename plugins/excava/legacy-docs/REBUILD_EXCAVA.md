# REBUILD EXCAVA — the complete overhaul (owner-decided 2026-07-15)

Eitan paused the loop and made three founding decisions:
1. **The unlock = the free Oracle VPS** (real backend + unlimited local models). No paid engines — free is the point.
2. **The core = a TEAM that EXECUTES tasks using the Hub, + a Hub I can browse, learn from, and improve.** Not agent debate. Not 13 departments. Execution + a living library.
3. **A complete overhaul.** Rethink every feature (current AND buried in history), keep/cut/rebuild each, draw from real operating systems, make it look professional, make it self-improve. Start fresh.

This document is that fresh start. Paste it (or the "Fresh session prompt" at the bottom) to begin the redesign.

---

## 0. Names (Eitan's correction, 2026-07-15 — canonical)

- **EXCAVATORTRON = the HUB** — the excavated library of ~6,800 **elements**.
- **EXCAVA = the agents** — the team that acts on the HUB.
- **"Elements," not just "tools":** an element is any reusable AI ability — **skill, tool, MCP connector, model, prompt, or command** (six types). Agents use *elements*, plural types. See `EXCAVA_FUNDAMENTALS.md` for the full plain-language course (read it first if any word here is fuzzy).

## 1. The one-sentence product (finally clear)

> **EXCAVATORTRON (the HUB) is a living, browsable library of AI elements that EXCAVA (a team of agents) — and Eitan — learn from and act on.**

Everything is judged against that sentence. If a feature doesn't help the **agents execute using the elements**, or help **Eitan browse/learn from the HUB**, it is not the product. The HUB must be *living* — used on command AND working on its own via background services — or "the OS feels empty" (his words).

---

## 2. The honest, completely-critical assessment

**What's genuinely wrong (your situation):**
- **Debate instead of action.** 619 rooms were built to *talk*. You want *do*. Talk is theater; it looks impressive and produces nothing. The entire room paradigm has to flip: *task in → agent uses the Hub → artifact out → verified done.*
- **Breadth instead of depth.** 13 departments each 30%-working feels worse than 3 capabilities that fully work. Sprawl reads as "unprofessional" even when each piece is clever.
- **Fuel starvation.** The rooms died July 12 because 7 of 10 free engines are rate-limited and 3 survivors feed the whole system. A talking-agent OS is LLM-hungry; free tiers can't feed it. **This is why the VPS matters: Ollama on the VPS = unlimited free local models = the fuel.** Your "free" and your "VPS" answers are the same answer.
- **No backend = faked interactivity.** GitHub Actions is a batch job; GitHub Pages is static. "Type a command and watch it run" cannot fully exist until the VPS. Until then the shell is async (next-beat); after, real-time.
- **Amateur visuals.** The cockpit grew organically, tab by tab. It needs a real design system, not another panel bolted on.
- **Self-improvement too weak.** Today it archives silent rooms and files pitches. Real self-improvement = *measure the team's task success rate, find the top failure, fix it, prove the number moved.* A system that can't measure its own success can't improve.

**What's genuinely right (keep these — they're the moat):**
- **The Hub** (6,800 mined tools) — this is the actual product spine, and it's rare. Reframe it as the OS's **app-store + library**.
- **The beat** (the free always-on trick) — clever; keep, simplify.
- **The safety discipline** — `git_safe`, recall-before-change, guardrail tests, real-not-facade. This is what keeps it from breaking itself. Non-negotiable, keep.
- **Per-agent memory + the activator** (package manager). Keep.

**General (true for anyone building an "agentic OS"):**
- Everyone over-builds the *agents-talking* part (cheap, flashy) and under-builds *reliable execution + verification* (the hard 90%). Invert that.
- Free-tier limits force *frugality as architecture*: prefer deterministic code over LLM calls, cache hard, use small local models for routine steps, reserve strong engines for hard steps. Paid teams are sloppy here; your constraint can make EXCAVA *leaner*, not just poorer.
- A product is defined as much by what it refuses to do as what it does. The overhaul is mostly **subtraction**.

---

## 3. The target: EXCAVA as a real OS (borrow the proven model)

Map EXCAVA onto the parts of an operating system that already work. This gives a small set of primitives that compose, instead of 13 half-features.

| OS part | What it is | EXCAVA's version | Status |
|---|---|---|---|
| **Kernel** | schedules work, mediates calls | the beat | keep, simplify |
| **Shell** | you type commands, they run | **conversational EXCAVA** (execution, not chat-for-show) | REBUILD = your #1 |
| **Scheduler / init** | runs jobs + background services | a **task queue** + a few daemons (mining, news, analysis) | REBUILD (replaces 619 rooms) |
| **Processes** | small programs that do one thing | **agents** — single-purpose, composable, Unix-style | REBUILD |
| **System calls** | the real actions programs can take | a small, reliable **tool/action set** (fetch, analyze, write, search-hub, call-model) | DEFINE (new) |
| **Filesystem / library** | where everything lives, browsable | **the Hub** — the app-store you and agents read | KEEP + make viewable |
| **Package manager** | installs capabilities | the **activator** | keep |
| **Users / permissions** | who may do what | **autonomy tiers** + owner gating | keep, simplify |
| **Desktop environment** | the face of the OS | the **cockpit** | REBUILD to professional |
| **Health / self-test** | the OS checks itself | **self-improvement** = measure success, fix top failure | REBUILD as first-class |

**The spine in one line:** *Shell (you type) → Scheduler (queues it) → Agent (executes, using the Hub as its library and a small set of real tools) → verified artifact → self-improvement watches the success rate and closes gaps.*

---

## 4. The keep / cut / rebuild audit (my critical first pass — you decide)

| Component | Verdict | Why |
|---|---|---|
| The Hub / mining / `elements_index` | **KEEP — promote to spine** | the actual product; make it browsable + agent-readable |
| Activator skill | **KEEP** | the package manager |
| Beat / kernel (`excava.py`) | **KEEP, simplify** | the free always-on engine |
| `git_safe`, guardrail tests, recall-before-change | **KEEP** | the safety net; without it the system breaks itself |
| Per-agent memory | **KEEP** | a real team needs memory |
| Autonomy tiers + owner gating | **KEEP, simplify** | governance |
| Conversational EXCAVA (`excava_chat`) | **REBUILD → the Shell** | make it *execute*, not debate |
| 619 rooms / multi-agent **debate** | **CUT** | replace with a task queue + execution logs |
| 13 departments as "departments" | **REBUILD → capabilities + one agent pool** | collapse breadth into a few real capabilities |
| News / analysis / mining lanes | **KEEP a few → Services (daemons)** | genuine background value |
| Cockpit UI | **REBUILD** | needs a professional design system |
| Rehab plan / `history_mine` (208 wants) | **REFRAME → the backlog** | it *is* the backlog, not a blocker |
| Pitch system (incl. the v3 detail I just built) | **BACKLOG** | not core; I over-built it — proof of the sprawl problem |
| Tutorial department (just built) | **BACKLOG** | not core |
| Graph expansion, track-record leaderboards, formation A/B | **BACKLOG** | vanity/metrics before the core works |
| Context-paging / temporal-validity / token-diet "AIOS" modules | **BACKLOG / evaluate** | over-engineered for the current stage |
| "Fulfill EVERY request ever" law | **RETIRE as a blocker** | replace with: *one core, done well, then expand from the backlog* |

**Acquire (new components to consider):** a small local-model runner (Ollama on the VPS); a proper task-queue store; a design system for the cockpit; an outcome/success-rate tracker (the missing self-improvement primitive).

---

## 5. How "free" actually works (so you never starve again)

1. **Ollama on the VPS runs 2–3 DIFFERENT models at once** (e.g. llama-3.2 + qwen2.5 + mistral-small) with **no quota** — and each is wired as a *different agent*. This matters: one model talking to itself is fake debate (the "all conversations same length" tell). Real agents need genuinely different brains — free, unlimited, 24/7, and *diverse*.
2. **The strong free cloud engines** (groq, mistral, nvidia) add more distinct brains and are *reserved* for the hard steps — not burned on routine work.
   *(So "free" and "multi-agent" are compatible: 2–3 local models + the cloud engines = a real team of different minds, at zero cost.)*
3. **Deterministic code beats LLM calls** wherever possible (parsing, filtering, formatting). Every call you *don't* make is capacity saved.
4. **Cache aggressively.** Same question, same answer — don't pay twice.

Result: the team can run continuously on free infrastructure, because 90% of steps are local/free and only the hard 10% touch the shared engines.

---

## 6. Build order (after this plan is approved)

- **Phase 0 — now, free, no VPS needed:** lock the redesign (this doc + your answers). Rebuild the cockpit into a **professional Shell + task-queue + Hub-browser**. Convert **ONE** capability to true execution as the proof-of-life. Everything else → backlog.
- **Phase 1 — VPS up:** install Ollama = unlimited free fuel. Turn on the real-time Shell. Agents execute continuously from the queue.
- **Phase 2 — depth:** self-improvement measures task success and closes its own gaps. The Hub-browser becomes something you genuinely learn from. Bring capabilities back from the backlog one at a time, each fully working before the next.

---

## 7. The new question sequence (the design interview)

Answer these in your own words — they design the overhaul. (Grouped; the four that decide the most are asked as clickable choices when this runs.)

**A · The Shell (how you command it)**
1. When you type a command, what are the 3 most common things you'd ask for?
2. Do you type in Hebrew, English, or both?
3. Should the Shell show its *plan* before it acts, or just act and show the result?
4. If a command needs a decision, should it ask you, or pick a default and tell you?

**B · The team (agents that execute)**
5. How many agents feels right — a handful you know by name, or a swarm?
6. Should agents specialize (one per capability) or be generalists?
7. When an agent finishes, what proof do you want — the artifact, a log, a screenshot?
8. Should agents be allowed to start work on their own, or only when you command?

**C · The Hub (the library you browse & learn from)**
9. When you "view the Hub," what do you want to see first — newest tools, best tools, by category?
10. What does "learn from the Hub" mean to you — read summaries, watch demos, try tools?
11. Should the Hub teach *you*, or teach the *agents*, or both?
12. Which categories of AI tools matter most to you (image, video, writing, code, research…)?

**D · The look (professional)**
13. Name one app whose look you'd want EXCAVA to feel like.
14. Dark, light, or both? Playful or serious?
15. Is it a "desktop" (windows/panels) or a "feed" (one stream you scroll)?
16. What's the first screen you want to see when you open it?

**E · Scope (keep/cut)**
17. Read the audit table (§4) — which verdicts do you disagree with?
18. Of the capabilities, which ONE should be the Phase-0 proof-of-life?
19. Is there anything in the backlog you'd fight to keep in the core?
20. Anything buried in history you want resurrected?

**F · Self-improvement**
21. What does "EXCAVA got better this week" look like to you — a number, a new skill, fewer failures?
22. Should it improve itself silently, or show you what it changed and why?
23. What failure annoys you most right now that it should learn to stop doing?

**G · Governance & pace**
24. Post-overhaul, should I ask permission less and move faster?
25. Keep the harsh criticism each tick, or trade it for more building?
26. Is the loop-every-8-minutes right, or do you want fewer, bigger sessions?
27. When you change your mind, should I lock the decision and push back, or just follow?

**H · The VPS (the unlock)**
28. Realistically, when can the Oracle signup happen with your parents — this week, this month?
29. Is there a home machine that can run Ollama in the meantime, even a few hours a day?
30. Would you sit through a one-time 30-minute setup with me when the box exists?

---

## 8. Laws that survive the overhaul

Free-only; everything operable **in the app**; **real-not-facade** (never "verified" without operating the read side + a number); ship only via `git_safe`; recall-before-change + log why; quarantine-never-delete; harsh criticism of both sides every tick.

## 9. The law that changes

**Retire:** "fulfill EVERY request I ever made, before anything new."
**Replace with:** "**one core, done well and professional, then expand from the backlog — nothing new until the core works and looks right.**" The 208 mined wants become the backlog we draw from, not a wall that blocks focus.

---

## Fresh session prompt (paste this to start the redesign — Eitan will run it in a NEW session)

> You are re-founding EXCAVA with Eitan (17, Israel, non-coder who wants to LEARN this, not just receive output). **Read two files first, in order:** `EXCAVA_FUNDAMENTALS.md` (the plain-language course — teach from it), then `REBUILD_EXCAVA.md` (the overhaul plan he approved 2026-07-15).
>
> **Names (canonical):** **EXCAVATORTRON = the HUB** (library of ~6,800 *elements*: skill / tool / MCP connector / model / prompt / command). **EXCAVA = the agents** that act on it. **Product in one line:** a *living* browsable HUB of elements that a team of agents — and Eitan — learn from and act on. **Core = execution, not debate. Fuel = Ollama on the free Oracle VPS (free is the point). Overhaul = subtract first.**
>
> **How Eitan wants to work (2026-07-15):** he wants to *understand from the ground up* — teach the fundamentals as you go (a short "course" is welcome). He'll give general direction and let it run in a loop, answering only when a real decision needs him. Cockpit shape = **desktop with panels**. The plan must be **precise, comprehensive, and portable — it must work beyond a single Claude session** (survive token/context limits; carry into other tools). Past failures came from shipping features faster than his understanding, under token/time pressure — do NOT repeat that.
>
> **Start here, in this order:** (1) make sure the fundamentals are his — offer to walk any concept live; (2) discuss **the HUB first** — how it uses elements AND acts on its own so the OS isn't empty; (3) run the §7 design interview; (4) only then produce a Phase-0 plan (professional desktop cockpit + task queue + HUB-browser + ONE capability executing for real) before any code. Follow §4 keep/cut/rebuild, build order §6, laws §8, changed law §9. Be completely critical of both of you, every step.
