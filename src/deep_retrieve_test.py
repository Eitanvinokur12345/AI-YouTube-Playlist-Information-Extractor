"""
src/deep_retrieve_test.py — regression test for fusable()'s egress-awareness (fire 133) and
select_batch()'s filler-fusability gate (fire 134).

Fires 131/132 both burned ~39/40 deep_retrieve batch slots on github/website-link-only stubs
whose network fetches silently return "" under this session's restricted egress — because the
old fusability check counted any link as fusable regardless of whether it was actually
reachable. Fire 133 fixed that for the `fresh` selection path but left the cursor-walk
`filler` fallback unfiltered, so a restricted-egress run could still fill a whole batch with
doomed readme_excerpt()/homepage_meta() network timeouts via filler alone once fresh ran dry.
This asserts both: fusable()'s egress-awareness, and that select_batch() never places a
non-fusable element into the batch via either path.

Free, stdlib, no network. Run:  python -m src.deep_retrieve_test
"""
from __future__ import annotations

import sys

from src.deep_retrieve import fusable, select_batch

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

    # select_batch(): filler must skip non-fusable elements too (fire 134 fix). Two stubs,
    # neither attempted recently, neither fusable (restricted egress, no local transcript) —
    # fresh is empty (fusable-gated), and filler must NOT fall back to them unfiltered.
    def egress_closed(e: dict) -> bool:
        return fusable(e, egress_open=False)

    unfusable_stub_a = {"id": "u1", "stub": True, "links": {"github": "https://github.com/a/b"},
                         "source_videos": []}
    unfusable_stub_b = {"id": "u2", "stub": True, "links": {"website": "https://example.com"},
                         "source_videos": []}
    todo = [unfusable_stub_a, unfusable_stub_b]
    batch, fresh = select_batch(todo, egress_closed, attempts={}, cutoff="9999",
                                 start=0, limit=5)
    check("select_batch: fresh pool is empty when no element is fusable",
          fresh == [])
    check("select_batch: filler does NOT fill the batch with non-fusable elements "
          "(the fire 133 self-criticism, closed this fire)",
          batch == [], f"batch={[e['id'] for e in batch]}")

    # Sanity: a fusable element (local transcript on disk, so fusable regardless of egress)
    # DOES get picked up by filler once fresh is empty for it.
    fusable_stub = {"id": "u3", "stub": True, "links": {}, "source_videos": []}

    def always_fusable(e: dict) -> bool:
        return True

    batch2, _ = select_batch([fusable_stub], always_fusable, attempts={}, cutoff="9999",
                              start=0, limit=5)
    check("select_batch: filler still fills the batch with genuinely fusable elements",
          [e["id"] for e in batch2] == ["u3"])

    print(f"\n{'ALL PASS' if not FAILS else f'{len(FAILS)} FAIL(S): ' + ', '.join(FAILS)}")
    return 1 if FAILS else 0


if __name__ == "__main__":
    raise SystemExit(main())
