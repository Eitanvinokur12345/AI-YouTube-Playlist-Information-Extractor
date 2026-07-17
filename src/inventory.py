"""src/inventory.py — STEP-0 SYSTEM MAP: which modules are WIRED, ORPHANED, or DEAD.

The overhaul (EXCAVA_END_PLAN §11 FIRST MOVE) stands on one honest fact nobody had
actually computed: of the ~98 src modules, which are truly reachable and which are dead
weight? The plan asserts "21 dead modules" but never enumerated them — this derives the
real list, deterministically, with no engine.

METHOD (pure static analysis, reproducible):
  entrypoints = every `python -m src.X` in .github/workflows/*.yml  +  the beat (src.excava)
  edges       = `import src.X` / `from src.X import` / `from src import X` (incl. lazy
                in-function imports — ast walks the whole tree, which is how the beat wires
                most lanes).
  reachable   = BFS over edges from the entrypoints.
  WIRED    = an entrypoint, or reachable from one (it actually runs).
  ORPHANED = some module imports it, but no entrypoint reaches it (referenced, never run).
  DEAD     = nothing imports it AND no workflow runs it (genuinely unreferenced).

Writes data/excava/system_inventory.json (the cockpit System Map reads this) and prints a
summary. Feeds the quarantine-never-delete cleanup: only DEAD modules are safe to retire.

Run: python -m src.inventory            (rebuild the map + print summary)
     python -m src.inventory --json     (print the full map as JSON)
"""
from __future__ import annotations

import ast
import json
import re
from collections import deque
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
SRC = ROOT / "src"
WF = ROOT / ".github" / "workflows"
OUT = ROOT / "data" / "excava" / "system_inventory.json"

# Modules run by a HUMAN/AGENT from the shell, not by CI or an import — they are entrypoints
# too, and must never be graded "dead". (git_safe is the mandated shipper; inventory is this
# very tool.) Everything else earns "operator" status by being referenced as a runnable
# command in the docs/config, so the list stays tiny and honest.
KNOWN_OPERATOR = {"git_safe", "inventory"}

# Where a runnable command would be documented (NOT data/excava/artifacts — that's agent
# output, and a module named in a stale artifact must not count as "alive").
REF_GLOBS = ["*.md", "CLAUDE.md", "config.json", "docs/*.md", "docs/*.js", "docs/*.html",
             "brain/*.md", "data/*.json", "data/dev_construction.json"]


def _modules() -> dict[str, Path]:
    """Every importable src module (stem -> path), excluding the package marker."""
    return {p.stem: p for p in sorted(SRC.glob("*.py")) if p.stem != "__init__"}


def _imports_of(path: Path, known: set[str]) -> set[str]:
    """src modules imported by this file — handles `import src.X`, `from src.X import ...`,
    and `from src import X, Y` (the beat's lazy-import style). Falls back to a regex scan if
    the file doesn't parse, so a syntax error never silently drops edges."""
    text = path.read_text(encoding="utf-8", errors="replace")
    out: set[str] = set()
    try:
        tree = ast.parse(text)
    except SyntaxError:
        for m in re.finditer(r"(?:import\s+src\.(\w+)|from\s+src\.(\w+)\s+import|"
                             r"from\s+src\s+import\s+([\w,\s]+))", text):
            for g in m.groups():
                if g:
                    for name in re.split(r"[,\s]+", g.strip()):
                        if name in known:
                            out.add(name)
        return out
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:                       # import src.X  /  import src.X as y
                if a.name.startswith("src.") and a.name.split(".")[1] in known:
                    out.add(a.name.split(".")[1])
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            if mod == "src":                           # from src import X, Y
                for a in node.names:
                    if a.name in known:
                        out.add(a.name)
            elif mod.startswith("src."):               # from src.X import y
                head = mod.split(".")[1]
                if head in known:
                    out.add(head)
    # Runtime edges AST can't see: subprocess dispatch / importlib, where the target module is a
    # QUOTED string literal (`"src.power_scan"`, `subprocess.run([...,"src.foo"])`). A module a
    # wired module shells out to is wired too. Quoted-only on purpose: it skips the unquoted
    # `python -m src.X` examples in docstrings, which are documentation, not calls.
    for m in re.finditer(r"['\"]src\.(\w+)", text):
        if m.group(1) in known and m.group(1) != path.stem:      # ignore self's own run-example
            out.add(m.group(1))
    return out


def _repo_references(known: set[str]) -> dict[str, list[str]]:
    """module -> [doc/config files that name it as a runnable command] (`src.X` / `src/X`).
    This is the 'operator tool' signal: a module CI never touches but the docs tell a human
    to run is ALIVE, not dead. One findall pass per file (not 98 regexes), and giant data
    dumps are skipped — a runnable command is never documented inside an 8 MB index."""
    tok = re.compile(r"src[./](\w+)")
    refs: dict[str, set[str]] = {name: set() for name in known}
    seen: set[Path] = set()
    for pattern in REF_GLOBS:
        for f in ROOT.glob(pattern):
            if not f.is_file() or f in seen or f.stat().st_size > 512_000:
                continue
            seen.add(f)
            text = f.read_text(encoding="utf-8", errors="replace")
            rel = f.relative_to(ROOT).as_posix()
            for name in set(tok.findall(text)) & known:
                refs[name].add(rel)
    return {k: sorted(v) for k, v in refs.items()}


def _workflow_entrypoints(known: set[str]) -> dict[str, list[str]]:
    """module -> [workflow files that run it via `python -m src.X`]."""
    hits: dict[str, list[str]] = {}
    if not WF.exists():
        return hits
    for yml in sorted(WF.glob("*.yml")) + sorted(WF.glob("*.yaml")):
        text = yml.read_text(encoding="utf-8", errors="replace")
        for m in set(re.findall(r"python\s+-m\s+src\.(\w+)", text)):
            if m in known:
                hits.setdefault(m, []).append(yml.name)
    return hits


def build() -> dict:
    mods = _modules()
    known = set(mods)
    imports = {name: _imports_of(path, known) for name, path in mods.items()}
    imported_by: dict[str, set[str]] = {name: set() for name in known}
    for name, deps in imports.items():
        for d in deps:
            imported_by[d].add(name)

    wf = _workflow_entrypoints(known)
    refs = _repo_references(known)
    entry = set(wf) | ({"excava"} if "excava" in known else set())   # the beat is an entrypoint

    # BFS reachability from every entrypoint over the import graph
    reachable: set[str] = set()
    q = deque(entry)
    while q:
        cur = q.popleft()
        if cur in reachable:
            continue
        reachable.add(cur)
        for d in imports.get(cur, ()):
            if d not in reachable:
                q.append(d)

    modules = {}
    for name, path in mods.items():
        operator = name in KNOWN_OPERATOR or bool(refs[name])
        if name in reachable:
            status = "wired"                      # CI/beat runs it (directly or via import)
        elif operator:
            status = "operator"                   # a human/agent runs it; docs name the command
        elif imported_by[name]:
            status = "orphaned"                   # referenced by code, but nothing runs that code
        else:
            status = "dead"                       # nobody imports, nothing runs, no doc names it
        modules[name] = {
            "status": status,
            "loc": path.read_text(encoding="utf-8", errors="replace").count("\n") + 1,
            "entrypoint": name in entry,
            "invoked_by": sorted(wf.get(name, [])),
            "documented_in": refs[name],
            "imported_by": sorted(imported_by[name]),
            "imports": sorted(imports[name]),
        }

    counts = {"wired": 0, "operator": 0, "orphaned": 0, "dead": 0}
    for m in modules.values():
        counts[m["status"]] += 1
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total": len(modules),
        "counts": counts,
        "entrypoints": sorted(entry),
        "modules": dict(sorted(modules.items())),
    }


def refresh() -> dict:
    """Rebuild the map and persist it. The beat calls this every tick so the System Map the
    owner browses is never stale. Returns the inventory dict."""
    inv = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(inv, ensure_ascii=False, indent=1), encoding="utf-8")
    return inv


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    inv = refresh()
    if "--json" in sys.argv:
        print(json.dumps(inv, ensure_ascii=False, indent=1))
        return 0
    c = inv["counts"]
    print(f"SYSTEM MAP  ·  {inv['total']} modules  ·  wired {c['wired']}  ·  "
          f"operator {c['operator']}  ·  orphaned {c['orphaned']}  ·  dead {c['dead']}")
    for status, blurb in (("dead", "nothing imports, no workflow runs, no doc names it — QUARANTINE"),
                          ("orphaned", "imported by code, but nothing runs that code — review"),
                          ("operator", "CI never runs it; a human/agent does (doc-named CLI)")):
        rows = [(n, m) for n, m in inv["modules"].items() if m["status"] == status]
        if not rows:
            continue
        print(f"\n{status.upper()} ({blurb}):")
        for n, m in rows:
            tail = (f"imported_by={m['imported_by']}" if status == "orphaned"
                    else (f"doc={m['documented_in'][:2]}" if m["documented_in"] else ""))
            print(f"  · {n:<26} {m['loc']:>4} loc  {tail}")
    print(f"\nwrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
