"""
src/deep_retrieve_test.py — regression test for fusable()'s egress-awareness (fire 133).

Fires 131/132 both burned ~39/40 deep_retrieve batch slots on github/website-link-only stubs
whose network fetches silently return "" under this session's restricted egress — because the
old fusability check counted any link as fusable regardless of whether it was actually
reachable. This asserts the fix: a link-only element is fusable when egress is open and NOT
fusable when it's closed, while a locally-transcribed element is fusable either way.

Free, stdlib, no network. Run:  python -m src.deep_retrieve_test
"""
from __future__ import annotations

import sys

from src.deep_retrieve import fusable

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
    print("deep_retrieve fusable() egress-awareness regression test")

    link_only = {"id": "t1", "links": {"github": "https://github.com/x/y"}, "source_videos": []}
    check("link-only element IS fusable when egress is open",
          fusable(link_only, egress_open=True))
    check("link-only element is NOT fusable when egress is restricted (the fire 131/132 bug)",
          not fusable(link_only, egress_open=False))

    no_source = {"id": "t2", "links": {}, "source_videos": ["nonexistent-video-id"]}
    check("no-source element is fusable under neither egress state (open)",
          not fusable(no_source, egress_open=True))
    check("no-source element is fusable under neither egress state (closed)",
          not fusable(no_source, egress_open=False))

    print(f"\n{'ALL PASS' if not FAILS else f'{len(FAILS)} FAIL(S): ' + ', '.join(FAILS)}")
    return 1 if FAILS else 0


if __name__ == "__main__":
    raise SystemExit(main())
