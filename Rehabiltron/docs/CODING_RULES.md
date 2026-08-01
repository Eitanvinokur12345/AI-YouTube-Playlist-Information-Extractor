# Coding Rules — Rehabiltron

**Version:** 0.1 (pre-implementation)
**Date:** 2026-08-01

Rules exist to make the architecture survive contact with a tired developer at 2am. Where a rule can
be enforced by a tool, it is — because a rule that depends on remembering it is a rule that will be
broken. Each rule below is marked:

- **[CI]** — enforced automatically; violation fails the build
- **[REVIEW]** — checked by a human before merge

---

## 1. TypeScript

### Compiler configuration **[CI]**

```jsonc
{
  "strict": true,
  "noUncheckedIndexedAccess": true,      // arr[0] is T | undefined — it genuinely is
  "exactOptionalPropertyTypes": true,
  "noImplicitOverride": true,
  "noFallthroughCasesInSwitch": true,
  "noUnusedLocals": true,
  "noUnusedParameters": true,
  "forceConsistentCasingInFileNames": true,
  "verbatimModuleSyntax": true
}
```

### Rules

| # | Rule | Enforcement |
|---|---|---|
| TS-1 | No `any`. Use `unknown` and narrow. `@ts-expect-error` requires a comment explaining why and never lands in `domain/` | [CI] |
| TS-2 | No non-null assertion (`!`). If a value can be null, handle it | [CI] |
| TS-3 | Validate every external input with a schema (Zod) at the boundary — backup files, imports, AI responses, deep-link params. Inside the boundary, types are trusted | [CI] + [REVIEW] |
| TS-4 | Branded types for `EntityId`, `LocalDate`, `Iso8601`. Never pass a bare `string` where one is expected | [REVIEW] |
| TS-5 | Discriminated unions over optional-field soup. `{ status: 'loading' } \| { status: 'ready'; data: T }`, not `{ loading: boolean; data?: T }` | [REVIEW] |
| TS-6 | Exhaustive switches with a `never` default. Adding an event type must break the build everywhere it needs handling — that is a feature | [CI] |
| TS-7 | `readonly` on entity fields and array parameters by default. Domain entities are immutable; changes produce new objects | [REVIEW] |
| TS-8 | No default exports (except Expo Router route files, which require them) | [CI] |
| TS-9 | Explicit return types on all exported functions. Inference is fine internally; a public signature should not change silently | [CI] |
| TS-10 | `enum` is banned; use `as const` objects and union types | [CI] |

---

## 2. Architecture rules **[CI]**

The four project rules, expressed as lint configuration. These are the ones that matter most — every
other rule in this document is style by comparison.

```jsonc
// eslint import/no-restricted-paths zones
[
  { "target": "src/domain",      "from": "src/features" },
  { "target": "src/domain",      "from": "src/services" },
  { "target": "src/domain",      "from": "src/ui" },
  { "target": "src/domain",      "from": "src/core" },     // domain imports NOTHING
  { "target": "src/ui",          "from": "src/features" },
  { "target": "src/ui",          "from": "src/domain" },
  { "target": "src/features/*/ui", "from": "src/features/*/data" },   // UI never touches data
  { "target": "src/app",         "from": "src/features/*/data" },
  { "target": "src/app",         "from": "src/features/*/application" }
]
```

Plus these package-level restrictions:

| # | Rule |
|---|---|
| AR-1 | Only `core/db/**` and `features/*/data/**` may import the SQLite driver |
| AR-2 | Only `services/ai/providers/**` may import a model-provider SDK |
| AR-3 | Only `core/crypto/**` may import a crypto library |
| AR-4 | A feature may import another feature only through its `index.ts` |
| AR-5 | `app/**` route files contain layout and wiring only — no queries, no business logic, no `useEffect` doing work |
| AR-6 | No React import anywhere in `domain/**` or in `features/*/application/**` |

If a rule needs bypassing, the fix is a discussion about the design, not an eslint-disable.

---

## 3. Business logic placement **[REVIEW]**

The single question for every piece of code: *if this rule is wrong, where would I write the test?*
If the answer requires rendering a component, the logic is in the wrong place.

| Logic | Lives in |
|---|---|
| "Is this habit due today?" | `domain/rules/scheduleRules.ts` |
| "Does this check-in extend or break the streak?" | `domain/rules/streakRules.ts` |
| "How much XP is this worth?" | `domain/rules/xpRules.ts` |
| "What level does 4,200 XP mean?" | `domain/rules/levelCurve.ts` |
| "Check in, award XP, record the timeline entry" | `features/habits/application/CompleteHabitUseCase.ts` |
| "Which habits show on the Today card, sorted how" | `features/habits/ui/useTodayHabits.ts` |
| "Render a habit row" | `features/habits/ui/HabitRow.tsx` |

Components may contain: rendering, layout, animation, local UI state (open/closed, focused), and
calls into use cases. Nothing else.

---

## 4. Naming conventions

| Kind | Convention | Example |
|---|---|---|
| Files: components | `PascalCase.tsx` | `HabitRow.tsx` |
| Files: everything else | `camelCase.ts` | `streakRules.ts` |
| Files: tests | mirror the subject | `streakRules.test.ts` |
| Directories | `kebab-case` | `features/progression/` |
| Types & interfaces | `PascalCase`, no `I` prefix | `HabitRepository` |
| Functions & variables | `camelCase` | `completeHabit` |
| Constants | `UPPER_SNAKE_CASE` | `DEFAULT_GRACE_DAYS` |
| Booleans | `is` / `has` / `can` / `should` prefix | `isDueToday`, `canComplete` |
| Use cases | `<Verb><Noun>UseCase` | `CompleteHabitUseCase` |
| Events | `noun.past_tense_verb` | `habit.completed` |
| Event types | `PascalCase` past tense | `HabitCompleted` |
| Hooks | `use` prefix | `useTodayHabits` |
| DB tables/columns | `snake_case` | `habit_entry.local_date` |

Domain vocabulary is fixed and used everywhere — code, database, UI copy, and these docs:
**goal, habit, habit entry (never "completion" or "log"), task, XP, level, streak, timeline event,
milestone, achievement, reward, attachment.** One concept, one word.

---

## 5. Code organization

### Feature structure

```
features/habits/
├── index.ts               # public surface — the ONLY external import target
├── data/
│   ├── habitRepository.ts
│   ├── habitEntryRepository.ts
│   ├── mappers.ts
│   └── queries.ts         # SQL string constants
├── application/
│   ├── completeHabitUseCase.ts
│   ├── createHabitUseCase.ts
│   └── habitEventHandlers.ts
└── ui/
    ├── screens/
    ├── components/
    └── hooks/
```

| # | Rule |
|---|---|
| ORG-1 | One exported concept per file. A file exporting three unrelated things should be three files |
| ORG-2 | Files stay under ~300 lines. Longer usually means a missing abstraction |
| ORG-3 | Functions stay under ~50 lines, with one level of abstraction each |
| ORG-4 | Tests sit beside their subject (`streakRules.ts` / `streakRules.test.ts`); only E2E lives in `tests/` |
| ORG-5 | No `utils.ts`, no `helpers.ts`, no `common/`. Name the thing after what it does |
| ORG-6 | Imports ordered: node → external → `@/core` → `@/domain` → `@/features` → `@/ui` → relative **[CI]** |
| ORG-7 | Path alias `@/` for `src/`. No `../../..` chains **[CI]** |

---

## 6. Testing rules

| # | Rule | Enforcement |
|---|---|---|
| T-1 | Every domain rule has tests covering the happy path, every boundary, and every failure | [REVIEW] |
| T-2 | Domain coverage ≥ 90%; overall ≥ 70%. Coverage is a floor, not a goal | [CI] |
| T-3 | Time is injected via `Clock`. `new Date()` and `Date.now()` are banned outside `core/time` | [CI] |
| T-4 | Randomness is injected. `Math.random()` and direct UUID calls are banned outside `core/id` | [CI] |
| T-5 | Repository tests run against a real temporary SQLite file, not a mock. Mocked SQL tests only prove the mock works | [REVIEW] |
| T-6 | Every event handler has an idempotency test: handle the same event twice, assert one effect | [REVIEW] |
| T-7 | Every migration keeps its fresh-install, upgrade-path, and idempotency tests forever | [REVIEW] |
| T-8 | Property-based tests for the XP ledger and streak rules — arbitrary event sequences must never produce a wrong total | [REVIEW] |
| T-9 | No network in any test. There is no network in this app | [CI] |
| T-10 | A bug fix starts with a failing test that reproduces it | [REVIEW] |
| T-11 | Tests read as specifications: `it('repairs a broken streak using a grace day')`, not `it('works')` | [REVIEW] |
| T-12 | No snapshot tests of whole screens. They assert nothing and are updated blindly when they break | [REVIEW] |

**Test the rules, not the framework.** A test that verifies React re-renders is worthless; a test
that verifies a 3-times-per-week habit does not break its streak on Tuesday is the reason this app
can be trusted.

---

## 7. Security and privacy rules

These are the rules where a mistake is not a bug but a betrayal of the product's only promise.

| # | Rule | Enforcement |
|---|---|---|
| S-1 | Never log user content. The logger takes an explicit allow-list of safe fields; it does not filter unsafe ones. Deny-lists always miss something | [CI] + [REVIEW] |
| S-2 | Never log or embed key material, passphrases, or derived keys — including in error messages and `context` | [REVIEW] |
| S-3 | Parameterised SQL only. Template-literal SQL with interpolation fails lint | [CI] |
| S-4 | No secrets in source. There are no API keys in this app; user-supplied provider keys live in the keychain | [CI] |
| S-5 | All media written through `FileStore`, never `FileSystem` directly — that is what guarantees encryption | [CI] |
| S-6 | Delete means shred: overwrite before unlinking, and verify the row is gone (P-10) | [REVIEW] |
| S-7 | Every AI call goes through `AiService`. A provider SDK imported anywhere else fails lint (AR-2) | [CI] |
| S-8 | Consent defaults to denied. A new `PrivacyClass` is private until explicitly allowed | [REVIEW] |
| S-9 | Zero telemetry, analytics, crash reporting, or attribution. Adding any requires a documented decision and a default-off toggle | [CI] — dependency allow-list |
| S-10 | Permissions requested at the moment of use, with an in-app explanation before the OS prompt | [REVIEW] |
| S-11 | New dependencies touching crypto, storage, or network require a written justification in the PR | [REVIEW] |
| S-12 | App storage excluded from OS cloud backups; captured media never written to the shared gallery (P-16, P-17) | [REVIEW] + E2E |

---

## 8. Error handling

| # | Rule |
|---|---|
| E-1 | Expected failures return `Result`. Exceptions are for programmer errors only |
| E-2 | Every user-facing error has a `userMessage` that says what happened and what to do — never a code, never a stack |
| E-3 | Never swallow an error. Handle it, return it, or log it with context — silence is the worst option |
| E-4 | Never catch and rethrow without adding information |
| E-5 | Every write path that can fail has a defined recovery. "It probably won't happen" is not a recovery |
| E-6 | Data-loss-adjacent operations (migration, restore, key rotation, wipe) are transactional and verified before the old state is discarded |

---

## 9. Performance rules

| # | Rule |
|---|---|
| P-1 | Lists of unbounded length are virtualized. No exceptions — the timeline will have 150,000 rows |
| P-2 | No query without an index on its filter and sort columns. New queries include an `EXPLAIN QUERY PLAN` check |
| P-3 | No N+1 queries. Fetch in a batch or join |
| P-4 | Encryption, thumbnailing, and audio analysis run off the UI thread |
| P-5 | Images decrypted and decoded lazily, at display size, never at full resolution for a thumbnail |
| P-6 | Aggregates maintained incrementally on write, never computed by scanning on render |
| P-7 | Cold start under 2 seconds: nothing at startup except key bootstrap, migration check, and the first screen |

---

## 10. Git and review

| # | Rule |
|---|---|
| G-1 | Conventional commits: `feat(habits):`, `fix(xp):`, `docs(architecture):`, `test(streaks):`, `chore:` |
| G-2 | One logical change per commit. A refactor and a feature are two commits |
| G-3 | Never commit failing tests, `.only`, `console.log`, or commented-out code |
| G-4 | A schema change and its migration and its tests land together |
| G-5 | A contract change (`index.ts`, event payload, service interface) updates `API_CONTRACTS.md` in the same commit |
| G-6 | Every PR states what was tested and how |

### Review checklist

- Is any business logic in a component?
- Does any feature reach into another feature's internals?
- Does any code outside `data/` touch the database?
- Does any code outside `services/ai/` call a model?
- Is every event handler idempotent?
- Could any user content reach a log?
- Is time or randomness used directly instead of injected?
- Does the failure path leave data in a valid state?
- Are the tests specifications, or are they restating the implementation?

---

## 11. Documentation rules

| # | Rule |
|---|---|
| D-1 | Comments explain *why*, never *what*. The code says what it does |
| D-2 | Every non-obvious business rule cites its source: `// PRD §7.2 X-2: idempotent by source event` |
| D-3 | ADRs are appended to `ARCHITECTURE.md` §12 when a decision is made or reversed — including the reversal reason |
| D-4 | These documents are living. A change that makes one wrong is incomplete until the document is updated |
| D-5 | No TODO without an owner and a date. `// TODO(2026-09): …` |

---

## 12. Explicit anti-patterns

Named because they are the specific ways this codebase would decay:

- **Business logic in `useEffect`.** If a rule lives in a component lifecycle, it cannot be tested and
  will fire twice under Strict Mode.
- **A feature importing another feature's repository** to "just read one field". This is how the
  module boundary dies — always as a small, reasonable-seeming shortcut.
- **Awarding XP directly from a use case** instead of publishing an event. Breaks idempotency and
  makes the ledger untrustworthy.
- **Storing derived state as truth.** A cached level that cannot be recomputed is a level that will
  eventually be wrong with no way to find out.
- **Hard deletes.** Unsyncable, unrecoverable.
- **`catch (e) { console.log(e) }`.** An error swallowed silently in an offline app with one user is
  an error nobody will ever learn about.
- **A generic `Item` or `Entry` abstraction** covering habits, tasks, and goals because they "look
  similar". They have different rules; merging them means every rule grows a conditional.
- **Building for the future phase instead of this one.** The seams are already in place. Do not build
  the sync engine while writing the habit tracker.
