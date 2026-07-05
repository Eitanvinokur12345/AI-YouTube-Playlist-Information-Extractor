"""
src/make_monsters.py — M3.2: the MONSTER CAST, code-drawn SVG (free-first).

11 species, one per department, matched to the job — friendly-but-distinctive with a cool
edge (owner's direction): organic blob bodies (nothing is a plain circle), department color,
a signature feature + tool. Three variants each: AGENT (named), LEAD (suit-and-tie, slightly
bigger), WORKER (small, generic, no unique features). Output: docs/assets/monsters/*.svg
(and a sample sheet docs/assets/monsters/index.html for Eitan to judge the quality).

These are the SAMPLES (owner: "create the creatures, I'll see them") — if the style misses,
an image-gen round replaces the bodies; the rig (names/variants/wiring) stays.
Run: python -m src.make_monsters
"""
from __future__ import annotations

from pathlib import Path

OUT = Path(__file__).parent.parent / "docs" / "assets" / "monsters"

# dept: (name, hue-color body, accent, blob path seed, eyes, feature, tool emblem)
SPECIES = {
    "transcripts": ("Echo",   "#8ecae6", "#219ebc", 1, 2, "big-ears",   "scroll"),
    "analysis":    ("Marrow", "#b5838d", "#6d6875", 2, 1, "loupe-eye",  "gear"),
    "watch":       ("Iris",   "#cdb4db", "#8956a8", 3, 3, "tri-eye",    "screen"),
    "links":       ("Ledger", "#ffb703", "#fb8500", 4, 2, "chain-arm",  "link"),
    "memory":      ("Root",   "#95d5b2", "#40916c", 5, 2, "root-legs",  "brain"),
    "mining":      ("Boulder","#d5bdaf", "#7f5539", 6, 1, "rock-back",  "pick"),
    "visual":      ("Chroma", "#f7a8c4", "#d81159", 7, 2, "paint-drip", "brush"),
    "news":        ("Wire",   "#a8dadc", "#457b9d", 8, 2, "antenna",    "mega"),
    "improve":     ("Ratchet","#b9fbc0", "#2d6a4f", 9, 2, "bolt-head",  "wrench"),
    "security":    ("Bastion","#adb5bd", "#343a40", 10, 1, "shield-chest","shield"),
    "creators":    ("Nova",   "#ffd166", "#ef476f", 11, 3, "spark-crown","bulb"),
}

# organic body blobs (each species its own silhouette — never a plain circle)
BLOBS = {
    1: "M50 12 C74 8 90 30 86 52 C83 72 70 90 48 88 C26 86 12 70 14 48 C16 26 30 15 50 12 Z",
    2: "M50 10 C68 14 88 24 87 46 C86 70 74 92 50 90 C30 88 10 74 13 50 C15 28 32 7 50 10 Z",
    3: "M48 14 C70 6 92 26 88 50 C85 74 66 92 46 89 C24 86 8 66 14 44 C18 26 32 19 48 14 Z",
    4: "M52 10 C72 12 86 32 88 54 C90 76 68 92 46 88 C26 84 10 68 14 44 C18 24 34 8 52 10 Z",
    5: "M50 16 C72 10 88 28 86 48 C84 70 72 84 52 88 C30 92 12 72 14 50 C15 30 30 20 50 16 Z",
    6: "M46 14 C68 8 90 22 88 46 C87 68 76 88 52 90 C28 91 10 72 12 48 C14 28 26 19 46 14 Z",
    7: "M50 10 C68 10 84 22 88 44 C92 68 74 90 50 90 C28 90 12 74 12 50 C12 28 30 10 50 10 Z",
    8: "M50 14 C70 10 88 26 87 48 C86 72 70 90 48 90 C26 89 12 70 13 46 C14 26 32 17 50 14 Z",
    9: "M48 12 C70 8 88 24 88 48 C88 70 72 90 48 90 C26 90 10 72 12 46 C13 26 28 15 48 12 Z",
    10: "M50 12 C74 10 88 28 88 50 C88 74 70 92 48 90 C26 88 12 72 12 48 C12 26 28 13 50 12 Z",
    11: "M50 8 C70 12 88 26 86 50 C84 74 70 92 48 90 C26 88 10 70 14 46 C17 24 32 5 50 8 Z",
}

TOOL = {
    "scroll": '<rect x="66" y="58" width="18" height="24" rx="4" fill="#fff" stroke="#333" stroke-width="2"/><line x1="70" y1="65" x2="80" y2="65" stroke="#999" stroke-width="1.6"/><line x1="70" y1="70" x2="80" y2="70" stroke="#999" stroke-width="1.6"/><line x1="70" y1="75" x2="77" y2="75" stroke="#999" stroke-width="1.6"/>',
    "gear": '<circle cx="74" cy="68" r="9" fill="none" stroke="#333" stroke-width="3"/><circle cx="74" cy="68" r="3" fill="#333"/><path d="M74 55 v-4 M74 81 v4 M61 68 h-4 M87 68 h4" stroke="#333" stroke-width="3"/>',
    "screen": '<rect x="62" y="58" width="24" height="17" rx="3" fill="#222" stroke="#333" stroke-width="2"/><rect x="65" y="61" width="10" height="4" fill="#7ae582"/><rect x="65" y="67" width="16" height="3" fill="#555"/>',
    "link": '<path d="M64 66 a6 6 0 0 1 8-8 l4 4 M80 70 a6 6 0 0 1 -8 8 l-4 -4 M68 74 l10 -10" stroke="#333" stroke-width="3.4" fill="none" stroke-linecap="round"/>',
    "brain": '<path d="M66 64 c-3-6 5-11 9-7 c5-5 13 1 9 7 c5 3 1 11-4 10 c-2 5-10 5-11 0 c-5 1-7-7-3-10 Z" fill="#fff" stroke="#333" stroke-width="2"/>',
    "pick": '<path d="M62 78 l16-16" stroke="#5c4033" stroke-width="4" stroke-linecap="round"/><path d="M72 56 c6-2 12 0 16 6 c-6-1-11 0-14 2 Z" fill="#666" stroke="#333" stroke-width="2"/>',
    "brush": '<path d="M64 80 l12-14" stroke="#8a5a44" stroke-width="4" stroke-linecap="round"/><path d="M76 66 c2-6 8-8 12-6 c-2 5-5 9-9 9 Z" fill="#d81159" stroke="#333" stroke-width="2"/>',
    "mega": '<path d="M62 70 l14-8 v16 Z" fill="#fff" stroke="#333" stroke-width="2.4"/><path d="M78 64 a10 10 0 0 1 0 16" stroke="#333" stroke-width="2.4" fill="none"/>',
    "wrench": '<path d="M64 80 l12-12" stroke="#555" stroke-width="4" stroke-linecap="round"/><path d="M76 68 a8 8 0 1 0 8-8 l-5 5 -4-1 1-4 5-5 a8 8 0 0 0-8 8" fill="#888" stroke="#333" stroke-width="1.8"/>',
    "shield": '<path d="M73 56 l10 4 v8 c0 7-5 11-10 13 c-5-2-10-6-10-13 v-8 Z" fill="#fff" stroke="#333" stroke-width="2.4"/><path d="M73 61 v14 M66 68 h14" stroke="#adb5bd" stroke-width="2.4"/>',
    "bulb": '<circle cx="74" cy="64" r="8" fill="#fffbe6" stroke="#333" stroke-width="2.4"/><path d="M71 72 h6 v5 h-6 Z" fill="#ccc" stroke="#333" stroke-width="1.6"/><path d="M74 50 v-5 M62 54 l-3-3 M86 54 l3-3" stroke="#ef476f" stroke-width="2.4" stroke-linecap="round"/>',
}


def eyes(n: int, accent: str, big: bool = False) -> str:
    r = 7 if big else 5.5
    xs = {1: [46], 2: [38, 56], 3: [34, 47, 60]}[n]
    out = ""
    for x in xs:
        out += (f'<ellipse cx="{x}" cy="42" rx="{r}" ry="{r + 1.5}" fill="#fff" stroke="#333" stroke-width="2.2"/>'
                f'<circle cx="{x + 1}" cy="43" r="{r * 0.45}" fill="#222"/>'
                f'<circle cx="{x + 2.4}" cy="41" r="{r * 0.16}" fill="#fff"/>')
    return out


def feature(kind: str, body: str, accent: str) -> str:
    return {
        "big-ears": f'<path d="M14 34 C4 20 12 8 22 14 C28 18 26 30 20 36 Z" fill="{body}" stroke="#333" stroke-width="2.4"/><path d="M86 34 C96 20 88 8 78 14 C72 18 74 30 80 36 Z" fill="{body}" stroke="#333" stroke-width="2.4"/>',
        "loupe-eye": f'<circle cx="46" cy="42" r="13" fill="none" stroke="{accent}" stroke-width="3.4"/><line x1="55" y1="52" x2="63" y2="60" stroke="{accent}" stroke-width="3.4" stroke-linecap="round"/>',
        "tri-eye": "",
        "chain-arm": f'<circle cx="16" cy="62" r="4" fill="none" stroke="{accent}" stroke-width="2.6"/><circle cx="12" cy="70" r="4" fill="none" stroke="{accent}" stroke-width="2.6"/><circle cx="10" cy="78" r="4" fill="none" stroke="{accent}" stroke-width="2.6"/>',
        "root-legs": f'<path d="M34 88 c-2 8-8 10-12 14 M50 90 c0 8 3 10 3 14 M66 88 c3 8 9 10 12 13" stroke="{accent}" stroke-width="3.4" fill="none" stroke-linecap="round"/>',
        "rock-back": f'<path d="M24 26 l8-10 8 8 8-12 8 10 8-6 6 10" fill="none" stroke="{accent}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>',
        "paint-drip": f'<path d="M30 14 c2 8 8 8 8 14 a4 4 0 0 1-8 0 c0-6 -2-8 0-14 Z" fill="{accent}"/><path d="M62 10 c2 6 6 7 6 12 a3.4 3.4 0 0 1-7 0 c0-5-1-6 1-12 Z" fill="#7ae582"/>',
        "antenna": f'<path d="M38 16 c-2-8-8-10-8-14 M62 16 c2-8 8-10 8-14" stroke="{accent}" stroke-width="3" fill="none" stroke-linecap="round"/><circle cx="30" cy="4" r="3.4" fill="{accent}"/><circle cx="70" cy="4" r="3.4" fill="{accent}"/>',
        "bolt-head": f'<path d="M44 12 l6-8 2 6 8-6 -2 9" fill="none" stroke="{accent}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
        "shield-chest": "",
        "spark-crown": f'<path d="M34 12 l4-9 5 7 6-10 6 10 5-7 4 9" fill="none" stroke="{accent}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
    }.get(kind, "")


def monster(dept: str, variant: str) -> str:
    name, body, accent, blob, n_eyes, feat, tool = SPECIES[dept]
    scale = {"lead": 1.0, "agent": 0.92, "worker": 0.66}[variant]
    parts = [f'<path d="{BLOBS[blob]}" fill="{body}" stroke="#333" stroke-width="3"/>']
    parts.append(f'<path d="{BLOBS[blob]}" fill="url(#tex)" opacity="0.5"/>')
    if variant != "worker":
        parts.append(feature(feat, body, accent))
        parts.append(TOOL[tool])
    parts.append(eyes(1 if variant == "worker" else n_eyes, accent, big=(variant == "lead")))
    mouth = ('<path d="M40 62 q8 8 18 1" stroke="#333" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
             if variant != "worker" else
             '<path d="M42 60 q6 5 12 0" stroke="#333" stroke-width="2.2" fill="none" stroke-linecap="round"/>')
    parts.append(mouth)
    if variant == "lead":                                       # suit-and-tie
        parts.append(f'<path d="M36 78 l14 8 14-8 v14 h-28 Z" fill="#2b2d42" stroke="#333" stroke-width="2"/>'
                     f'<path d="M50 84 l-4 4 4 8 4-8 Z" fill="{accent}" stroke="#333" stroke-width="1.4"/>'
                     f'<circle cx="43" cy="86" r="1.4" fill="#fff"/><circle cx="57" cy="86" r="1.4" fill="#fff"/>')
    label = {"lead": name, "agent": f"{dept} agent", "worker": "worker"}[variant]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 104" width="{int(100 * scale)}" '
            f'height="{int(104 * scale)}" role="img" aria-label="{label}">'
            f'<defs><pattern id="tex" width="4" height="4" patternUnits="userSpaceOnUse">'
            f'<path d="M0 0 L4 4" stroke="#00000010" stroke-width="1"/></pattern></defs>'
            + "".join(parts) + "</svg>")


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    cards = []
    for dept in SPECIES:
        for variant in ("lead", "agent", "worker"):
            svg = monster(dept, variant)
            (OUT / f"{dept}-{variant}.svg").write_text(svg, encoding="utf-8")
        name = SPECIES[dept][0]
        cards.append(f'<div class="m"><h3>{name} <small>({dept})</small></h3>'
                     f'<div class="row"><img src="{dept}-lead.svg" title="lead (suit)">'
                     f'<img src="{dept}-agent.svg" title="agent">'
                     f'<img src="{dept}-worker.svg" title="worker"></div></div>')
    (OUT / "index.html").write_text(
        '<!doctype html><meta charset="utf-8"><title>Monster cast — samples</title>'
        '<style>body{font-family:system-ui;background:#faf7ef;padding:30px;max-width:1080px;margin:auto}'
        'h1{font-family:"Arial Black"} .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px}'
        '.m{border:2px solid #333;border-radius:14px 18px 12px 16px;background:#fff;padding:14px;'
        'box-shadow:4px 5px 0 #33333326}.row{display:flex;align-items:flex-end;gap:10px}</style>'
        '<h1>THE MONSTER CAST — code-drawn samples (M3.2)</h1>'
        '<p>11 species, one per department: lead (suit-and-tie) · agent · worker. '
        'Judge the style — if it misses, an image-gen round replaces the bodies; the rig stays.</p>'
        f'<div class="grid">{"".join(cards)}</div>', encoding="utf-8")
    print(f"monsters: {len(SPECIES) * 3} SVGs + sample sheet -> docs/assets/monsters/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
