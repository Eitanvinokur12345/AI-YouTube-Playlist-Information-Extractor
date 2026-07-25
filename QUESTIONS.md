# Open questions for Eitan (non-blocking — answer whenever; work continues meanwhile)

_Per your rule: questions live here + in memory so they never block work or waste tokens. Answer any subset, in any order, whenever you want. Each has my default so you can also just say "defaults"._

---

## ⏸ AWAY WEEK — batched while you're out (since 2026-07-21)
You're away ~1 week; the offline loop is running (non-brain fronts, hourly) and collecting questions HERE instead of asking. Every question I hit this period is appended below with the default I proceeded on. I'll present this whole list the moment you're back. Contract: `data/excava/away_mode.json`.

### Away-week questions

**Overhaul audit — next decision batch (§7; items 5–8 of 122).** These are YOURS to decide; I did NOT auto-apply them — `data/excava/overhaul_decisions.json` stays OPEN. My proposed verdict on each (confirm or change with `python -m src.audit_decisions set <id> <verdict>`):
- **#5 "Should I just buy Gemini Pro?"** → proposed **REMOVE the worry.** The free path (VPS + Ollama + the free model pool) is real and proven this week — 11/11 engines answered, four brain families live. Paying is unnecessary.
- **#6 Direct in-app write to EXCAVA (no GitHub step)** → proposed **REBUILD.** Async-via-GitHub works now; true real-time in-app write needs the VPS (ties to A1, which you already KEEP'd).
- **#7 API keys work offline / without your PC** → proposed **KEEP the answer (yes).** Proven this week: the cloud beat ran the keys 24/7 with your machine off; the VPS will too.
- **#8 EXCAVATORTRON = HUB, EXCAVA = agents (naming)** → proposed **KEEP + lock everywhere.** This is the canonical naming and it's used consistently across the code and docs.

**The real hub blocker: enrichment is stalled at 0, and away-mode can't fix it (decision for your return).**
Three loop fires this week shipped read-side hub wins (v125 type-aware Activate · v126 "ready to use" filter
· v127 inline payload in the detail view). All real, but all BROWSE-layer — because the actual problem is
CONTENT: 3,628 of 10,133 elements are bare stubs and the local drain has enriched **0** for days (guardrail
G-O). deep_retrieve rides the brains/Ollama subsystem, which away-mode tells me not to touch, so I keep
polishing how you browse the library instead of filling it. → **Proposed default (on your return):** stand up
a DETERMINISTIC enricher (no LLM) that fills stubs from real sources — GitHub API repo description / topics /
homepage / README first line for the ~1,600 repo elements — network-bounded with a hard timeout (the 793-min
hang lesson). Free, non-brain, attacks completeness directly. Until you approve a network front or lift the
brain freeze, these fires keep producing browse-layer polish of diminishing value.

---

## A. The new look ("Heavy Machinery" v58)
1. **Direction check:** hazard-yellow + warm ink, chunky borders, hard offset shadows, Archivo Black display type — is this the right direction, or push further (more color pops per tab?) / pull back? _Default: keep, then add per-tab accent colors next pass._
2. Dark mode variant of the same theme — wanted? _Default: later._
3. Should the Designs tab get an even more expressive skin than the rest (it's the taste tab)? _Default: yes, next visual pass._

## B. North Star — proposed goal additions (needs your sign-off; goals are law)
The 6 goals miss two things we now actually build for:
4. **G7 Security & trust** — "nothing untrusted ever runs un-sandboxed; your data/keys can never leak." (We built security_preflight + the Activator gate; nothing *scores* it.) Approve adding G7? _Default: add._
5. **G8 Personal fit** — "every recommendation/design/plan is tailored to Eitan's taste and workflow (Arena taste, NOSG, his stack)." Approve adding G8? _Default: add._

## C. EXCAVA — the big one (deferred build; these shape the spec)
6. **Creators department:** should created things (new skills/tools/formats) be auto-published into the hub after passing the gate, or always wait for your approval per creation? _Default: approval per creation until trust is earned._
7. What may EXCAVA do **fully autonomously** at night: only internal work (resolve/verify/organize)? Or also create drafts? Or also publish? _Default: internal + drafts._
8. Where does EXCAVA live long-term: GitHub Actions only (free, current), or also a small always-on runner (e.g. your PC when on / a free VPS) for continuous operation? _Default: Actions now, revisit after the program._
9. The OS "manages the entire project **and can do a lot of other things**" — name 2–3 concrete non-project things you want it to do first (e.g. manage Budoaris tasks? your learning? content posting?). _No default — needs you._

## D. Program gaps I found (will do unless you object)
10. `formats.json` is collected but has no tab — fold formats INTO the Designs tab as a "Formats" filter? _Default: yes._
11. Brain graph still has ~191 empty "white" nodes + 10 title collisions — clean next maintenance pass? _Default: yes._
12. ~~Transcript lane blocked on `YT_PROXY_URL`~~ — RESOLVED 2026-07-02: Bright Data's residential-proxy tier needs a card on file even for free credits, which conflicts with the free-only rule, so declined. Not a blocker — Gemini-watches-video (already running) is the free analysis path, just slower per video than a transcript read would be. Cockpit now shows this as an optional "(skipped by choice)" chip, not a red MISSING.

## C2. EXCAVA conversation — installment 2 (answer anytime)
14. **Crew scope:** residents now wander every tab (bubbles = real dept status, click → cockpit). More of them / bigger / also on phone / quieter? Kill switch exists. _Default: keep as is, tune on your feedback._
15. **Creators quality gate:** before a creation (skill/prompt/scaffold/design) is accepted into the hub, what proof? _Default: EXCAVA self-test + your one-click review; nothing publishes untested._
16. **Dynamic departments:** who may open/close them? _Default: EXCAVA proposes with a reason, you approve; it may auto-close its own idle ones._

## E. Working mode
13. Confirm: keep doing big autonomous chunks on Fable (all visuals), Opus only for your own refinement passes; questions parked here. _Default: yes._

## F. Program gate decisions D1–D5 (from EXCAVA_PROGRAM.md, 2026-07-03)
17. **D1 — architecture** — ✅ ANSWERED 2026-07-03: **cron heartbeat** (Eitan picked it live in-session). Phase 0 built on it same day: the hourly `python -m src.excava` beat in bulk_analyze.yml IS the heartbeat; the file bus resumes state between beats.
18. **D2** — ✅ ANSWERED 2026-07-03: **direction-loop + change-tutorials first**, and the integration must be DAEMON-GRADE ("like a daemon for the entire project, not something casual, like in cortexOS — a clean daemon part of the OS that connects, or full integration"). HORSE-style fan-out pulled into Phase 6 scope. First daemon step shipped same day: every lane's runs now become OS bus events (the cockpit's 📡 feed).
19. **D3 — approval style:** approve the program as ONE block, or phase-by-phase sign-off? _Default: one block, with the per-phase ask-checkpoints still running._
20. **D4 — rebuild order:** spine-first as planned (P0 before any cleanup), or interleave small cleanups? _Default: spine-first._
21. **D5 — connectors tab:** OK to shrink it to verified-only once Phase 4 resolves real installs (94% are empty today)? _Default: yes._

## H. Phase checkpoints — ✅ ANSWERED 2026-07-03 (second batch)
26. **P3 creators** — ✅: creations enter the project autonomously WHEN labeled "Created by EXCAVA"; an independent test re-runs before first use; creators may build MCP servers/connectors/tools; **"PACKAGES"** = the owner's term for multi-element bundles (skills+tools+commands+designs+prompts+formats+outlines+MCP servers). Now guardrail G-12.
27. **P4 connectors** — ✅: **sandbox test-run EVERYTHING** (all 1,142; 6-hourly CI batches; verified-only tab per D5).
28. **P7 porting** — ✅: skip for now; harness stays a clean documented package (PORTABLE_HARNESS.md).
29. **P8 G9** — ✅: "Agency/Orchestration", equal weight — live on the North Star (scored 80 at birth).

## G. Omni-source intake + memory master (2026-07-03 owner additions)
22. **Your communities:** which subreddits / public Telegram channels / search queries should tier-1 intake watch? Starter set is in `data/social_sources.json` (LocalLLaMA, ClaudeAI, ChatGPTCoding, artificial, AI_Agents; Telegram empty — t.me/s only works for PUBLIC channels). _Default: keep the starter set, grow it over time._
23. **WhatsApp groups:** the only free path is you exporting a group chat (.txt, no media) from your phone into `data/whatsapp_exports/` occasionally — the miner parses the links out. Want a short how-to tutorial for that? _Default: yes, added with the Phase-6 change-tutorials._
24. **D6 — locked feeds (Instagram/TikTok/Facebook/LinkedIn):** these need your logged-in cookies stored as CI secrets, with real risk of account flags. Ever opt in? _Default: no — public-only stands._
25. **Daemon interpretation check:** I read your D2 note as "every part of the project reports through the OS bus (all 16 lanes now emit events), residents/cockpit react to real machine-wide events, and EXCAVA is the single connective layer — not a cosmetic overlay." First step shipped (lane events). If you meant something MORE (e.g. an actual resident process on a host), say so — the free-only + PC-off rules currently make the cron heartbeat the only clean daemon body. _Default: my reading._
