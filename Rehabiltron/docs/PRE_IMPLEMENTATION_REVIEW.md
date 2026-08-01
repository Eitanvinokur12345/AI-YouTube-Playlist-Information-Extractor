# Pre-Implementation Review — Rehabiltron

**Version:** 0.1
**Date:** 2026-08-01
**Reviewer:** Lead architect (self-review of the foundation documents)
**Purpose:** Find what is wrong with this plan *before* it becomes code.

This document is deliberately adversarial toward the plan in the other eight documents. A review that
concludes "everything looks good" is a review that was not performed.

---

## 1. Summary judgment

The foundation is sound and the plan is buildable. Three things genuinely worry me, in order:

1. **Over-engineering is a bigger threat to this project than under-engineering.** (§2.1)
2. **The privacy promise and the AI feature set are in real, unresolvable-by-design tension.** (§2.2)
3. **"No limits on uploaded content" is a promise a phone cannot keep.** (§2.3)

None of these blocks Sprint 1. All three need a conscious decision rather than a discovered one.

---

## 2. Architecture risks

### 2.1 Over-engineering — **the highest risk in the project**

A solo, personal app has been given: clean architecture, a repository layer, an event bus with a
transactional outbox, an AI provider abstraction, sync-ready columns, multi-user-ready columns, and a
seven-phase roadmap. Every one of those is individually justified in
[`ARCHITECTURE.md`](./ARCHITECTURE.md). Collectively they are also the exact profile of a project
that spends four months on infrastructure and never ships a habit tracker.

**Why I still recommend them:** each was chosen against the test *"is this cheap now and expensive
later?"* Repositories, `user_id`, UUIDv7, soft deletes, and the AI interface all pass. They are hours
now and weeks later.

**What I deliberately cut:** DI container, plugin system, sync engine, auth system, GraphQL/REST
layer, feature-flag service, abstraction layers with one implementation and no second in sight.

**The one item I am least sure about: the transactional outbox.** It is the most complex piece of
Sprint 1 and the least visible. The simpler alternative is synchronous in-process event dispatch with
no persistence — perhaps a third of the code.

I still recommend the outbox, for a specific reason: without it, a crash between "habit checked in"
and "XP awarded" leaves the two permanently inconsistent, with no way to detect or repair it. In an
app whose core value proposition is *a trustworthy record of your progress*, silent divergence is the
worst possible failure. But this is the single best candidate if you want to cut Sprint 1 down —
**decide it consciously, not by discovering the complexity halfway through.**

**Mitigation:** M4 (habits + XP, the first genuinely useful milestone) is the forcing function. If M0
through M3 start feeling like architecture astronautics, that is the signal to cut scope, not to keep
building infrastructure.

### 2.2 Privacy vs. AI capability — an inherent contradiction, not a bug

The brief asks for both "privacy is the highest priority, local processing where practical" and
"image analysis, coaching, pattern detection." These conflict, and no architecture resolves it:

- On-device models cannot currently match cloud models at image understanding or nuanced coaching.
- The most valuable AI features here (skin analysis, physique comparison, communication coaching) act
  on the most sensitive data (body photos, voice).
- So the privacy-maximal configuration is also the least capable one, precisely where capability
  matters most.

**What the architecture does:** makes the tradeoff explicit, per category, revocable, with the
processing location shown on every result and an audit log of every outbound request. It does not
resolve the tension — it hands you the dial with honest labelling instead of choosing for you.

**What you should expect:** on-device analysis will be noticeably weaker. If you eventually want
strong photo analysis, the realistic options are (a) send images to a provider you have chosen and
accept that, or (b) run a capable model on your own machine and sync to it over your LAN. Option (b)
is the best fit for this project's values and is why `self_hosted` is a first-class provider type
rather than an afterthought.

**Recommendation:** decide this before M10, not during it. It changes which provider gets built first.

### 2.3 "No artificial limits" vs. physical device storage

`PRODUCT_REQUIREMENTS.md` P-11 promises no limits on uploaded content. The `DATABASE_DESIGN.md` §8
estimate is ~45 GB for ten years of progress photos — more than the free space on many phones, and
the app cannot expand storage it does not have.

**The honest framing:** the app imposes no limit; the device does. That is a meaningfully different
promise, and the app should say so rather than let the limit arrive as an out-of-space crash.

**Recommendation (accepted into the plan):** no app-imposed cap; a storage-usage screen in M5;
`attachment.location` in the schema from day one so offloading to your own storage (C-05 Option B)
is a later feature and not a later migration. Also: originals are never downscaled without asking,
because silently degrading a user's progress photos would be a betrayal of the same promise.

### 2.4 Timezone and "local day" correctness

Habits, streaks, and "today" are local-day concepts; timestamps are instants. Mixing them produces
bugs that only appear for some users, at some hours, in some seasons — the worst class of bug to
debug, and one that directly corrupts the streak numbers the app exists to show.

**Mitigations in the plan:** `LocalDate` as a branded type distinct from `Iso8601`; `local_date`
columns alongside instants; `Clock.today(timezone)` rather than `new Date()`; timezone stored on the
profile; explicit tests across DST transitions and timezone changes.

**Residual risk:** what happens to a streak when you fly across timezones, or when DST creates a
23-hour day. The plan does not fully specify this. **Recommended rule:** a habit check-in belongs to
the local day *at the moment of check-in*, and past entries are never re-bucketed when the timezone
changes. It is the least surprising behaviour and the only one that keeps history stable. Confirm
before M4.

### 2.5 SQLCipher and the Expo Go tradeoff

C-01's recommended option removes Expo Go from the workflow permanently and adds a native-module
dependency that must survive every Expo SDK upgrade.

**Risk:** an SDK upgrade breaks the encrypted-database module and the app cannot be built until it is
fixed upstream or replaced.
**Mitigations:** the M0 spike proves it on both platforms before anything is built on it; the
repository layer means swapping drivers touches `core/db` and the repositories, not features; SDK
upgrades happen between milestones, never during one.

### 2.6 Cached aggregates diverging from their logs

`habit.current_streak` and `progression_state.lifetime_xp` are caches. Caches drift.

**Mitigations:** both are recomputable from append-only logs; `recomputeFromLedger()` is a public,
user-reachable operation (`API_CONTRACTS.md` §4); a test asserts cache equals recomputation after
arbitrary event sequences.
**Residual risk:** drift that is never noticed. **Recommendation:** recompute-and-compare on app
start when the app has been closed for over 24 hours — cheap at this data volume, and it turns silent
corruption into a self-healing event.

### 2.7 Event bus complexity in a single-process app

At-least-once delivery, durable subscribers, retries, and backoff are distributed-systems machinery
inside one process.

**Justification:** the durability is not about distribution, it is about *crashes*. A phone app is
killed by the OS constantly. In-memory events die with the process, and any state change that lived
only in an event handler is lost.
**Residual risk:** debugging asynchronous flows is harder than debugging synchronous ones.
**Mitigation:** every event carries its `id` into every log line and every derived row
(`timeline_event.source_event`, `xp_ledger.source_event_id`), so any XP entry can be traced to the
check-in that caused it.

### 2.8 A seven-phase roadmap for a solo project

The full vision is realistically several years of part-time work. The risk is not technical.

**Mitigation:** the roadmap is dependency-ordered, so stopping after any milestone leaves a coherent
product. M6 alone — goals, habits, XP, timeline, encrypted and backed up — is a genuinely good app.
Everything after it is addition, not completion.

---

## 3. Missing decisions

Full detail in [`MISSING_INFORMATION.md`](./MISSING_INFORMATION.md). Consolidated here by when it
bites:

| Blocks | Decisions |
|---|---|
| **M0 — now** | C-01 encryption/Expo Go · C-02 platforms and build capability · C-03 key custody and recovery · C-04 single-user semantics · C-05 unlimited-content storage |
| M1 | I-01 RTL · I-11 offline-only mode |
| M4 | I-06 XP curve · I-07 grace days · **§2.4 timezone rule** |
| M6 | C-03 (again — backup key) · C-05 (again — storage screen) |
| M7 | I-02 health integrations · I-13 photo protections |
| M10 | I-03 providers · I-04 data classes permitted to leave |
| M12 | I-09 voice metrics |
| M13 | I-05 sync topology |

Two decisions are **absent from the brief entirely** and I flag them as newly surfaced:

- **N-01 — Timezone/streak rule** (§2.4). Not mentioned anywhere in the brief; directly determines
  whether streak numbers are correct. Needed before M4.
- **N-02 — Duress / plausible-deniability.** A privacy-first app holding intimate photos raises the
  question of what happens under coercion. Currently out of scope and documented as such
  (`ARCHITECTURE.md` §8.1). Flagged so it is a decision rather than an oversight.

---

## 4. Contradictions found in the requirements

| # | Contradiction | Resolution taken |
|---|---|---|
| 1 | "Privacy is highest priority" vs. "image analysis, coaching, AI recommendations" | Per-category consent, default denied, processing location always visible. Tension surfaced to the user rather than resolved silently (§2.2) |
| 2 | "No artificial limits on uploaded content" vs. finite phone storage | No app-imposed cap; storage visibility; `attachment.location` enables user-controlled offload later (§2.3) |
| 3 | "Encrypted storage" vs. React Native/Expo developer ergonomics | Custom dev client from day one; proven in M0 before anything depends on it (C-01) |
| 4 | "Primarily personal use" + "avoid unnecessary complexity" vs. multi-user, sync, event-driven, clean architecture | Seams not systems: cheap-now/expensive-later items built, everything else deferred (§2.1) |
| 5 | "Local processing where practical" vs. "user-controlled external AI providers" | Both, as an explicit routing policy with a per-request ceiling (`maxLocation`) |
| 6 | Gamification (XP, streaks, levels) vs. a wellbeing product | XP never lost, grace days on streaks, neutral copy, no loss-aversion mechanics (PRD X-4, X-8). Streak pressure without an escape valve makes bad weeks worse — a real harm, not a UX nitpick |
| 7 | "Skincare and product recommendations" vs. not being a medical product | Informational only, no affiliate links, explicit non-medical disclaimer, no diagnostic language (PRD Q-6) |

---

## 5. Recommended changes to the plan

Changes I would make to my own plan, in priority order:

| # | Recommendation | Rationale |
|---|---|---|
| R-1 | **Run the M0 encryption spike before anything else — including project setup.** | It can invalidate the entire storage strategy. Two days now versus a month of rework |
| R-2 | **Decide the transactional outbox consciously** (§2.1) | It is the biggest complexity item in Sprint 1. Keep it for correctness, or cut it deliberately — but not by accident |
| R-3 | **Add the timezone/streak rule (N-01) to the PRD before M4** | Directly determines whether the app's headline numbers are right |
| R-4 | **Add recompute-and-compare on cold start after 24h idle** (§2.6) | Turns silent cache drift into self-healing |
| R-5 | **Ship sleep tracking before progress photos in M7** | Sleep is simpler, lower-risk, and higher daily value; photos carry the sensitive-media risk and should follow verified protections |
| R-6 | **Build the `self_hosted` AI provider before the `external` one in M10** | Best fit for the project's values, and it resolves §2.2 without giving data to a third party |
| R-7 | **Add a "verify my data" screen** — row counts, orphan attachments, cache-vs-log comparison, last backup date | In an app with no server and no support channel, self-diagnosis is the only diagnosis |
| R-8 | **Write the backup passphrase warning copy carefully, and show it once at setup with a confirmation** | "Forgot passphrase = data gone forever" must be understood at the moment it is chosen, not discovered later |
| R-9 | **Consider deferring the `goal_milestone` table to M9** | Goals work without milestones; it is the one piece of M3 that could slip without loss |
| R-10 | **Reconsider `task` in Phase 1 if M4 runs long** | Tasks are the least differentiated feature and the easiest to defer — every phone already has a task app |

R-1 through R-4 I consider necessary. R-5 through R-10 are judgment calls I would make, and none of
them are irreversible.

---

## 6. What I am confident about

Stated for balance — these do not need revisiting:

- SQLite as the store. Correct at this data volume for at least a decade.
- Append-only ledger with database-enforced idempotency for XP. The unique index on
  `(source_event_id, reason)` makes double-awarding impossible rather than unlikely.
- Repository pattern and the lint-enforced boundaries. These are what keep the codebase navigable at
  year three.
- The AI abstraction shape. Requiring `processedAt` on every result and typing `SyncTransport` to
  accept only ciphertext turns privacy promises into things the compiler checks.
- Dependency-ordered milestones with the timeline built early to prove the event bus.
- UUIDv7 + soft deletes + `device_id`/`revision` from row one. Nearly free now; a migration nightmare
  later.

---

## 7. Implementation readiness assessment

| Dimension | Status | Note |
|---|---|---|
| Product scope | **Ready** | MVP boundary is clear and testable |
| Architecture | **Ready** | Layers, boundaries, and data flow specified to implementation detail |
| Data model | **Ready** | Full Phase 1 DDL with indexes and migration policy |
| Contracts | **Ready** | Repositories, events, services, AI — specified as signatures |
| Coding standards | **Ready** | Split into CI-enforced and review-enforced |
| Roadmap | **Ready** | Dependency-ordered; dates pending your availability |
| **Critical decisions** | **NOT READY** | C-01 … C-05 unanswered |
| **Technical validation** | **NOT READY** | M0 encryption spike not yet run |

### Verdict

**Documentation phase: complete. Implementation: not authorised.**

Two gates before Sprint 1 code:

1. **Answer C-01 … C-05.** Each has a stated default; confirming them is a short conversation.
2. **Run the M0 spike.** Prove encrypted SQLite works on a physical target device before any feature
   depends on it.

With both cleared, Sprint 1 can start immediately — the plan is detailed enough to implement without
further design work.

### If I could only ask one question

**C-01.** Whether the database is encrypted decides the development workflow, the dependency set, the
build pipeline, and the credibility of the entire privacy premise. Everything else can be adjusted
later; that one cannot.
