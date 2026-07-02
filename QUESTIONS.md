# Open questions for Eitan (non-blocking — answer whenever; work continues meanwhile)

_Per your rule: questions live here + in memory so they never block work or waste tokens. Answer any subset, in any order, whenever you want. Each has my default so you can also just say "defaults"._

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
18. **D2 — the 10 alignment systems (Phase 6):** name the 2–3 you want FIRST from: direction-loop, self-extending guardrails, DISCOVERY file, priority-weights, goals-re-score, approval queue, change-tutorials, proactive digest, session-start memory-audit, source trust-scores. _No default — needs you (only gates Phase 6, not Phase 0)._
19. **D3 — approval style:** approve the program as ONE block, or phase-by-phase sign-off? _Default: one block, with the per-phase ask-checkpoints still running._
20. **D4 — rebuild order:** spine-first as planned (P0 before any cleanup), or interleave small cleanups? _Default: spine-first._
21. **D5 — connectors tab:** OK to shrink it to verified-only once Phase 4 resolves real installs (94% are empty today)? _Default: yes._
