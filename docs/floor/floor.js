// EXCAVA floor — M3.3: the isometric factory floor (+ side-view cutaways).
// Pure code-drawn SVG (free-first), design per EXCAVA_V2_ADDITIONS §I: refined
// heavy-machinery + playful; yellow + warm ink; real metal framing; pockets of
// greenery; light surface; neobrutalist hard shadows; organic silhouettes.
// Exposes window.ExcavaFloor = { RING, ACCENT, ground, building, cutaway } —
// dashboard.js composes it into the #excava cockpit. Degrades gracefully: if this
// file is missing, dashboard.js falls back to the flat floor.
(function () {
  const INK = "#33291a";
  const _e = s => String(s == null ? "" : s)
    .replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

  // 8 ring slots around the core — a diamond, so the whole floor reads isometric.
  const RING = [[50, 9], [77, 22], [90, 48], [77, 74], [50, 87], [23, 74], [10, 48], [23, 22]];

  // department accents — the SAME accents the monster cast wears (src/make_monsters.py)
  const ACCENT = { transcripts: "#219ebc", analysis: "#6d6875", watch: "#8956a8", links: "#fb8500",
    memory: "#40916c", mining: "#7f5539", visual: "#d81159", news: "#457b9d", improve: "#2d6a4f",
    security: "#343a40", creators: "#ef476f" };

  // a pocket of greenery: an organic bush cluster (never a plain circle)
  function bush(x, y, s) {
    return `<g transform="translate(${x} ${y}) scale(${s})">
      <path d="M0 12 C-8 12 -12 4 -7 -1 C-9 -8 0 -12 4 -7 C12 -10 16 0 10 4 C13 10 6 14 0 12 Z"
        fill="#7fb069" stroke="${INK}" stroke-width="2"/>
      <path d="M-2 2 C0 -2 4 -3 6 0" fill="none" stroke="#5a8a4a" stroke-width="1.6"/></g>`;
  }
  function planter(x, y) {
    return `<g transform="translate(${x} ${y})">
      <path d="M-16 4 L16 4 L12 16 L-12 16 Z" fill="#b7a98a" stroke="${INK}" stroke-width="2"/>
      ${bush(-6, -4, 0.7)}${bush(7, -2, 0.55)}</g>`;
  }

  // The ground: iso platform + tile grid + hazard walkways + metal frame + greenery.
  function ground() {
    const tiles = [];
    for (let i = 1; i < 6; i++) {                       // tile seams parallel to both edges
      const t = i / 6;
      tiles.push(`<line x1="${500 + (972 - 500) * t}" y1="${28 + (230 - 28) * t}" x2="${28 + (500 - 28) * t}" y2="${230 + (432 - 230) * t}" class="seam"/>`);
      tiles.push(`<line x1="${500 - (500 - 28) * t}" y1="${28 + (230 - 28) * t}" x2="${500 + (972 - 500) * (1 - t)}" y2="${432 - (432 - 230) * t}" class="seam"/>`);
    }
    const walk = [[500, 60], [930, 230], [500, 400], [70, 230]].map(([x, y]) =>
      `<line x1="500" y1="230" x2="${x}" y2="${y}" class="walkway"/>`).join("");
    return `<svg class="iso-ground" viewBox="0 0 1000 460" preserveAspectRatio="none" aria-hidden="true">
      <path d="M500 40 L984 242 L500 444 L16 242 Z" fill="${INK}" opacity="0.16"/>
      <path d="M500 28 L972 230 L500 432 L28 230 Z" fill="#efe6cd" stroke="${INK}" stroke-width="4"/>
      <path d="M500 28 L972 230 L500 432 L28 230 Z" fill="none" stroke="#c9b98f" stroke-width="12" stroke-dasharray="1 26" opacity=".5"/>
      <g stroke="#d9cba4" stroke-width="1.6">${tiles.join("")}</g>
      <g stroke="#e9b400" stroke-width="9" opacity=".55" stroke-dasharray="14 9">${walk}</g>
      <path d="M436 202 L564 202 L596 230 L564 258 L436 258 L404 230 Z" fill="#e5d9b6" stroke="${INK}" stroke-width="2.5"/>
      ${bush(85, 215, 1.2)}${bush(120, 240, 0.8)}${bush(905, 250, 1.1)}${bush(875, 222, 0.7)}
      ${planter(310, 330)}${planter(690, 330)}${planter(310, 132)}${planter(690, 132)}
    </svg>`;
  }

  // One department building: iso box + accent roof + door + window + roof lamp.
  // seed varies the silhouette (chimney / vent / tank) so no two buildings are identical.
  function building(accent, status, seed) {
    const live = status === "live";
    const extra = [
      `<path d="M62 8 L74 8 L74 24 L62 30 Z" fill="#9a9182" stroke="${INK}" stroke-width="2.4"/>
       ${live ? '<circle class="puff" cx="68" cy="2" r="4"/><circle class="puff p2" cx="72" cy="-6" r="3"/>' : ""}`,
      `<path d="M24 16 L36 10 L36 26 L24 32 Z" fill="${accent}" stroke="${INK}" stroke-width="2.4"/>
       <path d="M26 14 L34 10" stroke="${INK}" stroke-width="2"/>`,
      `<ellipse cx="70" cy="16" rx="9" ry="5" fill="#c8bda2" stroke="${INK}" stroke-width="2.2"/>
       <path d="M61 16 L61 28 A9 5 0 0 0 79 28 L79 16" fill="#c8bda2" stroke="${INK}" stroke-width="2.2"/>`,
    ][seed % 3];
    return `<svg class="bldg" viewBox="0 0 100 92" aria-hidden="true">
      <path d="M54 22 L96 43 L54 64 L54 88 L14 68 L14 43 Z" transform="translate(4 5)" fill="${INK}" opacity=".22"/>
      <path d="M8 35 L50 56 L50 82 L8 61 Z" fill="#efe4c6" stroke="${INK}" stroke-width="2.6"/>
      <path d="M50 56 L92 35 L92 61 L50 82 Z" fill="#ddd0ac" stroke="${INK}" stroke-width="2.6"/>
      <path d="M50 14 L92 35 L50 56 L8 35 Z" fill="${accent}" stroke="${INK}" stroke-width="2.8"/>
      <path d="M50 20 L84 37 L50 54 L16 37 Z" fill="#fff" opacity=".14"/>
      ${extra}
      <path d="M28 50 L38 55 L38 70 L28 65 Z" fill="${live ? "#ffe9a3" : "#4a4132"}" stroke="${INK}" stroke-width="2.2"/>
      <path d="M60 56 L72 50 L72 60 L60 66 Z" fill="#bfe3ef" stroke="${INK}" stroke-width="2.2"/>
      <circle class="rooflamp ${live ? "live" : status === "slow" ? "slow" : "off"}" cx="50" cy="13" r="4.5" stroke="${INK}" stroke-width="2"/>
    </svg>`;
  }

  // The side-view CUTAWAY — shown when you enter a department: the building sliced
  // open, three real levels (lead office / agent floor / worker line), live numbers.
  function cutaway(o) {
    const monsters = (n, src, w) => {
      let out = "";
      for (let i = 0; i < Math.min(n, 5); i++) out += `<img src="${src}" style="width:${w}px" alt="">`;
      return out + (n > 5 ? `<b class="more">+${n - 5}</b>` : "");
    };
    const crates = (n) => {
      let out = "";
      for (let i = 0; i < Math.min(n, 6); i++)
        out += `<span class="crate" style="transform:rotate(${(i % 3 - 1) * 3}deg)"></span>`;
      return out + (n > 6 ? `<b class="more">+${n - 6}</b>` : "");
    };
    const lead = o.lead || {};
    return `<div class="cutaway" style="--acc:${o.accent}">
      <div class="cut-roof"><span>${_e(o.label)}</span><i class="cut-saw">side cutaway</i></div>
      <div class="cut-level">
        <span class="cut-tag">LEAD OFFICE</span>
        ${o.dept ? `<img src="assets/monsters/${o.dept}-lead.svg" style="width:44px" alt="">` : ""}
        <div class="cut-info"><b>${_e(lead.name || lead.id || "unstaffed")}</b>
          <span>${_e(lead.persona || "directs the department")}</span></div>
        <div class="cut-nums">${o.usage.handoffs || 0} hand-offs</div>
      </div>
      <div class="cut-level">
        <span class="cut-tag">AGENT FLOOR</span>
        ${o.dept ? monsters(o.staff, `assets/monsters/${o.dept}-agent.svg`, 34) : ""}
        <div class="cut-info"><b>${o.staff} agents</b><span>${_e(o.roles)}</span></div>
        <div class="cut-nums">${o.usage.done || 0} done · ${o.usage.fails || 0} fails</div>
      </div>
      <div class="cut-level ground">
        <span class="cut-tag">WORKER LINE</span>
        ${o.dept ? monsters(Math.max(o.counts.working || 0, 1), `assets/monsters/${o.dept}-worker.svg`, 26) : ""}
        <div class="cut-belt">${crates(o.counts.queued || 0)}</div>
        <div class="cut-nums">${o.counts.queued || 0} queued · ${o.counts.working || 0} working</div>
      </div>
    </div>`;
  }

  // ── M3.4 the ANIMATION CATALOG: 11 action props, each drawn from the real action ──
  // fix=weld · build=hammer · test=magnify · verify=stamp · deliver=party · research=dig ·
  // make-media=film · hand-off=carry · pitch=wave · idle=rest · open=pancake
  const PROPS = {
    weld: `<path d="M12 2 L14 9 L21 7 L15 13 L20 19 L12 15 L4 19 L9 13 L3 7 L10 9 Z" fill="#ffd23f" stroke="${INK}" stroke-width="1.6"/>`,
    hammer: `<g class="fx-swing"><rect x="10" y="8" width="3.4" height="14" rx="1.6" fill="#8a5a44" stroke="${INK}" stroke-width="1.4"/>
      <rect x="4" y="3" width="15" height="7" rx="2" fill="#9aa0a6" stroke="${INK}" stroke-width="1.6"/></g>`,
    magnify: `<g class="fx-scan"><circle cx="10" cy="10" r="6.5" fill="none" stroke="${INK}" stroke-width="2.6"/>
      <line x1="15" y1="15" x2="21" y2="21" stroke="${INK}" stroke-width="3" stroke-linecap="round"/></g>`,
    stamp: `<g class="fx-slam"><rect x="6" y="2" width="12" height="6" rx="2" fill="#c1121f" stroke="${INK}" stroke-width="1.6"/>
      <rect x="9" y="8" width="6" height="6" fill="#9aa0a6" stroke="${INK}" stroke-width="1.4"/></g>
      <path class="fx-ok" d="M7 20 l3 3 l7 -7" fill="none" stroke="#2d6a4f" stroke-width="3" stroke-linecap="round"/>`,
    party: `<rect class="fx-cf c1" x="4" y="14" width="4" height="4" fill="#ef476f"/>
      <rect class="fx-cf c2" x="11" y="16" width="4" height="4" fill="#ffd166"/>
      <rect class="fx-cf c3" x="18" y="15" width="4" height="4" fill="#118ab2"/>`,
    dig: `<g class="fx-rock"><rect x="11" y="2" width="3" height="13" rx="1.4" fill="#8a5a44" stroke="${INK}" stroke-width="1.3"/>
      <path d="M8 14 h9 l-1.5 8 h-6 Z" fill="#9aa0a6" stroke="${INK}" stroke-width="1.6"/></g>
      <circle class="fx-dirt d1" cx="4" cy="20" r="1.8" fill="#7f5539"/><circle class="fx-dirt d2" cx="20" cy="21" r="1.5" fill="#7f5539"/>`,
    film: `<rect x="3" y="10" width="18" height="11" rx="2" fill="${INK}"/>
      <rect class="fx-clap" x="3" y="4" width="18" height="6" rx="2" fill="${INK}"/>
      <path d="M5 5.5 l3 3 M10 5.5 l3 3 M15 5.5 l3 3" stroke="#fff" stroke-width="1.6"/>`,
    carry: `<g class="fx-bob"><rect x="5" y="7" width="14" height="12" rx="2" fill="#d8b56a" stroke="${INK}" stroke-width="2"/>
      <line x1="12" y1="7" x2="12" y2="19" stroke="${INK}" stroke-width="1.6"/></g>`,
    wave: `<g class="fx-flap"><rect x="6" y="3" width="2.6" height="19" rx="1.2" fill="${INK}"/>
      <path d="M9 4 q7 -2 12 1 l0 7 q-5 -3 -12 -1 Z" fill="#e9b400" stroke="${INK}" stroke-width="1.6"/></g>`,
    rest: `<text class="fx-z z1" x="3" y="20" font-size="9" font-weight="800" fill="${INK}">z</text>
      <text class="fx-z z2" x="10" y="14" font-size="11" font-weight="800" fill="${INK}">z</text>
      <text class="fx-z z3" x="17" y="8" font-size="13" font-weight="800" fill="${INK}">Z</text>`,
    pancake: `<ellipse class="fx-cake" cx="12" cy="8" rx="7" ry="3" fill="#e9b400" stroke="${INK}" stroke-width="1.6"/>
      <path d="M4 16 h16" stroke="${INK}" stroke-width="2.4"/><ellipse cx="12" cy="16" rx="8" ry="2.6" fill="#5c5145" stroke="${INK}" stroke-width="1.8"/>`,
  };
  const CATALOG = { fix: "weld", build: "hammer", test: "magnify", verify: "stamp", deliver: "party",
    research: "dig", "make-media": "film", "hand-off": "carry", pitch: "wave", idle: "rest", open: "pancake" };
  // each department's signature action when its lane runs
  const DEPT_ACT = { mining: "dig", news: "dig", watch: "film", visual: "film", analysis: "magnify",
    transcripts: "magnify", links: "magnify", memory: "carry", security: "stamp", improve: "weld", creators: "hammer" };
  // real bus/beat event -> which of the 11 plays (grounded, never decorative)
  function animForEvent(kind, dept) {
    return kind === "failed" ? "weld"
      : kind === "claimed" ? "hammer"
      : kind === "completed" ? "stamp"
      : kind === "handoff" || kind === "routed" ? "carry"
      : kind === "unroutable" ? "wave"
      : kind === "enqueued" ? "pancake"
      : kind === "lane_ran" ? (DEPT_ACT[dept] || "hammer")
      : "rest";
  }
  function prop(name, x, y, delay, title) {
    if (!PROPS[name]) return "";
    return `<div class="fx fx-${name}" style="left:${x}%;top:${y}%;animation-delay:${delay || 0}s" title="${_e(title || name)}">
      <svg viewBox="0 0 24 24">${PROPS[name]}</svg></div>`;
  }

  window.ExcavaFloor = { RING, ACCENT, CATALOG, ground, building, cutaway, prop, animForEvent };
})();
