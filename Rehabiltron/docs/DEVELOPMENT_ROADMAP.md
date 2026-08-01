# Development Roadmap — Rehabiltron

**Version:** 0.1 (pre-implementation)
**Date:** 2026-08-01

---

## How this roadmap is ordered

**By dependency, not by date.** No deadline, budget, or availability was given, so any calendar
estimate here would be fiction presented as a plan. What *is* knowable is what must exist before what
else — and that ordering does not change with how many hours a week are available.

If you tell me your realistic weekly hours, I will attach dates. Until then, the relative sizes below
(S / M / L / XL) let you do that yourself.

Two ordering principles:

1. **Highest-risk, hardest-to-reverse first.** Encryption, the migration runner, and the event bus
   come before any feature. If encrypted SQLite does not work on your target platform, that must be
   discovered in week one, not month four.
2. **Daily usability as early as possible.** Milestone M4 is the first point where the app is worth
   opening every day. Everything before it is scaffolding; everything after it is addition.

---

## Milestone map

```
M0 Decisions ──► M1 Foundation ──► M2 Profile+Timeline ──► M3 Goals ──► M4 Habits+XP
                                                                            │
                                            ┌───────────────────────────────┤
                                            ▼                               ▼
                                     M5 Tasks+Settings              M6 Backup+Hardening
                                                                            │
                                                                            ▼
                                                                   ═══ PHASE 1 DONE ═══
                                                                            │
                        ┌───────────────────┬───────────────────┬───────────┴──────┐
                        ▼                   ▼                   ▼                  ▼
                   M7 Health          M8 Notifications    M9 Achievements    M10 AI Foundation
                        │                                                          │
                        ├──────────────────────────────────────────┬───────────────┤
                        ▼                                          ▼               ▼
                  M11 Appearance                             M12 Voice      M13 Sync
                                                                                   │
                                            ┌──────────────────────────────────────┤
                                            ▼                                      ▼
                                   M14 Productivity+Knowledge              M15 Web/Desktop
                                                                                   │
                                                                                   ▼
                                                                          M16 Multi-user
```

---

## Phase 1 milestones

### M0 — Decisions and spike · size S · **blocking everything**

| Item | Detail |
|---|---|
| Answer C-01 … C-05 | The five Critical questions in [`MISSING_INFORMATION.md`](./MISSING_INFORMATION.md) |
| Encryption spike | Prove an encrypted SQLite database opens, migrates, and reads on **both** target platforms on a **physical device** before writing any feature code |
| Toolchain spike | Confirm the custom dev-client build loop is workable day to day |

**Exit:** a throwaway app that writes and reads an encrypted row on a real device.

This milestone exists because C-01's answer determines the entire development workflow, and because
"the encryption library does not work" is the single failure that would invalidate the most
downstream work. Two days here can save a month.

### M1 — Foundation · size L · depends on M0

Sprint 1 of [`MVP_PLAN.md`](./MVP_PLAN.md): project scaffold, tooling and CI, layered structure,
encrypted database, migration runner, core primitives, event bus with transactional outbox, encrypted
file store, app shell and navigation, app lock, first-run flow.

**Exit:** app installs, locks/unlocks, persists across restarts, CI green, database unreadable
externally.
**Risk:** highest in the project. The event bus and outbox are subtle; budget for getting the
idempotency tests genuinely right rather than nominally present.

### M2 — Profile and timeline · size M · depends on M1

Sprint 2. Profile CRUD and screen; the timeline service, repository, and screen.

**Exit:** profile persists; every published event appears in the timeline.
**Why here:** the timeline is the integration test for the event bus. Building it before any feature
that publishes events means the bus is proven before three features depend on it — and every later
feature inherits history for free.

### M3 — Goals · size M · depends on M2

Sprint 3. Goal entity and rules, milestones, list and detail screens, create/edit forms, goal events.

**Exit:** goals can be created, progressed, completed; transitions land in the timeline.
**Why before habits:** goals are the simpler state machine, and building them first validates the
whole vertical slice pattern (domain → repository → use case → screen) on lower-risk logic.

### M4 — Habits, streaks, XP · size L · depends on M3 · **the pivotal milestone**

Sprint 4. Schedules, streak rules with grace days, check-in and undo, the idempotent XP service, the
level curve, the Today screen, habit history, level-up.

**Exit:** daily check-ins work; streaks survive grace days; replaying the entire event log reproduces
the identical XP total.
**Why it matters:** this is where the app becomes worth opening. It is also where the hardest
correctness problems live — timezone-sensitive local dates, idempotent awards, streaks over irregular
schedules. Do not rush it; every later feature trusts this ledger.

### M5 — Tasks and settings · size S · depends on M4

Sprint 5. Tasks, the unified Today view, settings, storage usage.

**Exit:** Today is a single coherent answer to "what am I doing today".

### M6 — Backup and hardening · size M · depends on M5 · **Phase 1 gate**

Sprint 6. Encrypted export/import, delete and wipe with shredding, media protection verification,
performance and accessibility passes, E2E flows.

**Exit:** all seven MVP acceptance criteria pass on a physical device, including wipe-and-restore.

> **Then stop and use it for two weeks before starting Phase 2.** Real daily use will reorder
> everything below more usefully than any planning session can.

---

## Post-MVP milestones

### M7 — Health · size XL · depends on M6

Sleep, workouts with an exercise catalogue, body measurements, **progress photos** (the first
sensitive-media feature), recovery, nutrition. Optional platform health-store integration behind an
interface.

**Blocked on:** I-02 (health integrations), I-13 (photo protections must be verified *before* the
first photo is captured, not after).
**Note:** by far the largest feature area. Ship it in slices — sleep first (simplest and highest
daily value), photos last (highest risk).

### M8 — Notifications · size S · depends on M6

Local reminders for habits and tasks; quiet hours; per-habit configuration.
**Blocked on:** I-08. Deliberately after M6 so permission prompts arrive once the core loop is proven
worth being reminded about.

### M9 — Achievements and rewards · size M · depends on M4

Rule-driven achievement engine, user-defined rewards, redemption against `spendable_xp`.
**Note:** the XP engine already supports this; M9 is mostly content and UI. Good candidate to slot in
whenever motivation for a smaller milestone is needed.

### M10 — AI foundation · size L · depends on M6 · *depends on M7 for image tasks*

`AiService`, consent gate, redactor, audit log, processing-location UI; on-device provider first,
then self-hosted, then external; first analyses over Phase 1 data (pattern detection, weekly
narrative).

**Blocked on:** I-03 (which providers), I-04 (which data classes may ever leave).
**Sequencing rule:** the consent gate and audit log ship *before* the first AI feature. Retrofitting
privacy controls onto shipped AI features never works — the features get built assuming unrestricted
access, and the controls become exceptions instead of the path.

### M11 — Appearance · size L · depends on M7 (photos) and M10 (analysis)

Skin, hair/grooming, style tracking; progress comparisons; image-based analysis; recommendations
with the informational-only posture and disclaimers (I-10).

### M12 — Voice and communication · size L · depends on M7 (media pipeline), partly M10

On-device acoustic analysis (volume, pace, pauses) needs no model and can ship on the media pipeline
alone. Transcription, confidence indicators, and coaching feedback need M10.
**Blocked on:** I-09. Includes the recording-consent warning (P-20).

### M13 — Synchronization · size XL · depends on M6, benefits from a stable schema

Encrypted event-log sync, zero-knowledge relay or LAN-direct transport, HLC conflict resolution,
new-device bootstrap.
**Blocked on:** I-05.
**Note:** the largest and riskiest post-MVP item. Do it only when a second device genuinely matters —
and not before the schema has stopped changing every month, because sync amplifies every migration
problem across devices.

### M14 — Productivity and knowledge · size L · depends on M6

Focus sessions and analytics; the resource library with linked books/articles/papers/courses and
reading state; learning recommendations tied to active goals; phone-usage restriction if O-04
research says it is reachable.

### M15 — Web/desktop · size XL · depends on M6

New presentation layer and platform adapters (SQLite, keychain, filesystem, camera, mic, biometrics)
over the existing domain and application layers.

### M16 — Multi-user · size L · depends on M13

Profile switching, per-user keys, and — beyond one household device — a real identity model. Only if
it is ever wanted.

---

## Dependency table

| Milestone | Hard dependencies | Blocked on decisions |
|---|---|---|
| M0 | — | **C-01 … C-05** |
| M1 | M0 | I-01 (RTL), I-11 (offline) |
| M2 | M1 | I-12 (design) |
| M3 | M2 | — |
| M4 | M3 | I-06 (XP curve), I-07 (grace days) |
| M5 | M4 | — |
| M6 | M5 | C-03 (backup key), C-05 (storage) |
| M7 | M6 | I-02, I-13 |
| M8 | M6 | I-08 |
| M9 | M4 | — |
| M10 | M6 (+M7 for images) | I-03, I-04 |
| M11 | M7, M10 | I-10 |
| M12 | M7 (+M10 for models) | I-09 |
| M13 | M6, stable schema | I-05 |
| M14 | M6 | O-04 |
| M15 | M6 | O-01 |
| M16 | M13 | O-06 |

---

## Priority rationale

**Why encryption before features (M0/M1):** it is the one decision that touches every byte written.
Retrofitting encryption means migrating a live personal history, and discovering a platform problem
late invalidates months of work.

**Why the timeline before goals and habits (M2):** it proves the event bus with one subscriber
instead of debugging it with three, and it makes every later feature's history free.

**Why habits and XP together (M4):** XP without habits has nothing to reward; habits without XP is a
checklist. The daily loop needs both to be worth opening.

**Why backup before Phase 2 (M6):** Phase 2 introduces photos — the data that would hurt most to
lose and is hardest to recreate. Backup must work before there is anything irreplaceable to back up.

**Why AI is not early:** it is the most visible feature and the least foundational. Building it
before the data model settles means building analyses over a schema that keeps moving, and building
it before the consent system means privacy becomes an exception path rather than the only path.

**Why sync is late (M13):** it is the largest technical risk and only matters with a second device.
The columns that make it possible are already in place from day one, so waiting costs nothing.

---

## Risk register

| Risk | Severity | Mitigation |
|---|---|---|
| Encrypted SQLite driver fails on a target platform | **Critical** | M0 spike on a physical device before any feature code |
| Over-engineering stalls the project before daily use | **Critical** | Seams-not-systems; M4 is the forcing function; nothing built for a phase that has not started |
| XP/streak correctness bugs erode trust in the whole app | High | Append-only ledger, DB-enforced idempotency, property tests, recompute-from-log |
| Timezone bugs break "today" | High | Local dates as a branded type, injected clock, explicit tests across DST and timezone changes |
| Scope creep from the long feature vision | High | Phase gates; anything not in the current milestone goes to the roadmap, not the branch |
| Sensitive media leaks to cloud backup or gallery | High | P-16 … P-19 verified by E2E before the first photo feature ships |
| Migration corrupts a live personal history | High | Forward-only, transactional, permanent upgrade-path fixtures, pre-migration snapshot from M6 |
| Losing the backup passphrase | Medium | Clear one-time warning at setup; recovery is impossible by design and must be stated plainly |
| Solo-project motivation over a long roadmap | Medium | Milestones sized to be finishable; M9 available as a small, satisfying detour |
| Expo SDK upgrades breaking native modules | Medium | Pin versions; upgrade deliberately between milestones, never mid-milestone |

---

## Definition of done (every milestone)

1. Acceptance criteria met on a physical device.
2. Tests written and passing; coverage floors held.
3. Lint, typecheck, and boundary rules green.
4. Documentation updated where the milestone changed a contract, schema, or decision.
5. No known data-loss defect. Ever. This one is not negotiable and not tradeable against schedule.
