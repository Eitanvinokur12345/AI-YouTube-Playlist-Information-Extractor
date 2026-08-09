"""
src/analyze_batch_test.py — regression test for compute_age_months()'s live-clock fix (fire 137).

`TODAY` used to be a module-level constant frozen at 2026-06-03. Every day past that date, every
video's computed age understated its true age by the growing gap between the frozen date and the
real one — and any video published after 2026-06-03 got a NEGATIVE delta, clamped to age 0 by the
`max(0, ...)` guard, so it always won `rate_quality()`'s recency penalty regardless of its real
publish date. Fixed by computing `datetime.now(timezone.utc)` at call time instead. This asserts
the age is computed relative to the real current time, not a frozen constant, and that two videos
published a known distance apart keep that same distance in the computed ages.

Free, stdlib, no network. Run:  python -m src.analyze_batch_test
"""
from __future__ import annotations

import sys
from datetime import datetime, timedelta, timezone

from src.analyze_batch import compute_age_months

FAILS: list = []


def check(name: str, cond: bool, detail: str = "") -> None:
    print(f"  {'PASS' if cond else 'FAIL'}  {name}{'' if cond else ' — ' + detail}")
    if not cond:
        FAILS.append(name)


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    print("analyze_batch compute_age_months() live-clock regression test")

    now = datetime.now(timezone.utc)

    five_months_ago = (now - timedelta(days=150)).isoformat().replace("+00:00", "Z")
    age = compute_age_months(five_months_ago)
    check("a video published ~150 days ago computes to ~5 months old (not frozen-clock skewed)",
          4.5 <= age <= 5.5, f"got {age}")

    just_published = now.isoformat().replace("+00:00", "Z")
    age0 = compute_age_months(just_published)
    check("a video published right now computes to ~0 months old",
          age0 < 0.1, f"got {age0}")

    # The fire-137 bug: with TODAY frozen in the past, anything published after that frozen date
    # produced a negative delta, clamped by max(0, ...) to 0 — indistinguishable from brand new.
    # Two videos a known distance apart must stay that distance apart under the live clock.
    older = (now - timedelta(days=200)).isoformat().replace("+00:00", "Z")
    newer = (now - timedelta(days=20)).isoformat().replace("+00:00", "Z")
    age_older = compute_age_months(older)
    age_newer = compute_age_months(newer)
    check("an older video is NOT clamped to the same age as a newer one (the fire 137 bug)",
          age_older > age_newer + 5, f"older={age_older}, newer={age_newer}")

    print(f"\n{'ALL PASS' if not FAILS else f'{len(FAILS)} FAIL(S): ' + ', '.join(FAILS)}")
    return 1 if FAILS else 0


if __name__ == "__main__":
    raise SystemExit(main())
