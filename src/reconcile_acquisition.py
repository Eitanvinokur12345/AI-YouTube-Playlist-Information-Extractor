"""Reconcile concurrent acquisition writes. Ambiguous edits require manual recovery."""
import json
import subprocess
from pathlib import Path

CATALOGUES = {"skills": "skill_name", "tools": "name", "connectors": "name",
              "designs": "name", "prompts": "title", "commands": "command"}
VIEWS = {"brain_graph", "cross_tab_conflicts", "data_guard", "effectiveness", "health",
         "hub", "models", "self_check", "safety", "guardrails_status", "pipeline_graph",
         "pipeline_status", "maintenance_check"}
MISSING = object()


def combine(base, upstream, local, field=""):
    if local == base or upstream == local:
        return upstream
    if upstream == base:
        return local
    if isinstance(upstream, dict) and isinstance(local, dict) and (base is MISSING or isinstance(base, dict)):
        old = {} if base is MISSING else base
        merged = {}
        for key in dict.fromkeys([*upstream, *local]):
            value = combine(old.get(key, MISSING), upstream.get(key, MISSING), local.get(key, MISSING), key)
            if value is not MISSING:
                merged[key] = value
        return merged
    if isinstance(upstream, list) and isinstance(local, list) and (base is MISSING or isinstance(base, list)):
        old = [] if base is MISSING else base
        if field in CATALOGUES:
            def index(rows):
                result = {}
                for row in rows:
                    key = (row.get("slug") or row.get(CATALOGUES[field]) or "").casefold()
                    if not key or key in result:
                        raise ValueError("Ambiguous catalogue identity")
                    result[key] = row
                return result
            return list(combine(index(old), index(upstream), index(local)).values())
        def signature(v):
            return json.dumps(v, sort_keys=True)
        known = {signature(v) for v in upstream + old}
        return upstream + [v for v in local if signature(v) not in known]
    if field in {"updated_at", "generated_at", "last_updated"} and isinstance(local, str) and isinstance(upstream, str):
        return max(local, upstream)
    raise ValueError("Concurrent changes to " + field)


def main():
    def git(*args):
        return subprocess.check_output(["git", *args])
    for name in filter(None, git("diff", "--name-only", "--diff-filter=U", "-z").decode().split("\0")):
        path = Path(name)
        if path.parent == Path("data") and path.stem in VIEWS and path.suffix == ".json":
            content = git("show", ":2:" + name)
        elif path.parent == Path("data") and path.stem in {*CATALOGUES, "mined_state", "gemini_analyzed"} and path.suffix == ".json":
            result = combine(*(json.loads(git("show", f":{i}:{name}")) for i in (1, 2, 3)))
            content = json.dumps(result, ensure_ascii=False, indent=2).encode()
        else:
            raise ValueError("Unresolved conflict: " + name)
        path.write_bytes(content)
        git("add", "--", name)


if __name__ == "__main__":
    main()
