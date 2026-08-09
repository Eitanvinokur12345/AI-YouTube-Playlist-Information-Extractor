"""
src/net_canary.py — the ONE shared "is general internet egress actually open right now?" check.

Fire 50 (2026-07-28) discovered that an interactive cloud dev sandbox's outbound HTTPS goes
through a policy-restricted proxy that 403s/400s any host outside a small allowlist — not a
real outage, but indistinguishable from one to a plain urlopen() call. That fire's fix (a
two-anchor canary: github.com + www.wikipedia.org, treated as "egress is open" if either
answers) got copy-pasted into three call sites (verify_elements.py fire 50,
verify_connectors.py fire 50, github_meta_enrich.py fire 51) instead of shared. This module
is the shared version, built (fire 124) so a fourth caller (standing_checks.py) wouldn't need
a fourth copy, and so the next fire that wants to KNOW the verdict up front (before choosing
which increment to attempt) has one place to ask instead of re-deriving it by hand. Fire 135
(2026-08-08) finished the consolidation: all three original call sites now delegate their
`_network_open()` to `network_open()` below instead of carrying their own anchor loop.

Deliberately does NOT test api.github.com: a Claude-Code-on-web session's GitHub access is
scoped to one repo, so api.github.com calls for OTHER repos 403 with "not enabled for this
session" — a response that looks identical over the wire to GitHub's own real rate-limiting,
which is exactly the ambiguity the two neutral anchors below exist to sidestep (verified live
by fire 124: api.github.com/repos/octocat/Hello-World -> 403 in this exact session type, while
api.github.com/ with no repo path -> 200 — a false-open signal a same-host check would have
produced). github.com and www.wikipedia.org need no per-repo grant, so a clean answer from
either is real signal.
"""
from __future__ import annotations

import urllib.request

ANCHORS = ("https://github.com", "https://www.wikipedia.org")


def network_open(timeout: int = 12) -> bool:
    """True if general web egress looks open (either anchor answers <400). False means:
    do not write live-link verdicts, do not treat a 403 from a scoped API as real rate-limiting
    — skip the batch untouched rather than poison data on a false diagnosis."""
    for anchor in ANCHORS:
        try:
            req = urllib.request.Request(anchor, headers={"User-Agent": "excava-net-canary"}, method="HEAD")
            with urllib.request.urlopen(req, timeout=timeout) as r:
                if r.status < 400:
                    return True
        except Exception:
            continue
    return False


# Lanes that self-abort (by design, now via a direct call into this module — fire 135,
# 2026-08-08 closed the "copy-pasted instead of shared" debt this module's own docstring
# used to flag) when egress is restricted — kept here so a caller can explain the
# consequence, not just the verdict.
NETWORK_DEPENDENT_LANES = (
    "verify_elements", "verify_connectors", "github_meta_enrich",
)


def describe() -> dict:
    open_ = network_open()
    return {
        "open": open_,
        "note": ("general web egress open." if open_ else
                 "general web egress restricted (repo-scoped session, e.g. Claude Code on the "
                 f"web) — {', '.join(NETWORK_DEPENDENT_LANES)} will self-abort untouched rather "
                 "than risk false verdicts; pick a local/deterministic increment instead."),
    }


if __name__ == "__main__":
    import json
    print(json.dumps(describe(), indent=2))
