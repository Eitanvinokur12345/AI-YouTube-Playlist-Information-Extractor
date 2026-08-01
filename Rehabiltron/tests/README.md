# tests/ — cross-cutting test suites

**Empty by design.** Implementation has not been authorised — see
[`../docs/PRE_IMPLEMENTATION_REVIEW.md`](../docs/PRE_IMPLEMENTATION_REVIEW.md) §7.

Unit and integration tests live **beside their subject** in `src/` (`streakRules.ts` /
`streakRules.test.ts`) — see [`../docs/CODING_RULES.md`](../docs/CODING_RULES.md) ORG-4. This folder
holds only the suites that span the whole app.

```
tests/
├── e2e/          Maestro flows covering the MVP acceptance criteria
├── migrations/   fixture databases at each schema version + upgrade-path tests
└── fixtures/     shared seed data
```

The `migrations/` fixtures are committed and **never regenerated** — a fixture recreated from current
code stops testing the upgrade it exists to test
([`../docs/DATABASE_DESIGN.md`](../docs/DATABASE_DESIGN.md) §5).

Test bars: domain coverage ≥ 90%, overall ≥ 70%, no network in any test, time and randomness always
injected.
