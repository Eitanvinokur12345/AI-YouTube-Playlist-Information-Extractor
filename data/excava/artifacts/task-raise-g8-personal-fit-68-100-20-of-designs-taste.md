# Raise G8 Personal fit (68/100): 20% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-30268` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Leverage taste-tagged designs in existing repos, wire NOSG for Arena learning, and curate taste beyond current scope.

**Steps:**
1. **Audit taste tags** in `designs/` dirs across repos (grep `taste:` in `.md`/`.json` files) and export IDs to `taste-tagged-ids.txt`.
2. **Run Arena learning** via `arena-learning-cli` (v1.2.0) with `--input taste-tagged-ids.txt --output arena-models/` and `--epochs 50`.
3. **Wire NOSG** by updating `nosg-config.yaml` to include `arena-models/` path and `--taste-threshold 0.75`; restart service (`systemctl restart nosg`).
4. **Curate taste beyond** by scraping 100 high-res images from `unsplash.com` (query: "aesthetic interior") and tagging them in `taste-curated.json` with `{"id": "unsplash-<hash>", "tags": ["minimalism", "warm-neutral"]}`.

**Needs:**
- `grep` (GNU), `arena-learning-cli` (v1.2.0), `nosg-config.yaml` (access: `sudo`), `jq` (for JSON tagging)
- Unsplash API key (env: `UNSPLASH_KEY`)
- Write access to `designs/`, `arena-models/`, `nosg-config.yaml`
```
