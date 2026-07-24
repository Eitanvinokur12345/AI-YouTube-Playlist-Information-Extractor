// AI Skills Tracker dashboard — vanilla JS, no external libraries (works offline).
// Reads the committed JSON files from ../data (GitHub Pages must serve from repo root).
const DATA = "../data/";
const view = document.getElementById("view");
// Visible build stamp — bump with every sw.js shell version. If the badge matches the latest, you're
// on the newest bundle (ends the "did anything change?" doubt when a service worker serves a stale copy).
const APP_BUILD = "v125";
{ const _bb = document.getElementById("build-badge"); if (_bb) _bb.textContent = "build " + APP_BUILD; }
// One global clipboard handler for setup-recipe commands (any [data-copy] button copies its value).
document.addEventListener("click", (e) => {
  const b = e.target.closest && e.target.closest("[data-copy]"); if (!b) return;
  e.preventDefault();
  try { navigator.clipboard.writeText(b.dataset.copy || ""); } catch (_) {}
  const t = b.textContent; b.textContent = "✓ copied"; setTimeout(() => { b.textContent = t; }, 1200);
});
const meta = document.getElementById("meta");
const countersEl = document.getElementById("counters");

// ── PWA install prompt ───────────────────────────────────────────────────────
// Chrome/Edge desktop + Android Chrome fire beforeinstallprompt when the site
// qualifies as installable. Capture it; show the Install button; trigger on click.
// iOS Safari doesn't support this — we show a static "Add to Home Screen" hint instead.
let _installPrompt = null;
window.addEventListener("beforeinstallprompt", (e) => {
  e.preventDefault();
  _installPrompt = e;
  const wrap = document.getElementById("install-wrap");
  if (wrap) wrap.hidden = false;
});
window.addEventListener("appinstalled", () => {
  _installPrompt = null;
  const wrap = document.getElementById("install-wrap");
  if (wrap) wrap.hidden = true;
});
function triggerInstall() {
  if (_installPrompt) { _installPrompt.prompt(); _installPrompt = null; }
}
// iOS detection — show a static Add-to-Home-Screen hint
(function detectIOS() {
  const ios = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
  const standalone = window.navigator.standalone;   // true if already installed
  if (ios && !standalone) {
    const hint = document.getElementById("ios-hint");
    if (hint) hint.hidden = false;
  }
})();

const state = { status: null, config: null, selectedCategory: "all", newsWindow: "weekly",
  stars: new Set(), hideLowQuality: false, multiToolOnly: false, dynamicTabs: [],
  query: "", activeTab: "excava" };

// True if a skill/connector slug is starred (frozen, best-in-class — never auto-changed).
const isStarred = (s) =>
  (s && (s.starred === true || s.locked === true)) ||
  (s && s.slug && state.stars.has(String(s.slug).toLowerCase()));

// Cross-tool: the skill/technique works with 2+ AI tools (e.g. Claude, ChatGPT, Gemini).
const isMultiTool = (s) =>
  !!s && (s.multi_tool === true || ((s.compatibility || []).length > 1));
// "Claude ≤ Sonnet 4.6" — a tool plus the highest version it's known to work with.
const compatLabel = (c) => {
  const v = c && c.up_to_version;
  return esc(c && c.tool || "?") + (v && v !== "any" && v !== "latest" ? " &le; " + esc(v) : "");
};

// ── data loader with in-memory cache ─────────────────────────────────────────
// Caches each JSON file in memory for the session so switching tabs is instant.
// The service worker independently handles network-first + offline persistence.
const _cache = {};
async function load(file) {
  if (_cache[file] !== undefined) return _cache[file];
  try {
    const r = await fetch(DATA + file, { cache: "no-store" });
    if (!r.ok) { _cache[file] = null; return null; }
    _cache[file] = await r.json();
    return _cache[file];
  } catch { _cache[file] = null; return null; }
}
// Invalidate a specific file's cache (e.g. after an approve action)
function invalidate(file) { delete _cache[file]; }
// ── P1 LIVE REFRESH (owner: 'the project updates only when I open it — it must work online') ──
// Every 60s: poll ONE small status file; if the cloud beat produced a new stamp, drop the cache,
// re-render the ACTIVE tab, and pulse the live dot. Never refreshes while a modal is open (no
// yanking the owner mid-decision) or while the tab is hidden (no wasted requests).
let _liveStamp = null;
async function _livePoll(force) {
  if (!force && document.hidden) return "hidden";
  const m1 = document.getElementById("ex-modal"), m2 = document.getElementById("pitch-modal");
  if ((m1 && m1.style.display === "flex") || (m2 && !m2.hidden)) return "modal-open";
  let stamp;
  try {
    const r = await fetch(DATA + "excava_status.json", { cache: "no-store" });
    const s = await r.json();
    stamp = s.generated_at || s.updated_at || JSON.stringify(s).slice(0, 80);
  } catch (_) { return "offline"; }
  if (_liveStamp === null) { _liveStamp = stamp; _liveDot("live"); return "first"; }
  if (stamp === _liveStamp) { _liveDot("live"); return "unchanged"; }
  _liveStamp = stamp;
  for (const k in _cache) delete _cache[k];       // fresh data for every tab
  await show(state.activeTab);                    // re-render what the owner is looking at
  _liveDot("updated");
  return "refreshed";
}
function _liveDot(kind) {
  let d = document.getElementById("live-dot");
  if (!d) {
    const bb = document.getElementById("build-badge");
    if (!bb) return;
    d = document.createElement("span"); d.id = "live-dot"; d.className = "build-badge";
    bb.after(d);
  }
  const t = new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
  d.textContent = kind === "updated" ? `🟢 live · new data ${t}` : `🟢 live · checked ${t}`;
  d.style.color = "oklch(0.55 0.15 150)";
}
setInterval(_livePoll, 60000);
// P2 (owner): EXCAVA's own creations ROUTE to their tabs — a created prompt shows in Prompts,
// a created tool in Tools, a created design in Designs (packages already merge into Packages).
// Each carries the 'Created by EXCAVA' label so provenance stays visible.
async function _plusCreations(data, kind, listKey) {
  const made = await load("created_by_excava.json");
  const mine = ((made && made.creations) || []).filter(c => c.type === kind && c.status !== "failed-test");
  if (!mine.length) return data;
  const mapped = mine.map(c => ({
    title: "🦾 " + c.name, name: "🦾 " + c.name,                       // both key styles used by tabs
    purpose: c.what || "", description: c.what || "",
    prompt_text: c.body || c.how_to_use || "", category: "creation",
    created_by: "EXCAVA", label: c.label || "Created by EXCAVA",
    quality_score: (c.self_test && c.self_test.ok) ? 7 : 5,
    url: "", at: c.created_at || "",
  }));
  const out = Object.assign({}, data || {});
  out[listKey] = mapped.concat((data && data[listKey]) || []);
  return out;
}
// Raw-text loader (JSONL traces etc.) — no cache, "" on miss. Phase 5 trace viewer uses it.
async function loadText(file) {
  try {
    const r = await fetch(DATA + file, { cache: "no-store" });
    return r.ok ? await r.text() : "";
  } catch { return ""; }
}

// ── M1: the ELEMENT layer — unified index, badges, action row, detail view ──
let _eidx = null, _ewarm = null;
async function eidx() {
  if (_eidx) return _eidx;
  const [idx, pw] = await Promise.all([load("elements_index.json"), load("prewarm.json")]);
  _eidx = { byId: {}, byKey: {}, meta: idx || {} };
  _ewarm = {};
  ((pw && pw.warm) || []).forEach(w => { _ewarm[w.id] = w; });
  ((idx && idx.elements) || []).forEach(e => {
    _eidx.byId[e.id] = e;
    _eidx.byKey[e.type + "|" + e.name.toLowerCase().trim()] = e;
  });
  return _eidx;
}
function elBadge(e) {
  const s = (e.verified || {}).status || "unverified";
  const map = { verified: ["v", "✓ verified"], niche: ["n", "◆ niche-verified"],
    unverified: ["u", "unverified"], dead: ["d", "✗ dead"] };
  const [cls, label] = map[s] || map.unverified;
  const src = (e.verified || {}).sources || 0;
  return `<span class="el-badge ${cls}" title="${esc((e.verified || {}).method || "")}${src ? " · " + src + " sources" : ""}${e.trust ? " · trust " + e.trust : ""}">${label}</span>`;
}
// M1.4 — the per-card ACTION ROW: Activate / Open(<10s) / Use / Video / Bundle / Source
function elementActions(e, always) {
  const links = e.links || {};
  const warm = _ewarm && _ewarm[e.id];
  const vid = (e.source_videos || [])[0];
  const acts = [];
  acts.push(`<button class="primary" data-el-activate="${esc(e.id)}" title="Copy the ready-to-use payload for this element — the prompt text, a paste-ready MCP config, or the setup + repo">⚡ Activate</button>`);
  acts.push(`<button data-el-open="${esc(e.id)}" title="${warm ? "Pre-warmed — opens instantly" : "Derives a runnable target (<10s)"}">${warm ? "🟢" : "🥞"} Open</button>`);
  acts.push(`<a target="_blank" href="${_exIssue("EXCAVA: use " + e.name + " for a task", "Element: " + e.id)}" title="Send to the EXCAVA console as a task">🦾 Use for a task</a>`);
  if (vid) acts.push(`<a target="_blank" href="${yt(vid)}">▶ Video</a>`);
  if ((e.source_videos || []).length > 1)
    acts.push(`<a href="#element/${encodeURIComponent(e.id)}" title="${e.source_videos.length} source videos">🎬 Bundle (${e.source_videos.length})</a>`);
  const src = links.source_url || links.website || links.github;
  if (src) acts.push(`<a target="_blank" href="${esc(src)}">↗ Source</a>`);
  acts.push(`<a href="#element/${encodeURIComponent(e.id)}">🔍 Detail</a>`);
  return `<div class="el-actions${always ? " always" : ""}" data-elid="${esc(e.id)}">${acts.join("")}</div>`;
}
// M1.5 — Open: warm = instant; cold = derive under the pancake (<10s)
async function elOpen(id, btn) {
  await eidx();
  const w = _ewarm[id];
  if (w && w.open_url) { window.open(w.open_url, "_blank"); return; }
  const e = _eidx.byId[id];
  if (!e) return;
  const old = btn.innerHTML;
  btn.innerHTML = `<span class="el-warm"><span class="pan">🥞</span> warming…</span>`;
  const links = e.links || {};
  const gh = (links.github || (String(links.website || "").includes("github.com") ? links.website : ""));
  const m = String(gh).match(/github\.com\/([\w.\-]+)\/([\w.\-]+)/);
  const target = m ? `https://github.dev/${m[1]}/${m[2].replace(/\.git$/, "")}`
    : (links.website || links.source_url || "");
  setTimeout(() => { btn.innerHTML = old; if (target) window.open(target, "_blank"); }, 600);
}
/*<<ACTIVATION>>*/
// Type-aware ACTIVATION payload (M1.4 · items 14/16 "6 element types USABLE, not links"):
// hand back the ONE thing you actually need for THIS element type, paste-ready —
//   prompt/command → the raw text you paste into your AI
//   connector      → a paste-ready MCP-server config skeleton + the repo holding the exact command
//   skill/tool/…   → a clean setup card (what it is · install · real repo/site links)
// Pure (no DOM / no globals) so it is unit-tested headless in scratchpad/test_activation.mjs.
function _slug(s) { return String(s || "server").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 40) || "server"; }
function _cleanLine(s) {
  return String(s || "").replace(/!\[[^\]]*\]\([^)]*\)/g, "").replace(/\[([^\]]*)\]\([^)]*\)/g, "$1")
    .replace(/[#>*`|]+/g, " ").replace(/\s+/g, " ").trim().slice(0, 200);
}
// Best-effort MCP launch command from a REAL install string; null when we can't know it honestly
// (→ the config gets a clearly-labelled placeholder instead of a fabricated command).
function _mcpCmd(inst) {
  const m = String(inst || "").trim().match(/\b(npx|uvx|uv|pnpm|bunx|docker|python|node)\b[^\n]*/i);
  if (!m) return null;
  // Strip trailing prose annotations so they don't become fake args:
  //   "npx @playwright/mcp (open-source)" · "uvx foo — needs a key" · "npx bar, then configure"
  const line = m[0].split(/\s+[—–-]\s+/)[0].split(/[,;]/)[0].replace(/\s*\([^)]*\)\s*/g, " ").trim();
  const p = line.split(/\s+/).filter(Boolean);
  return p.length ? { command: p[0], args: p.slice(1) } : null;
}
function activationRecipe(e) {
  const L = (e && e.links) || {}, t = (e && e.type) || "";
  const gh = L.github || (/github\.com/.test(L.website || "") ? L.website : "") || (/github\.com/.test(L.source_url || "") ? L.source_url : "");
  const site = (L.website && !/github\.com/.test(L.website)) ? L.website : "";
  const src = L.source_url || "";
  const inst = (e && (e.install || e.install_or_source)) || "";
  // PROMPT / COMMAND — the payload IS the text you paste (commands store the text in `name`).
  if (t === "prompt" || t === "command") {
    const text = ((e.body || "").trim()) || (t === "command" ? (e.name || "").trim() : "") || (e.what || "").trim() || (e.name || "");
    return { label: t, kind: "paste", text, note: "Paste this straight into your AI." };
  }
  // CONNECTOR (MCP server) — paste-ready config skeleton + the repo that holds the exact command.
  if (t === "connector") {
    const cmd = _mcpCmd(inst);
    const cfg = { mcpServers: { [_slug(e.name)]: cmd ? { command: cmd.command, args: cmd.args } : { command: "npx", args: ["-y", "<package — see the repo README>"] } } };
    const text = [`// MCP server: ${e.name}`,
      gh ? `// Repo (the exact run command is in its README): ${gh}` : "",
      inst ? `// Install: ${inst}` : "",
      cmd ? "" : "// NOTE: fill command/args from the repo before saving this.",
      JSON.stringify(cfg, null, 2)].filter(Boolean).join("\n");
    return { label: "MCP config", kind: "mcp", text, note: "Add to your MCP client config; confirm the command from the repo." };
  }
  // SKILL / TOOL / MODEL / DESIGN / FORMAT — a clean setup card.
  const lines = [`# ${e.name} — ${t}`];
  const w = _cleanLine(e.what); if (w) lines.push(`# ${w}`);
  if (inst) lines.push(inst);
  if (gh) lines.push(`# Repo: ${gh}`);
  if (site) lines.push(`# Site: ${site}`);
  if (!inst && !gh && !site && src) lines.push(`# Source: ${src}`);
  return { label: "setup", kind: "setup", text: lines.filter(Boolean).join("\n"), note: gh ? "Open the repo, then run the install." : "" };
}
/*<</ACTIVATION>>*/
function elActivate(id, btn) {
  const e = _eidx && _eidx.byId[id];
  if (!e) return;
  const r = activationRecipe(e);
  try { navigator.clipboard.writeText(r.text); } catch (_) {}
  const t = btn.textContent, ot = btn.title;
  btn.textContent = "✓ " + r.label + " copied"; if (r.note) btn.title = r.note;
  setTimeout(() => { btn.textContent = t; btn.title = ot; }, 1600);
}
// One delegated handler for every action row on any tab
document.addEventListener("click", (ev) => {
  const o = ev.target.closest && ev.target.closest("[data-el-open]");
  if (o) { ev.preventDefault(); elOpen(o.dataset.elOpen, o); return; }
  const a = ev.target.closest && ev.target.closest("[data-el-activate]");
  if (a) { ev.preventDefault(); elActivate(a.dataset.elActivate, a); }
});
// M1.8 — decorate every list tab's cards with badges + the action row (post-render pass)
const TAB_ELTYPE = { skills: "skill", tools: "tool", models: "model", prompts: "prompt",
  connectors: "connector", designs: "design", comingsoon: "tool" };
async function decorateCards(tab) {
  const etype = TAB_ELTYPE[tab];
  if (!etype) return;
  const ix = await eidx();
  view.querySelectorAll(".card h3").forEach(h3 => {
    if (h3.querySelector(".el-badge")) return;
    const card = h3.closest(".card");
    if (!card || card.querySelector(".el-actions")) return;
    const name = (h3.cloneNode(true).childNodes[0] && h3.textContent || "")
      .replace(/^[★\s]*\d+(\.\d+)?\/10\s*/, "").split("\n")[0]
      .replace(/(frozen|official|✓.*|✗.*)$/g, "").trim().toLowerCase();
    let e = ix.byKey[etype + "|" + name];
    if (!e) {  // fuzzy: longest index name contained in the heading
      const cands = Object.keys(ix.byKey).filter(k => k.startsWith(etype + "|"))
        .filter(k => name.includes(k.split("|")[1])).sort((a, b) => b.length - a.length);
      e = cands.length ? ix.byKey[cands[0]] : null;
    }
    if (!e) return;
    h3.insertAdjacentHTML("beforeend", " " + elBadge(e));
    card.insertAdjacentHTML("beforeend", elementActions(e));
  });
}
// M1.6 — the ELEMENT DETAIL view at #element/<id>
async function renderElement(id) {
  const ix = await eidx();
  const e = ix.byId[id];
  if (!e) { view.innerHTML = empty(`No element "${esc(id)}" in the index.`); return; }
  const links = e.links || {};
  const vids = (e.source_videos || []).slice(0, 4);
  const rel = (e.related || []).map(rid => ix.byId[rid]).filter(Boolean);
  const enr = e.enrichment || {};
  view.innerHTML = `
    <div class="card" style="border-top:3px solid var(--gold)">
      <p class="sub"><a href="#" onclick="history.back();return false">← back</a></p>
      <div class="el-detail-hero"><h3 style="font-size:22px">${esc(e.name)}</h3>
        <span class="pill">${esc(e.type)}</span> ${elBadge(e)}
        ${e.created_by === "EXCAVA" ? '<span class="pill" style="background:var(--gold-soft)">🦾 Created by EXCAVA</span>' : ""}</div>
      <p>${esc(e.what || "(deep-retrieve will enrich this element on its next pass)")}</p>
      ${e.body ? `<pre style="white-space:pre-wrap;font-size:12.5px;background:var(--panel2);border:1.5px solid var(--line);border-radius:9px;padding:10px">${esc(e.body)}</pre>` : ""}
      ${elementActions(e, true)}
      <p class="sub" style="margin-top:10px">
        ${e.category ? `category: <b>${esc(e.category)}</b> · ` : ""}trust ${e.trust || "?"} ·
        verified: <b>${esc((e.verified || {}).status)}</b>${(e.verified || {}).method ? ` (${esc(e.verified.method)}, ${((e.verified || {}).sources || 0)} sources)` : ""}
        ${enr.method ? ` · enriched via ${esc(enr.method)} [${(enr.sources || []).map(esc).join(", ")}]` : ""}</p>
      ${e.install ? `<p class="sub"><b>Install / source:</b> <code>${esc(e.install)}</code></p>` : ""}
    </div>
    ${vids.length ? `<div class="card"><h3>🎬 Source video${vids.length > 1 ? " bundle" : ""} <span class="sub">— where it was really shown</span></h3>
      <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:10px">
      ${vids.map(v => `<iframe width="100%" height="180" src="https://www.youtube.com/embed/${encodeURIComponent(v)}" frameborder="0" allowfullscreen loading="lazy" style="border-radius:10px;border:1.5px solid var(--line)"></iframe>`).join("")}</div></div>` : ""}
    ${rel.length ? `<div class="card"><h3>🧠 Related <span class="sub">— shown together / same topic (M1.7)</span></h3>
      <div class="el-rel">${rel.map(r => `<a href="#element/${encodeURIComponent(r.id)}">${_exIcon(r.type)} ${esc(r.name)} ${elBadge(r)}</a>`).join("")}</div></div>` : ""}`;
}
// ── M1.C13/21: THE HUB — one browsable, searchable library across ALL element types ──
// Every per-type tab shows one slice; this is the whole 9,500-element hub in one place,
// filterable by type + verification, searchable by the global box. Reuses eidx / elBadge /
// elementActions (Ponytail — no new data, no new action code).
async function renderHub() {
  const ix = await eidx();
  const all = Object.values(ix.byId);
  const typeF = state.hubType || "all", statusF = state.hubStatus || "all", query = q();
  const tCounts = {};
  all.forEach(e => { tCounts[e.type] = (tCounts[e.type] || 0) + 1; });
  const types = Object.keys(tCounts).sort((a, b) => tCounts[b] - tCounts[a]);
  let list = all;
  if (typeF !== "all") list = list.filter(e => e.type === typeF);
  if (statusF !== "all") list = list.filter(e => ((e.verified || {}).status || "unverified") === statusF);
  if (query) list = list.filter(e =>
    (e.name + " " + (e.what || "") + " " + (e.category || "") + " " + e.type).toLowerCase().includes(query));
  const rank = { verified: 0, niche: 1, unverified: 2, dead: 3 };
  list.sort((a, b) => (rank[(a.verified || {}).status] ?? 2) - (rank[(b.verified || {}).status] ?? 2)
    || String(a.name).localeCompare(String(b.name)));
  const CAP = 120, shown = list.slice(0, CAP);
  const chip = (attr, val, label, on) =>
    `<button class="qr-btn${on ? " on" : ""}" ${attr}="${val}" style="${on ? "background:var(--gold);border-color:var(--gold-line);color:#1a1205" : ""}">${label}</button>`;
  const nVer = all.filter(e => (e.verified || {}).status === "verified").length;
  const nNiche = all.filter(e => (e.verified || {}).status === "niche").length;
  view.innerHTML = `
    <div class="card" style="border-top:3px solid var(--gold)">
      <h3>🛢 The Hub <span class="sub">— the whole library, one place · <b>${all.length.toLocaleString()}</b> elements · ${nVer.toLocaleString()} verified · ${nNiche.toLocaleString()} niche · type the search box above to filter</span></h3>
      <div style="display:flex;flex-wrap:wrap;gap:6px;margin:8px 0 4px">
        ${chip("data-hubtype", "all", `All types (${all.length.toLocaleString()})`, typeF === "all")}
        ${types.map(t => chip("data-hubtype", t, `${_exIcon(t)} ${t} (${tCounts[t]})`, typeF === t)).join("")}
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:6px">
        ${chip("data-hubstatus", "all", "any status", statusF === "all")}
        ${chip("data-hubstatus", "verified", "✓ verified", statusF === "verified")}
        ${chip("data-hubstatus", "niche", "◆ niche", statusF === "niche")}
        ${chip("data-hubstatus", "unverified", "unverified", statusF === "unverified")}
      </div>
      <p class="sub" style="margin-top:8px">${list.length.toLocaleString()} match${list.length === 1 ? "" : "es"}${list.length > CAP ? ` · showing the first ${CAP} (narrow with the search box or a type)` : ""}</p>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px">
      ${shown.map(e => `
        <div class="card" style="margin:0">
          <h3 style="font-size:15px"><a href="#element/${encodeURIComponent(e.id)}" style="color:inherit;text-decoration:none">${_exIcon(e.type)} ${esc(e.name)}</a> ${elBadge(e)}</h3>
          <p class="sub" style="min-height:32px">${esc((e.what || "(deep-retrieve will enrich this)").slice(0, 140))}</p>
          ${elementActions(e, true)}
        </div>`).join("") || empty(query ? `No elements match "${esc(state.query)}".` : "No elements.")}
    </div>`;
  view.querySelectorAll("[data-hubtype]").forEach(b =>
    b.onclick = () => { state.hubType = b.dataset.hubtype; show("hub"); });
  view.querySelectorAll("[data-hubstatus]").forEach(b =>
    b.onclick = () => { state.hubStatus = b.dataset.hubstatus; show("hub"); });
}

const esc = (s) => String(s ?? "").replace(/[&<>"]/g, c =>
  ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
// Turn EXCAVA's machine-y status strings into plain, readable sentences (owner: 'numbers that look
// like code, not sentences'). Rewrites the common code-like fragments; safe on normal prose too.
function humanize(text) {
  if (!text) return "";
  let s = String(text);
  s = s.replace(/RAN\s+src\.[a-z0-9_.]+\s*\(real work\):\s*/gi, "");     // legacy prefix -> drop
  s = s.replace(/\bRan the ([a-z0-9 ]+)\.\s*/gi, (_, m) => "Ran the " + m.trim() + ": ");
  s = s.replace(/failing\s+Qs?:\s*\[([^\]]*)\]/gi, (_, list) => {        // number arrays -> a count
    const n = list.split(",").map(x => x.trim()).filter(Boolean).length;
    return n + (n === 1 ? " check still needs work" : " checks still need work");
  });
  s = s.replace(/\[dispatched\s+(\d+)\s+workers?:[^\]]*\]/gi,            // worker-id artifact -> note
    (_, n) => "(handed off to " + n + (+n === 1 ? " worker)" : " workers)"));
  s = s.replace(/\b(\d{1,4})\/(\d{1,4})\b/g, "$1 of $2");               // 40/50 -> 40 of 50
  s = s.replace(/\s*\(mechanical\)/gi, "");                             // drop noise tag
  s = s.replace(/\s*\|\s*/g, ". ");                                     // pipes -> sentence breaks
  s = s.replace(/\.\s*\.\s*/g, ". ").replace(/\s{2,}/g, " ").trim();
  return s;
}
// Humanize + escape, and mark any remaining inline `code`/commands so they read as clearly-labelled
// code rather than sentences pretending to be prose.
function humanizeHTML(text) {
  return esc(humanize(text))
    .replace(/`([^`]+)`/g, '<code class="inl">$1</code>')   // inline code / commands
    .replace(/\*\*([^*]+)\*\*/g, "<b>$1</b>");              // agents' markdown bold -> real bold
}
// A readable model name for the byline: 'mistral/mistral-small-latest' -> 'Mistral'.
function _engFriendly(eng) {
  if (!eng) return "";
  const prov = String(eng).split("/")[0].split("-")[0];
  if (/^[a-z]/.test(prov) && prov.length > 2) return prov.charAt(0).toUpperCase() + prov.slice(1);
  return eng;
}
const empty = (msg) => `<p class="empty">${esc(msg)}</p>`;
const yt = (id) => `https://www.youtube.com/watch?v=${encodeURIComponent(id || "")}`;
const _ytid = (u) => { const m = String(u || "").match(/[?&]v=([\w-]+)/); return m ? m[1] : ""; };
// Real, usable links for any item: Website / GitHub / Open-in-Codespaces (already-runnable) / Source
// videos. The "Source" is the bundle of videos it came from — separate from the tool's own links.
function linksRow(it) {
  const out = [];
  const cand = it.homepage || it.source_url || it.url || "";
  const home = (cand && !/youtube\.com|youtu\.be/.test(cand)) ? cand : "";
  if (home) out.push(`<a class="lnk lnk-web" href="${esc(home)}" target="_blank" rel="noopener" title="Open the live site/app">Website ↗</a>`);
  if (it.github) out.push(`<a class="lnk lnk-gh" href="${esc(it.github)}" target="_blank" rel="noopener">GitHub ↗</a>`);
  // "Run it" = open it actually RUNNING. A repo boots live in-browser (StackBlitz, no signup) instead
  // of a deploy signup-wall; we only fall back to a deploy page when there's no live site at all.
  // "Use it now" = the live Website above. For source repos, open the code in github.dev — GitHub's
  // INSTANT in-browser editor (no clone, no build wait; the repo is just there). This replaced the
  // StackBlitz boot, which cloned on click and was slow/flaky ("the activation process is not working").
  const g = String(it.github || "").match(/github\.com\/([\w.-]+)\/([\w.-]+)/);
  if (g) out.push(`<a class="lnk lnk-run" href="https://github.dev/${g[1]}/${g[2].replace(/\.git$/, "")}" target="_blank" rel="noopener" title="Opens the repo instantly in github.dev (in-browser VS Code) — nothing to clone, nothing builds on click">⌨ Open code ↗</a>`);
  else if (!home && it.deploy_url) out.push(`<a class="lnk lnk-run" href="${esc(it.deploy_url)}" target="_blank" rel="noopener" title="Opens a one-click deploy page (may ask you to sign in)">⬆ Deploy your own ↗</a>`);
  if (it.install_or_source && !it.github) out.push(`<span class="lnk lnk-mcp">install: <code>${esc(String(it.install_or_source).slice(0,60))}</code></span>`);
  // Source bundle, earliest-first: first link = the video that first revealed it.
  const sv = (it.source_videos || []);
  if (sv.length) {
    out.push(`<a class="lnk lnk-src" href="${esc(sv[0].url)}" target="_blank" rel="noopener" title="First revealed here${sv[0].title ? ": " + esc(sv[0].title) : ""}">Source${sv.length > 1 ? ` (${sv.length} videos)` : " video"} ↗</a>`);
  } else {
    const vids = ((it.endorsement_video_ids || []).length ? it.endorsement_video_ids
      : [it.source_video_id || _ytid(it.source_url)]).filter(Boolean);
    if (vids.length) out.push(`<a class="lnk lnk-src" href="${yt(vids[0])}" target="_blank" rel="noopener">Source${vids.length > 1 ? ` (${vids.length} videos)` : " video"} ↗</a>`);
  }
  const noReal = !home && !it.github && !it.install_or_source;
  // ⚙ In-project SETUP recipe — what to actually run so it's set up WITHIN your tools (the future
  // activator/EXCAVA executes this; no link-out). Only shows when the item has a real recipe.
  const su = it.setup, cmd = su && (su.command || (su.steps || []).join(" && "));
  const setupBlock = cmd ? `<div class="setup"><span class="setup-k">⚙ ${esc(su.kind || "setup")}</span>
    <code class="setup-cmd">${esc(cmd)}</code>
    <button class="copy-btn" data-copy="${esc(cmd)}" title="Copy this setup command">copy</button>
    ${su.needs_key ? '<span class="setup-key" title="Needs an API key / sign-in for the external service">needs key</span>' : ""}</div>` : "";
  return `<div class="links">${out.join("")}${noReal ? '<span class="lnk-pending" title="No verified link yet — the links protocol resolves these each cycle">link pending</span>' : ""}</div>${setupBlock}`;
}

// ── Per-tab "how long until this updates" line (one bullet, lists every update type) ──
// Derived from the real workflow crons so it's accurate; shown at the top of each tab.
const TAB_CADENCE = {
  skills:     "new items within ~3h of a recovered transcript (free analysis lane, every 3h) · deep re-curation weekly (Sat night, Israel)",
  tools:      "new items within ~3h (free analysis lane, every 3h) · ranking &amp; de-duplication re-curated weekly (Sat night)",
  models:     "new items within ~3h (free analysis lane, every 3h) · re-ranked weekly (Sat night)",
  comingsoon: "refreshes with the Tool Rating tab — within ~3h of a new transcript",
  prompts:    "new prompts within ~3h (free analysis lane, every 3h)",
  tips:       "new tips &amp; commands within ~3h (free analysis lane, every 3h)",
  connectors: "new connectors within ~3h (free analysis lane, every 3h)",
  news:       "web AI news every 6h · daily / weekly / monthly digests roll up on their own cycle",
  sources:    "new channel suggestions daily (06:00 UTC) · tool discovery Sun/Tue/Thu",
  improvement:"weekly deep pass (Sat 20:00 UTC) · safe auto-fixes applied on the next run",
  selfimprove:"self-check + 3-agent review weekly (Sat night) · scores &amp; findings refresh then",
  effectiveness:"recomputed every analysis cycle (~3h) · the self-improvement system targets the weakest lanes weekly",
  devbuild:   "regenerated on each weekly deep pass (Sat night) and on code changes",
};
function cadenceLine(tab) {
  const txt = tab && !tab.startsWith("dyn:") && TAB_CADENCE[tab];
  return txt ? `<div class="cadence-line" title="How often this tab's data updates">&#8226; <b>Updates:</b> ${txt}</div>` : "";
}

// ── Quick-read: real content PROCESSING, not just tighter line-spacing ──
// Extractive summary: score each sentence by how much of the text's signal it carries (term
// frequency, stopwords removed, length-normalised) and surface the MOST informative one — which is
// often buried mid-paragraph, not the first. Then bold the single most salient term so the eye
// lands on the topic instantly. This processes the content for the reader instead of truncating.
const QR_STOP = new Set(("the a an and or but for with you your this that these those is are be to of in "
  + "on it its as at by from can will would could using use used make makes more most very our we they "
  + "their them then than so if not no yes new also just like into out over all any each which what how "
  + "when who why was were has have had do does done about across via per up down off").split(" "));
function _qrFreq(t) {
  const f = Object.create(null);
  (t.toLowerCase().match(/[a-z0-9][a-z0-9\-]{2,}/g) || []).forEach(w => {
    if (!QR_STOP.has(w)) f[w] = (f[w] || 0) + 1;
  });
  return f;
}
function summarizeText(t) {
  t = (t || "").trim().replace(/\s+/g, " ");
  if (!t) return t;
  const sents = t.match(/[^.!?]+[.!?]?/g) || [t];
  if (sents.length === 1 && t.split(" ").length <= 26) return t;
  const f = _qrFreq(t);
  let best = sents[0], bestScore = -1;
  for (const s of sents) {
    const words = (s.toLowerCase().match(/[a-z0-9][a-z0-9\-]{2,}/g) || []).filter(w => !QR_STOP.has(w));
    if (words.length < 2) continue;
    const score = words.reduce((a, w) => a + (f[w] || 0), 0) / Math.sqrt(words.length); // signal density
    if (score > bestScore) { bestScore = score; best = s; }
  }
  let s = best.trim();
  const w = s.split(" ");
  if (w.length > 28) s = w.slice(0, 28).join(" ") + "…";
  // bold the most salient term so the topic pops
  const top = Object.keys(f).sort((a, b) => f[b] - f[a])[0];
  return { text: s, top };
}
// In quick-read: replace each card's description with its extracted essence AND hide the secondary
// lines (extra paragraphs, sub-labels) so the card collapses to title + one scannable point.
function quickreadSummarize(on) {
  view.querySelectorAll(".card").forEach(card => {
    const ps = [...card.querySelectorAll(":scope > p")].filter(p => !p.querySelector("b, span, a, code"));
    const first = ps[0];
    if (on) {
      if (first) {
        if (first.dataset.qrFull === undefined) first.dataset.qrFull = first.textContent;
        const r = summarizeText(first.dataset.qrFull);
        const out = typeof r === "string" ? { text: r, top: "" } : r;
        if (out.text) {
          const safe = out.text.replace(/[&<>]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]));
          first.innerHTML = out.top
            ? safe.replace(new RegExp(`\\b(${out.top})\\b`, "i"), "<b>$1</b>") : safe;
        }
      }
      ps.slice(1).forEach(p => { p.dataset.qrHidden = "1"; p.style.display = "none"; });
    } else {
      if (first && first.dataset.qrFull !== undefined) {
        first.textContent = first.dataset.qrFull; delete first.dataset.qrFull;
      }
      card.querySelectorAll('[data-qr-hidden="1"]').forEach(p => { p.style.display = ""; delete p.dataset.qrHidden; });
    }
  });
}
// Human-readable date: "Jun 3, 2026, 2:30 PM" or "?" if unparseable.
const fmtDate = (s) => {
  if (!s || s === "?") return s || "?";
  try {
    const d = new Date(s);
    if (isNaN(d)) return String(s);
    return d.toLocaleString(undefined, { month:"short", day:"numeric", year:"numeric",
                                         hour:"numeric", minute:"2-digit" });
  } catch { return String(s); }
};

// ── "How do I actually USE this in my tool?" — make the catalogue ACTIONABLE ──────────
// The project catalogues skills as SKILL.md, but to use one you must get it INTO the tool's
// session. This generates a tool-specific deploy instruction + a ready-to-paste block so the
// skill works "as if uploaded to the environment" — paste it and the tool follows it.
function deployHowto(tool) {
  const t = (tool || "").toLowerCase();
  if (t.includes("claude"))
    return `Claude: save the SKILL.md to your skills folder — <code>~/.claude/skills/&lt;slug&gt;/SKILL.md</code> (Claude Code) or upload it under Settings → Capabilities → Skills on claude.ai. Claude auto-loads it when relevant. Or paste the block below into a Project's custom instructions.`;
  if (t.includes("chatgpt") || t.includes("openai") || t.includes("gpt"))
    return `ChatGPT: create a Custom GPT (or open a Project) and paste the block below as its instructions — or paste it as your first message in a normal chat.`;
  if (t.includes("cursor") || t.includes("windsurf"))
    return `Cursor / Windsurf: add the block below to your project rules (<code>.cursor/rules</code> or <code>.windsurfrules</code>) — or paste it into the chat.`;
  if (t.includes("gemini"))
    return `Gemini: create a Gem with the block below as its instructions, or paste it into the chat.`;
  if (t.includes("copilot"))
    return `GitHub Copilot: add the block below to <code>.github/copilot-instructions.md</code>, or paste it into Copilot Chat.`;
  return `Paste the block below into the tool's system prompt (or your first message). That loads the skill into the session — as if it were installed in the environment.`;
}
function skillPrompt(s) {
  const lines = [`# ${s.skill_name || s.slug}`, "", (s.description || "").trim()];
  if (s.use_case) lines.push("", `When to use: ${String(s.use_case).trim()}`);
  if (s.output) lines.push("", `What it produces: ${String(s.output).trim()}`);
  const tips = [].concat(s.tips || [], s.general_tips || []).filter(Boolean);
  if (tips.length) { lines.push("", "Tips:"); tips.slice(0, 6).forEach(t => lines.push(`- ${t}`)); }
  if ((s.compatibility || []).length)
    lines.push("", "Works with: " + s.compatibility.map(c => (c.tool || "") +
      (c.up_to_version && c.up_to_version !== "any" ? ` (${c.up_to_version})` : "")).join(", "));
  if ((s.slash_commands || []).length) lines.push("", "Commands: " + s.slash_commands.join(" "));
  if (s.source_url) lines.push("", `Source: ${s.source_url}`);
  return lines.join("\n");
}
function useBox(s) {
  return `<details class="usebox"><summary>⌁ Use this skill</summary>
    <p class="howto">${deployHowto(s.target_tool)}</p>
    <div class="copyrow"><button class="copybtn" type="button">Copy ready-to-paste block</button>
      ${s.slug ? `<a class="mdlink" href="../skills/${esc(s.slug)}/SKILL.md" title="The full SKILL.md package">SKILL.md ↗</a>` : ""}</div>
    <pre class="useprompt">${esc(skillPrompt(s))}</pre></details>`;
}
// Connectors are MCP servers — "using" one means registering it in your MCP client's config.
function connectorUseBox(c) {
  return `<details class="usebox"><summary>⌁ How to add this connector</summary>
    <p class="howto">It's an MCP connector — register it in your client, then restart and its tools appear in the session.
      <b>Claude Desktop:</b> add it under <code>claude_desktop_config.json → mcpServers</code>.
      <b>Claude Code:</b> <code>claude mcp add</code> (or a project <code>.mcp.json</code>).
      <b>Cursor / other MCP clients:</b> their MCP settings.${c.install_or_source ? ` <br><b>This one:</b> ${esc(c.install_or_source)}` : ""}</p>
    ${c.url ? `<div class="copyrow"><a class="mdlink" href="${esc(c.url)}" target="_blank" rel="noopener">Website / repo ↗</a></div>` : ""}</details>`;
}

// Fetch a repo-root file (e.g. config.json). Same offline/origin assumption as ../data/.
async function loadRoot(file) {
  try {
    const r = await fetch("../" + file, { cache: "no-store" });
    if (!r.ok) return null;
    return await r.json();
  } catch { return null; }
}

// ── client-side search (A4) ────────────────────────────────────────────────────
const q = () => state.query.trim().toLowerCase();
// True if any part contains the current query (an empty query matches everything).
const hit = (...parts) => {
  const qq = q();
  if (!qq) return true;
  return parts.some(p => String(p ?? "").toLowerCase().includes(qq));
};

// ── source attribution (handles linked-resource records from CLAUDE.md Step 2c) ──
function sourceLine(s) {
  if (s.source_type === "linked_resource" && s.source_url) {
    const via = s.via_video_id || s.source_video_id;
    return `<p><a href="${esc(s.source_url)}" target="_blank" rel="noopener">Linked resource</a>` +
      (via ? ` · <a href="${yt(via)}" target="_blank" rel="noopener">via video</a>` : "") + `</p>`;
  }
  if (s.source_video_id) return `<p><a href="${yt(s.source_video_id)}" target="_blank" rel="noopener">Source video</a></p>`;
  if (s.source_url) return `<p><a href="${esc(s.source_url)}" target="_blank" rel="noopener">Source</a></p>`;
  return "";
}
const linkedPill = (s) => (s && s.source_type === "linked_resource")
  ? '<span class="linkpill" title="Discovered via a link in a video description">linked</span>' : "";

// ── HTML model podium + run report (rendered from data; Claude writes no ASCII) ──
function podiumHtml(podium) {
  const p = (podium || []).filter(Boolean).slice(0, 3);
  if (!p.length) return "";
  const byRank = {}; p.forEach(x => { byRank[x.rank] = x; });
  const order = (byRank[1] && byRank[2] && byRank[3]) ? [byRank[2], byRank[1], byRank[3]] : p;
  const cls = (m) => "pod" + (m.rank === 1 ? "1" : m.rank === 2 ? "2" : "3");
  const medal = (r) => r === 1 ? "\u{1F947}" : r === 2 ? "\u{1F948}" : r === 3 ? "\u{1F949}" : "";
  return `<div class="podium">` + order.map(m => `
    <div class="podslot ${cls(m)}">
      <div class="podmedal">${medal(m.rank)}</div>
      <div class="podrank">#${esc(m.rank)}</div>
      <div class="podscore">${esc(m.score)}<span class="podten">/10</span></div>
      <div class="podname">${esc(m.name)}${m.version ? " " + esc(m.version) : ""}</div>
      ${m.company ? `<div class="podco">${esc(m.company)}</div>` : ""}
    </div>`).join("") + `</div>`;
}
function runReportHtml(status) {
  const rr = (status && status.run_report) || {};
  if (!Object.keys(rr).length) return "";
  const rows = [
    ["Run time (ET)", rr.run_time], ["Total in playlist", rr.total_in_playlist],
    ["Already seen", rr.already_seen], ["New found", rr.new_found],
    ["Analyzed this run", rr.analyzed_this_run], ["Skipped (not relevant)", rr.skipped_not_relevant],
    ["No transcript", rr.no_transcript], ["Errors", rr.errors],
    ["Pending remaining", rr.pending_to_analyze], ["Total analyzed (all time)", status.total_videos_analyzed],
  ];
  return `<div class="card runreport"><h3>Latest run report</h3><table>` +
    rows.map(([l, v]) => `<tr><td>${esc(l)}</td><td>${esc(v ?? 0)}</td></tr>`).join("") +
    `</table></div>`;
}

// ── reliability banner (A1/A2): analyze failure (red) or stalled pipeline (amber) ─
function staleMsg(status, config) {
  if (!status) return "";
  const now = Date.now();
  const lastFetch = Date.parse(status.last_fetch || status.last_run || "");
  if (isNaN(lastFetch)) return "";
  const nextRun = Date.parse(status.next_run || "");
  let intervalMs = (!isNaN(nextRun) && nextRun > lastFetch) ? (nextRun - lastFetch) : 0;
  if (!intervalMs) intervalMs = ((config && config.run_interval_hours) || 48) * 3600 * 1000;
  if (now - lastFetch > intervalMs * 2) {
    const days = Math.max(1, Math.round((now - lastFetch) / 86400000));
    const hrs = Math.round(intervalMs / 3600000);
    return `No new fetch for ~${days} day(s) (expected about every ${hrs}h). The scheduler may be ` +
      `paused — GitHub disables cron after ~60 days of repo inactivity. Check the Actions tab, ` +
      `or trigger the Fetch workflow manually.`;
  }
  return "";
}
function renderAlert(status, config) {
  // Token-renewal banner: only show when the pipeline has actually failed.
  const tokenwarn = document.getElementById("tokenwarn");
  if (tokenwarn) tokenwarn.hidden = !(status && status.analyze_ok === false);

  // Reliability banner (separate, below counters)
  const el = document.getElementById("alert");
  if (!el) return;
  let kind = "", msg = "";
  if (status && status.analyze_ok === false) {
    kind = "bad";
    msg = `<span class="badge">PIPELINE ERROR</span> The last analyze run failed — ` +
      esc(status.token_hint || "check the GitHub Actions log for details.");
  } else {
    const stale = staleMsg(status, config);
    if (stale) { kind = "warn"; msg = `<span class="badge">PIPELINE STALLED?</span> ` + esc(stale); }
  }
  if (kind) { el.hidden = false; el.className = "alert " + kind; el.innerHTML = msg; }
  else { el.hidden = true; el.className = "alert"; el.innerHTML = ""; }
}

// ── counters + meta ──────────────────────────────────────────────────────────
function renderHeader(status) {
  if (!status) { meta.textContent = "No runs yet — waiting for the first pipeline run."; return; }
  const rr = status.run_report || {};
  meta.textContent =
    `Last fetch: ${fmtDate(status.last_fetch || status.last_run)} • ` +
    `Last analyze: ${fmtDate(status.last_analyze)} • ` +
    `Next run: ${fmtDate(status.next_run)}`;

  // Lead with the HUB'S SCALE (what AI directories / info-center apps show first), not pipeline
  // internals — the size of the knowledge base is the headline. Pulled from health.json.
  const lib = (state.health || {}).library || {};
  const vid = (state.health || {}).videos || {};
  const nsrc = ((state.config || {}).news_sources || []).length;
  const c = [
    ["Skills", lib.skills ?? status.total_skills ?? 0, true],
    ["Tools", lib.tools ?? 0, true],
    ["Connectors", lib.connectors ?? 0, false],
    ["Prompts", lib.prompts ?? 0, false],
    ["News sources", nsrc || 0, false],
    ["Videos indexed", vid.total ?? status.videos_seen ?? 0, false],
  ];
  countersEl.innerHTML = c.map(([l, n, hl]) =>
    `<div class="counter ${hl ? "hl" : ""}"><div class="n">${esc(n)}</div>
     <div class="l">${esc(l)}</div></div>`).join("");

  // Catch-up (massive-addition) banner — shown only while a big backlog is draining.
  const cuEl = document.getElementById("catchup");
  if (cuEl) {
    const cu = status.catch_up || {};
    const pending = cu.pending ?? rr.pending_to_analyze ?? 0;
    if (cu.active) {
      cuEl.hidden = false;
      cuEl.innerHTML =
        `<span class="badge">⛏️ CATCHING UP</span> A large batch of videos was added — ` +
        `Excavatortron is sprinting through the backlog (newest first). ` +
        `<b>${esc(pending)}</b> still to analyze; new knowledge is being added continuously. ` +
        `<span class="cusub">${esc(cu.reason || "")}</span>`;
    } else {
      cuEl.hidden = true;
      cuEl.innerHTML = "";
    }
  }

  renderAlert(status, state.config);
}

// ── Tab: Skills Library ──────────────────────────────────────────────────────
function renderSkills(data) {
  const skills = (data && data.skills) || [];
  let html = "";
  if (!q()) html += runReportHtml(state.status);
  if (!skills.length) return view.innerHTML = html + empty("No skills extracted yet.");

  const cats = ["all", ...Array.from(new Set(skills.map(s => s.category || "other"))).sort()];
  html += `<div class="subnav">` + cats.map(c =>
    `<button class="${state.selectedCategory === c ? "active" : ""}" data-cat="${esc(c)}">${esc(c)}</button>`
  ).join("") + `</div>`;

  // Filter toggles: hide low-quality sources, and show only cross-tool (multi-tool) skills.
  const lowCount = skills.filter(s => s.low_quality_source).length;
  const multiCount = skills.filter(isMultiTool).length;
  html += `<div class="subnav">
    <button class="${state.multiToolOnly ? "active" : ""}" data-toggle="multitool"
      title="Show only skills/techniques that work across several AI tools">
      ${state.multiToolOnly ? "&#10003; " : ""}Multi-tool only${multiCount ? ` (${multiCount})` : ""}</button>
    <button class="${state.hideLowQuality ? "active" : ""}" data-toggle="lowq"
      title="Hide skills extracted from videos that scored below the quality threshold">
      ${state.hideLowQuality ? "&#10003; " : ""}Hide low-quality sources${lowCount ? ` (${lowCount})` : ""}</button></div>`;

  let list = skills.slice();
  if (state.selectedCategory !== "all")
    list = list.filter(s => (s.category || "other") === state.selectedCategory);
  if (state.hideLowQuality) list = list.filter(s => !s.low_quality_source);
  if (state.multiToolOnly) list = list.filter(isMultiTool);
  if (q()) list = list.filter(s => hit(s.skill_name, s.slug, s.description, s.use_case,
    s.category, s.company, s.target_tool, (s.tips || []).join(" "),
    (s.compatibility || []).map(c => c.tool).join(" ")));
  // Starred (frozen) skills first, then by quality score.
  list.sort((a, b) =>
    (isStarred(b) - isStarred(a)) || ((b.quality_score || 0) - (a.quality_score || 0)));

  html += list.map(s => `
    <div class="card ${isStarred(s) ? "starred" : ""} ${s.low_quality_source ? "lowq" : ""}">
      <h3>${isStarred(s) ? '<span class="star" title="Starred — kept in original form, never auto-changed">&#9733;</span>' : ""}<span class="score">${esc(s.quality_score ?? "?")}/10</span> ${esc(s.skill_name || s.slug)}
        <span class="pill">${esc(s.category || "other")}</span>
        <span class="pill">${esc(s.target_tool || "claude")}</span>
        ${isMultiTool(s) ? '<span class="multitool" title="Works across several AI tools">multi-tool</span>' : ""}
        ${linkedPill(s)}
        ${s.open_source ? '<span class="pill">open source</span>' : ""}
        ${s.video_quality_score != null ? `<span class="vq ${s.low_quality_source ? "low" : ""}" title="Source video quality (AI content review + recency)">vid ${esc(s.video_quality_score)}/10</span>` : ""}
        ${s.low_quality_source ? '<span class="lowsrc" title="Extracted from a low-quality video — treat with caution; its score was capped">low-quality source</span>' : ""}
        ${isStarred(s) ? '<span class="frozenpill">frozen</span>' : ""}</h3>
      ${s.company ? `<div class="sub">${esc(s.company)}${s.country ? " · " + esc(s.country) : ""}</div>` : ""}
      <p>${esc(s.description || "")}</p>
      ${s.use_case ? `<p><b>Use case:</b> ${esc(s.use_case)}</p>` : ""}
      ${(s.compatibility && s.compatibility.length) ? `<p class="compatline"><b>Works with:</b> ${s.compatibility.map(c => `<span class="compat">${compatLabel(c)}</span>`).join(" ")}</p>` : ""}
      ${(s.tips && s.tips.length) ? `<p><b>Tips:</b> ${s.tips.map(esc).join(" · ")}</p>` : ""}
      ${sourceLine(s)}
      ${useBox(s)}
    </div>`).join("");
  if (!list.length) html += empty(q() ? `No skills match "${esc(state.query)}".` : "No skills in this view.");

  view.innerHTML = html;
  view.querySelectorAll("[data-cat]").forEach(b =>
    b.addEventListener("click", () => { state.selectedCategory = b.dataset.cat; renderSkills(data); }));
  const tog = view.querySelector('[data-toggle="lowq"]');
  if (tog) tog.addEventListener("click", () => { state.hideLowQuality = !state.hideLowQuality; renderSkills(data); });
  const mt = view.querySelector('[data-toggle="multitool"]');
  if (mt) mt.addEventListener("click", () => { state.multiToolOnly = !state.multiToolOnly; renderSkills(data); });
}

// ── Tab: Tools (auto-tracked catalog of AI tools & models seen in the playlist) ─
// Skills = techniques you apply; Tools = the products/models themselves. Ranked by
// how many playlist videos mention each, so the most-talked-about tools float up.
// ── Tab: Tool Rating (every tool + model, ranked by category, with what each does) ──
// Merges the old Tools + Models Ranking tabs (a locked decision). Every tool appears,
// ranked within its category by quality, each with a "what it does" blurb. A 🥇🥈🥉 podium
// tops each category; models are badged and filterable via "models only".
function renderToolRating(toolsData, modelsData) {
  const items = (toolsData && toolsData.tools) || [];
  if (!items.length) return view.innerHTML = empty("No tools tracked yet.");
  // Which tools are models? (for the badge + "models only" filter) — from models.json names.
  const modelNames = new Set();
  if (modelsData) Object.values(modelsData).forEach(blk =>
    ((blk && blk.full_ranking) || []).forEach(r => modelNames.add(String(r.name || "").toLowerCase())));
  const isModel = t => modelNames.has(String(t.name || "").toLowerCase());

  const cats = ["all", ...Array.from(new Set(items.map(t => t.category || "other"))).sort()];
  const activeCat = state.toolCategory || "all";
  const modelsOnly = !!state.modelsOnly;

  let list = items.slice();
  if (modelsOnly) list = list.filter(isModel);
  if (q()) list = list.filter(t => hit(t.name, t.slug, t.company, t.country, t.category, t.description));

  let html = `<div class="sub">${items.length} AI tools &amp; models — ranked within each category by quality, each with what it does. Models are badged; tap “models only” to filter.</div>`;
  html += `<div class="subnav">` + cats.map(c =>
      `<button class="${activeCat === c ? "active" : ""}" data-tcat="${esc(c)}">${esc(c)}</button>`).join("")
    + `<button class="${modelsOnly ? "active" : ""}" data-mo="1">⚙ models only</button></div>`;

  const catList = activeCat === "all" ? cats.filter(c => c !== "all") : [activeCat];
  let body = "";
  catList.forEach(cat => {
    const inCat = list.filter(t => (t.category || "other") === cat);
    if (!inCat.length) return;
    inCat.sort((a, b) => ((b.quality_score || 0) - (a.quality_score || 0)) || ((b.mentions || 0) - (a.mentions || 0)));
    const podium = q() ? "" : podiumHtml(inCat.slice(0, 3).map((t, i) =>
      ({ rank: i + 1, name: t.name, score: t.quality_score ?? "?", company: t.company })));
    body += `<section class="cat-section"><h2 class="cat-title">${esc(cat)}<span class="cat-count">${inCat.length}</span></h2>${podium}`;
    body += inCat.map((t, i) => `
      <div class="card ${t.low_quality_source ? "lowq" : ""}">
        <h3><span class="rank">#${i + 1}</span> <span class="score">${esc(t.quality_score ?? "?")}/10</span> ${esc(t.name)}
          ${isModel(t) ? '<span class="modelpill">model</span>' : ""}
          ${t.open_source ? '<span class="pill">open source</span>' : ""}
          ${t.mentions ? `<span class="mentions" title="How many playlist videos mention this">${esc(t.mentions)}× seen</span>` : ""}</h3>
        ${t.company ? `<div class="sub">${esc(t.company)}${t.country ? " · " + esc(t.country) : ""}${t.model_version ? " · v" + esc(t.model_version) : ""}</div>` : ""}
        <p>${esc(t.description || "")}</p>
        ${linksRow(t)}
      </div>`).join("");
    body += `</section>`;
  });
  html += body || empty(q() ? `No tools match "${esc(state.query)}".` : "No tools here.");
  view.innerHTML = html;
  view.querySelectorAll("[data-tcat]").forEach(b =>
    b.addEventListener("click", () => { state.toolCategory = b.dataset.tcat; renderToolRating(toolsData, modelsData); }));
  const moBtn = view.querySelector("[data-mo]");
  if (moBtn) moBtn.addEventListener("click", () => { state.modelsOnly = !state.modelsOnly; renderToolRating(toolsData, modelsData); });
}

// ── Tab: Improvement Log ─────────────────────────────────────────────────────
async function renderImprovement() {
  let merges = await load("merge_log.json"); let deleted = await load("deleted_skills.json");
  if (merges && !Array.isArray(merges)) merges = merges.merges || merges.entries || [];
  if (deleted && !Array.isArray(deleted)) deleted = deleted.deleted || deleted.entries || [];
  merges = merges || []; deleted = deleted || [];
  // Search filtering
  if (q()) {
    merges  = merges.filter(e  => hit(e.merged_from, e.merged_into, e.reason));
    deleted = deleted.filter(e => hit(e.slug, e.skill_name, e.reason));
  }
  let html = `<div class="card"><h3>Merge log (${merges.length})</h3>` +
    (merges.length ? merges.map(e =>
      `<p>${esc(fmtDate(e.timestamp))}: <b>${esc(e.merged_from)}</b> → <b>${esc(e.merged_into)}</b>
       <span class="sub">${esc(e.reason || "")}</span></p>`).join("") : empty(q() ? `No merges match "${esc(state.query)}".` : "No merges yet.")) + `</div>`;
  html += `<div class="card"><h3>Deleted / superseded (${deleted.length})</h3>` +
    (deleted.length ? deleted.map(e =>
      `<p><b>${esc(e.slug || e.skill_name || "?")}</b> — <span class="sub">${esc(e.reason || "")}</span></p>`
    ).join("") : empty(q() ? `No deleted skills match "${esc(state.query)}".` : "Nothing deleted yet.")) + `</div>`;
  view.innerHTML = html;
}

// ── Tab: Tips & Commands ─────────────────────────────────────────────────────
async function renderTips() {
  const tips = await load("tips.json"); const cmds = await load("commands.json");
  let html = "";
  // When searching: a tool whose NAME matches keeps all its tips; otherwise keep matching tips.
  const filterTips = (t, arr) => {
    if (!q()) return arr || [];
    if (hit(t)) return arr || [];
    return (arr || []).filter(x => hit(x));
  };
  const byTool = (tips && tips.by_tool) || {}; const general = (tips && tips.general) || {};
  // Each tool / topic becomes its own labelled group with a short bullet list (easier to scan
  // than one long "·"-joined line).
  const groupHtml = (t, arr) =>
    `<div class="tipgroup"><div class="tiptool">${esc(t)}</div><ul>` +
    arr.map(x => `<li>${esc(x)}</li>`).join("") + `</ul></div>`;
  const byToolEntries = Object.entries(byTool)
    .map(([t, arr]) => [t, filterTips(t, arr)]).filter(([, a]) => a.length);
  if (byToolEntries.length) {
    html += `<div class="card"><h3>Tips by tool</h3>` +
      byToolEntries.map(([t, arr]) => groupHtml(t, arr)).join("") + `</div>`;
  }
  const gen = Object.entries(general)
    .map(([t, arr]) => [t, filterTips(t, arr)]).filter(([, a]) => a.length);
  if (gen.length) {
    html += `<div class="card"><h3>General tips</h3>` +
      gen.map(([t, arr]) => groupHtml(t, arr)).join("") + `</div>`;
  }
  let list = (cmds && cmds.commands) || [];
  if (q()) list = list.filter(c => hit(c.command, c.description, c.tool));
  if (list.length || !q()) {
    html += `<div class="card"><h3>Slash commands (${list.length})</h3>` + (list.length ?
      `<table><tr><th>Command</th><th>Description</th><th>Tool</th></tr>` +
      list.map(c => `<tr><td><code>${esc(c.command)}</code></td><td>${esc(c.description || "")}</td>
        <td>${esc(c.tool || "")}</td></tr>`).join("") + `</table>` : empty("No commands yet.")) + `</div>`;
  }
  view.innerHTML = html || empty(q() ? `No tips or commands match "${esc(state.query)}".` : "No tips or commands yet.");
}

// ── Tab: News Feed (videos + official sites, merged every day) ────────────────
async function renderNews() {
  const vfiles = { daily: "daily_news.json", weekly: "weekly_news.json", monthly: "monthly_news.json" };
  const wfiles = { daily: "daily_web_news.json", weekly: "weekly_web_news.json", monthly: "monthly_web_news.json" };
  let html = `<div class="subnav">` + ["daily", "weekly", "monthly"].map(w =>
    `<button class="${state.newsWindow === w ? "active" : ""}" data-news="${w}">${w}</button>`).join("") + `</div>`;
  const [vdata, wdata, digestData] = await Promise.all([
    load(vfiles[state.newsWindow]), load(wfiles[state.newsWindow]), load("news_digest.json")]);
  const ventries = (vdata && vdata.entries) || [];
  const wentries = (wdata && wdata.entries) || [];
  const ts = (s) => { const d = Date.parse(s || ""); return isNaN(d) ? 0 : d; };
  let entries = ventries.concat(wentries).sort((a, b) => ts(b.publishedAt) - ts(a.publishedAt));
  if (q()) entries = entries.filter(e => hit(e.title, e.summary, e.source_name, e.channel_name));
  const hdr = (vdata && vdata.header) || (wdata && wdata.header) || {};
  html += `<div class="sub">Window: ${esc(hdr.window || state.newsWindow)} ·
    ${ventries.length} from videos + ${wentries.length} from official sites</div>`;
  // The system's OWN synthesized brief (src/news_digest.py) — a real summary, grouped into themes,
  // not a list of headlines. Shown first when available for this window.
  const syn = digestData && digestData.windows && digestData.windows[state.newsWindow];
  if (syn && syn.summary && !q()) {
    html += `<div class="card news-brief"><h3>📰 The brief <span class="sub">— our summary of ${esc(state.newsWindow)} AI news</span></h3>
      <p class="brief-lede">${esc(syn.summary)}</p>` +
      ((syn.themes || []).length ? `<div class="brief-themes">` + syn.themes.map(t =>
        `<div class="brief-theme"><b>${esc(t.theme)}</b><span>${esc(t.detail)}</span></div>`).join("") + `</div>` : "") +
      `<p class="hint">Synthesized free from ${esc(syn.n_sources || 0)} sources${syn.engine ? ` · ${esc(syn.engine)}` : ""}. Headlines below.</p></div>`;
  }
  // Pinned "most important" digest (CLAUDE.md/news writes header.digest); shown above the full array.
  const digest = (vdata && vdata.header && vdata.header.digest)
    || (wdata && wdata.header && wdata.header.digest) || [];
  if (digest.length && !q()) {
    html += `<div class="card digest"><h3>📌 Most important — ${esc(state.newsWindow)}</h3><ol>` +
      digest.map(d => {
        const txt = typeof d === "string" ? d : (d.text || d.title || "");
        const url = d && d.url;
        return `<li>${esc(txt)}${url ? ` <a href="${esc(url)}" target="_blank" rel="noopener">↗</a>` : ""}</li>`;
      }).join("") + `</ol></div>`;
  }
  if (entries.length) {
    html += entries.map(e => {
      const web = e.source_type === "web" || (e.url && !e.video_id);
      const src = web ? (e.source_name || "web") : (e.channel_name || "");
      const link = web ? (e.url || "#") : yt(e.video_id);
      const label = web ? "Read" : "Watch";
      const tag = web ? '<span class="webpill">web</span>' : '<span class="vidpill">video</span>';
      const low = e.low_quality_source ? '<span class="lowsrc">low-quality source</span>' : "";
      return `<div class="card newscard ${e.low_quality_source ? "lowq" : ""}">
        <h3>${esc(e.title || "?")} ${tag} ${low}</h3>
        <div class="sub">${esc(src)} · ${esc(fmtDate(e.publishedAt))}</div>
        <p class="newsum">${esc(e.summary || "(summary pending)")}</p>
        <p><a href="${esc(link)}" target="_blank" rel="noopener">${label} &rarr;</a></p></div>`;
    }).join("");
  } else { html += empty(q() ? `No ${state.newsWindow} news matches "${esc(state.query)}".` : `No ${state.newsWindow} news entries.`); }
  view.innerHTML = html;
  view.querySelectorAll("[data-news]").forEach(b =>
    b.addEventListener("click", () => { state.newsWindow = b.dataset.news; renderNews(); }));
}

// ── Tab: dynamic trend tabs (auto-created by the self-improvement stage) ──────
function renderDynamicTab(id) {
  const t = state.dynamicTabs.find(x => x.id === id);
  if (!t) return view.innerHTML = empty("This tab is no longer available.");
  const isNew = tabIsNew(t);
  const evCount = (t.evidence_video_ids || []).length;
  const newUntil = (t.badge_until || "").slice(0, 10);
  let html = `<div class="card"${isNew ? ' style="border-color:#2b4a7a;box-shadow:inset 3px 0 0 var(--accent)"' : ""}>
    <h3>${isNew ? '<span class="newbadge">NEW</span> ' : ""}${esc(t.title || t.id)}</h3>
    <div class="sub">${esc(t.description || "")}</div>
    <p class="hint">Auto-created from a recurring sequence spotted across ${evCount}
    video${evCount === 1 ? "" : "s"} during the first days of tracking.${isNew && newUntil ? ` Marked NEW until ${esc(newUntil)}.` : ""}
    Not useful? Dismiss it from the offline MCP:
    <code class="cmd">dismiss_dynamic_tab("${esc(t.id)}")</code>.</p></div>`;
  const items = t.items || [];
  html += items.length ? items.map(it => `<div class="card">
    <h3>${esc(it.title || "?")}</h3>
    ${it.sub ? `<div class="sub">${esc(it.sub)}</div>` : ""}
    <p>${esc(it.body || "")}</p>
    ${it.url ? `<p><a href="${esc(it.url)}" target="_blank" rel="noopener">Open</a></p>` : ""}
  </div>`).join("") : empty("No items in this tab yet.");
  view.innerHTML = html;
}

// A dynamic tab wears its NEW badge until `badge_until` (the improve stage sets
// it to created_at + new_badge_days). Fall back to created_at + 7 days for tabs
// written before badge_until existed. The badge auto-expires — no human action.
function tabIsNew(t) {
  const until = Date.parse(t.badge_until || "");
  if (!isNaN(until)) return Date.now() < until;
  const created = Date.parse(t.created_at || "");
  if (!isNaN(created)) return Date.now() < created + 7 * 24 * 3600 * 1000;
  return false;
}

// Add a nav button for each active dynamic tab (with a NEW badge if still fresh).
function injectDynamicTabs() {
  const nav = document.getElementById("tabs");
  if (!nav) return;
  nav.querySelectorAll("[data-dyntab]").forEach(b => b.remove());
  state.dynamicTabs.forEach(t => {
    const btn = document.createElement("button");
    btn.dataset.tab = "dyn:" + t.id;
    btn.dataset.dyntab = t.id;
    btn.innerHTML = esc(t.title || t.id) + (tabIsNew(t) ? ' <span class="newbadge">NEW</span>' : "");
    btn.addEventListener("click", () => show(btn.dataset.tab));
    nav.appendChild(btn);
  });
}

// ── Tab: Connectors ──────────────────────────────────────────────────────────
const _slugify = (s) => String(s || "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
function safetyPill(rating, reasons) {
  if (!rating) return "";
  const map = { safe: ["safe", "saf-ok"], caution: ["caution", "saf-warn"], risky: ["risky", "saf-bad"] };
  const m = map[rating]; if (!m) return "";
  return `<span class="safpill ${m[1]}" title="${esc((reasons || []).join(" · "))}"><i class="dot"></i>${m[0]}</span>`;
}
async function renderConnectors(data) {
  const safety = ((await load("safety.json")) || {}).connectors || {};
  // Phase 4: sandbox verification verdicts (owner: test-run EVERYTHING; D5: shrink to verified)
  const cv = (await load("connectors_verified.json")) || {};
  const vmap = cv.verified || {};
  const vsum = cv.summary || {};
  let items = (data && data.connectors) || [];
  if (!items.length) return view.innerHTML = empty("No connectors or MCP servers tracked yet.");
  if (q()) items = items.filter(c => hit(c.name, c.provider, c.what_it_does, c.category, c.type));
  const passCount = Object.values(vmap).filter(v => v.status === "pass").length;
  const showVerifiedOnly = localStorage.getItem("excavatortron.connverified") !== "off" && passCount >= 25;
  if (showVerifiedOnly) items = items.filter(c => (vmap[c.name] || {}).status === "pass");
  items.sort((a, b) =>
    (isStarred(b) - isStarred(a)) || ((b.quality_score || 0) - (a.quality_score || 0)));
  const prog = `<div class="card"><h3>🧪 Sandbox verification <span class="sub">— your call: test-run ALL ${vsum.total || 1142} in isolated CI batches</span>
      ${passCount >= 25 ? `<button class="qr-btn" id="conn-vtoggle">${showVerifiedOnly ? "show all" : "verified only"}</button>` : ""}</h3>
    <p class="sub">checked <b>${vsum.checked || 0}</b> / ${vsum.total || 1142} so far · ${Object.entries(vsum.by_status || {}).map(([k, v]) => `${esc(k)}: <b>${v}</b>`).join(" · ") || "first batches queued"} —
      each one resolves a REAL install command, then runs it in a clean sandbox (no secrets, temp dir, timeout). ${showVerifiedOnly ? "Showing verified-only (D5)." : `The tab shrinks to verified-only once ≥25 pass${passCount ? ` (now ${passCount})` : ""}.`}</p>
  </div>`;
  view.innerHTML = prog + items.map(c => {
    const v = vmap[c.name];
    const vPill = v ? (v.status === "pass"
        ? `<span class="freepill free-yes" title="${esc(v.cmd || "")} — ${esc((v.log || "").slice(0, 120))}">✓ sandbox-verified</span>`
        : v.status === "fail" ? `<span class="freepill free-no" title="${esc((v.log || "").slice(0, 120))}">✗ failed sandbox</span>`
        : `<span class="freepill free-mid" title="${esc(v.note || v.log || "")}">${esc(v.status)}</span>`) : "";
    return _connCard(c, safety, vPill);
  }).join("") || empty(showVerifiedOnly ? "No verified connectors match — toggle 'show all'." : `No connectors match "${esc(state.query)}".`);
  const vt = view.querySelector("#conn-vtoggle");
  if (vt) vt.addEventListener("click", () => {
    localStorage.setItem("excavatortron.connverified", showVerifiedOnly ? "off" : "on");
    show("connectors");
  });
}
function _connCard(c, safety, vPill) {
  {
    const via = c.via_video_id || c.source_video;
    const srcLine = (c.source_type === "linked_resource" && c.source_url)
      ? `<p><a href="${esc(c.source_url)}" target="_blank" rel="noopener">Linked resource</a>` +
        (via ? ` · <a href="${yt(via)}" target="_blank" rel="noopener">via video</a>` : "") + `</p>`
      : c.source_video ? `<p><a href="${yt(c.source_video)}" target="_blank" rel="noopener">Source video</a></p>`
      : c.source_url ? `<p><a href="${esc(c.source_url)}" target="_blank" rel="noopener">Source</a></p>` : "";
    // Free / paid + which Claude surface it runs in (CLAUDE.md Step 8 extended fields).
    const freeRaw = String(c.free ?? "").toLowerCase();
    const freeMap = { yes: ["Free", "free-yes"], no: ["Paid", "free-no"], freemium: ["Freemium", "free-mid"] };
    const fm = freeMap[freeRaw];
    const freePill = fm ? `<span class="freepill ${fm[1]}">${fm[0]}</span>` : "";
    const works = c.works_in ? `<span class="workspill" title="Which Claude surface this runs in">${esc(c.works_in)}</span>` : "";
    const saf = safety[c.slug || _slugify(c.name)];
    const safPill = saf ? safetyPill(saf.rating, saf.reasons) : "";
    const metaBits = [];
    if (c.free_tokens) metaBits.push(`<span class="metapill"><b>Free tier:</b> ${esc(c.free_tokens)}</span>`);
    if (c.paid_version) metaBits.push(`<span class="metapill"><b>Paid:</b> ${esc(c.paid_version)}</span>`);
    const metaRow = metaBits.length ? `<div class="connmeta">${metaBits.join("")}</div>` : "";
    const urlLine = c.url ? `<p><a href="${esc(c.url)}" target="_blank" rel="noopener">Website / repo</a></p>` : "";
    return `<div class="card ${isStarred(c) ? "starred" : ""}">
    <h3>${isStarred(c) ? '<span class="star" title="Starred — frozen, never auto-changed">&#9733;</span>' : ""}<span class="score">${esc(c.quality_score ?? "?")}/10</span> ${esc(c.name)}
      <span class="pill">${esc(c.type || "")}</span>
      ${safPill}
      ${freePill}
      ${works}
      ${c.official ? '<span class="official">official</span>' : ""}
      ${linkedPill(c)}
      ${vPill || ""}
      ${isStarred(c) ? '<span class="frozenpill">frozen</span>' : ""}</h3>
    <div class="sub">${esc(c.provider || "")}${c.category ? " · " + esc(c.category) : ""}${c.source ? " · src: " + esc(c.source) : ""}</div>
    <p>${esc(c.what_it_does || "")}</p>
    ${metaRow}
    ${c.install_or_source ? `<p><b>Install / source:</b> ${esc(c.install_or_source)}</p>` : ""}
    ${urlLine}
    ${srcLine}
    ${connectorUseBox(c)}
  </div>`;
  }
}

// ── Tab: Self-Improvement (health + suggestion queue + audit) ─────────────────
async function renderSelfImprove() {
  const [health, sugData, apprData, audit, starsData, selfCheck, fixTasks, review, trends, maint] =
    await Promise.all([
      load("health.json"), load("improvement_suggestions.json"),
      load("approvals.json"), load("improvement_audit.json"), load("stars.json"),
      load("self_check.json"), load("improvement_tasks.json"), load("review_findings.json"),
      load("trends.json"), load("maintenance.json"),
    ]);
  const [improveLog, tokenActive] = await Promise.all([load("improve_log.json"), load("token_active.json")]);
  if (window.__improveTimer) clearInterval(window.__improveTimer);
  let html = "";
  html += await goalsPanel();
  html += await prioritiesPanel();

  // ── Countdown to the next self-improvement run + proof of what it last changed ──
  const nextImprove = (() => {
    const n = new Date();
    const d = new Date(Date.UTC(n.getUTCFullYear(), n.getUTCMonth(), n.getUTCDate(), 20, 0, 0));
    let add = (6 - d.getUTCDay() + 7) % 7;                  // days until Saturday
    if (add === 0 && n.getTime() > d.getTime()) add = 7;    // today's 20:00 already passed
    d.setUTCDate(d.getUTCDate() + add);
    return d;
  })();
  const lastSC = (selfCheck && selfCheck.ran_at) ? fmtDate(selfCheck.ran_at) : "—";
  const scScore = selfCheck ? `${selfCheck.score}/${selfCheck.total || 50}` : "—";
  const openTasks = (fixTasks && (fixTasks.tasks || []).filter(t => (t.status || "open") !== "done").length) || 0;
  const lastReview = (review && review.generated_at) ? fmtDate(review.generated_at) : "—";
  const lastEff = (await load("effectiveness.json"));
  const effLine = lastEff ? `${lastEff.lanes ? lastEff.lanes.length : 0} lanes scored, weakest = ${esc((lastEff.summary || {}).weakest_lane || "?")}` : "—";
  html += `<div class="card improve-clock">
    <h3>⏱ Self-improvement</h3>
    <div class="ic-row">
      <div class="ic-timer"><div class="ic-label">Next deep pass in</div>
        <div class="ic-count" id="improve-countdown">…</div>
        <div class="sub">weekly · Sat 20:00 UTC (${esc(fmtDate(nextImprove.toISOString()))})</div></div>
      <div class="ic-last">
        <div class="sub" style="margin-bottom:6px"><b>What it last did</b> (so you can verify it's actually running):</div>
        <ul class="ic-changes">
          <li>Reference self-check ran <b>${esc(lastSC)}</b> &rarr; score <b>${esc(scScore)}</b></li>
          <li><b>${esc(openTasks)}</b> open improvement task(s) queued for auto-fix</li>
          <li>Effectiveness scoreboard: ${effLine}</li>
          <li>3-agent review last ran <b>${esc(lastReview)}</b></li>
        </ul></div>
    </div></div>`;

  // ── Recent self-improvement activity — a short line after each cycle (proof it's running) ──
  if (improveLog && (improveLog.entries || []).length) {
    const rows = improveLog.entries.slice(-8).reverse().map(e =>
      `<li><span class="il-when">${esc(fmtDate(e.at))}</span> ${esc(e.text)}</li>`).join("");
    html += `<div class="card improve-clock"><h3>📝 Recent self-improvement activity</h3>
      <p class="sub">One short line each time the self-improvement system runs, so you can see it's working.</p>
      <ul class="il-list">${rows}</ul></div>`;
  }

  // ── Token-reduction PROTOCOL — runs every startup, applies all reducers to the Claude lanes ──
  if (tokenActive && tokenActive.status === "active") {
    const reducers = (tokenActive.core_reducers || []).map(r =>
      `<li><b>${esc(r.name)}</b><br><span class="sub">${esc(r.technique)}</span></li>`).join("");
    html += `<div class="card improve-clock"><h3>🎟 Token-reduction protocol
        <span class="pl-badge pl-live" style="margin-left:8px">● ACTIVE</span></h3>
      <p class="sub">Runs on every cycle so the Claude lanes (deep analysis + the 2×/week review) spend as few Pro tokens as possible. <b>${esc(tokenActive.count || 0)}</b> reducers active · refreshed ${esc(fmtDate(tokenActive.generated_at))}.</p>
      <details><summary class="sub" style="cursor:pointer">Show the active reducers</summary>
        <ul class="tok-list">${reducers}</ul></details></div>`;
  }

  // ── Trend watch — surging topics the system proposes turning into tabs/features ──
  if (trends && (trends.proposals || []).length) {
    const goals = trends.goals || {};
    const top = trends.proposals.slice(0, 6);
    html += `<div class="card trend-card"><h3>📈 Trend watch <span class="sub">→ new tabs &amp; features</span></h3>
      <p class="sub">The system watches its own library for surging topics and proposes features, scored 1–10 and tied to one of the 5 goals. Strong ones are auto-queued for self-improvement.</p>
      <div class="trend-rows">` +
      top.map(p => `<div class="trend-row">
        <span class="trend-score s-${p.score >= 8 ? "hi" : p.score >= 6 ? "mid" : "lo"}">${esc(p.score)}</span>
        <div class="trend-main"><b>${esc(p.proposed_feature)}</b><span class="trend-why">${esc(p.trend)}</span></div>
        <span class="trend-goal" title="${esc(goals[p.goal] || "")}">${esc(p.goal)}</span>
      </div>`).join("") +
      `</div></div>`;
  }

  // ── Maintenance sweep — system integrity, incl. the brain "white lines" fix ──
  if (maint && (maint.issues || []).length !== undefined) {
    const g = maint.grade || "?";
    const gcls = g === "A" ? "good" : (g === "B" || g === "C") ? "warn" : "bad";
    html += `<div class="card"><h3>🧹 Maintenance sweep</h3>
      <div class="health"><div class="big ${gcls}">${esc(g)}<span style="font-size:18px"> · ${esc(maint.health_score)}/100</span></div>
      <div><div class="sub">Integrity of the brain + whole data layer · generated ${esc(fmtDate(maint.generated_at))}</div>
      <ul class="ic-changes" style="margin-top:8px">` +
      (maint.issues || []).slice(0, 6).map(i =>
        `<li><b class="sev-${esc(i.severity)}">${esc(i.severity)}</b> — ${esc(i.issue)} <b>(${esc(i.count)})</b><br><span class="sub">→ ${esc(i.fix)}</span></li>`).join("") +
      `</ul></div></div></div>`;
  }

  // Announcement when the self-improvement stage auto-created a new dashboard tab.
  if (health && health.new_tab_announcement) {
    html += `<div class="card" style="border-color:#2b4a7a;box-shadow:inset 3px 0 0 var(--accent)">
      <h3><span class="newbadge">NEW TAB</span> ${esc(health.new_tab_announcement)}</h3>
      <p class="hint">A recurring trend earned its own tab (see the nav bar). Dismiss it anytime with
      <code class="cmd">dismiss_dynamic_tab("id")</code>.</p></div>`;
  }

  // Health score + metrics
  if (health) {
    const sc = Number(health.score ?? 0);
    const cls = sc >= 80 ? "good" : sc >= 50 ? "warn" : "bad";
    html += `<div class="card"><h3>Data health</h3>
      <div class="health"><div class="big ${cls}">${esc(health.score ?? "?")}<span style="font-size:18px">/100</span></div>
      <div><div class="sub">Generated ${esc(health.generated_at || "?")}</div>
      <div class="metrics">` +
      Object.entries(health.metrics || {}).map(([k, v]) =>
        `<span class="metric"><b>${esc(v)}</b> ${esc(k.replace(/_/g, " "))}</span>`).join("") +
      `</div></div></div>`;
    const tok = (health.token_optimization || {}).advice;
    if (tok) html += `<p><b>Token advice:</b> ${esc(tok)}</p>`;
    if (health.cadence_advice) html += `<p><b>Cadence:</b> ${esc(health.cadence_advice)}</p>`;
    if ((health.advice || []).length)
      html += `<p><b>Recommendations:</b></p><ul>${health.advice.map(a => `<li>${esc(a)}</li>`).join("")}</ul>`;
    html += `</div>`;
  } else {
    html += `<div class="card"><h3>Data health</h3>${empty("No health report yet — runs every few days, or force it with the MCP tool run_improve().")}</div>`;
  }

  // Reference self-check — how well the system still matches the user's original
  // "System Prompt" spec (docs/REFERENCE_SPEC.md). The improve stage re-answers all
  // 50 questions each run and opens a fix task for every gap (loop closes itself).
  if (selfCheck && selfCheck.ran_at) {
    const sTotal = Number(selfCheck.total ?? 50);
    const sCount = Number(selfCheck.score ?? 0);
    const pct = sTotal ? Math.round((sCount / sTotal) * 100) : 0;
    const scls = pct >= 80 ? "good" : pct >= 50 ? "warn" : "bad";
    html += `<div class="card"><h3>Reference self-check</h3>
      <div class="health"><div class="big ${scls}">${esc(selfCheck.score ?? "?")}<span style="font-size:18px">/${esc(sTotal)}</span></div>
      <div><div class="sub">Last checked ${esc(selfCheck.ran_at)} · ${esc(selfCheck.improvements_logged ?? 0)} improvements logged</div>
      <p class="hint">Each run re-answers the ${esc(sTotal)} questions from the original System Prompt spec
      (<code class="cmd">docs/REFERENCE_SPEC.md</code>) and opens a fix task for every gap.</p></div></div>`;
    const flagged = (selfCheck.results || []).filter(r =>
      /\b(no|partial|missing|gap|todo)\b/i.test(String(r.answer || "")));
    if (flagged.length) {
      html += `<p><b>Gaps found (${flagged.length}):</b></p>` +
        flagged.slice(0, 12).map(r =>
          `<div class="sug"><b>Q${esc(r.n)}</b> <span class="sub">${esc(r.question || "")}</span>
           <p>${esc(r.answer || "")}${r.evidence ? ` <span class="sub">— ${esc(r.evidence)}</span>` : ""}</p></div>`).join("");
    }
    html += `</div>`;
  }

  // Open self-check fix tasks (Step 1b auto-applies the safe ones next run).
  const tasks = ((fixTasks && fixTasks.tasks) || []).filter(t => (t.status || "open") !== "done");
  if (tasks.length) {
    html += `<div class="card"><h3>Self-check fix tasks (${tasks.length} open)</h3>
      <p class="hint">The next self-improvement run auto-applies the safe fixes and queues the rest for your approval.</p>` +
      tasks.slice(0, 15).map(t =>
        `<div class="sug"><span class="stat st-${esc(t.kind || "needs_approval")}">${esc((t.kind || "task").replace(/_/g, " "))}</span>
         <b>Q${esc(t.n)}</b> <p>${esc(t.fix || "")}</p></div>`).join("") + `</div>`;
  }

  // 3-agent review (usability / cut-the-bullshit / deep code bugs) — Claude first,
  // then an external engine + CodeQL. Read-only summary of data/review_findings.json.
  if (review && ((review.scores && Object.keys(review.scores).length) || (review.findings || []).length)) {
    const sc = review.scores || {};
    const dim = (k, label) => sc[k] != null
      ? `<span class="metric"><b>${esc(sc[k])}</b>/10 ${esc(label)}</span>` : "";
    html += `<div class="card"><h3>Latest review <span class="sub">(${esc(review.mode || "weekly")} · ${esc(review.generated_at || "?")})</span></h3>
      <div class="metrics">${dim("usability", "usability")}${dim("cut_the_bullshit", "cut the bullshit")}${dim("deep_code_bugs", "deep code bugs")}` +
      (sc.overall != null ? `<span class="metric"><b>${esc(sc.overall)}</b>/10 overall</span>` : "") + `</div>`;
    const rv = review.reviewers || {};
    const rbits = [];
    if (rv.claude) rbits.push(`Claude ${rv.claude.ok === false ? "…" : "✓"}`);
    if (rv.external) rbits.push(`${esc(rv.external.provider || "external")}: ${esc(rv.external.status || "pending")}`);
    if (rv.codeql) rbits.push(`CodeQL: ${esc(rv.codeql.status || "—")}`);
    if (rbits.length) html += `<div class="sub">Reviewers — ${rbits.join(" · ")}</div>`;
    if ((review.top_actions || []).length)
      html += `<p><b>Top actions:</b></p><ul>${review.top_actions.map(a => `<li>${esc(a)}</li>`).join("")}</ul>`;
    html += `</div>`;

    // Competitor benchmark (usability vs Future Tools / TAAFT / Toolify / Product Hunt AI)
    const bm = review.benchmark || {};
    if ((bm.we_do_better || []).length || (bm.they_do_better || []).length || (bm.borrow_next || []).length) {
      const col = (title, arr) => `<div><div class="sub"><b>${esc(title)}</b></div>` +
        ((arr || []).length ? `<ul>${arr.map(x => `<li>${esc(x)}</li>`).join("")}</ul>` : `<p class="sub">—</p>`) + `</div>`;
      html += `<div class="card"><h3>Competitor benchmark</h3>
        ${(bm.competitors || []).length ? `<div class="sub">vs ${(bm.competitors || []).map(esc).join(", ")}</div>` : ""}
        <div class="bench">${col("We do better", bm.we_do_better)}${col("They do better", bm.they_do_better)}${col("Borrow next", bm.borrow_next)}</div></div>`;
    }

    // Open findings across all three dimensions (external-added ones are tagged).
    let finds = (review.findings || []).filter(f => (f.status || "open") === "open");
    if (q()) finds = finds.filter(f => hit(f.dimension, f.detail, f.where, f.suggestion, f.area));
    if (finds.length) {
      const sevRank = { high: 0, med: 1, low: 2 };
      finds.sort((a, b) => (sevRank[a.severity] ?? 3) - (sevRank[b.severity] ?? 3));
      html += `<div class="card"><h3>Open review findings (${finds.length})</h3>` +
        finds.slice(0, 25).map(f =>
          `<div class="sug"><span class="stat st-${esc(f.severity || "low")}">${esc(f.severity || "?")}</span>
           <b>${esc((f.dimension || "").replace(/_/g, " "))}</b>
           <span class="sub">${esc(f.where || "")}${f.source === "external" ? " · external" : ""}</span>
           <p>${esc(f.detail || "")}</p>
           ${f.suggestion ? `<p class="sub">Fix: ${esc(f.suggestion)}</p>` : ""}</div>`).join("") + `</div>`;
    }
  }

  // Suggestion queue (approve/dismiss are done from the MCP server — read-only here)
  const approved = new Set((apprData && apprData.approved_ids) || []);
  const dismissed = new Set((apprData && apprData.dismissed_ids) || []);
  let sugs = (sugData && sugData.suggestions) || [];
  if (q()) sugs = sugs.filter(s => hit(s.type, s.detail, (s.proposed_change && JSON.stringify(s.proposed_change))));
  const eff = (s) => approved.has(s.id) ? "approved" : dismissed.has(s.id) ? "dismissed" : (s.status || "pending");
  const pending = sugs.filter(s => eff(s) === "pending");
  html += `<div class="card"><h3>Suggestions awaiting your decision (${pending.length})</h3>
    <p class="hint">The self-improvement run proposes risky changes here; safe fixes it just makes.
    Approve or dismiss from Claude Desktop (offline MCP): <code class="cmd">approve_suggestion("id")</code>,
    <code class="cmd">dismiss_suggestion("id")</code>, <code class="cmd">run_improve()</code>. Frozen skills are never touched.</p>`;
  if (sugs.length) {
    html += sugs.map(s => {
      const st = eff(s);
      const pc = s.proposed_change || {};
      const detail = pc.detail || JSON.stringify(pc);
      return `<div class="sug"><span class="stat st-${esc(st)}">${esc(st)}</span>
        <b>${esc(s.type || "?")}</b> <span class="sub">${esc(s.id || "")}</span>
        <p>${esc(s.detail || "")}</p>
        ${Object.keys(pc).length ? `<p class="sub">Proposed: ${esc(detail)}</p>` : ""}</div>`;
    }).join("");
  } else { html += empty("No suggestions yet."); }
  html += `</div>`;

  // Starred / frozen overview
  const stars = (starsData && starsData.starred) || [];
  html += `<div class="card"><h3>Starred &amp; frozen skills (${stars.length})</h3>
    <p class="hint">Star a proven skill to freeze it: <code class="cmd">star_skill("slug","why")</code>; remove with <code class="cmd">unstar_skill("slug")</code>.</p>` +
    (stars.length ? stars.map(e =>
      `<p><span class="star">&#9733;</span> <b>${esc(e.slug)}</b> <span class="sub">${esc(e.reason || "")}</span></p>`).join("")
      : empty("No starred skills yet.")) + `</div>`;

  // Last audit run
  const runs = (audit && audit.runs) || [];
  if (runs.length) {
    const r = runs[runs.length - 1];
    html += `<div class="card"><h3>Last self-improvement run</h3>
      <div class="sub">${esc(r.run_at || "")} · health ${esc(r.health_score ?? "?")}/100</div>
      <p>${esc(r.notes || "")}</p>
      ${(r.caps_hit || []).length ? `<p class="sub">Caps hit: ${esc((r.caps_hit || []).join(", "))}</p>` : ""}</div>`;
  }

  view.innerHTML = html;
  // live countdown to the next self-improvement run
  const tickImprove = () => {
    const el = document.getElementById("improve-countdown");
    if (!el) { clearInterval(window.__improveTimer); return; }
    let ms = nextImprove.getTime() - Date.now(); if (ms < 0) ms = 0;
    const d = Math.floor(ms / 86400000), h = Math.floor(ms / 3600000) % 24,
          m = Math.floor(ms / 60000) % 60, s = Math.floor(ms / 1000) % 60;
    el.textContent = `${d}d ${h}h ${m}m ${s}s`;
  };
  tickImprove(); window.__improveTimer = setInterval(tickImprove, 1000);
}

// ── Tab: Grow Sources (suggest a channel when the playlist stalls) ────────────
async function renderSources() {
  const [data, gated, disc] = await Promise.all([
    load("channel_suggestions.json"), load("comment_gated.json"),
    load("discovered_elements.json")]);
  // R2 (owner: 'more retrieval sources beyond the playlist') — what the new sources found
  let discHTML = "";
  if (disc && disc.elements && disc.elements.length) {
    const bySrc = Object.entries(disc.by_source || {}).map(([s, n]) => `${esc(s)} ${esc(n)}`).join(" · ");
    discHTML = `<div class="card"><h3>🛰 Newly discovered <span class="sub">— ${esc(disc.total)} finds from the new retrieval sources beyond the playlist (${esc(bySrc)}); status 'discovered' = mined, not yet verified into the hub</span></h3>
      <div style="display:flex;flex-wrap:wrap;gap:6px;max-height:260px;overflow-y:auto">${
        disc.elements.slice(0, 40).map(e => `<a class="pill" href="${esc(e.url)}" target="_blank" rel="noopener" title="${esc(e.what)}">${esc(e.type)}: ${esc(e.name)}</a>`).join("")}</div></div>`;
  }
  const sugs = (data && data.suggestions) || [];
  const pending = sugs.filter(s => (s.status || "pending") === "pending");
  const th = (data && data.threshold) || 25;
  const wk = data && data.weekly_additions;
  let html = `<div class="sub">Keeps the playlist growing: when fewer than ${esc(th)} videos are added in a week, Excavatortron proposes one of your highest-value channels for you to approve.</div>`;
  if (wk != null) {
    const ok = wk >= th;
    html += `<div class="card"><h3>${ok ? "✅" : "⚠️"} ${esc(wk)} videos added in the last week <span class="pill">target ${esc(th)}</span></h3>
      <p class="sub">${ok ? "Growing well — no suggestion needed right now." : "Below target — review the suggested channel below."}</p></div>`;
  }
  if (pending.length) {
    html += pending.map(s => `
      <div class="card">
        <h3>📺 ${esc(s.channel_title || s.channel)} <span class="newbadge">NEEDS YOU</span></h3>
        <p>${esc(s.reason || "")}</p>
        <p class="hint">Approve to add these ${esc((s.videos || []).length)} videos to your playlist (they'll then be transcribed + analyzed). <b>Approve:</b> tell Claude “approve ${esc(s.channel)}”, or use the MCP tool <code class="cmd">approve_channel</code>. <b>Skip:</b> “dismiss ${esc(s.channel)}”.</p>
        <ol class="srcvids">${(s.videos || []).map(v =>
          `<li><a href="${esc(v.url || yt(v.id))}" target="_blank" rel="noopener">${esc(v.title || v.id)}</a>${v.published ? ` <span class="sub">${esc(String(v.published).slice(0, 10))}</span>` : ""}</li>`).join("")}</ol>
      </div>`).join("");
  } else {
    html += empty("No channel suggestions pending.");
  }

  // Resources hidden behind a comment-wall that we couldn't auto-retrieve (CLAUDE.md Step 2e)
  const gl = (gated && (gated.items || gated.resources)) || [];
  if (gl.length) {
    html += `<h2 class="cat-title">🔒 Behind a comment-wall <span class="cat-count">${esc(gl.length)}</span></h2>
      <div class="sub">These videos hide their file/link behind a comment (“comment X and I'll send it”) and it wasn't findable automatically — grab these few by hand.</div>`;
    html += gl.map(g => `
      <div class="card">
        <h3>🔒 ${esc(g.title || g.video_id)}</h3>
        ${g.what_it_is ? `<p>${esc(g.what_it_is)}</p>` : ""}
        <p class="hint">${g.comment_keyword ? `Comment <code class="cmd">${esc(g.comment_keyword)}</code> on the video to get it.` : "Check the video's comments / pinned comment for the link."} &nbsp;<a href="${esc(g.source_url || yt(g.video_id))}" target="_blank" rel="noopener">Open video ↗</a></p>
      </div>`).join("");
  }
  view.innerHTML = discHTML + html;
}

// ── Tab: Prompts (master / guardrail / creation prompt library) ──────────────
function renderPrompts(data) {
  const items = (data && data.prompts) || [];
  if (!items.length) return view.innerHTML = empty("No prompts yet — they'll fill in as videos are analyzed.");
  const LABELS = { master: "Master", system_guardrail: "System / guardrail", creation: "Creation",
    coding: "Coding", agents: "Agents", research: "Research", marketing: "Marketing", other: "Other" };
  const cats = ["all", ...Array.from(new Set(items.map(p => p.category || "other")))];
  const active = state.promptCat || "all";
  let list = items.slice();
  if (active !== "all") list = list.filter(p => (p.category || "other") === active);
  if (q()) list = list.filter(p => hit(p.title, p.purpose, p.prompt_text, p.category));
  let html = `<div class="sub">${items.length} prompts — master system prompts, anti-hallucination “don't lie” guardrails, and creation prompts. Hit Copy to use one.</div>`;
  html += `<div class="subnav">` + cats.map(c =>
    `<button class="${active === c ? "active" : ""}" data-pcat="${esc(c)}">${esc(c === "all" ? "all" : (LABELS[c] || c))}</button>`).join("") + `</div>`;
  html += list.map((p, i) => `
    <div class="card">
      <h3>${esc(p.title || "Prompt")} <span class="pill">${esc(LABELS[p.category] || p.category || "other")}</span>${p.curated ? '<span class="pill">curated</span>' : ""}</h3>
      ${p.purpose ? `<div class="sub">${esc(p.purpose)}</div>` : ""}
      <pre class="promptbox" id="pb${i}">${esc(p.prompt_text || "")}</pre>
      <p><button class="qr-btn" data-copy="pb${i}">Copy</button>${
        p.source_url ? ` <a href="${esc(p.source_url)}" target="_blank" rel="noopener">Source</a>`
          : (p.source_video_id ? ` <a href="${yt(p.source_video_id)}" target="_blank" rel="noopener">Source video</a>` : "")
      }${p.notes ? ` <span class="sub">${esc(p.notes)}</span>` : ""}</p>
    </div>`).join("");
  if (!list.length) html += empty("No prompts match.");
  view.innerHTML = html;
  view.querySelectorAll("[data-pcat]").forEach(b =>
    b.addEventListener("click", () => { state.promptCat = b.dataset.pcat; renderPrompts(data); }));
  view.querySelectorAll("[data-copy]").forEach(b => b.addEventListener("click", () => {
    const pre = document.getElementById(b.dataset.copy);
    if (pre && navigator.clipboard) {
      navigator.clipboard.writeText(pre.innerText);
      const o = b.textContent; b.textContent = "Copied ✓"; setTimeout(() => b.textContent = o, 1500);
    }
  }));
}

// ── Tab: Coming Soon (announced but not-yet-released tools) ───────────────────
function renderComingSoon(data) {
  const items = ((data && data.tools) || []).filter(t => (t.release_status || "released") === "upcoming");
  let html = `<div class="sub">AI tools &amp; models that have been <b>announced but not yet released</b> — kept out of the live rankings until they ship.</div>`;
  let list = items.slice();
  if (q()) list = list.filter(t => hit(t.name, t.company, t.category, t.description));
  if (!list.length) return view.innerHTML = html + empty(q() ? "No upcoming tools match." : "No upcoming tools tracked yet — they'll appear here as they're announced.");
  list.sort((a, b) => String(a.expected_release || "zzzz").localeCompare(String(b.expected_release || "zzzz")) || ((b.quality_score || 0) - (a.quality_score || 0)));
  html += list.map(t => `
    <div class="card upcoming">
      <h3><span class="soonpill">🔜 UPCOMING</span> ${esc(t.name)} <span class="pill">${esc(t.category || "other")}</span></h3>
      ${(t.company || t.expected_release) ? `<div class="sub">${esc(t.company || "")}${t.country ? " · " + esc(t.country) : ""}${t.expected_release ? " · expected " + esc(t.expected_release) : ""}</div>` : ""}
      <p>${esc(t.description || "")}</p>
      ${t.source_url ? `<p><a href="${esc(t.source_url)}" target="_blank" rel="noopener">Announcement ↗</a></p>`
        : (t.source_video_id ? `<p><a href="${yt(t.source_video_id)}" target="_blank" rel="noopener">Source video ↗</a></p>` : "")}
    </div>`).join("");
  view.innerHTML = html;
}

// ── Obsidian-style knowledge graph (lives in the Dev Construction tab) ────────
// Force-directed canvas graph of the WHOLE project, mirroring the Obsidian vault:
// skills/tools/prompts/connectors → category & tool hubs → Home. Reads data/brain_graph.json
// (built by src/build_graph.py). Pan = drag background, zoom = wheel, drag a node to move it,
// hover to focus its neighbours, click a node to open its source. Pure canvas, no libraries.
const GRAPH_COLORS = {
  home: "#d4a72c", hub: "#d4a72c", category: "#38bdf8", toolhub: "#a78bfa",
  skill: "#34d399", tool: "#f472b6", prompt: "#fbbf24", connector: "#60a5fa",
  star: "#f5c542", combo: "#fb923c",      // gold anchors ("don't change") + orange combinations
  // OWNER LAYER (owner 2026-07-13: the graph must hold his Q&A/problems/history, not just elements)
  "owner-hub": "#e11d48", "you-said": "#f87171", "excava-asked": "#c084fc",
  "you-answered": "#4ade80", "problem-fixed": "#fbbf24",
};
function ensureGraphCss() {
  if (document.getElementById("graphcss")) return;
  const st = document.createElement("style");
  st.id = "graphcss";
  st.textContent = `
    .braingraph{position:relative}
    .braincanvas{width:100%;height:600px;display:block;border-radius:14px;
      background:#000;cursor:grab;touch-action:none;
      border:1px solid rgba(255,255,255,.10);
      box-shadow:0 18px 50px rgba(0,0,0,.55), inset 0 1px 0 rgba(255,255,255,.05)}
    .graphbar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:10px;
      font-size:12px;color:var(--muted,#94a3b8)}
    .graphcount{font-weight:700;letter-spacing:.01em}
    .graphlegend{display:flex;align-items:center;gap:11px;flex-wrap:wrap;margin-left:auto}
    .graphlegend i{display:inline-block;width:9px;height:9px;border-radius:50%;
      margin-right:4px;vertical-align:middle;box-shadow:0 0 6px currentColor}
    .graphsearch,.graphreset{background:#0b0e17;border:1px solid rgba(255,255,255,.16);
      border-radius:7px;color:#e5e7eb;padding:4px 9px;font-size:12px}
    .graphsearch::placeholder{color:#64748b}
    .graphreset{cursor:pointer;transition:border-color .15s,background .15s}
    .graphreset:hover{border-color:rgba(255,255,255,.4);background:#11151f}
    .graphhint{font-size:11px;color:var(--muted,#94a3b8);margin:7px 0 0;opacity:.75}
    .graphsel{display:flex;align-items:center;gap:9px;flex-wrap:wrap;margin:0 0 8px;font-size:12.5px;
      border:2px solid var(--line,#333);border-radius:9px 12px 8px 11px;padding:6px 11px;
      background:var(--gold-soft,#fdf3d0);box-shadow:2px 2px 0 rgba(0,0,0,.25)}
    .graphsel a{font-weight:700;text-decoration:none;border:1.5px solid var(--line,#333);border-radius:7px;
      padding:2px 8px;background:#fff;color:#374151}
    .graphsel a:hover{border-color:var(--gold-line,#d4a900);color:var(--gold-ink,#7a5c00)}`;
  document.head.appendChild(st);
}
function legendItem(color, label) { return `<span><i style="background:${color};color:${color}"></i>${label}</span>`; }
async function mountBrainGraph(host, file = "brain_graph.json", legend = null) {
  ensureGraphCss();
  const data = await load(file);
  if (!data || !(data.nodes || []).length)
    return host.innerHTML = empty("Graph not generated yet — built in the pipeline.");
  const c = data.counts || {};
  const defaultLegend =
    legendItem(GRAPH_COLORS.skill, "skill") + legendItem(GRAPH_COLORS.tool, "tool") +
    legendItem(GRAPH_COLORS.prompt, "prompt") + legendItem(GRAPH_COLORS.connector, "connector") +
    legendItem(GRAPH_COLORS.category, "category") + legendItem(GRAPH_COLORS.toolhub, "tool-hub") +
    legendItem(GRAPH_COLORS.star, "★ anchor (doesn't change)") + legendItem(GRAPH_COLORS.combo, "combo (used together)");
  host.innerHTML = `
    <div class="graphbar">
      <span class="graphcount">${c.nodes || data.nodes.length} nodes · ${c.links || (data.links || []).length} links</span>
      <input class="graphsearch" placeholder="highlight…" aria-label="highlight nodes" />
      <button class="graphreset">reset view</button>
      <span class="graphlegend">${legend || defaultLegend}</span>
    </div>
    <canvas class="braincanvas"></canvas>
    <p class="graphhint">drag background to pan · scroll to zoom · drag a dot to move it · hover to focus · click a dot to EXPLORE it (element view, source, or turn its cluster into a 📦 package)</p>`;
  const canvas = host.querySelector("canvas");
  const ctx = canvas.getContext("2d");
  const H = 600;
  canvas.width = canvas.clientWidth || 800;
  canvas.height = H;
  let W = canvas.width;

  const _spread = data.nodes.length > 360 ? 2.2 : 1;     // huge graphs start dispersed, not piled up
  const N = data.nodes.map(n => ({ ...n, x: (Math.random() - .5) * W * _spread, y: (Math.random() - .5) * H * _spread, vx: 0, vy: 0, deg: 0 }));
  const byId = {}; N.forEach(n => byId[n.id] = n);
  const L = data.links.map(l => ({ s: byId[l.source], t: byId[l.target] })).filter(l => l.s && l.t);
  const nbr = {}; N.forEach(n => nbr[n.id] = new Set());
  L.forEach(l => { l.s.deg++; l.t.deg++; nbr[l.s.id].add(l.t.id); nbr[l.t.id].add(l.s.id); });
  const isHub = n => n.group === "home" || n.group === "category" || n.group === "toolhub" || n.group === "hub" || n.group === "combo" || n.group === "owner-hub";
  const rad = n => n.group === "home" ? 9 : n.group === "star" ? 5.5 : isHub(n) ? 6 + Math.min(4, n.deg / 8) : 3 + Math.min(3, n.deg / 3);
  const charge = n => isHub(n) ? 1500 : (n.group === "star" ? 720 : 560);   // hubs push others away harder
  N.forEach(n => n.q1 = charge(n));

  const big = N.length > 360;                 // huge graphs: spread wider, faint edges, grid physics
  let scale = big ? 0.42 : 0.8, ox = W / 2, oy = H / 2, alpha = 1;
  let hover = null, drag = null, panning = false, lastX = 0, lastY = 0, hl = "";
  let raf = null, running = false;
  // Spatial-hash repulsion: each node only pushes against nodes in nearby cells -> ~O(n) per tick,
  // so a 1000-node constellation stays fast AND actually spreads (no collapse into a white streak).
  const CELL = 150, REACH = CELL * 2;
  function tick() {
    const grid = new Map();
    for (const n of N) {
      n._cx = Math.floor(n.x / CELL); n._cy = Math.floor(n.y / CELL);
      const k = n._cx + ":" + n._cy; let c = grid.get(k); if (!c) { c = []; grid.set(k, c); } c.push(n);
    }
    for (const a of N) {
      for (let gx = a._cx - 1; gx <= a._cx + 1; gx++)
        for (let gy = a._cy - 1; gy <= a._cy + 1; gy++) {
          const cell = grid.get(gx + ":" + gy); if (!cell) continue;
          for (const b of cell) {
            if (b === a) continue;
            let dx = a.x - b.x, dy = a.y - b.y, d2 = dx * dx + dy * dy + .01;
            if (d2 < REACH * REACH) {                 // apply to a only; b gets its turn -> symmetric
              const d = Math.sqrt(d2), f = (a.q1 + b.q1) / d2 / 2; dx /= d; dy /= d;
              a.vx += dx * f; a.vy += dy * f;
            }
          }
        }
    }
    for (const l of L) { let dx = l.t.x - l.s.x, dy = l.t.y - l.s.y, d = Math.sqrt(dx * dx + dy * dy) + .01;
      const f = (d - 78) * .017; dx /= d; dy /= d;
      l.s.vx += dx * f; l.s.vy += dy * f; l.t.vx -= dx * f; l.t.vy -= dy * f; }
    const ctr = big ? .0008 : .0016;            // weak centering on big graphs so it spreads out wide
    for (const n of N) { n.vx += -n.x * ctr; n.vy += -n.y * ctr;
      if (n === drag) continue;
      n.x += n.vx * alpha; n.y += n.vy * alpha; n.vx *= .85; n.vy *= .85; }
    alpha *= .986;
  }
  function draw() {
    ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.clearRect(0, 0, W, H);
    ctx.setTransform(scale, 0, 0, scale, ox, oy);
    const focus = hover ? nbr[hover.id] : null;
    const settled = !running;                          // glow only when not animating (perf-safe)
    // edges — WHITE on black; highlighted neighbours brighten, the rest recede. On big graphs the
    // base opacity is very low so ~1200 lines read as a faint web, not a solid white blob.
    const baseFade = big ? .05 : .12, dimFade = big ? .02 : .045;
    for (const l of L) {
      const on = hover && (l.s === hover || l.t === hover);
      const fade = (hl || (hover && !on)) ? dimFade : baseFade;
      ctx.strokeStyle = on ? "rgba(255,255,255,.95)" : `rgba(255,255,255,${fade})`;
      ctx.lineWidth = (on ? 1.5 : .6) / scale;
      ctx.beginPath(); ctx.moveTo(l.s.x, l.s.y); ctx.lineTo(l.t.x, l.t.y); ctx.stroke();
    }
    ctx.font = (11 / scale) + "px ui-sans-serif, system-ui";
    for (const n of N) {
      const dim = (hover && n !== hover && !focus.has(n.id)) ||
                  (hl && !(n.label || "").toLowerCase().includes(hl));
      ctx.globalAlpha = dim ? .12 : 1;
      const col = GRAPH_COLORS[n.group] || "#94a3b8";
      ctx.fillStyle = col;
      // soft glow on the anchors (hubs), stars + the hovered node = premium "constellation" feel
      if (settled && !dim && (isHub(n) || n.group === "star" || n === hover)) {
        ctx.shadowColor = col; ctx.shadowBlur = isHub(n) ? 16 : (n.group === "star" ? 13 : 11); }
      if (n.group === "star") {                          // gold 5-point star = an anchor that doesn't change
        const R = rad(n) + 2.5 / scale, r = R * .46; ctx.beginPath();
        for (let k = 0; k < 10; k++) { const ang = -Math.PI / 2 + k * Math.PI / 5, rr = k % 2 ? r : R;
          ctx[k ? "lineTo" : "moveTo"](n.x + Math.cos(ang) * rr, n.y + Math.sin(ang) * rr); }
        ctx.closePath(); ctx.fill();
      } else {
        ctx.beginPath(); ctx.arc(n.x, n.y, rad(n), 0, 7); ctx.fill();
        if (n.group === "combo") { ctx.lineWidth = 1.4 / scale; ctx.strokeStyle = col; ctx.globalAlpha *= .8;
          ctx.beginPath(); ctx.arc(n.x, n.y, rad(n) + 3 / scale, 0, 7); ctx.stroke(); ctx.globalAlpha = dim ? .12 : 1; }
      }
      ctx.shadowBlur = 0;
      if (n === hover) { ctx.lineWidth = 2 / scale; ctx.strokeStyle = "#fff"; ctx.stroke(); }
      if (!dim && (isHub(n) || n === hover || scale > 1.6 || hl)) {
        ctx.globalAlpha = 1; ctx.fillStyle = isHub(n) ? "#ffffff" : "#cbd5e1";
        ctx.fillText(n.label, n.x + rad(n) + 2 / scale, n.y + 3.5 / scale);
      }
    }
    ctx.globalAlpha = 1; ctx.shadowBlur = 0;
    // depth vignette (screen space) — black at the rim so the graph reads as a lit core
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    const vg = ctx.createRadialGradient(W / 2, H / 2, Math.min(W, H) * 0.28, W / 2, H / 2, Math.max(W, H) * 0.72);
    vg.addColorStop(0, "rgba(0,0,0,0)"); vg.addColorStop(1, "rgba(0,0,0,0.5)");
    ctx.fillStyle = vg; ctx.fillRect(0, 0, W, H);
  }
  function loop() {
    tick(); draw();
    if (alpha > .02 && running) raf = requestAnimationFrame(loop);
    else { running = false; raf = null; }
  }
  function start() { if (!running) { running = true; raf = requestAnimationFrame(loop); } }
  function reheat(a) { alpha = Math.max(alpha, a || .3); start(); }
  const _prevStop = window.__graphStop;   // chain so multiple graphs (knowledge + pipeline) all stop
  window.__graphStop = () => { running = false; if (raf) cancelAnimationFrame(raf); if (_prevStop) _prevStop(); };

  function world(e) { const r = canvas.getBoundingClientRect();
    return { x: (e.clientX - r.left - ox) / scale, y: (e.clientY - r.top - oy) / scale }; }
  function pick(e) { const p = world(e); let best = null, bd = 1e9;
    for (const n of N) { const dx = n.x - p.x, dy = n.y - p.y, d = dx * dx + dy * dy, rr = (rad(n) + 4) ** 2;
      if (d < bd && d < rr) { bd = d; best = n; } } return best; }
  canvas.addEventListener("mousemove", e => {
    if (drag) { const p = world(e); drag.x = p.x; drag.y = p.y; reheat(.3); }
    else if (panning) { ox += e.clientX - lastX; oy += e.clientY - lastY; lastX = e.clientX; lastY = e.clientY; if (!running) draw(); }
    else { const h = pick(e); if (h !== hover) { hover = h; canvas.style.cursor = h ? "pointer" : "grab"; if (!running) draw(); } }
  });
  canvas.addEventListener("mousedown", e => { const n = pick(e);
    if (n) drag = n; else { panning = true; lastX = e.clientX; lastY = e.clientY; canvas.style.cursor = "grabbing"; } });
  window.addEventListener("mouseup", () => { drag = null; panning = false; canvas.style.cursor = "grab"; });
  // M3.9: click = EXPLORE — a panel for the node's cluster; the cluster can become a PACKAGE
  const selBar = document.createElement("div");
  selBar.className = "graphsel"; selBar.style.display = "none";
  host.querySelector(".graphbar").insertAdjacentElement("afterend", selBar);
  async function selectNode(n) {
    const neigh = [...(nbr[n.id] || [])].slice(0, 12).map(id => String((byId[id] || {}).label || id));
    const name = String(n.label || n.id);
    let elLink = "";
    try {
      const ix = await eidx();
      for (const t of ["skill", "tool", "prompt", "connector", "model"]) {
        const el = ix.byKey[t + "|" + name.toLowerCase()];
        if (el) { elLink = `<a href="#element/${encodeURIComponent(el.id)}">🔍 explore element</a>`; break; }
      }
    } catch (_) {}
    const members = [name, ...neigh].slice(0, 10);
    selBar.style.display = "";
    selBar.innerHTML = `<b>${esc(name)}</b> <span class="pill">${esc(n.group || "node")}</span>
      <span>· ${neigh.length} linked</span> ${elLink}
      ${n.url ? `<a target="_blank" href="${esc(n.url)}">↗ source</a>` : ""}
      <a target="_blank" href="${_exIssue('EXCAVA: package "' + name + ' kit"',
        "Assemble a PACKAGE from this brain-graph cluster (M3.9):\n- " + members.join("\n- "))}"
        title="Sends the cluster to EXCAVA as a package order — a room assembles it (M2.6)">📦 make this cluster a package (${members.length})</a>`;
  }
  canvas.addEventListener("click", e => { const n = pick(e); if (n) selectNode(n); });
  canvas.addEventListener("wheel", e => { e.preventDefault();
    const r = canvas.getBoundingClientRect(), mx = e.clientX - r.left, my = e.clientY - r.top;
    const wx = (mx - ox) / scale, wy = (my - oy) / scale;
    scale = Math.max(.2, Math.min(4, scale * (e.deltaY < 0 ? 1.1 : .9)));
    ox = mx - wx * scale; oy = my - wy * scale; if (!running) draw(); }, { passive: false });
  host.querySelector(".graphsearch").addEventListener("input", e => { hl = e.target.value.toLowerCase().trim(); if (!running) draw(); });
  host.querySelector(".graphreset").addEventListener("click", () => { scale = .8; ox = W / 2; oy = H / 2; reheat(1); });
  start();
}

// ── Tab: Developer Construction (rebuild spec + the live knowledge graph) ─────
// ── Live Pipeline monitor — proof that retrieval + analysis is actually running ──
// Reads data/pipeline_status.json (regenerated every workflow). Each lane's heartbeat
// comes from the git commit history, so a green row = that lane really committed recently.
function _ageAgo(h) {
  if (h == null) return "never";
  if (h < 1) return "&lt;1h ago";
  if (h < 48) return `${Math.round(h)}h ago`;
  return `${Math.round(h / 24)}d ago`;
}
const PIPE_REFRESH_MS = 180000;   // auto re-pull the live data every 3 minutes
function _movedLine(p) {
  const d = (p && (p.deltas_24h || p.deltas_since_last)) || {};
  const order = ["tools", "skills", "videos_analyzed", "videos_with_transcript", "models", "connectors", "prompts", "commands"];
  const moved = order.filter(k => d[k] > 0).map(k => `+${d[k]} ${k.replace("videos_analyzed", "analyzed").replace("videos_with_transcript", "transcripts")}`);
  return moved.length ? moved.join(" · ") : "no new items in the last 24h (lanes may be between runs)";
}
// Push fresh numbers into the panel in place — so the percentages climb without a full re-render.
function applyPipeNumbers(p) {
  const snap = (p && p.snapshot) || {};
  const tot = snap.videos_total || 0;
  const anz = snap.videos_analyzed != null ? snap.videos_analyzed : (snap.videos_with_transcript || 0);
  const ag = tot ? (100 * anz / tot).toFixed(2) : "0.00";
  const tg = tot ? (100 * (snap.videos_with_transcript || 0) / tot).toFixed(2) : "0.00";
  const set = (id, v) => { const e = document.getElementById(id); if (e) e.textContent = v; };
  const wid = (id, v) => { const e = document.getElementById(id); if (e) e.style.width = v + "%"; };
  set("pl-anz", anz); set("pl-anzpct", ag); wid("pl-anzbar", ag);
  set("pl-tx", snap.videos_with_transcript || 0); set("pl-txpct", tg); wid("pl-txbar", tg);
  set("pl-since-line", _movedLine(p)); set("pl-snap-at", fmtDate(p.generated_at));
  set("pl-lib", `${snap.skills || 0} skills · ${snap.tools || 0} tools · ${snap.models || 0} models · ${snap.connectors || 0} connectors · ${snap.prompts || 0} prompts`);
}
// Live per-lane countdowns, an online/offline sign, and a 3-minute auto-refresh of the numbers.
function mountPipelineTimers() {
  if (window.__pipeTimer) clearInterval(window.__pipeTimer);
  window.__pipeNextRefresh = Date.now() + PIPE_REFRESH_MS;
  let refreshing = false;
  const doRefresh = async () => {
    if (refreshing) return; refreshing = true;
    try { const fresh = await load("pipeline_status.json"); if (fresh) applyPipeNumbers(fresh); } catch (e) {}
    window.__pipeNextRefresh = Date.now() + PIPE_REFRESH_MS; refreshing = false;
  };
  const tick = () => {
    const net = document.getElementById("pl-net");
    if (!net) { clearInterval(window.__pipeTimer); window.__pipeTimer = null; return; }
    const online = navigator.onLine;
    net.className = "pl-net " + (online ? "pl-on" : "pl-off");
    net.innerHTML = online ? '<span class="pl-netdot"></span>ONLINE · live'
                           : '<span class="pl-netdot"></span>OFFLINE · showing last saved data';
    const rf = document.getElementById("pl-refresh");
    if (rf) {
      let ms = window.__pipeNextRefresh - Date.now();
      if (ms <= 0) { rf.textContent = "refreshing…"; if (online) doRefresh(); }
      else { const m = Math.floor(ms / 6e4), s = Math.floor(ms / 1e3) % 60;
        rf.textContent = `auto-refresh in ${m}:${String(s).padStart(2, "0")}`; }
    }
    document.querySelectorAll(".pl-next[data-next]").forEach(el => {
      const next = Number(el.dataset.next);
      if (!next) { el.textContent = "next: unknown"; return; }
      let ms = next - Date.now();
      if (ms <= 0) { el.textContent = "due now"; el.classList.add("pl-due"); return; }
      el.classList.remove("pl-due");
      const h = Math.floor(ms / 3.6e6), m = Math.floor(ms / 6e4) % 60, s = Math.floor(ms / 1e3) % 60;
      el.textContent = h > 0 ? `next in ${h}h ${m}m` : `next in ${m}m ${s}s`;
    });
  };
  tick(); window.__pipeTimer = setInterval(tick, 1000);
  window.addEventListener("online", tick); window.addEventListener("offline", tick);
}
// North Star — the 6 main goals + live conformance. Shown atop self-improvement.
async function goalsPanel() {
  const g = await load("goals_status.json");
  if (!g || !(g.goals || []).length) return "";
  const rows = g.goals.map(o => {
    const sev = o.status === "met" ? "sev-low" : o.status === "at-risk" ? "sev-medium" : "sev-high";
    return `<div class="prio-row"><span class="prio-rank ${sev}">${o.id}</span>
      <div class="prio-main"><b>${esc(o.name)}</b> <span class="pl-runs">${o.score}/100 · ${esc(o.status)}</span>
        <span class="pl-what">${esc(o.gap)}</span></div></div>`;
  }).join("");
  return `<div class="card improve-clock"><h3>🌟 North Star — main goals (above all else)
      <span class="pl-badge ${g.overall >= 75 ? "pl-live" : g.overall >= 45 ? "pl-slow" : "pl-stale"}">${g.overall}/100</span></h3>
    <p class="sub">Every cycle the system scores itself against these 6 goals and queues a fix for any that aren't met. Concepts, not features.</p>
    <div class="prio-rows">${rows}</div></div>`;
}
// Top priorities right now — auto-ranked from the live state, shown atop the key tabs.
async function prioritiesPanel() {
  const p = await load("priorities.json");
  if (!p || !(p.priorities || []).length) return "";
  const rows = p.priorities.slice(0, 6).map(x => {
    const sev = x.impact >= 85 ? "sev-high" : x.impact >= 55 ? "sev-medium" : "sev-low";
    return `<div class="prio-row"><span class="prio-rank ${sev}">${x.rank}</span>
      <div class="prio-main"><b>${esc(x.title)}</b><span class="pl-what">${esc(x.detail)}</span></div>
      <span class="prio-area">${esc(x.area)}</span></div>`;
  }).join("");
  return `<div class="card improve-clock"><h3>🎯 Top priorities right now</h3>
    <p class="sub">Auto-ranked by impact from the live system state — it re-orders itself as things change (links resolved, a lane stalls, a regression appears).</p>
    <div class="prio-rows">${rows}</div></div>`;
}
async function pipelinePanel() {
  const p = await load("pipeline_status.json");
  if (!p || !p.lanes) return "";
  const cov = await load("coverage_log.json"), cl = (cov && cov.latest) || {};
  const cpct = cl.pct != null ? cl.pct : 0, cdelta = cov ? cov.delta_pct_vs_prev_day : null;
  const OV = { live: ["pl-live", "● LIVE — data is flowing"], slow: ["pl-slow", "● SLOWING — some lanes overdue"],
               stale: ["pl-stale", "● STALLED — lanes not running"] };
  const ov = OV[p.overall] || OV.stale;
  const snap = p.snapshot || {};
  const tot = snap.videos_total || 0;
  const anz = snap.videos_analyzed != null ? snap.videos_analyzed : (snap.videos_with_transcript || 0);
  const ag = tot ? (100 * anz / tot).toFixed(2) : "0.00";       // the number that CLIMBS as we analyze
  const tg = tot ? (100 * (snap.videos_with_transcript || 0) / tot).toFixed(2) : "0.00";
  let rows = p.lanes.map(L => {
    const next = L.last_run ? (new Date(L.last_run).getTime() + (L.cadence_h || 12) * 3.6e6) : 0;
    return `
    <div class="pl-row">
      <span class="pl-dot pl-${L.status}" title="${esc(L.status)}"></span>
      <div class="pl-main"><b>${esc(L.label)}</b><span class="pl-what">${esc(L.what)}</span></div>
      <div class="pl-meta"><span class="pl-age">ran ${_ageAgo(L.age_hours)}</span>
        <span class="pl-next" data-next="${next}">next…</span>
        <span class="pl-runs">${L.runs_7d}× / 7d · every ~${L.cadence_h}h</span></div>
    </div>`;
  }).join("");
  return `<div class="card pipe-panel">
      <div class="pipe-head"><h3>📡 Live Pipeline</h3><span class="pl-badge ${ov[0]}">${ov[1]}</span>
        <span id="pl-net" class="pl-net pl-on"><span class="pl-netdot"></span>…</span>
        <span id="pl-refresh" class="pl-refresh">auto-refresh…</span></div>
      <p class="sub">Is retrieval &amp; analysis actually running? Each lane shows its real last-commit time and a live countdown to its next run; the numbers auto-refresh every 3 minutes (no manual reload), and work offline from the last saved snapshot.</p>
      <div class="pl-since"><b>Retrieved in the last 24h:</b> <span id="pl-since-line">${esc(_movedLine(p))}</span><br>
        <span class="sub">snapshot from <span id="pl-snap-at">${esc(fmtDate(p.generated_at))}</span> · library: <span id="pl-lib">${snap.skills || 0} skills · ${snap.tools || 0} tools · ${snap.models || 0} models · ${snap.connectors || 0} connectors · ${snap.prompts || 0} prompts</span></span></div>
      <div class="pl-prog"><span><b>Analyzed</b> <span id="pl-anz">${anz}</span> / ${tot} (<span id="pl-anzpct">${ag}</span>%) <span class="sub">— transcript OR Gemini-watched; this climbs as work happens</span></span><span class="pl-bar"><i id="pl-anzbar" style="width:${ag}%"></i></span></div>
      <div class="pl-prog pl-prog2"><span>Transcripts <span id="pl-tx">${snap.videos_with_transcript || 0}</span> / ${tot} (<span id="pl-txpct">${tg}</span>%) <span class="sub">— captions only (rate-limited)</span></span><span class="pl-bar"><i id="pl-txbar" style="width:${tg}%"></i></span></div>
      <div class="pl-prog pl-prog2"><span><b>Links</b> ${cl.linked || 0} / ${cl.total || 0} (${cpct}%) <span class="sub">— real, working links${cdelta != null ? ` · ${cdelta >= 0 ? "+" : ""}${cdelta}%/day (target +5%)` : ""}</span></span><span class="pl-bar"><i style="width:${cpct}%"></i></span></div>
      <div class="pl-rows">${rows}</div>
    </div>`;
}

async function scoutPanel() {
  const s = await load("pipeline_scout.json");
  if (!s || !(s.processes || []).length) return "";
  const rows = s.processes.map(r => `<div class="prio-row">
      <span class="prio-rank sev-low">${r.count}</span>
      <div class="prio-main"><b>${esc(r.process)}</b><span class="pl-what">top free pick: ${r.recommended ? esc(r.recommended) : "—"}</span></div>
      <span class="prio-area">${esc(r.goal)}</span></div>`).join("");
  return `<div class="card"><h3>🔭 Pipeline scout <span class="sub">— ${esc(s.total_candidates || 0)} catalogue tools that could improve the system</span></h3>
    <p class="sub">Scans every catalogue type across 12 pipeline processes, ranks by quality, and queues the best into self-improvement. <b>Proposals — approve to integrate</b> (some matches are tangential; pick the genuinely free + useful ones).</p>
    <div class="prio-rows">${rows}</div></div>`;
}
async function excavaPanel() {
  const e = await load("excava_status.json");
  if (!e || !e.gate) return "";
  const g = e.gate;
  const stack = (e.tool_stack || []).map(t =>
    `<div class="prio-row"><span class="prio-area">${esc(t.status)}</span>
      <div class="prio-main"><b>${esc(t.role)}</b><span class="pl-what">${esc(t.tool)}</span></div></div>`).join("");
  return `<div class="card improve-clock"><h3>🛰 EXCAVA — the agentic OS
      <span class="pl-badge ${g.internal_allowed ? "pl-live" : "pl-stale"}">internal ${g.internal_allowed ? "OPEN" : "CLOSED"}</span>
      <span class="pl-badge ${g.outward_allowed ? "pl-live" : "pl-slow"}">outward ${g.outward_allowed ? "OPEN" : "CLOSED"}</span></h3>
    <p class="sub">${esc(e.phase || "")}. Verification gate (focused checkers) must be green before it acts; outward create/publish also needs G3≥70 + your approval — so it never acts on bad data.</p>
    <div class="pl-since"><b>Next action:</b> ${esc((e.next_action || {}).do || "—")} <span class="sub">(${esc((e.next_action || {}).type || "")})</span><br>
      <span class="sub">gate: data ${g.checks.data_guard_ok ? "ok" : "BAD"} · security ${g.checks.security_clean ? "clean" : "LEAK"} · truth/access G3 ${esc(g.checks.truth_access_G3)}/100 · holding ${(e.holding || []).length} outward action(s)</span></div>
    <details><summary class="sub" style="cursor:pointer">Tool stack (${(e.tool_stack || []).length})</summary><div class="prio-rows">${stack}</div>
      <p class="hint">${esc((e.stack_review || {}).note || "")}</p></details></div>`;
}
async function renderDevConstruction() {
  const data = await load("dev_construction.json");
  const secs = (data && data.sections) || [];
  let html = `<div class="sub">${esc((data && data.intro) || "")}</div>`;
  html += await excavaPanel();
  html += await prioritiesPanel();
  html += await pipelinePanel();
  html += await scoutPanel();
  html += `<div class="card">
      <h3>🧠 Brain 1 — knowledge graph (what the project KNOWS)</h3>
      <p class="sub">The best skills, tools, prompts and connectors clustered by category and tool (the full set lives in the tabs). Gold ★ = anchor skills that don't change; orange rings = combinations used together in the same video.</p>
      <p class="hint">Want the WHOLE brain (3,000+ nodes)? Download <a href="../data/brain.graphml">brain.graphml</a> and open it in <b>Graphify</b> / Gephi / Neo4j, or read the <a href="../docs/BIGGER_BRAIN.md">Obsidian + Graphify guide</a>.</p>
      <div id="braingraph" class="braingraph"></div>
    </div>`;
  html += `<div class="card">
      <h3>🛠 Brain 2 — system orchestration (how the project WORKS)</h3>
      <p class="sub">Every internal system/protocol and what depends on what. The big gold node, <b>data/ hub</b>, is the main one everything feeds and reads from (like an n8n flow). Nodes are tinted by which of the 5 goals they serve.</p>
      <div id="pipegraph" class="braingraph"></div>
    </div>`;
  let list = secs;
  if (q()) list = list.filter(s => hit(s.title, s.body));
  html += list.map(s => `
    <div class="card devsec">
      <h3>${esc(s.title)}</h3>
      <div class="devbody">${esc(s.body)}</div>
    </div>`).join("");
  if (!secs.length) html += empty("Developer construction doc not generated yet.");
  else if (!list.length) html += empty(`No sections match "${esc(state.query)}".`);
  view.innerHTML = html;
  mountPipelineTimers();
  const gh = document.getElementById("braingraph");
  if (gh) mountBrainGraph(gh);
  const pg = document.getElementById("pipegraph");
  if (pg) {
    const pipeLegend =
      legendItem(GRAPH_COLORS.home, "the hub (main)") + legendItem(GRAPH_COLORS.connector, "source") +
      legendItem(GRAPH_COLORS.tool, "transcripts") + legendItem(GRAPH_COLORS.skill, "analysis") +
      legendItem(GRAPH_COLORS.toolhub, "quality/self-improve") + legendItem(GRAPH_COLORS.category, "output");
    mountBrainGraph(pg, "pipeline_graph.json", pipeLegend);
  }
}

// ── Tab: Effectiveness — how good & how rigid each retrieval/analysis lane is ──
// Measured scoreboard (data/effectiveness.json) that the self-improvement system targets.
const DIM_LABEL = { quality: "Quality", quantity: "Quantity", form: "Form", time: "Time",
  tokens: "Tokens", ease_external: "Ext.access", ease_project: "Proj.access", ease_user: "User access" };
async function renderEffectiveness() {
  const [d, diet] = await Promise.all([load("effectiveness.json"), load("excava/token_diet.json")]);
  if (!d || !d.lanes) {
    view.innerHTML = `<div class="card"><h3>Extraction Effectiveness</h3>${empty(
      "Scoreboard not generated yet — it runs every analysis cycle (~3h).")}</div>`;
    return;
  }
  const dims = d.dimensions || [];
  let html = await prioritiesPanel();
  // TOKEN DIET — owner 2026-07-12: "you say it's happening but I can't verify it — show me in a tab"
  if (diet && diet.per_day) {
    const rows = diet.per_day.map(x =>
      `<tr><td>${esc(x.day)}</td><td>${esc(x.turns)}</td><td><b>~${esc(x.approx_tokens_per_turn)}</b></td></tr>`).join("");
    const caps = Object.entries(diet.hard_caps || {}).map(([k, v]) =>
      `<span class="pill" title="${esc(k)}">${esc(k.replace(/_/g, " "))}: <b>${esc(v)}</b></span>`).join(" ");
    html += `<div class="card"><h3>🥗 Token diet <span class="sub">— the saving laws, with numbers you can check (not a claim)</span></h3>
      ${(diet.laws || []).map(l => `<p class="sub">• ${esc(l)}</p>`).join("")}
      <div style="display:flex;flex-wrap:wrap;gap:6px;margin:6px 0">${caps}</div>
      <table class="pv-table"><thead><tr><th>day</th><th>agent turns</th><th>≈ tokens per turn</th></tr></thead>
        <tbody>${rows}</tbody></table>
      <p class="sub">${esc(diet.note || "")} Honest read: turns got LONGER after the plain-language switch (prose beats bash in words) — the new no-filler law is the counterweight; watch this line fall.</p></div>`;
  }
  html += `<div class="card"><h3>Extraction Effectiveness &amp; Rigidity</h3>
    <p class="hint">🎯 ${esc(d.north_star || "")}</p>
    <p class="sub">🌐 <b>Public hub API</b> (for external/future systems): <a href="../data/hub.json">data/hub.json</a> — a CORS-open, machine-readable manifest of every dataset · <a href="../HUB_API.md">HUB_API.md</a></p>
    <p class="sub">Weakest lane: <b>${esc(d.summary.weakest_lane)}</b> (${esc(d.summary.weakest_effectiveness)}/10)
      · transcript coverage ${esc(d.summary.transcript_coverage_pct)}% · library quality ${esc(d.library_quality)}/10
      · generated ${esc(fmtDate(d.generated_at))}</p>
    <p class="sub">Effectiveness = weighted mean of the dimensions (higher better). Rigidity = how brittle/locked-in the lane is (lower better). The self-improvement system focuses on the lowest rows.</p></div>`;
  html += `<div class="card"><div class="efftable-wrap"><table class="efftable">
    <thead><tr><th>Lane</th><th title="Weighted effectiveness">Eff</th><th title="Brittleness (lower=better)">Rigid</th>` +
    dims.map(k => `<th title="${esc(k)}">${esc(DIM_LABEL[k] || k)}</th>`).join("") + `</tr></thead><tbody>`;
  d.lanes.forEach(L => {
    const sev = L.effectiveness >= 8 ? "ok" : (L.effectiveness >= 6.5 ? "warn" : "bad");
    html += `<tr class="eff-${sev}"><td><b>${esc(L.name)}</b><br><span class="sub">${esc(L.engine)} · ${esc(L.kind)}</span></td>
      <td class="effnum">${esc(L.effectiveness)}</td><td class="effnum">${esc(L.rigidity)}</td>` +
      dims.map(k => {
        const v = L.metrics[k];
        return `<td class="${(L.weak_dims || []).includes(k) ? "weak" : ""}">${esc(v)}</td>`;
      }).join("") + `</tr>`;
    html += `<tr class="eff-note"><td colspan="${dims.length + 3}">→ ${esc(L.improve_note)}</td></tr>`;
  });
  html += `</tbody></table></div></div>`;
  view.innerHTML = html;
}

// ── Global fuzzy search — closest match across EVERY tab, even without the exact name ──
function _bigrams(s) { s = (s || "").toLowerCase(); const g = new Set();
  for (let i = 0; i < s.length - 1; i++) g.add(s.slice(i, i + 2)); return g; }
function _sim(a, b) { const A = _bigrams(a), B = _bigrams(b); if (!A.size || !B.size) return 0;
  let inter = 0; A.forEach(x => { if (B.has(x)) inter++; }); return (2 * inter) / (A.size + B.size); }
function _scoreItem(ql, name, blob) {
  const nl = (name || "").toLowerCase(), bl = ((name || "") + " " + (blob || "")).toLowerCase();
  let s = 0;
  if (nl === ql) s += 20; else if (nl.includes(ql)) s += 12;
  if ((blob || "").toLowerCase().includes(ql)) s += 3;
  s += ql.split(/\s+/).filter(w => w.length > 2).reduce((a, w) => a + (bl.includes(w) ? 2 : 0), 0);
  s += _sim(ql, nl) * 6;                       // fuzzy closeness so a near-name still ranks
  return s;
}
async function renderSearchAll() {
  const query = (state.query || "").trim();
  if (!query) return view.innerHTML = empty("Type in the search box and press Enter to search across every tab — closest matches first, even if you don't know the exact name.");
  const [sk, to, mo, co, pr, cm] = await Promise.all([load("skills.json"), load("tools.json"),
    load("models.json"), load("connectors.json"), load("prompts.json"), load("commands.json")]);
  const ql = query.toLowerCase();
  const sets = [
    ["skill", "skills", (sk && sk.skills) || [], x => x.skill_name || x.slug, x => `${x.description || ""} ${x.use_case || ""} ${x.category || ""}`, x => x.source_url],
    ["tool", "tools", (to && to.tools) || [], x => x.name, x => `${x.description || ""} ${x.category || ""} ${x.company || ""}`, x => x.source_url],
    ["model", "tools", (mo && mo.models) || [], x => x.name, x => `${x.description || ""} ${x.category || ""}`, x => x.source_url],
    ["connector", "connectors", (co && co.connectors) || [], x => x.name, x => `${x.what_it_does || ""} ${x.category || ""}`, x => x.url || x.source_url],
    ["prompt", "prompts", (pr && pr.prompts) || [], x => x.title, x => `${x.purpose || ""} ${x.category || ""}`, x => ""],
    ["command", "tips", (cm && cm.commands) || [], x => x.command || x.name, x => x.description || "", x => ""],
  ];
  const tabFor = { skill: "skills", tool: "tools", model: "tools", connector: "connectors", prompt: "prompts", command: "tips" };
  let results = [];
  for (const [type, , arr, nameF, blobF, urlF] of sets)
    for (const x of arr) {
      const name = String(nameF(x) || ""); if (!name) continue;
      const blob = String(blobF(x) || ""); const score = _scoreItem(ql, name, blob);
      if (score > 1.6) results.push({ type, name, blob: blob.slice(0, 170), score, url: urlF(x) || "" });
    }
  results.sort((a, b) => b.score - a.score); results = results.slice(0, 40);
  let html = `<div class="cadence-line">&#8226; <b>Search:</b> closest matches across every tab for &ldquo;${esc(query)}&rdquo; (${results.length})</div>`;
  if (!results.length) html += empty(`Nothing close to "${esc(query)}" yet — try fewer / different words.`);
  html += results.map(r => `<div class="card srch">
    <h3><span class="pill">${esc(r.type)}</span> ${esc(r.name)}
      <span class="sub" style="font-weight:400">&rarr; <a href="#" data-goto="${esc(tabFor[r.type])}">open ${esc(tabFor[r.type])} tab</a></span></h3>
    ${r.blob ? `<p>${esc(r.blob)}</p>` : ""}
    ${r.url ? `<p class="sourceline"><a href="${esc(r.url)}" target="_blank" rel="noopener">source</a></p>` : ""}
  </div>`).join("");
  view.innerHTML = html;
  view.querySelectorAll("[data-goto]").forEach(a => a.addEventListener("click", e => {
    e.preventDefault(); show(a.dataset.goto);
  }));
}

// ── EXCAVA: the OS you can SEE working (cockpit home + a live presence strip on every tab) ──
// The GitHub-issue channel (Phase 1 "you drive it"): the static page can't write to the repo,
// so drive actions open a PREFILLED issue titled "EXCAVA: …" — CI applies it, replies a
// receipt, closes the issue. Works from the phone.
const GH_REPO = "https://github.com/Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor";
const GH_PAGES = "https://eitanvinokur12345.github.io/AI-YouTube-Playlist-Information-Extractor/docs";
const _exIssue = (title, body = "") =>
  `${GH_REPO}/issues/new?title=${encodeURIComponent(title)}&body=${encodeURIComponent(body)}`;
// ── IN-APP viewer (owner's #1 ask: open/read things IN the app, not on GitHub) ──
function _showModal(title, html) {
  let m = document.getElementById("ex-modal");
  if (!m) {
    m = document.createElement("div"); m.id = "ex-modal"; m.className = "ex-modal";
    document.body.appendChild(m);
    m.addEventListener("click", e => { if (e.target === m) m.style.display = "none"; });
  }
  m.innerHTML = `<div class="ex-modal-box"><div class="ex-modal-head"><b>${esc(title)}</b>
    <button class="ex-modal-x" aria-label="close">✕</button></div><div class="ex-modal-body">${html}</div></div>`;
  m.querySelector(".ex-modal-x").addEventListener("click", () => { m.style.display = "none"; });
  m.style.display = "flex";
}
async function _openArtifact(ref, title) {
  _showModal(title || "Artifact", `<p class="sub">loading…</p>`);
  let txt = "";
  try { txt = await (await fetch("../" + ref, { cache: "no-store" })).text(); } catch (e) {}
  let shown = txt, note = "";
  if (txt && /\.json$/.test(ref)) {                       // pretty-print JSON so it's readable, not a blob
    try { shown = JSON.stringify(JSON.parse(txt), null, 2); } catch (_) {}
  }
  const CAP = 60000;                                      // don't dump multi-MB files into the modal
  if (shown.length > CAP) {
    note = ` <b>(showing the first ${Math.round(CAP / 1000)}KB of ${Math.round(shown.length / 1000)}KB)</b>`;
    shown = shown.slice(0, CAP) + "\n… (truncated — use the GitHub link for the whole file)";
  }
  const body = txt
    ? `<pre class="ex-artifact">${esc(shown)}</pre><p class="sub">file: <code>${esc(ref)}</code>${note} · <a target="_blank" data-ex-raw="1" href="${GH_REPO}/blob/main/${esc(ref)}">full file on GitHub ↗</a></p>`
    : `<p class="sub">Couldn't load it in-app — <a target="_blank" data-ex-raw="1" href="${GH_REPO}/blob/main/${esc(ref)}">open on GitHub ↗</a></p>`;
  _showModal(title || ref.split("/").pop(), body);
}
// The in-app "send a task to EXCAVA" confirm — used by the console AND every dispatch button.
// YOU ↔ EXCAVA (owner 2026-07-13: 'communicate and write directly to EXCAVA, independently of you').
// Your sent messages (this device) + EXCAVA's inbox items and their status, as one visible two-way
// thread — so you can SEE that you drive it directly and it acts. (True one-click without the GitHub
// step needs a tiny always-on receiver — that rides on the VPS, R1.)
function _commsThread(inbox) {
  let mine = [];
  try { mine = JSON.parse(localStorage.getItem("excavatortron.mytasks") || "[]"); } catch (_) {}
  const inboxT = (inbox && inbox.tasks) || [];
  const rows = [
    ...mine.map(m => ({ who: "you", text: m.task, at: m.at, status: "sent from this device" })),
    ...inboxT.map(t => ({ who: "excava", text: t.task, at: t.added_at, status: t.status || "queued" })),
  ].sort((a, b) => String(b.at || "").localeCompare(String(a.at || ""))).slice(0, 14);
  const bubble = r => `<div class="msg ${r.who === "you" ? "lead" : ""}" style="justify-content:${r.who === "you" ? "flex-end" : "flex-start"}">
    <div class="bub" style="max-width:80%"><div class="who">${r.who === "you" ? "🧑 you" : "🦾 EXCAVA"} <span class="eng">${esc(String(r.at || "").slice(0, 16))} · ${esc(r.status)}</span></div>${esc(r.text || "")}</div></div>`;
  return `<div class="card"><h3>💬 You ↔ EXCAVA <span class="sub">— write to EXCAVA directly (the bar above); here's your thread with it. It acts independently of Claude — CI reads your message, works it, and the status updates here.</span></h3>
    <div class="chat" style="max-height:280px">${rows.length ? rows.map(bubble).join("") : `<p class="sub">No messages yet — type a task or a direction in the bar above and dispatch it. It reaches EXCAVA through the free channel and comes back here with a status.</p>`}</div>
    <p class="sub">Commands EXCAVA understands directly: a plain <b>task</b> · <b>direction &lt;text&gt;</b> · <b>approve/decline &lt;id&gt;</b> · <b>weight &lt;area&gt; &lt;0-100&gt;</b> · <b>kill/safe/run</b> · <b>horse &lt;goal&gt;</b>. One-click-in-app (no GitHub step) arrives with the VPS.</p></div>`;
}
function _sendModal(title, body, decisionId) {
  try { const q = JSON.parse(localStorage.getItem("excavatortron.mytasks") || "[]");
    q.unshift({ task: title, at: new Date().toISOString() });
    localStorage.setItem("excavatortron.mytasks", JSON.stringify(q.slice(0, 40))); } catch (_) {}
  _showModal("Send to EXCAVA", `<p><b>${esc(title)}</b></p>
    <p class="sub"><b>One more click finishes it:</b> the button below opens a pre-filled message — press
    “Submit” there and the cloud beat receives your decision. If you stop here, it stays ONLY on this
    device and EXCAVA never sees it (the truthful chip will keep nagging).</p>
    <div class="el-actions always"><a class="primary" target="_blank" href="${_exIssue(title, body)}" data-ex-raw="1" data-send-click="1">📮 Send to the cloud beat ↗</a>
    <button class="ex-modal-cancel2">keep on this device only</button></div>`);
  const send = document.querySelector('#ex-modal [data-send-click]');
  if (send && decisionId) send.addEventListener("click", () => {
    const d = _localDecisions();                       // mark truthfully: the dispatch was opened
    if (d[decisionId]) { d[decisionId].sent = true;
      try { localStorage.setItem("excavatortron.decisions", JSON.stringify(d)); } catch (_) {}
      if (typeof renderExcava === "function" && state.activeTab === "excava") setTimeout(renderExcava, 600);
    }
  });
  const c = document.querySelector("#ex-modal .ex-modal-cancel2");
  if (c) c.addEventListener("click", () => { document.getElementById("ex-modal").style.display = "none"; });
}
// SWEEP: intercept EVERY GitHub-issue link (current + future) → show the in-app modal instead of
// flinging the owner to GitHub. The only exception is the modal's own explicit "Send to cloud" link.
document.addEventListener("click", e => {
  const a = e.target.closest && e.target.closest('a[href*="/issues/new"]');
  if (a && !a.dataset.exRaw) {
    e.preventDefault();
    try { const u = new URL(a.href);
      _sendModal(u.searchParams.get("title") || "task", u.searchParams.get("body") || ""); }
    catch (_) {}
  }
}, true);
// P2c SWEEP: every repo-FILE link (github.com/...>/blob/main/<path>) opens IN-APP via the
// artifact modal — current links and any future ones. The modal's own "full file on GitHub"
// fallback carries data-ex-raw and stays external (that's the explicit escape hatch).
document.addEventListener("click", e => {
  const a = e.target.closest && e.target.closest('a[href*="/blob/main/"]');
  if (a && !a.dataset.exRaw) {
    e.preventDefault();
    try {
      const ref = decodeURIComponent(new URL(a.href).pathname.split("/blob/main/")[1] || "");
      if (ref) _openArtifact(ref, ref.split("/").pop());
    } catch (_) {}
  }
}, true);
const EX_ICONS = { gemini: "📺", transcript: "📜", analysis: "⚙️", mining: "⛏️", external: "⛏️",
  news: "📰", links: "🔗", memory: "🧠", visual: "🎨", deep: "🔬", improve: "🧬", security: "🛡️",
  watch: "📺", core: "🦾" };
function _exIcon(label) {
  const l = (label || "").toLowerCase();
  if (AGENT_EMOJI[l]) return AGENT_EMOJI[l];   // exact department match first (e.g. visualization vs visual)
  for (const k in EX_ICONS) if (l.includes(k)) return EX_ICONS[k];
  return "🤖";
}
// ── M3.2 MONSTER CAST: one species per department (docs/assets/monsters/, src/make_monsters.py).
// variant: lead (suit) | agent | worker. Falls back to "" so callers keep their emoji fallback.
const MONSTER_DEPTS = ["transcripts", "analysis", "watch", "links", "memory", "mining",
  "visual", "news", "improve", "security", "creators"];
const MONSTER_ALIAS = { transcript: "transcripts", gemini: "watch", external: "mining",
  deep: "analysis", social: "mining", connector: "links", design: "visual" };
function _monsterDept(label) {
  const l = (label || "").toLowerCase();
  for (const d of MONSTER_DEPTS) if (l.includes(d)) return d;
  for (const k in MONSTER_ALIAS) if (l.includes(k)) return MONSTER_ALIAS[k];
  return null;
}
function _monsterImg(label, variant, cls) {
  const d = _monsterDept(label);
  return d ? `<img class="${cls || "m-ava"}" src="assets/monsters/${d}-${variant}.svg" alt="${esc(d)} ${variant}">` : "";
}
// M3.8: an n-pointed star path (each goal-star gets a DISTINCT silhouette)
function _starPath(n, R, r) {
  let p = "";
  for (let i = 0; i < n * 2; i++) {
    const a = Math.PI / n * i - Math.PI / 2, rad = i % 2 ? r : R;
    p += (i ? "L" : "M") + (20 + rad * Math.cos(a)).toFixed(1) + " " + (20 + rad * Math.sin(a)).toFixed(1);
  }
  return p + "Z";
}
// per-tab accent colors — each area of the machine wears its own paint
const TAB_ACCENT = { excava: "oklch(0.85 0.165 95)", skills: "oklch(0.62 0.17 280)", tools: "oklch(0.66 0.18 40)",
  comingsoon: "oklch(0.65 0.16 310)", prompts: "oklch(0.68 0.17 340)", improvement: "oklch(0.62 0.15 150)",
  tips: "oklch(0.7 0.13 200)", news: "oklch(0.6 0.19 25)", connectors: "oklch(0.6 0.15 250)",
  designs: "oklch(0.66 0.19 0)", sources: "oklch(0.62 0.12 170)", devbuild: "oklch(0.55 0.1 260)" };
// which pipeline department serves each tab (so the strip talks about THIS tab's work)
const TAB_DEPT = { skills: "analysis", tools: "analysis", comingsoon: "analysis", prompts: "analysis",
  tips: "analysis", news: "news", connectors: "mining", designs: "visual", sources: "mining",
  improvement: "improve", selfimprove: "improve", effectiveness: "improve", devbuild: "deep" };
async function excavaStrip(tab) {
  const [ex, ps] = await Promise.all([load("excava_status.json"), load("pipeline_status.json")]);
  if (!ex || !ex.gate) return "";
  const g = ex.gate, act = (ex.next_action || {}).do || "idle";
  let dept = "";
  const key = TAB_DEPT[tab];
  if (key && ps && ps.lanes) {
    const lc = l => (l.label || "").toLowerCase();
    const L = ps.lanes.find(l => lc(l).includes(key) && !lc(l).includes("audio+"))
           || ps.lanes.find(l => lc(l).includes(key));
    if (L) dept = `<span>this dept: ${_exIcon(L.label)} ${esc(L.label)} · ${esc(L.status)} · ran ${_ageAgo(L.age_hours)}</span>`;
  }
  const mode = ((ex.os || {}).mode || "run");
  return `<div class="ex-strip"><b>🦾 EXCAVA</b>
    ${mode !== "run" ? `<span class="ex-mode ${esc(mode)}">${esc(mode.toUpperCase())}</span>` : ""}
    <span><span class="ex-lamp ${g.internal_allowed ? "on" : "off"}"></span> internal</span>
    <span><span class="ex-lamp ${g.outward_allowed ? "on" : "off"}"></span> outward</span>
    <span>working: ${esc(String(act).slice(0, 48))}</span>${dept}
    <a data-goto="excava">cockpit →</a></div>`;
}
// ── CREW: virtual residents who live on EVERY tab, wired to the OS. Their speech bubbles are real
// department status (from the same cached JSON the cockpit uses — zero extra network). Click one →
// the cockpit. Kill switch: localStorage.setItem("excavatortron.crew","off").
let _crewTimer = null;
async function renderCrew(tab) {
  let host = document.getElementById("crew");
  if (!host) { host = document.createElement("div"); host.id = "crew"; host.className = "crew"; document.body.appendChild(host); }
  if (localStorage.getItem("excavatortron.crew") === "off") { host.innerHTML = ""; return; }
  const [ps, ex] = await Promise.all([load("pipeline_status.json"), load("excava_status.json")]);
  const lanes = (ps && ps.lanes) || [];
  const lc = l => (l.label || "").toLowerCase();
  const key = TAB_DEPT[tab];
  const dept = key ? (lanes.find(l => lc(l).includes(key) && !lc(l).includes("audio+")) || lanes.find(l => lc(l).includes(key))) : null;
  const live = lanes.filter(l => l.status !== "stale").slice(0, 3);
  const people = [{ c: "var(--gold)", dur: 34,
    say: "🦾 " + String(((ex || {}).next_action || {}).do || "on patrol").slice(0, 46) }];
  if (dept) people.push({ c: TAB_ACCENT[tab] || "var(--gold)", dur: 22,
    say: `${_exIcon(dept.label)} ${dept.label}: ${dept.status === "live" ? "working now" : dept.status === "slow" ? "due to run" : "resting"}` });
  live.forEach((L, i) => {
    if (dept && L.label === dept.label) return;
    people.push({ c: ["oklch(0.75 0.15 200)", "oklch(0.75 0.17 330)", "oklch(0.78 0.17 145)"][i % 3],
      dur: 18 + i * 7, say: _exIcon(L.label) + " " + String(L.what || L.label || "").slice(0, 42) });
  });
  host.innerHTML = people.slice(0, 4).map((p, i) => `
    <div class="crew-p" style="background:${p.c};--x0:${3 + i * 6}%;--x1:${68 + i * 7}%;--dur:${p.dur}s;--delay:${-i * 9}s"
      title="a resident of the OS — click to open the cockpit"><span class="say">${esc(p.say)}</span></div>`).join("");
  host.querySelectorAll(".crew-p").forEach(el => el.addEventListener("click", () => show("excava")));
  if (_crewTimer) clearInterval(_crewTimer);
  let turn = 0;                                     // residents take turns "talking"
  _crewTimer = setInterval(() => {
    const ppl = host.querySelectorAll(".crew-p"); if (!ppl.length) return;
    ppl.forEach(x => x.classList.remove("talk"));
    ppl[turn % ppl.length].classList.add("talk"); turn++;
  }, 6000);
}
async function renderExcava() {
  const [ex, ps, inbox, gs, rc, ap, excfg, reg, dirs, tuts, made, grd, caps, engh, expr, dec, membrain, brains] = await Promise.all([load("excava_status.json"),
    load("pipeline_status.json"), load("excava_inbox.json"), load("goals_status.json"),
    load("resources.json"), load("excava_approvals.json"), load("excava_config.json"),
    load("excava/agents.json"), load("excava_direction.json"), load("tutorials.json"),
    load("created_by_excava.json"), load("guardrails_status.json"), load("excava/capabilities.json"),
    load("excava/engine_health.json"), load("excava/experiments.json"), load("excava/overhaul_decisions.json"),
    load("excava/memory_brain.json"), load("excava/brains.json")]);
  const gate = (ex && ex.gate) || {}, mem = (ex && ex.memory) || {};
  const os = (ex && ex.os) || {};
  const mode = os.mode || (excfg && excfg.mode) || "run";
  const lanes = ((ps && ps.lanes) || []).slice(0, 8);
  const act = (ex && ex.next_action) || {};
  const tasks = (inbox && inbox.tasks) || [];
  const goals = (gs && gs.goals) || [];
  // department stations around the core (percent coords on the floor)
  // M3.3: the isometric ring when floor.js is loaded; the old flat scatter otherwise
  const iso = window.ExcavaFloor || null;
  const POS = iso ? iso.RING : [[16, 22], [50, 14], [84, 22], [10, 62], [90, 62], [25, 86], [50, 90], [75, 86]];
  const stations = lanes.map((L, i) => ({ ...L, x: POS[i % POS.length][0], y: POS[i % POS.length][1] }));
  const stHTML = stations.map((s, i) => {
    const stat = `${s.status === "live" ? "working" : s.status === "slow" ? "due" : "idle"} · ran ${_ageAgo(s.age_hours)}`;
    if (iso) {                                          // M3.3 isometric building + monster at the door
      const dep = _monsterDept(s.label);
      const acc = (dep && iso.ACCENT[dep]) || "var(--gold)";
      return `
    <div class="ex-station iso ${s.status === "stale" ? "stale" : ""}" style="left:${s.x}%;top:${s.y}%">
      ${iso.building(acc, s.status || "stale", i)}
      ${dep ? `<img class="door-m" src="assets/monsters/${dep}-agent.svg" alt="">` : ""}
      <div class="plate"><div class="nm">${esc(s.label || "")}</div><div class="st">${stat}</div></div>
    </div>`;
    }
    return `
    <div class="ex-station ${s.status === "stale" ? "stale" : ""}" style="left:${s.x}%;top:${s.y}%">
      <span class="lamp ${esc(s.status || "stale")}"></span>
      <div class="ic">${_monsterImg(s.label, "agent", "st-m") || _exIcon(s.label)}</div><div class="nm">${esc(s.label || "")}</div>
      <div class="st">${stat}</div>
    </div>`;
  }).join("");
  // worker bots: one per non-stale department, walking core <-> station with a task chip.
  // Each department's crew has its own color — you can tell WHO is doing WHAT at a glance.
  const BOTC = ["oklch(0.85 0.165 95)", "oklch(0.72 0.17 40)", "oklch(0.75 0.15 200)", "oklch(0.75 0.17 330)",
    "oklch(0.78 0.17 145)", "oklch(0.75 0.14 280)", "oklch(0.8 0.15 60)", "oklch(0.82 0.12 170)"];
  const bots = stations.filter(s => s.status !== "stale").map((s, i) => {
    const word = (s.what || s.label || "task").split(" ").slice(0, 2).join(" ");
    const m = _monsterImg(s.label, "worker", "ex-bot-m");
    return `<div class="ex-bot ${m ? "has-m" : ""}" style="background:${m ? "transparent" : BOTC[i % BOTC.length]};--sx:50%;--sy:45%;--ex:${s.x}%;--ey:${s.y}%;--dur:${5.5 + (i % 4) * 1.6}s;--delay:${-i * 1.7}s">
      ${m}<span class="ex-chip">${esc(word)}</span></div>`;
  }).join("");
  const taskHTML = tasks.length ? tasks.map(t => `<div class="ex-task">
      <span class="tk ${t.status === "working" ? "w" : t.status === "held" ? "h" : "q"}">${esc((t.status || "queued").toUpperCase())}</span>
      <span>${esc(t.task || "")}</span></div>`).join("")
    : `<p class="sub">No tasks in the inbox. Use the send box above, tell Claude "EXCAVA: <task>", or edit <code>data/excava_inbox.json</code> — it works the queue on its own, holding anything outward until the gate is green.</p>`;
  // ── OS SPINE (Phase 0-2): the bus board, beat log, drive controls, approval queue ──
  const busPer = (os.bus && os.bus.per_department) || {};
  const deptChips = Object.entries(busPer).map(([d, c]) =>
    `<span class="os-dept">${_exIcon(d)} <b>${esc(d)}</b> ${c.queued || 0}q · ${c.working || 0}w · ${c.done || 0}✓${c.held ? ` · <span style="color:#92400e;font-weight:700">${c.held} held</span>` : ""}</span>`).join("")
    || `<p class="sub">The bus is empty — send a task above.</p>`;
  const logHTML = ((os.beat_log || []).length ? os.beat_log : ["quiet beat — everything waits on the next cron heartbeat"])
    .map(l => `<div>· ${esc(l)}</div>`).join("");
  const lastH = os.bus && os.bus.last_handoff;
  const weights = (excfg && excfg.priority_weights) || {};
  const wBars = Object.entries(weights).sort((a, b) => b[1] - a[1]).map(([k, v]) =>
    `<div class="taste-bar"><span>${esc(k)}</span><i style="width:${v}%"></i><b>${v}</b></div>`).join("");
  const auditOK = !os.audit || os.audit.ok;
  const digest = (os.beat_log || []).filter(l => !String(l).startsWith("quiet")).slice(-2).join(" · ");
  const driveHTML = `
    <div class="card console-hero" style="border-top:3px solid var(--gold)">
      <h2>How can EXCAVA help?</h2>
      <div class="console-bar">
        <button class="cb-ic" id="ex-attach" title="Attach context — adds a body to the task issue">＋</button>
        <input id="ex-send-input" maxlength="240" placeholder="Type a task, a direction, or /nosg /horse /plan /research /watch …">
        <select id="ex-dept" title="Send to a department (or auto-route)">
          <option value="">auto-route</option>
          ${Object.keys((reg && reg.departments) || {}).sort().map(d => `<option value="${esc(d)}">${_exIcon(d)} ${esc(d)}</option>`).join("")}
        </select>
        <button class="cb-ic" id="ex-mic" title="Speak the task">🎙</button>
        <button class="cb-ic" id="ex-send-btn" title="Dispatch" style="background:var(--gold)">➤</button>
      </div>
      <div class="console-hints">
        <span data-hint="/nosg ">NOSG — just do the best thing</span>
        <span data-hint="/horse ">HORSE — 10 executions, merge best</span>
        <span data-hint="/plan ">PLAN — show the plan first</span>
        <span data-hint="/research ">RESEARCH — deep brief</span>
        <span data-hint="/watch ">WATCH — track a topic</span>
        <span data-hint="direction ">🧭 state a direction</span>
      </div>
      ${digest ? `<div class="console-digest">While you were away: ${esc(digest)}</div>` : ""}
      <h3 style="margin-top:18px">🕹 You drive it <span class="sub">— mode + dial</span>
        <span class="ex-mode ${esc(mode)}">${esc(mode.toUpperCase())}</span></h3>
      <p class="sub">The bar dispatches through a prefilled GitHub issue (works on your phone) — CI queues it at <b>owner rank</b>, replies a receipt, closes the issue; /triggers follow P6. Mode, same channel:
        <a target="_blank" href="${_exIssue("EXCAVA: kill")}">🔴 kill</a> ·
        <a target="_blank" href="${_exIssue("EXCAVA: safe")}">🟡 safe</a> ·
        <a target="_blank" href="${_exIssue("EXCAVA: run")}">🟢 run</a> ·
        or <a target="_blank" href="https://github.dev/Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor/blob/main/data/excava_inbox.json">edit the inbox directly</a> · or tell Claude “EXCAVA: &lt;task&gt;”.</p>
      <div class="ex-grid" style="margin-top:10px">
        <div>
          <b class="sub">⚙ OS spine — beat #${os.beats || "?"} · audit ${auditOK ? "✅ code matches the guardrails" : `⚠ ${esc(((os.audit || {}).problems || []).join("; ") || "problems")} — auto SAFE`}</b>
          <div style="margin-top:8px">${deptChips}</div>
          <div class="os-log">${logHTML}</div>
          ${lastH ? `<p class="sub" style="margin-top:6px">last hand-off: <a target="_blank" href="${GH_REPO}/blob/main/${esc(lastH)}">${esc(lastH.split("/").pop())}</a> · <a target="_blank" href="${GH_REPO}/tree/main/data/excava/traces">all traces</a></p>` : ""}
        </div>
        <div>
          <b class="sub">🎚 Priority weights — which auto-work reaches the bus first (your inbox always outranks)</b>
          <div class="taste-bars" style="margin-top:8px">${wBars || "<p class='sub'>defaults active</p>"}</div>
          <p class="sub">change from anywhere: issue “EXCAVA: weight access 95”</p>
        </div>
      </div>
    </div>`;
  const pend = (ap && ap.pending) || [];
  _apprCache = pend.slice();
  const _dec = _localDecisions();
  const waiting = pend.filter(p => !_dec[p.id]);
  const apHTML = `
    <div class="card"><h3>🖊 Approval queue <span class="sub">— the only things waiting on YOU (${waiting.length})</span></h3>
      ${pend.length ? pend.map(p => {
        const d = _dec[p.id];
        // TRUTHFUL chip (owner caught the lie 2026-07-12): a decision is only 'sent' after the
        // cloud-dispatch click; until then it lives ONLY on this device and EXCAVA can't see it.
        const decided = d ? (d.sent
          ? `<span class="qr-btn" style="margin-left:auto;flex:none;pointer-events:none;background:${d.decision === "approve" ? "var(--ok,#1c7)" : "#b44"};color:#fff;border:0">${d.decision === "approve" ? "✓ you approved" : "✕ you declined"} · sent ✓</span>`
          : `<a class="qr-btn" style="margin-left:auto;flex:none;cursor:pointer;background:#c80;color:#fff;border:0" data-open-approval="${esc(p.id)}" title="your decision is saved ONLY on this device — EXCAVA hasn't received it yet; tap to finish sending">${d.decision === "approve" ? "✓ approved" : "✕ declined"} · NOT SENT — tap to send</a>`)
          : `<a class="qr-btn" style="margin-left:auto;flex:none;cursor:pointer;background:var(--gold);border-color:var(--gold-line)" data-open-approval="${esc(p.id)}">Review &amp; decide →</a>`;
        return `<div class="ex-task" style="align-items:flex-start">
          <span class="tk h">${esc((p.category || "held").toUpperCase())}</span>
          <span style="flex:1"><b>${esc(p.title || "")}</b>
            <span class="sub" style="display:block;margin-top:2px">${esc(p.what || p.why || "")}</span></span>
          ${decided}</div>`;
      }).join("")
      : `<p class="sub">Nothing waits on you. Tasks land here only after 3-tier escalation, an outward gate hold, or an unroutable/missing-resource hold.</p>`}
    </div>`;
  const goalsMini = goals.map(g => `<span class="pill" title="${esc(g.gap || "")}">${esc(g.id)} ${g.score}</span>`).join(" ");
  // ── PHASE 5, the LIVING OS: residents 1:1 with real agents, fleet health, queue + trace viewer ──
  const deptsReg = (reg && reg.departments) || {};
  const regAgents = (reg && reg.agents) || [];
  const busTasks = os.tasks || [];
  // residents v2: one bot per department with REAL open work; its chip is the actual task
  const workBots = Object.entries(busPer)
    .filter(([d, c]) => d !== "(unrouted)" && (c.queued || 0) + (c.working || 0) > 0)
    .slice(0, 8).map(([d], i) => {
      const hint = String((deptsReg[d] || {}).lane_hint || d).split(" ")[0].toLowerCase();
      const st = stations.find(s => (s.label || "").toLowerCase().includes(hint))
        || stations[i % Math.max(stations.length, 1)] || { x: 50, y: 80 };
      const t = busTasks.find(x => x.department === d) || {};
      const w = regAgents.find(a => a.department === d && a.tier === 1) || {};
      const m = _monsterImg(d, "worker", "ex-bot-m");
      return `<div class="ex-bot ${m ? "has-m" : ""}" style="background:${m ? "transparent" : BOTC[i % BOTC.length]};--sx:50%;--sy:45%;--ex:${st.x}%;--ey:${st.y}%;--dur:${5.5 + (i % 4) * 1.6}s;--delay:${-i * 1.7}s"
        title="${esc(w.id || d)} — ${esc(t.title || "on the bus")}">
        ${m}<span class="ex-chip">${esc(d)}: ${esc(String(t.title || "work").split(" ").slice(0, 2).join(" "))}</span></div>`;
    }).join("");
  // ── M3.4: the animation catalog — every prop on the floor is a REAL last-beat event ──
  let fxHTML = "";
  if (iso) {
    const at = {};                                     // department -> its building's coords
    stations.forEach(s => { const d = _monsterDept(s.label); if (d && !at[d]) at[d] = [s.x, s.y]; });
    (os.recent_events || []).slice(-8).forEach((e, i) => {
      const d = e.department || _monsterDept(e.lane || e.by || "") || null;
      const a = iso.animForEvent(e.kind, d);
      const p = at[d] || [50, 40];
      fxHTML += iso.prop(a, p[0] + 5.5, p[1] - 11, i * 0.35, `${e.kind}${d ? " · " + d : ""}`);
      if (e.kind === "completed") fxHTML += iso.prop("party", 50, 33, i * 0.35, "delivered to the core");
    });
    stations.filter(s => s.status === "stale").forEach(s =>
      fxHTML += iso.prop("rest", s.x - 5.5, s.y - 11, 0, "idle — lane resting"));
  }
  const bpMap = os.backpressure || {}, usage = os.usage || {};
  const fleetHTML = `
    <div class="card"><h3>🛠 Fleet health <span class="sub">— every department: its worker, real counters, who's resting</span></h3>
      <div class="fleet">${Object.keys(deptsReg).sort().map(d => {
        const u = usage[d] || {}, c = busPer[d] || {}, bp = bpMap[d] || {};
        const cooling = bp.cooldown_until && bp.cooldown_until > new Date().toISOString();
        const w = regAgents.find(a => a.department === d && a.tier === 1);
        return `<div class="dep">${_exIcon(d)} <b>${esc(d)}</b>${deptsReg[d].gated ? " 🔒 gated" : ""}<br>
          <span class="sub">${esc(w ? w.id : "unstaffed until Phase 3")}</span><br>
          ${c.queued || 0} queued · ${c.working || 0} working · ${u.done || 0} done · ${u.handoffs || 0} hand-offs · ${u.fails || 0} fails
          ${cooling ? `<br><span class="cool">😮‍💨 resting until ${esc(String(bp.cooldown_until).slice(11, 16))} UTC (backpressure)</span>` : ""}</div>`;
      }).join("")}</div></div>`;
  const evs = (os.recent_events || []).slice().reverse();
  const _evTxt = e => String(e.why || e.what || e.doc || e.result || e.reason || "").slice(0, 70);
  const queueHTML = `
    <div class="ex-grid">
      <div class="card"><h3>🚌 Live bus queue <span class="sub">— click a task to see its full trace (why X over Y)</span></h3>
        ${busTasks.length ? busTasks.map(t => `<div class="ex-task os-task-row" data-trace="${esc(t.id)}">
          <span class="tk ${t.status === "working" ? "w" : t.status === "held" ? "h" : "q"}">${esc(String(t.status).toUpperCase())}</span>
          <span>${_exIcon(t.department || "")} <b>${esc(t.department || "unrouted")}</b> · ${esc(t.title)}
            <span class="sub">step ${t.steps || 0} · from ${esc(t.source || "?")}${t.doc ? " · has hand-off doc" : ""}</span></span></div>`).join("")
        : `<p class="sub">Bus is clear — everything is done or waiting for the next heartbeat.</p>`}
        <div id="trace-view"></div>
      </div>
      <div class="card"><h3>📡 OS events <span class="sub">— the daemon feed: everything the OS saw machine-wide</span></h3>
        <div class="os-log" style="max-height:280px">${evs.length ? evs.map(e =>
          `<div>· [${esc(String(e.at || "").slice(11, 16))}] <b>${esc(e.kind)}</b> ${esc(e.lane || e.chose || e.department || "")} ${esc(_evTxt(e))}</div>`).join("")
          : "<div>· events appear here as beats run</div>"}</div>
      </div>
    </div>`;
  const maint = mode !== "run"
    ? `<div class="ex-maint"><b>${mode === "kill" ? "⛔ KILL SWITCH — the OS is stopped" : "🔧 MAINTENANCE — safe mode, assess only"}</b></div>` : "";
  // ── PHASE 6: the DIRECTION LOOP + CHANGE TUTORIALS (D2 — the loop that was missed once) ──
  const dirList = ((dirs && dirs.directions) || []).filter(d => d.status === "active").slice(-4).reverse();
  // newest first — the old slice(0,4) took the OLDEST entries, so new walkthroughs (the whole
  // point of the Phase-6 law) could never appear; part of why the owner 'lost his bearings'
  const tutList = ((tuts && tuts.tutorials) || [])
    .slice().sort((a, b) => (b.pinned ? 1 : 0) - (a.pinned ? 1 : 0)
      || String(b.at || "").localeCompare(String(a.at || ""))).slice(0, 6);
  _tourTuts = tutList;                                // M3.13: expose for the interactive tour runner
  const directionHTML = `
    <div class="card" style="border-top:3px solid var(--gold)">
      <h3>🧭 Direction & tutorials <span class="sub">— you steer; EXCAVA shows its reading; every change gets a walkthrough</span></h3>
      <div class="ex-send">
        <input id="ex-dir-input" maxlength="300" placeholder='State a direction… e.g. "focus on making the activator real before anything visual"'>
        <button class="qr-btn" id="ex-dir-btn">set direction ➤</button>
      </div>
      <div class="ex-grid" style="margin-top:10px">
        <div>
          <b class="sub">Your active directions — and how EXCAVA reads them (correct it by re-stating)</b>
          ${dirList.length ? dirList.map(d => `<div class="ex-task" style="display:block">
            <div><span class="tk q">${esc(d.id.toUpperCase())}</span> <b>${esc(d.text)}</b></div>
            <div class="sub" style="margin-top:4px">${d.excava_reading ? "🦾 reading: " + esc(d.excava_reading) : "🦾 acknowledgment arrives next beat (hourly)"}</div>
          </div>`).join("") : `<p class="sub">No directions yet — the standing rules apply until you state one.</p>`}
        </div>
        <div>
          <b class="sub">What changed — walkthroughs, newest first (Phase-6 law: no major change without one)</b>
          ${tutList.map((t, ti) => `<details class="ex-task" style="display:block" ${ti === 0 ? "open" : ""}><summary><b>${esc(t.build)}</b> · ${esc(t.title)} <span class="sub">${esc(t.at || "")}</span></summary>
            ${(t.interactive || []).length ? `<div style="margin:6px 0"><button class="qr-btn" data-tour="${ti}" style="background:var(--gold-soft);border-color:var(--gold-line)">▶ Take the interactive tour (${(t.interactive || []).length} stops)</button>${t.podcast ? ` <a class="qr-btn" href="${esc(t.podcast.replace(/^docs\//, ""))}" target="_blank">🎧 podcast</a>` : ""}</div>` : ""}
            <ol style="margin:6px 0 2px 18px;font-size:12.5px">${(t.steps || []).map(s => `<li>${esc(s)}</li>`).join("")}</ol></details>`).join("")
          || `<p class="sub">No tutorials recorded yet.</p>`}
        </div>
      </div>
    </div>`;
  // ── PHASE 3: what the Creators department made (always labeled, tested before first use) ──
  const creations = ((made && made.creations) || []).slice(-8).reverse();
  const creationsHTML = creations.length ? `
    <div class="card"><h3>🦾 Created by EXCAVA <span class="sub">— autonomous creations; every one labeled + independently tested before first use (G-12)</span></h3>
      ${creations.map(c => `<details class="ex-task" style="display:block">
        <summary><span class="tk ${c.status === "published" ? "w" : "h"}">${esc((c.status || "").toUpperCase())}</span>
          <b>${esc(c.name)}</b> <span class="pill">${esc(c.type)}</span> <span class="pill" style="background:var(--gold-soft)">🦾 ${esc(c.label || "Created by EXCAVA")}</span>
          <span class="sub">fills: ${esc(c.gap || "")}</span></summary>
        <p class="sub" style="margin:6px 0 2px">${esc(c.what || "")}<br><b>use:</b> ${esc(c.how_to_use || "")}<br>
          <b>self-test:</b> ${c.self_test ? (c.self_test.ok ? "✅ passed" : "❌ " + esc(JSON.stringify(c.self_test.checks))) : "pending"} ·
          before first run: <code>python -m src.excava_creators --test-before-run "${esc(c.name)}"</code></p>
      </details>`).join("")}
    </div>` : "";
  // ── M4.6 PROVE IT'S REAL: (a) an artifact built unattended by a CI beat, (b) goal → package ──
  const _unattended = (os.recent_events || []).filter(e => e.kind === "handoff" && e.doc)
    .concat(creations.map(c => ({ kind: "creation", doc: c.name, at: c.created_at, by: "creators" })))
    .sort((a, b) => String(b.at || "").localeCompare(String(a.at || "")))[0];
  const proveHTML = `
    <div class="card" style="border-top:3px solid oklch(0.68 0.16 148)"><h3>✅ Proof it's real <span class="sub">— M4.6: EXCAVA builds unattended, and a goal becomes a runnable package</span></h3>
      <div class="ex-grid">
        <div><b class="sub">① Built while you were away (unattended)</b>
          ${_unattended ? `<div class="ex-task"><span class="tk w">${esc((_unattended.kind || "").toUpperCase())}</span>
            <span>${esc(String(_unattended.doc).split("/").pop().replace(/\.md$/, ""))}
            <span class="sub">— ${esc(_unattended.by || "a department")}, beat #${os.beats || "?"}, ${esc(fmtDate(_unattended.at))}</span></span>
            ${_unattended.doc && String(_unattended.doc).includes("/") ? `<a class="qr-btn" style="margin-left:auto;flex:none" target="_blank" href="${GH_REPO}/blob/main/${esc(_unattended.doc)}">open</a>` : ""}</div>
            <p class="sub">Hourly CI beats run the departments + rooms with no one watching — this is the newest thing they produced. See them all in 📦 <a href="#" data-goto="results">Results</a>.</p>`
          : `<p class="sub">The next hourly beat will land one here — rooms + creators produce artifacts unattended.</p>`}
        </div>
        <div><b class="sub">② Type a goal → get a working package</b>
          <p class="sub">Use the console above (or a <code>/horse</code> goal), or assemble in 🧰 <a href="#" data-goto="packages">Packages</a>: you get a runnable KIT of real elements — open it, run each or all. Another project can pull it via the 🛢 hub endpoint.</p>
          <div class="ex-task"><span class="tk q">TRY</span><span>Type “<b>build me a research agent</b>” in the console, or open 🧰 Packages → “Research &amp; browse” → Run all.</span></div>
        </div>
      </div>
    </div>`;
  // ── GUARDRAILS: the information-loss protections, visible so you can trust the project won't topple ──
  const gl = (grd && grd.guardrails) || [];
  const guardHTML = gl.length ? `
    <div class="card" style="border-top:3px solid ${grd.critical_failures ? "oklch(0.62 0.19 28)" : "oklch(0.68 0.16 148)"}">
      <h3>🛡 Guardrails <span class="sub">— ${grd.passing}/${grd.total} holding · ${grd.critical_failures ? `<b style="color:var(--bad)">${grd.critical_failures} CRITICAL</b>` : "0 critical"} · so the project never loses information or topples</span></h3>
      <div class="guard-grid">${gl.map(r => `<div class="guard ${r.ok ? "ok" : r.severity === "critical" ? "crit" : "warn"}" title="${esc(r.detail)}">
        <span class="gm">${r.ok ? "✓" : r.severity === "critical" ? "✕" : "!"}</span>
        <b>${esc(r.id)}</b> ${esc(r.name)}</div>`).join("")}</div>
      <p class="sub" style="margin-top:6px">Runs every beat (last ${esc(fmtDate(grd.generated_at))}). Fixes the two mechanical failures: safe-git QUARANTINES colliding files (never deletes) and commits via a UTF-8 message file. Full contract: <a target="_blank" href="${GH_REPO}/blob/main/GUARDRAILS.md">GUARDRAILS.md</a>.</p>
    </div>` : "";
  // ── CAPABILITIES: the ≥30 things EXCAVA can do, tagged HONESTLY (live/planned/gated/pitch) ──
  const cl = (caps && caps.capabilities) || [];
  const capOrder = { live: 0, planned: 1, "gated-M5": 2, pitch: 3 };
  const capLabel = { live: "✓ live", planned: "◔ planned", "gated-M5": "🔒 M5-gated", pitch: "🖊 needs you" };
  const capsHTML = cl.length ? `
    <div class="card" style="border-top:3px solid oklch(0.62 0.17 280)">
      <h3>🧩 Capabilities <span class="sub">— ${caps.total} things EXCAVA can do · <b style="color:oklch(0.5 0.14 150)">${caps.live} live</b> · ${caps.planned} planned · ${caps.gated_M5} M5-gated · ${caps.pitch} needs you (honest, per the 2026-07-06 audit)</span></h3>
      <div class="cap-grid">${cl.slice().sort((a, b) => (capOrder[a.status] - capOrder[b.status])).map(c => `
        <div class="cap cap-${c.status.replace('-', '')}" title="${esc(c.what)} — ${esc(c.evidence)}">
          <span class="cap-s">${capLabel[c.status] || c.status}</span>
          <b>${esc(c.name)}</b> <span class="cap-d">${_exIcon(c.department)} ${esc(c.department)}</span></div>`).join("")}</div>
    </div>` : "";
  // ── OVERHAUL DECISIONS: the ~300 calls are the OWNER'S — verdicts land here and gate every milestone (END PLAN §7) ──
  const di = (dec && dec.items) || [];
  const decided = di.filter(i => i.verdict);
  const nextIds = di.filter(i => !i.verdict).slice(0, 4).map(i => "#" + i.id).join(" ");
  const vHue = { keep: 150, fix: 60, improve: 230, rebuild: 300, wire: 280, backlog: 80, remove: 28 };
  const decHTML = di.length ? `
    <div class="card" style="border-top:3px solid oklch(0.7 0.14 60)">
      <h3>🗳 Overhaul decisions <span class="sub">— <b>${decided.length}/${di.length}</b> decided by the owner · verdicts gate every milestone (§7) · next clickable batch: ${nextIds || "all decided"}</span></h3>
      <div class="cap-grid">${decided.slice(-8).reverse().map(i => `
        <div class="cap" title="${esc(i.what || "")}${i.note ? " — " + esc(i.note) : ""}">
          <span class="cap-s" style="color:oklch(0.55 0.15 ${vHue[i.verdict] || 230})">${esc(i.verdict.toUpperCase())}</span>
          <b>#${i.id} ${esc(i.title)}</b></div>`).join("")}</div>
      <p class="sub" style="margin-top:6px">Answer in-session (clickable, 4 per batch), bulk-write "12: rebuild" lines from <a target="_blank" href="${GH_REPO}/blob/main/EXCAVA_MASTER_AUDIT.md">EXCAVA_MASTER_AUDIT.md</a>, or <code>python -m src.audit_decisions set &lt;id&gt; &lt;verdict&gt;</code> — decisions persist in data/excava/overhaul_decisions.json.</p>
    </div>` : "";
  // ── ONE-BRAIN MEMORY: the formerly-fragmented stores now answer to a single recall() (M1) ──
  const mb = membrain || {};
  const mbStores = mb.stores || {};
  const mbLabel = { "why-log": "🧾 WHY-log (episodes)", "hub": "🛢 hub semantic index",
    "brain-graph": "🕸 brain graph", "agent-log": "🗣 agent conversations", "pipeline": "⚙ pipeline graph" };
  const memHTML = mb.total_records ? `
    <div class="card" style="border-top:3px solid oklch(0.62 0.17 280)">
      <h3>🧠 One-Brain Memory <span class="sub">— <b>${mb.total_records.toLocaleString()}</b> records across <b>${mb.n_stores}</b> formerly-separate stores, now one <code>recall()</code> every agent calls (M1: unify memory)</span></h3>
      <div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:6px">
        ${Object.entries(mbStores).sort((a, b) => b[1] - a[1]).map(([s, n]) =>
          `<span class="pill" title="${esc(s)}">${mbLabel[s] || s}: <b>${n.toLocaleString()}</b></span>`).join("")}
      </div>
      <p class="sub" style="margin-top:8px">One deterministic façade (<code>python -m src.memory_brain recall "…"</code>) spans all of them — no more hand-querying five files. Semantic re-rank (the hub vectors) layers on next.</p>
    </div>` : "";
  view.innerHTML = `
    <div class="card" style="border-top:3px solid var(--gold)">
      <h3>🦾 EXCAVA <span class="sub">— the agentic OS running this project</span>
        <span class="pl-badge ${gate.internal_allowed ? "pl-live" : "pl-stale"}">${gate.internal_allowed ? "OPERATING" : "GATE CLOSED"}</span></h3>
      <p class="sub">Phase: ${esc(ex && ex.phase || "OS-1 operator")} · memory: <b>${mem.vectors || 0}</b> vectors ·
        outward actions ${gate.outward_allowed ? "OPEN" : `held (${esc((gate.checks || {}).truth_access_G3 ?? "?")} / 70 truth&access)`} · goals: ${goalsMini}</p>
      <div class="ex-floor ${iso ? "iso" : ""}">${iso ? iso.ground() : ""}${maint}${stHTML}${workBots || bots}${fxHTML}
        <div class="ex-core">EXCAVA<small>AGENTIC CORE</small></div>
        <div class="floor-clock" title="M2.7: the visible timing readout">⏱ beat #${os.beats || "?"} · ${((os.beat_log || []).length || 0)} events last beat</div>
      </div>
      <div class="ex-detail" id="ex-detail">Click a department station to inspect it — what it does, its real status, cadence and last run.</div>
      <p class="sub" style="margin-top:8px">The floor is LIVE: each station is a real pipeline department (lamp = its actual status), each colored bot is a real registered agent carrying its department's actual bus task — hover one to see who it is and what it holds.</p>
    </div>
    ${driveHTML}
    ${_commsThread(inbox)}
    ${capsHTML}
    ${decHTML}
    ${memHTML}
    ${guardHTML}
    ${proveHTML}
    ${directionHTML}
    ${creationsHTML}
    ${fleetHTML}
    ${queueHTML}
    ${apHTML}
    ${brains && brains.brains ? `<div class="card" style="border-top:3px solid oklch(0.62 0.17 280)">
      <h3>🧠 The Brains <span class="sub">— a brain = a <b>LEAD</b> model + a <b>COMPLEMENTARY-strength SUPPORT</b> of a different lineage (real fallback) · brains are PEERS (the only ranking is inside a brain, so none dominates the conversation)</span></h3>
      ${(brains.assembled_brains || []).length ? `<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:10px;margin:8px 0">
        ${brains.assembled_brains.map(b => `<div class="card" style="margin:0;border-left:3px solid var(--gold)">
          <b>Brain ${esc(b.id)}</b> <span class="pill" title="brains are equal peers — no dominance order">peer</span>
          <p class="sub" style="margin:5px 0 0">⭐ lead: <b>${esc((b.lead||{}).lineage||"—")}</b> <span class="pill">${esc((b.lead||{}).tier||"")}</span> <code>${esc((b.lead||{}).model||"")}</code><br>
          🛟 support: ${b.support ? `<b>${esc(b.support.lineage)}</b> <span class="pill">${esc(b.support.tier||"")}</span> <code>${esc(b.support.model)}</code> — complements the lead, answers if it fails` : "<i>none yet (needs a 2nd live lineage)</i>"}</p></div>`).join("")}
      </div>` : ""}
      <p class="sub" style="margin-top:4px"><b>All lineages</b> that can be a lead or support (${brains.live}/${brains.total} live):</p>
      <div style="display:flex;flex-wrap:wrap;gap:6px;margin-top:4px">
        ${brains.brains.map(b => `<span class="pill" style="border-color:${b.status === "live" ? "oklch(0.62 0.16 148)" : "oklch(0.6 0.02 90)"}" title="${esc(b.lineage)} · ${esc(b.role)} · ${esc(b.model)}">${esc(b.family)} ${b.status === "live" ? "✓" : "🔑"}</span>`).join("")}
      </div>
      <p class="sub" style="margin-top:8px">Ranked from the hourly benchmark; the local Qwen/Llama runs zero-quota, GLM · DeepSeek · Kimi need <code>OPENROUTER_API_KEY</code> (§12). Every model — plan-named or already in the project — can earn a lead or back one as support.</p>
      ${(brains.debate_lineages || []).length ? `<p class="sub" style="margin-top:4px">⚔ A debate now picks <b>DISTINCT lineages only</b> (never the same model on two providers — §2 correlated-errors ban): <b>${brains.debate_lineages.map(esc).join(" · ")}</b></p>` : ""}
      ${Object.keys(brains.spoke_today || {}).length ? `<p class="sub" style="margin-top:4px">🗣 Actually spoke in rooms today: ${Object.entries(brains.spoke_today).map(([l, n]) => `<b>${esc(l)}</b> ${n}`).join(" · ")} — real turns, not just the roster</p>` : ""}</div>` : ""}
    ${engh && engh.results ? `<div class="card"><h3>🔌 Engine health <span class="sub">— hourly benchmark canary (a self-improvement experiment): each free engine answers one golden prompt; agents prefer the healthy ones</span></h3>
      <div style="display:flex;flex-wrap:wrap;gap:6px">${engh.results.map(r => {
        const c = r.status === "healthy" ? "oklch(0.62 0.16 148)" : r.status === "no-key" ? "oklch(0.6 0.02 90)" : "oklch(0.6 0.18 25)";
        return `<span class="pill" style="border-color:${c}" title="${esc(r.note || r.model || "")}">${esc(r.engine)} · ${esc(r.status)}${r.ms ? " · " + r.ms + "ms" : ""}</span>`; }).join("")}</div>
      <p class="sub" style="margin-top:6px">measured ${esc(fmtDate(engh.generated_at))} · ranking: ${esc((engh.ranking || []).slice(0, 5).join(" → "))}</p></div>` : ""}
    ${expr && expr.experiments ? `<div class="card"><h3>🧪 Self-experiments <span class="sub">— how EXCAVA improves ITSELF, honestly labeled (live = running now, next = designed)</span></h3>
      ${expr.experiments.map(x => `<div class="ex-task" style="align-items:flex-start">
        <span class="tk ${x.status === "live" ? "q" : "h"}">${x.status === "live" ? "🟢 LIVE" : "◔ NEXT"}</span>
        <span style="flex:1"><b>${esc(x.id)}</b> <span class="sub">(${esc(x.method)})</span>
          <span class="sub" style="display:block;margin-top:2px">${esc(x.what)}</span></span></div>`).join("")}
      <p class="sub" style="margin-top:6px">Autonomy (agreed 10 Jul): EXCAVA alone may tune prompts/configs, change its own code IF a sandbox test passes (auto-revert), and add agents ('Added by EXCAVA'); new tools, departments, or features go through a pitch to you.</p></div>` : ""}
    <div class="card"><h3>⭐ North Star <span class="sub">— the ${goals.length} goals as a CONSTELLATION: live scores orbit the core; click a star to open its goal</span></h3>
      <div class="constel">
        <div class="constel-core"><b>EXCAVATORTRON</b><small>the hub</small></div>
        <div class="orbit">${goals.map((g, i) => {
          const ang = Math.round(i / Math.max(goals.length, 1) * 360);
          const pts = 4 + (i % 5), size = 30 + (g.score || 0) * 0.26;
          const col = ["#ffd166", "#8ecae6", "#f7a8c4", "#b5e48c", "#f4978e", "#cdb4db", "#a8dadc", "#ffb703", "#b9fbc0"][i % 9];
          return `<div class="nstar ${g.status === "met" ? "met" : g.status === "at-risk" ? "risk" : ""}"
            data-goal="${i}" style="--ang:${ang}deg" title="${esc(g.name)}: ${g.score}/100">
            <div class="body" style="width:${size}px;height:${size}px;animation-delay:${-i * 0.7}s">
              <svg viewBox="0 0 40 40"><path d="${_starPath(pts, 19, 8.5)}" fill="${col}" stroke="#0e0c1a" stroke-width="2"/></svg>
              <b>${esc(g.id)}<i>${g.score}</i></b>
            </div></div>`;
        }).join("")}</div>
      </div>
      <div class="ex-detail" id="nstar-detail">Click a star — its goal, live score and current gap open here.</div>
      <div class="links" style="margin-top:8px">${goals.map((g, i) =>
        `<span class="lnk" data-goal-chip="${i}" style="cursor:pointer" title="${esc(g.gap || "")}">${esc(g.id)} ${esc(g.name)} · ${g.score}</span>`).join("")}</div>
    </div>
    <div class="ex-grid">
      <div class="card"><h3>📥 Task inbox <span class="sub">— send EXCAVA work</span></h3>${taskHTML}</div>
      <div class="card"><h3>🎯 Now / next</h3>
        <div class="ex-task"><span class="tk w">NOW</span><span>${esc(act.do || "idle")}</span></div>
        ${(act.use_tools || []).length ? `<p class="sub">using (recalled by meaning): ${act.use_tools.map(t => esc(t.name)).join(" · ")}</p>` : ""}
        ${((ex && ex.holding) || []).map(h => `<div class="ex-task"><span class="tk h">HELD</span><span>${esc(h.priority || "")} <span class="sub">${esc(h.why_held || "")}</span></span></div>`).join("")}
      </div>
    </div>
    ${rc && rc.resources ? `<div class="card"><h3>🔋 Resources <span class="sub">— checked before any task is attempted; free-only, on purpose</span></h3>
      <div class="links">${Object.entries(rc.resources).map(([k, v]) => {
        const bad = !v.ok && !v.optional, style = bad ? "border-color:var(--bad);color:var(--bad);font-weight:700"
          : !v.ok ? "border-color:var(--muted);color:var(--muted)" : "";
        const mark = v.ok ? "✓" : v.optional ? "○" : "✗";
        return `<span class="lnk" style="${style}" title="${esc(v.note || "")}">${mark} ${esc(k.replace(/_/g, " "))}${v.optional && !v.ok ? " (optional)" : ""}</span>`;
      }).join("")}</div>
      ${(rc.missing || []).length ? `<p class="sub">Missing (blocking): <b>${rc.missing.map(esc).join(", ")}</b> — tasks needing these are HELD, not attempted. Hover a chip for the fix.</p>`
        : `<p class="sub">Nothing critical missing — every core task type is runnable, 100% free.</p>`}
      ${(rc.optional_missing || []).length ? `<p class="sub">Skipped by choice (stay free): <b>${rc.optional_missing.map(esc).join(", ")}</b> — a free fallback covers these already, just slower.</p>` : ""}
      <p class="sub">Can do now: ${Object.entries(rc.can_do || {}).map(([k, v]) => `${v.ok ? "✅" : "⛔"} ${esc(k)}`).join(" · ")}</p>
    </div>` : ""}`;
  view.querySelectorAll("[data-goto]").forEach(a => a.addEventListener("click", e => { e.preventDefault(); show(a.dataset.goto); }));
  // M3.11: a pitch in the approval queue opens as a conversation
  view.querySelectorAll("[data-open-pitch]").forEach(a =>
    a.addEventListener("click", e => { e.preventDefault(); openPitch(a.dataset.openPitch); }));
  // 2026-07-10: every pending approval opens the in-app Review & decide modal (Approve/Decline + note)
  view.querySelectorAll("[data-open-approval]").forEach(a =>
    a.addEventListener("click", e => { e.preventDefault(); openApproval(a.dataset.openApproval); }));
  // M3.13: the interactive walkthrough
  view.querySelectorAll("[data-tour]").forEach(b =>
    b.addEventListener("click", () => startTour(+b.dataset.tour)));
  // Phase 1 task-send: the box builds the prefilled "EXCAVA: …" issue (owner-rank channel)
  let attachBody = "";
  const sendIt = () => {
    const inp = view.querySelector("#ex-send-input");
    let v = (inp && inp.value || "").trim();
    if (!v) return;
    // P6 trigger parsing: /nosg /horse /plan /research /watch map to the trigger words
    v = v.replace(/^\/(nosg|horse|plan|research|watch)\s*/i, (_, t) => t.toUpperCase() + " ");
    const dept = (view.querySelector("#ex-dept") || {}).value || "";
    const body = [attachBody, dept ? `route-to: ${dept}` : "", "Sent from the EXCAVA console."]
      .filter(Boolean).join("\n");
    // IN-APP first (owner: don't just fling me to GitHub): keep a local record + confirm in-app,
    // then dispatch to the cloud beat via the free issue channel on an explicit click.
    try { const q = JSON.parse(localStorage.getItem("excavatortron.mytasks") || "[]");
      q.unshift({ task: v, dept, at: new Date().toISOString() });
      localStorage.setItem("excavatortron.mytasks", JSON.stringify(q.slice(0, 40))); } catch (_) {}
    _showModal("Send task to EXCAVA", `<p>Task: <b>${esc(v)}</b>${dept ? ` → <b>${esc(dept)}</b> department` : ""}</p>
      <p class="sub">Saved to your in-app task list. EXCAVA runs in the cloud, so to hand it to the running beat, send it through the free issue channel (one click). A tiny always-free backend would make this fully one-click in-app — that's your call (an owner pitch).</p>
      <div class="el-actions always"><a class="primary" target="_blank" href="${_exIssue("EXCAVA: " + v, body)}">📮 Send to the cloud beat ↗</a>
      <button class="ex-modal-cancel">keep in-app only</button></div>`);
    const mc = document.querySelector("#ex-modal .ex-modal-cancel");
    if (mc) mc.addEventListener("click", () => { document.getElementById("ex-modal").style.display = "none"; });
    const inp2 = view.querySelector("#ex-send-input"); if (inp2) inp2.value = "";
  };
  const sBtn = view.querySelector("#ex-send-btn");
  if (sBtn) sBtn.addEventListener("click", sendIt);
  const sInp = view.querySelector("#ex-send-input");
  if (sInp) sInp.addEventListener("keydown", e => { if (e.key === "Enter") sendIt(); });
  view.querySelectorAll(".console-hints [data-hint]").forEach(h =>
    h.addEventListener("click", () => { if (sInp) { sInp.value = h.dataset.hint; sInp.focus(); } }));
  const attach = view.querySelector("#ex-attach");
  if (attach) attach.addEventListener("click", () => {
    attachBody = prompt("Attach context for this task (a link, notes, a task body):", attachBody) || attachBody;
    attach.style.background = attachBody ? "var(--gold)" : "";
  });
  const mic = view.querySelector("#ex-mic");
  if (mic) mic.addEventListener("click", () => {
    const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SR) { mic.title = "This browser has no speech recognition"; return; }
    const rec = new SR();
    rec.lang = "en-US"; mic.style.background = "var(--gold)";
    rec.onresult = ev => { if (sInp) sInp.value = ev.results[0][0].transcript; };
    rec.onend = () => { mic.style.background = ""; };
    rec.start();
  });
  // Phase 6 direction-send: same issue channel, "EXCAVA: direction …"
  const dirIt = () => {
    const inp = view.querySelector("#ex-dir-input");
    const v = (inp && inp.value || "").trim();
    if (v) _sendModal("EXCAVA: direction " + v, "Stated from the cockpit Direction card.");
  };
  const dBtn = view.querySelector("#ex-dir-btn");
  if (dBtn) dBtn.addEventListener("click", dirIt);
  const dInp = view.querySelector("#ex-dir-input");
  if (dInp) dInp.addEventListener("keydown", e => { if (e.key === "Enter") dirIt(); });
  // Phase 5 trace viewer: click a bus task -> fetch its real JSONL trace, show why X over Y
  view.querySelectorAll(".os-task-row").forEach(el => el.addEventListener("click", async () => {
    const id = el.dataset.trace;
    const tv = view.querySelector("#trace-view");
    if (!tv) return;
    tv.innerHTML = `<p class="sub">loading trace ${esc(id)}…</p>`;
    const txt = await loadText(`excava/traces/${id}.jsonl`);
    if (!txt) { tv.innerHTML = `<p class="sub">no trace on disk for ${esc(id)} (it may not be committed yet).</p>`; return; }
    const rows = txt.trim().split("\n").map(l => { try { return JSON.parse(l); } catch { return null; } }).filter(Boolean);
    tv.innerHTML = `<p class="sub" style="margin-top:8px"><b>trace — ${esc(id)}</b> (${rows.length} events)</p>` + rows.map(ev => {
      const extra = ev.kind === "routed"
        ? `chose <b>${esc(ev.chose)}</b>${(ev.over || []).length ? ` over ${(ev.over || []).map(esc).join(", ")}` : ""} — ${esc(ev.why || "")}`
        : esc(String(ev.doc || ev.result || ev.reason || ev.by || ev.title || "").slice(0, 140));
      return `<div class="tr-ev">[${esc(String(ev.at || "").slice(0, 16))}] <b>${esc(ev.kind)}</b> ${extra}</div>`;
    }).join("");
  }));
  // station click-through: ENTER a department — M3.3 side-view cutaway + real numbers
  const det = view.querySelector("#ex-detail");
  view.querySelectorAll(".ex-station").forEach((el, i) => el.addEventListener("click", () => {
    view.querySelectorAll(".ex-station").forEach(x => x.classList.remove("sel"));
    el.classList.add("sel");
    const s = stations[i] || {};
    const next = s.last_run ? new Date(new Date(s.last_run).getTime() + (s.cadence_h || 12) * 3.6e6) : null;
    const laneLine = `<b>${_exIcon(s.label)} ${esc(s.label || "")}</b> — ${esc(s.what || "")}<br>
      status <b>${esc(s.status || "?")}</b> · ran ${_ageAgo(s.age_hours)} · every ~${esc(s.cadence_h)}h ·
      ${esc(s.runs_7d)}× this week${next ? ` · next ~${esc(fmtDate(next.toISOString()))}` : ""}`;
    const dep = _monsterDept(s.label);
    if (window.ExcavaFloor && dep) {
      const staff = regAgents.filter(a => a.department === dep);
      const lead = staff.find(a => a.role === "lead") || staff.find(a => a.tier === 1) || {};
      const roles = ["doer", "checker", "improver"].map(r =>
        `${staff.filter(a => a.role === r).length} ${r}`).join(" · ");
      det.innerHTML = ExcavaFloor.cutaway({ dept: dep, label: s.label || dep,
        accent: ExcavaFloor.ACCENT[dep] || "#e9b400", lead, staff: Math.max(staff.length - 1, 0),
        roles, counts: busPer[dep] || {}, usage: usage[dep] || {} }) + `<p class="cut-lane">${laneLine}</p>`;
    } else det.innerHTML = laneLine;
  }));
  // M3.8: constellation — a star (or its legend chip) opens the goal, live score + gap
  const nd = view.querySelector("#nstar-detail");
  const openGoal = i => {
    const g = goals[+i]; if (!g || !nd) return;
    view.querySelectorAll(".nstar").forEach((x, xi) => x.classList.toggle("sel", xi === +i));
    nd.innerHTML = `<b>⭐ ${esc(g.id)} — ${esc(g.name)}</b> · score <b>${g.score}</b>/100 · ${esc(g.status || "")}
      <div class="taste-bar" style="margin-top:6px"><i class="${g.status === "met" ? "gb-met" : g.status === "at-risk" ? "gb-risk" : "gb-unmet"}" style="width:${Math.max(g.score, 3)}%"></i><b>${g.score}</b></div>
      ${g.gap ? `<p class="sub" style="margin:6px 0 0">gap: ${esc(g.gap)}</p>` : ""}`;
  };
  view.querySelectorAll(".nstar").forEach(el => el.addEventListener("click", () => openGoal(el.dataset.goal)));
  view.querySelectorAll("[data-goal-chip]").forEach(el => el.addEventListener("click", () => openGoal(el.dataset.goalChip)));
}

// ── APPROVAL DECISIONS: every pending item is reviewable + decidable IN THE APP ──
// The decision is saved locally instantly (visible + persists your review) and dispatched to the
// cloud beat via the free issue channel, which writes granted/declined to excava_approvals.json.
let _apprCache = [];
function _localDecisions() {
  try { return JSON.parse(localStorage.getItem("excavatortron.decisions") || "{}"); }
  catch (_) { return {}; }
}
function _recordDecision(id, decision, review) {
  const d = _localDecisions();
  d[id] = { decision, review: review || "", at: new Date().toISOString() };
  try { localStorage.setItem("excavatortron.decisions", JSON.stringify(d)); } catch (_) {}
}
// Open the in-app decision modal for a pending approval — plain language, review box, Approve/Decline.
function openApproval(id) {
  const p = _apprCache.find(x => x.id === id) || { id, title: id, what: "", why: "", category: "held" };
  const modal = document.getElementById("pitch-modal"); if (!modal) return;
  modal.hidden = false;
  const close = () => { modal.hidden = true; };
  const row = (label, val) => val ? `<p class="sub" style="margin:.15rem 0"><b>${label}:</b> ${esc(val)}</p>` : "";
  const planList = (p.plan && p.plan.length)
    ? `<p class="sub" style="margin:.4rem 0 .1rem"><b>The plan — exactly what EXCAVA will do if you approve:</b></p>`
      + `<ol style="margin:.1rem 0 .3rem 1.1rem;padding:0">`
      + p.plan.map(s => `<li class="sub" style="margin:.12rem 0">${esc(s)}</li>`).join("") + `</ol>`
    : "";
  const hub = (p.hub_candidates || []).map(c =>
    `<a class="pill" href="#element/${encodeURIComponent(c.id)}" title="${esc(c.id)}">${esc(c.name)}</a>`).join(" ");
  modal.innerHTML = `<div class="pitch-box">
    <div class="ph">🖊 NEEDS YOUR DECISION — ${esc((p.category || "held").toUpperCase())} <button class="px" data-appr-x>✕</button></div>
    <p style="font-weight:600;margin:.4rem 0">${esc(p.title || "")}</p>
    <p class="sub" style="margin:.2rem 0 .6rem">${esc(p.what || "")}</p>
    ${row("Who asks", p.requested_by)}
    ${row("The need", p.need || p.why)}
    ${row("How important", p.importance)}
    ${row("What's missing", p.missing)}
    ${planList}
    ${row("Effort", p.effort)}
    ${row("Reversible?", p.reversible)}
    ${hub ? `<p class="sub" style="margin:.3rem 0 .1rem"><b>What EXCAVA found in its own hub</b> (click to open):</p><p style="margin:.1rem 0 .4rem">${hub}</p>` : ""}
    ${!p.need && p.why ? "" : (p.why && p.need ? `<p class="sub" style="opacity:.7;font-size:.82em">raw trigger: ${esc(p.why)}</p>` : "")}
    <label class="sub" style="display:block;margin:.5rem 0 .2rem">Your review / note (optional — the cloud beat and history keep it):</label>
    <textarea id="appr-review" rows="3" style="width:100%;box-sizing:border-box;border-radius:8px;padding:8px;font:inherit" placeholder="e.g. yes, but route it to analysis instead / no, not worth it right now"></textarea>
    <div class="pitch-actions" style="margin-top:.7rem">
      <button class="ok" data-appr-yes>✓ Approve</button>
      <button class="no" data-appr-no>✕ Decline</button>
    </div></div>`;
  const decide = (decision) => {
    const review = (modal.querySelector("#appr-review") || {}).value || "";
    _recordDecision(id, decision, review);
    close();
    invalidate("excava_approvals.json");
    _sendModal("EXCAVA: " + decision + " " + id, review || ("(" + decision + " — no note)"), id);
    if (typeof renderExcava === "function") renderExcava();
  };
  modal.querySelector("[data-appr-x]").addEventListener("click", close);
  modal.querySelector("[data-appr-yes]").addEventListener("click", () => decide("approve"));
  modal.querySelector("[data-appr-no]").addEventListener("click", () => decide("decline"));
  modal.querySelectorAll("a.pill").forEach(a => a.addEventListener("click", close));  // hub chip -> element view
  modal.addEventListener("click", e => { if (e.target === modal) close(); });
}

// ── M3.11 STEERING: bell + count, "needs your approval" banner, walk-up monster, pitches ──
let _pitchCache = [];
async function renderSteering() {
  const [ap, pit] = await Promise.all([load("excava_approvals.json"), load("excava/pitches.json")]);
  const pend = (ap && ap.pending) || [];
  _pitchCache = (pit && pit.pitches) || [];
  const n = pend.length;
  const bell = document.getElementById("approve-bell");
  const count = document.getElementById("bell-count");
  if (bell && count) {
    bell.hidden = n === 0; count.textContent = n;
    bell.onclick = () => { show("excava").then(() => {
      const q = document.querySelector(".ex-task .tk.h"); if (q) q.closest(".card").scrollIntoView({ behavior: "smooth", block: "center" }); }); };
  }
  // a NEW approval since last visit → ring the bell + walk a herald monster up to the door
  const seen = +(localStorage.getItem("excavatortron.approvals.seen") || 0);
  const newest = pend.map(p => p.since || p.at || "").sort().slice(-1)[0] || "";
  const newestN = pend.filter(p => (p.since || p.at || "") > (localStorage.getItem("excavatortron.approvals.seenAt") || "")).length;
  if (bell && n > seen && n > 0) { bell.classList.add("ring"); setTimeout(() => bell.classList.remove("ring"), 1600); }
  if (newestN > 0 && n > 0) heraldWalkUp(pend[0]);
  localStorage.setItem("excavatortron.approvals.seen", n);
  if (newest) localStorage.setItem("excavatortron.approvals.seenAt", newest);
  // the dismissible banner (re-appears whenever the count changes)
  const banner = document.getElementById("approve-banner");
  if (banner) {
    const dkey = "excavatortron.approveBanner.dismissed";
    const dismissedFor = localStorage.getItem(dkey);
    if (!n || dismissedFor === String(n)) { banner.hidden = true; }
    else {
      const top = pend[0];
      const pitchN = pend.filter(p => p.category === "pitch").length;
      banner.hidden = false;
      banner.innerHTML = `🔔 <b>${n} thing${n > 1 ? "s" : ""} need${n > 1 ? "" : "s"} your approval</b>
        — ${esc((top.title || "").slice(0, 70))}${pitchN ? ` <span class="pill">${pitchN} pitch${pitchN > 1 ? "es" : ""}</span>` : ""}
        <span class="ab-open"><a href="#" data-steer-review>review →</a></span>
        <button class="ab-x" data-steer-x title="dismiss until the next one">✕</button>`;
      banner.querySelector("[data-steer-review]").addEventListener("click", e => { e.preventDefault();
        const p0 = pend.find(p => p.category === "pitch");
        if (p0) openPitch(p0.id); else show("excava"); });
      banner.querySelector("[data-steer-x]").addEventListener("click", () => { localStorage.setItem(dkey, String(n)); banner.hidden = true; });
    }
  }
}
function heraldWalkUp(item) {
  const w = document.getElementById("walkup"); if (!w) return;
  const isPitch = item && item.category === "pitch";
  const dep = isPitch ? "improve" : (item && _monsterDept(item.category || "")) || "news";
  document.getElementById("walkup-img").src = `assets/monsters/${dep}-lead.svg`;
  document.getElementById("walkup-say").textContent = isPitch
    ? `Pitch for you: ${(item.title || "").slice(0, 40)}` : `Needs your call: ${(item && item.title || "").slice(0, 40)}`;
  w.hidden = false;
  w.onclick = () => { w.hidden = true; if (isPitch) openPitch(item.id); else show("excava"); };
  clearTimeout(w._t); w._t = setTimeout(() => { w.hidden = true; }, 9000);
}
function openPitch(id) {
  const p = _pitchCache.find(x => x.id === id) || { id, what: "pitch", why: "", class: "" };
  const modal = document.getElementById("pitch-modal"); if (!modal) return;
  const bubble = (dep, name, eng, text) =>
    `<div class="msg"><div class="ava has-m">${_monsterImg(dep, "lead") || "🤖"}</div>
      <div class="bub"><div class="who">${esc(name)} <span class="eng">${esc(eng)}</span></div>${esc(text)}</div></div>`;
  modal.hidden = false;
  modal.innerHTML = `<div class="pitch-box">
    <div class="ph">⚡ PITCH — ${esc(p.class || "proposal")} <button class="px" data-pitch-x>✕</button></div>
    <div class="chat">
      ${bubble("improve", "Ratchet", "self-improve lead", `I want to ${p.what}.`)}
      ${bubble("improve", "Ratchet", "reasoning", p.why || "It clears a recurring problem.")}
      ${bubble("security", "Bastion", "checker", "Reviewed — it's reversible and scoped. Your call, boss.")}
    </div>
    <div class="pitch-actions">
      <a class="ok" target="_blank" href="${_exIssue("EXCAVA: approve " + p.id, "Approving pitch: " + p.what)}">✓ Approve</a>
      <a class="no" target="_blank" href="${_exIssue("EXCAVA: decline " + p.id, "Declining pitch: " + p.what)}">✕ Decline</a>
    </div></div>`;
  const close = () => { modal.hidden = true; };
  modal.querySelector("[data-pitch-x]").addEventListener("click", close);
  modal.addEventListener("click", e => { if (e.target === modal) close(); });
}

// ── M3.13 / E7 INTERACTIVE WALKTHROUGH: navigate, highlight the new thing, let you try it ──
let _tourTuts = [];
async function startTour(idx) {
  const t = _tourTuts[idx]; if (!t || !(t.interactive || []).length) return;
  const steps = t.interactive; let i = 0;
  let ov = document.getElementById("tour-ov");
  if (!ov) { ov = document.createElement("div"); ov.id = "tour-ov"; ov.className = "tour-ov"; document.body.appendChild(ov); }
  const ring = document.createElement("div"); ring.className = "tour-ring"; ov.appendChild(ring);
  const box = document.createElement("div"); box.className = "tour-box"; ov.appendChild(box);
  const done = () => { ov.remove(); };
  async function go() {
    const s = steps[i];
    if (state.activeTab !== s.go) { await show(s.go); await new Promise(r => setTimeout(r, 550)); }
    let el = null, tries = 0;
    while (!el && tries < 14) { el = document.querySelector(s.look_for); if (!el) { await new Promise(r => setTimeout(r, 180)); tries++; } }
    if (el) {
      el.scrollIntoView({ behavior: "smooth", block: "center" });
      await new Promise(r => setTimeout(r, 260));
      const r = el.getBoundingClientRect();
      ring.style.cssText = `display:block;top:${r.top - 6}px;left:${r.left - 6}px;width:${r.width + 12}px;height:${r.height + 12}px`;
    } else { ring.style.display = "none"; }
    box.innerHTML = `<div class="tour-n">Stop ${i + 1} of ${steps.length} · <b>${esc(s.go)}</b></div>
      <p>${esc(s.try)}</p>
      <div class="tour-btns">
        ${i > 0 ? `<button class="qr-btn" data-tprev>‹ Back</button>` : ""}
        <button class="qr-btn" data-tskip>Exit</button>
        <button class="qr-btn" data-tnext style="background:var(--gold);border-color:var(--gold-line)">${i < steps.length - 1 ? "Next ›" : "Done ✓"}</button>
      </div>`;
    box.querySelector("[data-tnext]").onclick = () => { if (i < steps.length - 1) { i++; go(); } else done(); };
    const pv = box.querySelector("[data-tprev]"); if (pv) pv.onclick = () => { i--; go(); };
    box.querySelector("[data-tskip]").onclick = done;
  }
  go();
}

// ── tab router ───────────────────────────────────────────────────────────────
async function show(tab) {
  state.activeTab = tab;
  if (window.__graphStop) window.__graphStop();   // stop any running graph animation
  document.querySelectorAll("nav button").forEach(b =>
    b.classList.toggle("active", b.dataset.tab === tab));
  view.innerHTML = empty("Loading…");
  // M1.6: #element/<id> routes to the element detail view on top of any tab
  if (tab && tab.startsWith("element/")) {
    await renderElement(decodeURIComponent(tab.slice(8)));
    renderCrew("excava");
    return;
  }
  await renderTab(tab);
  decorateCards(tab);                             // M1.8: badges + action rows on every list tab
  // One bulleted "Updates: …" line at the very top of the tab (lists every update type).
  const c = cadenceLine(tab);
  if (c) view.insertAdjacentHTML("afterbegin", c);
  // Per-tab accent: every department wears its own color (maximalist, way-finding).
  view.style.borderTop = `5px solid ${TAB_ACCENT[tab] || "var(--gold)"}`;
  // EXCAVA presence on every tab: the OS strip (gate lamps + what it's working on right now).
  if (tab !== "excava") {
    const s = await excavaStrip(tab);
    if (s) {
      view.insertAdjacentHTML("afterbegin", s);
      view.querySelectorAll(".ex-strip [data-goto]").forEach(a =>
        a.addEventListener("click", e => { e.preventDefault(); show(a.dataset.goto); }));
    }
  }
  // Virtual residents on every tab (fire-and-forget; reuses cached JSON).
  renderCrew(tab);
  renderSteering();                                 // M3.11: keep the bell/banner current
  // If quick-read is on, actually condense the descriptions (not just CSS-clamp them).
  quickreadSummarize(document.body.classList.contains("quickread"));
}

// Designs — AI-made / open-source website+app looks, tailored to your taste, with screenshots.
// Includes a Design ARENA (Are.na-inspired): pick what you like, and the project learns your taste.
const _shot = (u, w = 1200) => u ? `https://s.wordpress.com/mshots/v1/${encodeURIComponent(u)}?w=${w}` : "";
function _arena() { try { return JSON.parse(localStorage.getItem("excavatortron.arena") || "{}"); } catch { return {}; } }
function _arenaTaste(a) {
  const s = a.styles || {}; return Object.keys(s).sort((x, y) => s[y] - s[x]).filter(k => s[k] > 0);
}
function _tasteWeights(a) {
  const s = a.styles || {}, keys = Object.keys(s).filter(k => s[k] > 0).sort((x, y) => s[y] - s[x]);
  const max = Math.max(1, ...keys.map(k => s[k]));
  return keys.map(k => ({ k, v: s[k], pct: Math.round(100 * s[k] / max) }));
}
// Where your Arena votes ACTUALLY show up: a visible panel (here), the gallery re-rank (_pscore),
// the "♥ your taste" badge per design, and the build command (your styles get injected into it).
function _tastePanel(a) {
  const w = _tasteWeights(a), votes = a.total || 0;
  if (!votes) return `<div class="taste-panel"><b>⚔ Your taste</b> <span class="sub">— pick designs in the Arena and this whole tab re-ranks to what YOU like (0 votes yet). Your top styles also flow into the "build" command on each card.</span></div>`;
  return `<div class="taste-panel"><div class="taste-head"><b>⚔ Your taste</b>
      <span class="sub">${votes} vote${votes > 1 ? "s" : ""} · gallery ranked for you · styles feed the build command</span>
      <button class="qr-btn" data-arena-reset title="Clear your taste votes">reset</button></div>
    <div class="taste-bars">${w.slice(0, 6).map(t => `<div class="taste-bar"><span>${esc(t.k)}</span><i style="width:${t.pct}%"></i><b>${t.v}</b></div>`).join("")}</div></div>`;
}
function _pscore(x, a) {
  const s = a.styles || {}, w = a.wins || {};
  return (x.style_tags || []).reduce((t, k) => t + (s[k] || 0), 0) * 3 + (w[x.slug] || 0) * 5 + (x.stars || 0) / 1000;
}
// ── M3.11b EDITABLE TASTE PANEL — separate DESIGN-taste (learned) vs WORK-taste (explicit) ──
// Design taste lives in excavatortron.arena.styles (also grown by Arena votes); work taste is a
// set of explicit dials in excavatortron.worktaste that feed HORSE best-of-results merges (M4.2).
const WORK_DIMS = [
  ["thoroughness", "fast &amp; lean", "thorough &amp; complete"],
  ["detail", "concise", "detailed &amp; explained"],
  ["boldness", "safe &amp; conventional", "bold &amp; opinionated"],
  ["novelty", "proven patterns", "novel approaches"],
  ["scope", "minimal / focused", "featureful"],
  ["polish", "rough &amp; quick", "polished &amp; production"],
];
function _workTaste() {
  let w; try { w = JSON.parse(localStorage.getItem("excavatortron.worktaste") || "{}"); } catch { w = {}; }
  WORK_DIMS.forEach(([k]) => { if (typeof w[k] !== "number") w[k] = 50; });
  return w;
}
function _saveWorkTaste(w) { localStorage.setItem("excavatortron.worktaste", JSON.stringify(w)); }
// ── M4.3 PACKAGES: reusable kits — assemble / edit / pin / reuse in one click ──
function _localPkgs() { try { return JSON.parse(localStorage.getItem("excavatortron.packages") || "{}"); } catch { return {}; } }
function _saveLocalPkgs(o) { localStorage.setItem("excavatortron.packages", JSON.stringify(o)); }
async function _allPackages() {
  const [srv, made] = await Promise.all([load("packages.json"), load("created_by_excava.json")]);
  const local = _localPkgs();
  const map = {};
  ((srv && srv.packages) || []).forEach(p => { map[p.id] = { ...p }; });
  // room / creators package artifacts also become packages (attributed)
  (((made && made.creations) || []).filter(c => c.type === "package" && Array.isArray(c.elements)))
    .forEach(c => { const id = "pkg-made-" + (c.name || "").toLowerCase().replace(/\W+/g, "-").slice(0, 24);
      map[id] = map[id] || { id, name: c.name, what: c.what || "", elements: c.elements, created_by: "EXCAVA", source: "made", at: c.created_at }; });
  // your local overlay: assembles, edits, pins, deletes
  Object.values(local.pkgs || {}).forEach(p => { if (p._deleted) delete map[p.id]; else map[p.id] = { ...(map[p.id] || {}), ...p, _local: true }; });
  Object.entries(local.pins || {}).forEach(([id, v]) => { if (map[id]) map[id].pinned = v; });
  return Object.values(map).sort((a, b) => (b.pinned ? 1 : 0) - (a.pinned ? 1 : 0) || String(b.at || "").localeCompare(String(a.at || "")));
}
async function renderPackages() {
  const pkgs = await _allPackages();
  const ix = await eidx();
  const elId = e => typeof e === "string" ? e : (e && (e.id || e.name)) ? String(e.id || e.name) : String(e);
  const elName = e => { const id = elId(e); return (ix.byId[id] || {}).name || id.split(":").pop(); };
  const card = p => {
    const chips = (p.elements || []).map(e => { const id = elId(e);
      return `<a class="pill" href="#element/${encodeURIComponent(id)}" title="${esc(id)}">${esc(elName(e))}</a>`; }).join(" ");
    const kitBody = "Kit: " + p.name + "\n" + (p.elements || []).map(e => "- " + elId(e)).join("\n");
    return `<div class="card pkg-card">
      <h3>${p.pinned ? "📌 " : ""}${esc(p.name)} <span class="pill">${(p.elements || []).length} items</span>
        <span class="mentions">${esc(p.created_by || "you")}${p.source ? " · " + esc(p.source) : ""}</span></h3>
      ${p.what ? `<p class="sub">${esc(p.what)}</p>` : ""}
      <div class="pkg-els">${chips || '<span class="sub">empty kit</span>'}</div>
      <div class="el-actions always">
        <a target="_blank" href="${_exIssue("EXCAVA: run kit " + p.name, kitBody + "\n\nRun each element for this task.")}">▶ Run all</a>
        <a href="#" data-pkg-runeach="${esc(p.id)}">▶ Run each</a>
        <a href="#" data-pkg-pin="${esc(p.id)}">${p.pinned ? "📌 Unpin" : "📌 Pin"}</a>
        <a href="#" data-pkg-edit="${esc(p.id)}">✎ Edit</a>
        <a target="_blank" href="${_exIssue("EXCAVA: save package " + p.name, kitBody)}">💾 Save to EXCAVA</a>
        ${p._local ? `<a href="#" data-pkg-del="${esc(p.id)}">🗑 Remove</a>` : ""}
      </div></div>`;
  };
  view.innerHTML = `
    <div class="card" style="border-top:3px solid var(--gold)">
      <h3>🧰 Packages <span class="sub">— reusable KITS of hub elements. Assemble once, pin the frequent ones, reuse in one click.</span></h3>
      <div class="pkg-assemble">
        <input id="pkg-name" placeholder="new kit name…" maxlength="40">
        <input id="pkg-els" placeholder="element ids or names, comma-separated (e.g. tool:claude-code, firecrawl)…">
        <button class="qr-btn" id="pkg-add" style="background:var(--gold-soft);border-color:var(--gold-line)">+ assemble</button>
      </div>
      <p class="sub">Auto-suggested + your assembles. “Run all” sends the kit to EXCAVA as one task; “Run each” opens each element. Pins float to the top. Edits live on this device; “Save to EXCAVA” persists a kit for the cloud.</p>
    </div>
    <div class="card hubapi-card"><h3>🛢 Hub-as-database <span class="sub">— M4.5: pull these packages + real elements into ANY project</span></h3>
      <p class="sub">Excavatortron publishes a public read endpoint (refreshed every beat). Budoaris / FreeDup / any tool — or the activator offline — can GET it and pull a package or an element (each carries install + url).</p>
      <div class="sub">Endpoint: <code id="hubapi-url">${GH_PAGES}/hub_api.json</code>
        <button class="qr-btn" data-copy="${GH_PAGES}/hub_api.json">copy</button>
        <a class="qr-btn" target="_blank" href="${GH_PAGES}/hub_api.json">open</a></div>
      <div class="sub" style="margin-top:6px">Pull a package: <code>const hub = await (await fetch("${GH_PAGES}/hub_api.json")).json(); const kit = hub.packages.find(p =&gt; p.name === "Research &amp; browse");</code></div>
    </div>
    ${pkgs.length ? pkgs.map(card).join("") : empty("No packages yet — assemble one above, or turn a brain-graph cluster into a package (Dev Construction → brain graph).")}`;
  // assemble
  view.querySelector("#pkg-add").addEventListener("click", () => {
    const name = (view.querySelector("#pkg-name").value || "").trim();
    const raw = (view.querySelector("#pkg-els").value || "").split(",").map(s => s.trim()).filter(Boolean);
    if (!name || !raw.length) return;
    const els = raw.map(tok => {                       // resolve loose names to real element ids
      if (ix.byId[tok]) return tok;
      const hit = Object.keys(ix.byId).find(id => id.toLowerCase().includes(tok.toLowerCase()) ||
        (ix.byId[id].name || "").toLowerCase().includes(tok.toLowerCase()));
      return hit || tok;
    });
    const lp = _localPkgs(); lp.pkgs = lp.pkgs || {};
    const id = "pkg-you-" + name.toLowerCase().replace(/\W+/g, "-").slice(0, 24) + "-" + Date.now().toString(36).slice(-4);
    lp.pkgs[id] = { id, name, what: "your kit", elements: els, created_by: "you", source: "assembled", at: new Date().toISOString(), pinned: true };
    _saveLocalPkgs(lp); renderPackages();
  });
  view.querySelectorAll("[data-pkg-pin]").forEach(a => a.addEventListener("click", e => { e.preventDefault();
    const id = a.dataset.pkgPin; const lp = _localPkgs(); lp.pins = lp.pins || {};
    const cur = pkgs.find(p => p.id === id); lp.pins[id] = !(cur && cur.pinned); _saveLocalPkgs(lp); renderPackages(); }));
  view.querySelectorAll("[data-pkg-del]").forEach(a => a.addEventListener("click", e => { e.preventDefault();
    const id = a.dataset.pkgDel; const lp = _localPkgs(); lp.pkgs = lp.pkgs || {};
    lp.pkgs[id] = { id, _deleted: true }; _saveLocalPkgs(lp); renderPackages(); }));
  view.querySelectorAll("[data-pkg-edit]").forEach(a => a.addEventListener("click", e => { e.preventDefault();
    const p = pkgs.find(x => x.id === a.dataset.pkgEdit); if (!p) return;
    const next = prompt("Edit kit elements (comma-separated ids):", (p.elements || []).join(", "));
    if (next == null) return;
    const lp = _localPkgs(); lp.pkgs = lp.pkgs || {};
    lp.pkgs[p.id] = { ...p, elements: next.split(",").map(s => s.trim()).filter(Boolean), _local: true };
    _saveLocalPkgs(lp); renderPackages(); }));
  view.querySelectorAll("[data-pkg-runeach]").forEach(a => a.addEventListener("click", e => { e.preventDefault();
    const p = pkgs.find(x => x.id === a.dataset.pkgRuneach); if (!p || !(p.elements || []).length) return;
    show("element/" + encodeURIComponent(elId(p.elements[0])));   // open the first; each chip opens the rest
  }));
}
async function renderTaste() {
  const a = _arena(); a.styles = a.styles || {};
  const wt = _workTaste();
  const styleKeys = Object.keys(a.styles).filter(k => a.styles[k] > 0).sort((x, y) => a.styles[y] - a.styles[x]);
  const maxS = Math.max(1, ...styleKeys.map(k => a.styles[k]));
  const designSliders = styleKeys.length ? styleKeys.slice(0, 10).map(k => {
    const pct = Math.round(100 * a.styles[k] / maxS);
    return `<div class="tp-row"><label>${esc(k)}</label>
      <input type="range" min="0" max="100" value="${pct}" data-dtaste="${esc(k)}">
      <b class="tp-val">${pct}</b></div>`;
  }).join("") : `<p class="sub">No design taste yet — vote in the Design Arena (Designs tab) and your styles appear here to fine-tune. You can also add one below.</p>`;
  const workSliders = WORK_DIMS.map(([k, lo, hi]) =>
    `<div class="tp-row wide"><label>${esc(k)} <span class="sub">${lo} ↔ ${hi}</span></label>
      <input type="range" min="0" max="100" value="${wt[k]}" data-wtaste="${esc(k)}">
      <b class="tp-val">${wt[k]}</b></div>`).join("");
  view.innerHTML = `
    <div class="card" style="border-top:3px solid var(--gold)">
      <h3>🎛 Your taste <span class="sub">— two profiles EXCAVA steers by: how designs should look, and how work should be done. Learned + editable.</span></h3>
      <p class="sub">Design taste feeds every design + the "build" command; work taste feeds <b>HORSE</b> best-of-results merges (M4.2) and how agents execute. Edits save instantly (on this device); “Save to EXCAVA” persists them for the cloud beats too.</p>
    </div>
    <div class="ex-grid">
      <div class="card"><h3>🎨 Design taste <span class="sub">— learned from your Arena votes, tunable here</span></h3>
        <div class="tp-list">${designSliders}</div>
        <div class="tp-add"><input id="tp-newstyle" placeholder="add a style (e.g. brutalist, minimal, glassy)…" maxlength="24">
          <button class="qr-btn" id="tp-addbtn">+ add</button>
          <button class="qr-btn" data-taste-reset="design">reset</button></div>
      </div>
      <div class="card"><h3>🛠 Work taste <span class="sub">— how you want things built; feeds HORSE merges</span></h3>
        <div class="tp-list">${workSliders}</div>
        <div class="tp-add"><button class="qr-btn" data-taste-reset="work">reset to balanced</button></div>
      </div>
    </div>
    <div class="card"><button class="qr-btn" id="tp-save" style="background:var(--gold-soft);border-color:var(--gold-line)">💾 Save to EXCAVA (persist for the cloud beats)</button>
      <span class="sub" id="tp-savenote"> — writes your taste through the owner channel so HORSE + designers use it server-side.</span></div>`;
  // wire design-taste sliders
  view.querySelectorAll("[data-dtaste]").forEach(s => s.addEventListener("input", () => {
    const k = s.dataset.dtaste; a.styles[k] = +s.value;
    s.nextElementSibling.textContent = s.value;
    localStorage.setItem("excavatortron.arena", JSON.stringify(a));
  }));
  // wire work-taste sliders
  view.querySelectorAll("[data-wtaste]").forEach(s => s.addEventListener("input", () => {
    wt[s.dataset.wtaste] = +s.value; s.nextElementSibling.textContent = s.value; _saveWorkTaste(wt);
  }));
  const addBtn = view.querySelector("#tp-addbtn");
  if (addBtn) addBtn.addEventListener("click", () => {
    const inp = view.querySelector("#tp-newstyle"); const k = (inp.value || "").trim().toLowerCase();
    if (!k) return; a.styles[k] = Math.max(a.styles[k] || 0, Math.round(maxS * 0.6) || 3);
    localStorage.setItem("excavatortron.arena", JSON.stringify(a)); renderTaste();
  });
  view.querySelectorAll("[data-taste-reset]").forEach(b => b.addEventListener("click", () => {
    if (b.dataset.tasteReset === "design") { a.styles = {}; localStorage.setItem("excavatortron.arena", JSON.stringify(a)); }
    else { localStorage.removeItem("excavatortron.worktaste"); }
    renderTaste();
  }));
  view.querySelector("#tp-save").addEventListener("click", () => {
    const body = "Design taste (style: weight):\n" +
      Object.entries(a.styles).filter(([, v]) => v > 0).map(([k, v]) => `- ${k}: ${v}`).join("\n") +
      "\n\nWork taste (dimension: 0-100):\n" + WORK_DIMS.map(([k]) => `- ${k}: ${wt[k]}`).join("\n");
    _sendModal("EXCAVA: set taste", body);
    view.querySelector("#tp-savenote").textContent = " — opened the save channel; approve the issue and the next beat stores it.";
  });
}
window.arenaVote = function (slug, tags) {
  const a = _arena(); a.styles = a.styles || {}; a.wins = a.wins || {}; a.total = (a.total || 0) + 1;
  if (slug) { a.wins[slug] = (a.wins[slug] || 0) + 1; (tags || []).forEach(t => a.styles[t] = (a.styles[t] || 0) + 1); }
  localStorage.setItem("excavatortron.arena", JSON.stringify(a)); renderTab("designs");
};
// Preview vs. full live-site view, per design (default = full-page image). Screenshots are async and
// unreliable, so we use TWO free providers with fallback — mShots first, then thum.io (full-page) — then
// a graceful "open live" tile. A real full-page shot is TALL; a "Generating Preview"/blank placeholder
// is short/wide, which is how we detect not-ready-yet and advance. Toggle is in BOTH gallery and arena.
function _shotURL(prov, u, w) {
  if (prov === "thum") return `https://image.thum.io/get/fullpage/width/${w}/${u}`;
  return `https://s.wordpress.com/mshots/v1/${encodeURIComponent(u)}?w=${w}`;
}
function _previewHTML(live, w, name) {
  return `<a class="design-fullpage" href="${esc(live)}" target="_blank" rel="noopener" title="Open the live design">
    <img class="mshot" loading="lazy" src="${esc(_shotURL("mshots", live, w))}" data-url="${esc(live)}" data-w="${w}" data-try="0" alt="${esc(name || "")}">
    <span class="fp-hint">full page — scroll ↓ · click to open live</span></a>`;
}
function _liveHTML(live) {
  return `<div class="design-live"><iframe class="livefr" src="${esc(live)}" loading="lazy" referrerpolicy="no-referrer"
      sandbox="allow-scripts allow-same-origin allow-popups allow-forms"></iframe>
    <span class="fp-hint">live site — if blank, <a href="${esc(live)}" target="_blank" rel="noopener">open ↗</a></span></div>`;
}
// WAY 3 (client safety net): if a live iframe errors or never loads (blocked/dead), swap it for the
// reliable full-page screenshot. Catches the cases server-side header detection misses.
function _liveFallback(fr) {
  const media = fr.closest(".design-media"); if (!media) return;
  const body = media.querySelector(".dview-body"); if (!body) return;
  const live = media.dataset.live || "", w = +media.dataset.w || 1200, name = media.dataset.name || "";
  body.innerHTML = `<div class="dnopreview">Can't embed this one live — <a href="${esc(live)}" target="_blank" rel="noopener">open live ↗</a>. Full screenshot:</div>` + _previewHTML(live, w, name);
  _wireMshots(media);
}
function _wireLive(scope) {
  (scope || view).querySelectorAll("iframe.livefr:not([data-wired])").forEach(fr => {
    fr.dataset.wired = "1"; let loaded = false;
    fr.addEventListener("load", () => { loaded = true; });
    fr.addEventListener("error", () => _liveFallback(fr));
    setTimeout(() => { if (!loaded) _liveFallback(fr); }, 5000);   // never fired load → blocked/dead → screenshot
  });
}
function _designMedia(x, w, liveDefault) {
  const live = x.source_url || x.homepage || "";
  if (!live) return x.look ? `<div class="dnopreview">No live URL captured — described look below.</div>` : "";
  // Only embed sites we've VERIFIED resolve AND don't block framing. Everything else (unverified, blocked,
  // or dead) shows the full-page screenshot — still the whole site, but never a blank/broken iframe.
  const canEmbed = x.url_status === "ok" && x.no_embed === false;
  const useLive = liveDefault && canEmbed;
  const body = useLive ? _liveHTML(live) : _previewHTML(live, w, x.name);
  return `<div class="design-media" data-live="${esc(live)}" data-w="${w}" data-name="${esc(x.name || "")}" data-embed="${canEmbed ? "1" : "0"}">
    <div class="dview-tabs"><button class="${liveDefault ? "" : "active"}" data-dview="preview" title="Preview image">🖼 Preview</button>
      <button class="${liveDefault ? "active" : ""}" data-dview="live" title="Live site if it allows embedding, else its full screenshot">🔍 Full site</button></div>
    <div class="dview-body">${body}</div></div>`;
}
// Screenshot loader with PROVIDER FALLBACK. Real full-page shot = tall; short/blank = not-ready → advance:
// re-poll mShots (it's async), then switch to thum.io, then show a graceful open-live tile.
function _wireMshots(scope) {
  (scope || view).querySelectorAll("img.mshot:not([data-wired])").forEach(img => {
    img.dataset.wired = "1";
    const advance = () => {
      const t = (+img.dataset.try || 0) + 1; img.dataset.try = String(t);
      const u = img.dataset.url, w = img.dataset.w || 1200;
      if (t === 1) {                                 // try the faster provider first (thum.io)
        setTimeout(() => { img.src = _shotURL("thum", u, w) + "?r=" + t; }, 800);
      } else if (t <= 5) {                           // poll mShots as it generates async (can take 5–15s) — be patient
        setTimeout(() => { img.src = _shotURL("mshots", u, w) + "&r=" + t; }, 2500 + t * 1200);
      } else if (t <= 7) {                           // one more thum.io pass
        setTimeout(() => { img.src = _shotURL("thum", u, w) + "?r=" + t; }, 1500);
      } else {                                       // exhausted → graceful open-live tile
        const a = img.closest(".design-fullpage");
        if (a) a.outerHTML = `<div class="dnopreview">Preview still generating — <a href="${a.href}" target="_blank" rel="noopener">open live ↗</a>.</div>`;
      }
    };
    img.addEventListener("load", () => {
      if (img.naturalWidth >= 50 && img.naturalHeight > img.naturalWidth * 1.1) return;  // tall = real
      advance();
    });
    img.addEventListener("error", advance);
  });
}
function renderDesigns(d) {
  let list = (d && d.designs) || [];
  const a = _arena(), mode = state.designMode || "gallery", styleFilter = state.designStyle || "all";
  if (styleFilter !== "all") list = list.filter(x => (x.style_tags || []).includes(styleFilter));
  if (q()) list = list.filter(x => hit(x.name, x.look, (x.kind || ""), (x.tech || []).join(" "), (x.style_tags || []).join(" ")));
  const taste = _arenaTaste(a);
  const STYLES = ["all", "bold", "colorful", "playful", "brutalist", "minimal", "retro", "dark", "gradient"];
  let html = `<div class="card"><h3>🎨 Designs <span class="sub">— tuned to your taste</span>
      <span class="pl-badge ${mode === "arena" ? "pl-live" : "pl-slow"}" style="margin-left:8px">${mode === "arena" ? "ARENA" : "GALLERY"}</span></h3>
    <p class="sub">Designs only — real looks from AI websites &amp; the videos, captured full-page so you can react to every part. ⚔ Arena learns what you like; "build like this" via the activator keeps the real style.</p>
    <div class="subnav"><button class="${mode === "gallery" ? "active" : ""}" data-mode="gallery">Gallery</button>
      <button class="${mode === "arena" ? "active" : ""}" data-mode="arena">⚔ Arena</button></div>
    ${_tastePanel(a)}
    ${mode === "gallery" ? `<div class="subnav">` + STYLES.map(s => `<button class="${styleFilter === s ? "active" : ""}" data-style="${s}">${s}</button>`).join("") + `</div>` : ""}</div>`;

  if (mode === "arena") {
    const pool = list.filter(x => (x.source_url || x.homepage));
    if (pool.length < 2) { view.innerHTML = html + empty("Need a couple more designs with previews for the arena — the visual protocol is adding them."); _designHooks(); return; }
    const i = Math.floor(Math.random() * pool.length); let j = Math.floor(Math.random() * pool.length);
    while (j === i) j = Math.floor(Math.random() * pool.length);
    html += `<p class="sub" style="text-align:center;margin:6px 0">Which do you like more? Pick it — the project learns your taste. (🔍 Full site shows it live.)</p>
      <div class="arena-pair">${[pool[i], pool[j]].map(x => `
        <div class="card arena-card">
          ${_designMedia(x, 900, true)}
          <h3>${esc(x.name)} ${(x.style_tags || []).map(t => `<span class="pill">${esc(t)}</span>`).join("")}</h3>
          <p class="sub">${esc((x.look || "").slice(0, 90))}</p>
          <button class="qr-btn pick-btn" data-pick="${esc(x.slug)}" data-tags="${esc((x.style_tags || []).join(","))}">👍 I like this</button></div>`).join("")}</div>
      <div style="text-align:center;margin-top:10px"><button class="qr-btn" data-pick="">Skip / both meh →</button></div>`;
    view.innerHTML = html; _designHooks(); return;
  }

  list.sort((x, y) => _pscore(y, a) - _pscore(x, a));   // gallery: rank by YOUR taste
  if (!list.length) { view.innerHTML = html + empty(q() ? `No designs match "${esc(state.query)}".` : "No designs yet — the visual protocol watches the videos and collect_designs pulls AI websites each cycle."); _designHooks(); return; }
  const SRC = { "ai-product": "AI product", "ai-builder": "AI builder", "gallery": "gallery", "dribbble": "concept", "video": "from video", "visual": "from video", "oss": "open-source" };
  html += list.map(x => {
    const liked = (a.wins || {})[x.slug];
    const src = SRC[x.source_type] || x.source_type || "";
    const match = taste.length && (x.style_tags || []).some(t => taste.slice(0, 3).includes(t));
    const styleBit = taste.length ? ` in my style: ${taste.slice(0, 3).join(", ")}` : "";
    const buildCmd = `activator: build a site like "${x.name}"${styleBit}`;
    return `<div class="card design-card">
      ${_designMedia(x, 1200)}
      <h3>${esc(x.name || "Design")} ${(x.style_tags || []).map(t => `<span class="pill">${esc(t)}</span>`).join("")}${match ? `<span class="taste-match" title="matches your Arena taste">♥ your taste</span>` : ""}${src ? `<span class="mentions">${esc(src)}</span>` : ""}
        <button class="qr-btn ${liked ? "active" : ""}" data-like="${esc(x.slug)}" data-tags="${esc((x.style_tags || []).join(","))}" title="I like this">♥${liked ? " " + liked : ""}</button></h3>
      ${x.look ? `<p>${esc(x.look)}</p>` : ""}
      <div class="sub">Build: <code>${esc(buildCmd)}</code> <button class="copy-btn" data-copy="${esc(buildCmd)}" title="Copy build command">copy</button></div>
      ${linksRow(x)}
    </div>`;
  }).join("");
  view.innerHTML = html; _designHooks();
}
function _designHooks() {
  view.querySelectorAll("[data-style]").forEach(b => b.addEventListener("click", () => { state.designStyle = b.dataset.style; renderTab("designs"); }));
  view.querySelectorAll("[data-mode]").forEach(b => b.addEventListener("click", () => { state.designMode = b.dataset.mode; renderTab("designs"); }));
  view.querySelectorAll("[data-pick]").forEach(b => b.addEventListener("click", () => window.arenaVote(b.dataset.pick, (b.dataset.tags || "").split(",").filter(Boolean))));
  view.querySelectorAll("[data-like]").forEach(b => b.addEventListener("click", () => window.arenaVote(b.dataset.like, (b.dataset.tags || "").split(",").filter(Boolean))));
  view.querySelectorAll("[data-arena-reset]").forEach(b => b.addEventListener("click", () => { localStorage.removeItem("excavatortron.arena"); renderTab("designs"); }));
  // Preview <-> Full-site toggle (gallery + arena). stopPropagation so it never triggers an arena vote.
  view.querySelectorAll("[data-dview]").forEach(b => b.addEventListener("click", (e) => {
    e.preventDefault(); e.stopPropagation();
    const media = b.closest(".design-media"); if (!media) return;
    const body = media.querySelector(".dview-body"), live = media.dataset.live || "", w = +media.dataset.w || 1200;
    media.querySelectorAll(".dview-tabs button").forEach(x => x.classList.toggle("active", x === b));
    if (b.dataset.dview === "live") {
      if (media.dataset.embed === "1") { body.innerHTML = _liveHTML(live); _wireLive(media); }
      else { body.innerHTML = `<div class="dnopreview">This site blocks live embedding — <a href="${esc(live)}" target="_blank" rel="noopener">open live ↗</a>. Showing its full screenshot:</div>` + _previewHTML(live, w, media.dataset.name || ""); _wireMshots(media); }
    }
    else { body.innerHTML = _previewHTML(live, w, media.dataset.name || ""); _wireMshots(media); }
  }));
  _wireMshots();
  _wireLive();
  return "";
}
// ── M3.5 ROOMS: the messenger chat over real agent conversations ─────────────
const AGENT_EMOJI = { transcripts: "📜", analysis: "⚙️", watch: "📺", links: "🔗", memory: "🧠",
  mining: "⛏️", visual: "🎨", news: "📰", improve: "🧬", security: "🛡️", creators: "✨",
  visualization: "🖼️", accessibility: "♿", power: "⚡", core: "🦾" };
async function renderRooms(selId) {
  const [rooms, reg, syschk] = await Promise.all([load("excava/rooms.json"), load("excava/agents.json"),
    load("excava/systemcheck.json")]);
  // P2b (owner): flag departments that only TALK — no real executor wired — honestly, in the app
  const deptCheck = ((syschk && syschk.systems) || []).find(s => s.system === "departments executable") || {};
  const talkOnly = new Set(deptCheck.talk_only || []);
  const blockedD = new Set(deptCheck.blocked || []);
  const list = ((rooms && rooms.rooms) || []).slice().reverse();
  if (!list.length) {
    view.innerHTML = `<div class="card"><h3>🗣 Rooms</h3><p class="sub">No conversations yet — rooms open and advance on every CI beat (the engines live in the cloud). Check back within the hour.</p></div>`;
    return;
  }
  const agents = {};
  ((reg && reg.agents) || []).forEach(a => { agents[a.id] = a; });
  // ROOMS-AS-OS (owner 2026-07-13): two-level nav. Level 1 = pick a DEPARTMENT or 🌐 GENERAL
  // (all inter-departmental). Level 2 (inside a department) = sub-tabs: Conversations | War rooms
  // | Group chat. Each list is the full scrollable history of that scope. A true OS shows the
  // inter-departmental traffic, not one flat pile.
  const depts = [...new Set(list.filter(r => r.kind === "dept" && r.dept).map(r => r.dept))].sort();
  const rmSub = (sc, sb) => sc === "general"
    ? list.filter(r => r.kind === "group" || r.kind === "war")
    : sb === "war" ? list.filter(r => r.kind === "war" && r.dept === sc)
    : sb === "group" ? list.filter(r => r.kind === "group")
    : list.filter(r => r.kind === "dept" && r.dept === sc);
  const selRoom0 = selId ? list.find(r => r.id === selId) : null;
  let scope = state.roomScope;
  if (selRoom0) scope = selRoom0.kind === "dept" ? selRoom0.dept : (state.roomScope || "general");
  if (!scope || (scope !== "general" && !depts.includes(scope))) scope = depts[0] || "general";
  let sub = state.roomSub || "convos";
  if (selRoom0 && scope !== "general") sub = selRoom0.kind === "war" ? "war"
    : selRoom0.kind === "group" ? "group" : "convos";
  state.roomScope = scope; state.roomSub = sub;
  const scopeRooms = rmSub(scope, sub);
  const sel = scopeRooms.find(r => r.id === selId) || scopeRooms.find(r => r.status === "open")
    || scopeRooms[0] || list[0];
  const scopeRail = depts.map(d => {
    const flag = talkOnly.has(d) ? " 🗣" : blockedD.has(d) ? " ⛔" : "";
    return `<button class="${d === scope ? "on" : ""}" data-scope="${esc(d)}" title="${esc(d)} department${talkOnly.has(d) ? " — talk-only (no real tool yet)" : blockedD.has(d) ? " — blocked on an owner resource" : ""}">${_exIcon(d)} <b>${esc(d.toUpperCase())}</b>${flag}</button>`;
  }).join("") + `<button class="${scope === "general" ? "on" : ""} k-war" data-scope="general" style="background:oklch(0.92 0.06 280)" title="every inter-departmental conversation">🌐 <b>GENERAL</b> — all cross-dept</button>`;
  const subLabels = { convos: "💬 Conversations", war: "⚔️ War rooms", group: "🏛 Group chat" };
  const subTabs = scope === "general" ? "" : `<div class="rooms-rail" style="margin-top:6px">${
    ["convos", "war", "group"].map(s => `<button class="${s === sub ? "on" : ""}" data-roomsub="${s}">${subLabels[s]} (${rmSub(scope, s).length})</button>`).join("")}</div>`;
  const roomList = `<div class="rooms-rail" style="margin-top:6px;max-height:120px;overflow-y:auto">${
    scopeRooms.length ? scopeRooms.map(r => `<button class="${r.id === sel.id ? "on" : ""}" data-room="${esc(r.id)}" title="${esc(r.goal)}">${esc(String(r.created_at || r.opened_at || "").slice(0, 10))} · ${esc((r.goal || "").slice(0, 40))}… ${r.status === "done" ? "✅" : "🟢"}</button>`).join("")
      : `<span class="sub">No ${scope === "general" ? "inter-departmental" : subLabels[sub].replace(/^\S+\s/, "").toLowerCase()} conversations yet — they appear as beats run.</span>`}</div>`;
  // P7 (owner pulled forward 2026-07-12): FULL per-department history — 14-day transcript
  // window so older rooms actually load, + a history strip of the department's earlier rooms.
  const days = [];
  for (let i = 13; i >= 0; i--) {
    const d = new Date(Date.now() - i * 864e5).toISOString().slice(0, 10);
    days.push([d, await loadText(`excava/chats/${d}/${sel.id}.jsonl`)]);
  }
  let msgs = [];
  days.forEach(([d, txt]) => {
    if (!txt) return;
    msgs.push({ day: d });
    txt.trim().split("\n").forEach(l => { try { msgs.push(JSON.parse(l)); } catch (_) {} });
  });
  const bubbles = msgs.map(m => {
    if (m.day) return `<div class="day-div">— ${esc(m.day)} —</div>`;
    const a = agents[m.agent] || {};
    const isLead = a.role === "lead";
    if (m.agent === "system") return `<div class="msg sys"><div class="bub">${esc(m.text)}</div></div>`;
    const mimg = _monsterImg(a.department || "", isLead ? "lead" : "agent");
    return `<div class="msg ${isLead ? "lead" : ""}">
      <div class="ava ${mimg ? "has-m" : ""}" title="${esc(a.persona || m.agent)}">${mimg || (AGENT_EMOJI[a.department || "core"] || "🤖") + (isLead ? "👔" : "")}</div>
      <div class="bub"><div class="who">${esc(m.name || m.agent)} <span class="eng">${esc(_engFriendly(m.engine))}${m.ms ? " · " + m.ms + "ms" : ""}</span></div>${humanizeHTML(m.text)}</div>
    </div>`;
  }).join("") || `<p class="sub">This room hasn't spoken yet — it advances on the next CI beat (engines live in the cloud).</p>`;
  // M3.7: the artifact appears INLINE in the making-chat, not just in the meta line
  const artInline = sel.artifact ? `<div class="msg sys artifact"><div class="bub">📦 <b>ARTIFACT</b> —
      this room produced a <b>${esc(sel.artifact.kind || sel.artifact_kind || "artifact")}</b>:
      ${esc(String(sel.artifact.ref || sel.artifact.id || ""))}
      · <a href="#" data-open-results>see it in 📦 Results</a></div></div>` : "";
  const inner = `
    <div class="room-meta"><span class="pill">${esc(sel.kind)}</span>
      <span>goal: <b>${esc(sel.goal)}</b></span><span>turns ${sel.turns}/${sel.max_turns}</span>
      <span>${sel.status === "done" ? "✅ closed" : "🟢 live"}</span>
      ${sel.last_turn_ms ? `<span>last turn ${sel.last_turn_ms}ms</span>` : ""}
      ${sel.artifact ? `<span>📦 artifact: <b>${esc(sel.artifact.kind)}</b> → ${esc(String(sel.artifact.ref || sel.artifact.id || ""))}</span>` : ""}</div>
    <div class="chat">${bubbles}${artInline}</div>`;
  // AGENT-PLATFORM LAYER 2: the visible track record — judge which agents earn trust
  const arecs = await load("excava/agent_records.json");
  const actives = ((arecs && arecs.agents) || []).filter(a => a.turns_7d > 0).slice(0, 12);
  const agentsCard = actives.length ? `
    <div class="card"><h3>👥 Agents — track record <span class="sub">— ${esc(arecs.window || "7 days")}: who actually works, on which brains, holding what positions (accountability, study §6)</span></h3>
      <table class="pv-table"><thead><tr><th>agent</th><th>dept · role</th><th>turns</th><th>rooms</th><th>brains used</th><th>latest held position</th></tr></thead>
      <tbody>${actives.map(a => `<tr>
        <td><b>${esc(a.name)}</b></td><td>${esc(a.dept)} · ${esc(a.role)}</td>
        <td>${esc(a.turns_7d)}</td><td>${esc(a.rooms_7d)}</td>
        <td>${esc((a.engines_used || []).length)} <span class="sub">(${esc((a.engines_used || []).join(", "))})</span></td>
        <td class="sub">${esc(a.last_position || "— memory starts accumulating from the next beats")}</td></tr>`).join("")}
      </tbody></table>
      <p class="sub">${esc((arecs && arecs.note) || "")}</p></div>` : "";
  view.innerHTML = `
    <div class="card"><h3>🗣 Rooms — the OS's conversations <span class="sub">— pick a department or 🌐 GENERAL (all inter-departmental). Inside a department: Conversations, War rooms, and Group chat — each fully scrollable.</span></h3>
      <div class="rooms-rail">${scopeRail}</div>
      ${subTabs}
      ${roomList}
      <div style="margin-top:8px">${sel && sel.kind === "war" ? `<div class="warroom"><div class="wr-head">⚔️ WAR ROOM — round table</div>${inner}</div>` : inner}</div>
    </div>${agentsCard}`;
  view.querySelectorAll("[data-scope]").forEach(b =>
    b.addEventListener("click", () => { state.roomScope = b.dataset.scope; state.roomSub = "convos"; renderRooms(); }));
  view.querySelectorAll("[data-roomsub]").forEach(b =>
    b.addEventListener("click", () => { state.roomSub = b.dataset.roomsub; renderRooms(); }));
  view.querySelectorAll("[data-room]").forEach(b =>
    b.addEventListener("click", () => renderRooms(b.dataset.room)));
  view.querySelectorAll("[data-open-results]").forEach(a =>
    a.addEventListener("click", e => { e.preventDefault(); show("results"); }));
}

// ── M3.7 RESULTS FEED: everything EXCAVA produced — attributed, filterable, openable ──
async function _resultItems() {
  const [rooms, made, ex, horse] = await Promise.all([load("excava/rooms.json"),
    load("created_by_excava.json"), load("excava_status.json"), load("horse_runs.json")]);
  const items = [];
  // M4.2: HORSE merged artifacts — 10 executions merged best-of to your work-taste
  ((horse && horse.runs) || []).forEach(h => items.push({
    at: h.at, dept: "core", agent: "HORSE ×" + (h.runners || 10),
    kind: "HORSE merge", title: h.goal,
    preview: `10 runners executed this; the best merged to your work-taste (winner #${(h.winner_idx || 0) + 1}, via ${h.engine || "?"})`,
    ref: h.file, open: h.file ? `${GH_REPO}/blob/main/${h.file}` : null }));
  ((rooms && rooms.rooms) || []).forEach(r => { if (r.artifact) items.push({
    at: r.artifact.at || r.created_at, dept: r.dept || "core", agent: r.id,
    kind: r.artifact.kind || r.artifact_kind || "artifact", title: r.goal,
    preview: `the room converged after ${r.turns} turns and produced this`,
    ref: String(r.artifact.ref || r.artifact.id || ""),
    open: r.artifact.ref ? `${GH_REPO}/blob/main/${r.artifact.ref}` : null, room: r.id }); });
  ((made && made.creations) || []).forEach(c => items.push({
    at: c.created_at, dept: "creators", agent: c.created_by || "EXCAVA",
    kind: c.type || "creation", title: c.name, preview: c.what || "", ref: c.name,
    open: null, useBody: c.how_to_use || "" }));
  (((ex || {}).os || {}).recent_events || []).filter(e => e.kind === "handoff" && e.doc)
    .forEach(e => items.push({
      at: e.at, dept: e.department || "core", agent: e.by || "worker", kind: "hand-off",
      title: String(e.doc).split("/").pop().replace(/\.md$/, ""), preview: e.why || e.what || "",
      ref: e.doc, open: `${GH_REPO}/blob/main/${e.doc}` }));
  return items.filter(x => x.at).sort((a, b) => String(b.at).localeCompare(String(a.at)));
}
function _resultCard(x) {
  return `<div class="card result-card">
    <h3>${esc(x.title)} <span class="pill">${esc(x.kind)}</span>
      <span class="mentions" title="produced by the ${esc(x.dept)} department">${_exIcon(x.dept)} <b>${esc((x.dept || "").toUpperCase())}</b> department</span></h3>
    ${x.preview ? `<p class="sub">${esc(String(x.preview).slice(0, 220))}</p>` : ""}
    <div class="el-actions always">
      ${x.ref && String(x.ref).endsWith(".md") ? `<button data-open-artifact="${esc(x.ref)}" data-title="${esc(x.title)}">📖 Open here</button>`
        : x.open ? `<a target="_blank" href="${esc(x.open)}" title="opens the raw file on GitHub">↗ Open (GitHub)</a>` : ""}
      <a target="_blank" href="${_exIssue("EXCAVA: use " + x.title, x.useBody || x.ref || "")}">🦾 Use</a>
      ${x.room ? `<a href="#" data-goto-room="${esc(x.room)}">🗣 The making-of chat</a>` : ""}
    </div>
    <p class="sub" style="margin-top:6px">${esc(fmtDate(x.at))}</p>
  </div>`;
}
// ── 🧾 PROOF: read the proof IN THE APP (owner: 'I shouldn't have to open GitHub') ──
function renderProof(p) {
  if (!p || !p.departments) {
    view.innerHTML = `<div class="card"><h3>🧾 Proof</h3><p class="sub">No proof file yet — it's written every beat (within ~10 min). It shows what each department actually did, honestly.</p></div>`;
    return;
  }
  const gh = p.gh || "";
  const vclass = v => v === "real" ? "pv-real" : v === "noop" ? "pv-noop" : v === "blocked" ? "pv-block" : v === "failed" ? "pv-fail" : "pv-plan";
  const vlabel = { real: "✓ REAL work", noop: "⚠ ran, did nothing", planned: "✕ only a plan", failed: "✕ failed", blocked: "⛔ needs YOU" };
  const dsum = Object.entries(p.delta || {}).map(([k, v]) => `${k} ${v >= 0 ? "+" : ""}${v}`).join(" · ");
  const rows = p.departments.map(d => `<tr class="${vclass(d.verdict)}">
      <td><b>${esc((d.dept || "").toUpperCase())}</b></td>
      <td><span class="pv-badge ${vclass(d.verdict)}">${vlabel[d.verdict] || d.verdict}</span></td>
      <td class="pv-out">${humanizeHTML(d.output || "")}</td>
      <td>${d.evidence ? `<button class="qr-btn" data-open-artifact="${esc(d.evidence)}" data-title="${esc((d.dept || "").toUpperCase())} — the real file">see the file</button>`
        : d.evidence_url ? `<a target="_blank" href="${esc(d.evidence_url)}">see the file ↗</a>` : "—"}</td>
    </tr>`).join("");
  view.innerHTML = `
    <div class="card" style="border-top:3px solid oklch(0.62 0.16 148)">
      <h3>🧾 Proof <span class="sub">— what EXCAVA actually did, honestly. Don't trust the words — the links go to the real files.</span></h3>
      <div class="pv-summary">
        <span class="pv-big">${p.real_pct != null ? p.real_pct + "%" : "?"}</span> of the last checks did <b>REAL</b> work
        <span class="sub">· ${esc(Object.entries(p.counts || {}).map(([k, v]) => v + " " + ({ real: "did real work", noop: "ran but changed nothing", planned: "only planned", failed: "failed", blocked: "need you" }[k] || k)).join(", ") || "no checks yet")} · updated ${esc(fmtDate(p.generated_at))}</span>
        ${dsum ? `<div class="sub" style="margin-top:4px">Change since last beat: <b>${esc(dsum)}</b></div>` : ""}
        ${p.totals ? `<div class="sub">Totals now: ${p.totals.elements} tools/skills · ${p.totals.verified} verified · ${p.totals.with_link} with a real link · ${p.totals.designs} designs · ${p.totals.creations} creations</div>` : ""}
      </div>
      <table class="pv-table"><thead><tr><th>department</th><th>did it work?</th><th>what it actually produced</th><th>proof</th></tr></thead>
        <tbody>${rows}</tbody></table>
      <p class="sub" style="margin-top:8px">Read the agents' real conversations:
        <a href="#" data-goto-tab="rooms">🗣 open Rooms</a> ·
        <a target="_blank" href="${gh}/tree/main/data/excava/chats">raw transcripts ↗</a> ·
        <a target="_blank" href="${gh}/actions/workflows/excava_beat.yml">every run's log ↗</a></p>
    </div>`;
  view.querySelectorAll("[data-goto-tab]").forEach(a =>
    a.addEventListener("click", e => { e.preventDefault(); show(a.dataset.gotoTab); }));
  view.querySelectorAll("[data-open-artifact]").forEach(b => b.addEventListener("click", () =>
    _openArtifact(b.dataset.openArtifact, b.dataset.title)));   // proof files open IN-APP, not GitHub
}
async function renderResults() {
  const items = await _resultItems();
  localStorage.setItem("excavatortron.results.seen", new Date().toISOString());
  const navBtn = document.querySelector('nav [data-tab="results"]');
  if (navBtn) navBtn.innerHTML = "📦 Results";
  const day = state.resDay || "", dept = state.resDept || "", agent = state.resAgent || "";
  const days = [...new Set(items.map(x => String(x.at).slice(0, 10)))].slice(0, 7);
  const depts = [...new Set(items.map(x => x.dept))];
  const agents = [...new Set(items.map(x => x.agent))].slice(0, 12);
  // DEPARTMENT-FIRST (owner: 'organized by department — click one, see everything it created')
  const byDept = {};
  items.forEach(x => { (byDept[x.dept || "core"] = byDept[x.dept || "core"] || []).push(x); });
  if (!dept) {                                        // overview: one card per department
    const cards = Object.keys(byDept).sort().map(d => `
      <div class="card dept-card" data-open-dept="${esc(d)}" style="cursor:pointer;border-left:4px solid var(--gold-line)">
        <h3>${_exIcon(d)} ${esc((d || "").toUpperCase())} department <span class="pill">${byDept[d].length} produced</span></h3>
        <p class="sub">Most recent: ${esc(String((byDept[d][0] || {}).title || "").slice(0, 90))}</p>
        <p class="sub" style="color:var(--gold-ink)">Click to see everything the ${esc(d)} department created →</p>
      </div>`).join("");
    view.innerHTML = `<div class="card"><h3>📦 Results — by department <span class="sub">everything EXCAVA produced, grouped by which department made it. Click a department.</span></h3></div>${cards || empty("No results yet — departments produce artifacts as they work; check back after a beat.")}`;
    view.querySelectorAll("[data-open-dept]").forEach(c =>
      c.addEventListener("click", () => { state.resDept = c.dataset.openDept; renderResults(); }));
    return;
  }
  const f = byDept[dept] || [];                        // one department opened: everything it made
  view.innerHTML = `<div class="card"><h3>${_exIcon(dept)} ${esc((dept || "").toUpperCase())} department <span class="sub">— everything it created (${f.length})</span>
      <button class="qr-btn" id="res-back" style="margin-left:10px">← all departments</button></h3></div>
    ${f.length ? f.map(_resultCard).join("") : empty("This department hasn't produced anything yet.")}`;
  const back = view.querySelector("#res-back");
  if (back) back.addEventListener("click", () => { state.resDept = ""; renderResults(); });
  view.querySelectorAll("[data-open-artifact]").forEach(b => b.addEventListener("click", () =>
    _openArtifact(b.dataset.openArtifact, b.dataset.title)));
  view.querySelectorAll("[data-goto-room]").forEach(a => a.addEventListener("click", e => {
    e.preventDefault(); show("rooms").then(() => renderRooms(a.dataset.gotoRoom));
  }));
}
async function resultsBadge() {                       // M3.7: the "new" count on the tab
  try {
    const seen = localStorage.getItem("excavatortron.results.seen") || "1970";
    const n = (await _resultItems()).filter(x => String(x.at) > seen).length;
    const navBtn = document.querySelector('nav [data-tab="results"]');
    if (navBtn && n) navBtn.innerHTML = `📦 Results <span class="nav-new">${n}</span>`;
  } catch (_) {}
}

async function renderTab(tab) {
  if (tab === "excava") return renderExcava();
  if (tab === "hub") return renderHub();
  if (tab === "rooms") return renderRooms();
  if (tab === "proof") return renderProof(await load("excava/proof.json"));
  if (tab === "results") return renderResults();
  if (tab === "packages") return renderPackages();
  if (tab === "taste") return renderTaste();
  if (tab === "skills") return renderSkills(await load("skills.json"));
  if (tab === "tools" || tab === "models")
    return renderToolRating(await _plusCreations(await load("tools.json"), "tool", "tools"), await load("models.json"));
  if (tab === "comingsoon") return renderComingSoon(await load("tools.json"));
  if (tab === "prompts") return renderPrompts(await _plusCreations(await load("prompts.json"), "prompt", "prompts"));
  if (tab === "devbuild") return renderDevConstruction();
  if (tab === "improvement") return renderImprovement();
  if (tab === "tips") return renderTips();
  if (tab === "news") return renderNews();
  if (tab === "designs") return renderDesigns(await _plusCreations(await load("designs.json"), "design", "designs"));
  if (tab === "connectors") return renderConnectors(await load("connectors.json"));
  if (tab === "sources") return renderSources();
  if (tab === "selfimprove") return renderSelfImprove();
  if (tab === "effectiveness") return renderEffectiveness();
  if (tab === "search") return renderSearchAll();
  if (tab && tab.startsWith("dyn:")) return renderDynamicTab(tab.slice(4));
}

// M1.6 hash routing: #element/<id> opens the detail view; back returns to the previous tab
window.addEventListener("hashchange", () => {
  const h = decodeURIComponent(location.hash.slice(1) || "");
  if (h.startsWith("element/")) show(h);
  else if (!h && state.activeTab && String(state.activeTab).startsWith("element/")) show("excava");
});
document.querySelectorAll("nav button").forEach(b => {
  b.addEventListener("click", () => show(b.dataset.tab));
  const c = TAB_ACCENT[b.dataset.tab];
  if (c) b.insertAdjacentHTML("afterbegin", `<i class="tab-dot" style="background:${c}"></i>`);
});

(async () => {
  resultsBadge();                                     // M3.7: fire-and-forget "new results" count
  renderSteering();                                   // M3.11: bell + banner + walk-up on new approvals
  const [status, stars, extra, config, health] = await Promise.all([
    load("status.json"), load("stars.json"), load("extra_tabs.json"), loadRoot("config.json"),
    load("health.json")]);
  state.status = status;
  state.config = config;
  state.health = health;
  state.stars = new Set(((stars && stars.starred) || []).map(e => String(e.slug || "").toLowerCase()));
  // Only show active (not dismissed) auto-created trend tabs.
  state.dynamicTabs = (((extra && extra.tabs) || []).filter(t => (t.status || "active") === "active"));
  injectDynamicTabs();
  renderHeader(state.status);

  // Client-side search (A4): debounce typing, then re-render whichever tab is open.
  const searchEl = document.getElementById("search");
  if (searchEl) {
    let t = null;
    searchEl.addEventListener("input", () => {
      clearTimeout(t);
      t = setTimeout(() => { state.query = searchEl.value || ""; show(state.activeTab); }, 180);
    });
    // Enter = search EVERYTHING (closest matches across all tabs, even without the exact name).
    searchEl.addEventListener("keydown", (e) => {
      if (e.key === "Enter") { state.query = searchEl.value || ""; show("search"); }
    });
  }

  // Quick-read mode: condense every tab's cards into scannable one-liners. Persisted.
  const qrBtn = document.getElementById("qr-toggle");
  if (qrBtn) {
    const applyQR = on => {
      document.body.classList.toggle("quickread", on);
      qrBtn.classList.toggle("active", on);
      qrBtn.setAttribute("aria-pressed", on ? "true" : "false");
      quickreadSummarize(on);   // actually condense the visible descriptions now
    };
    applyQR(localStorage.getItem("excavatortron.quickread") === "1");
    qrBtn.addEventListener("click", () =>
      { const on = !document.body.classList.contains("quickread");
        localStorage.setItem("excavatortron.quickread", on ? "1" : "0"); applyQR(on); });
  }

  // Copy the ready-to-paste skill block (delegated — works for every re-render).
  view.addEventListener("click", (e) => {
    const btn = e.target.closest(".copybtn");
    if (!btn) return;
    const box = btn.closest(".usebox");
    const txt = box ? (box.querySelector(".useprompt") || {}).textContent || "" : "";
    const done = (ok) => { const old = btn.textContent;
      btn.textContent = ok ? "✓ Copied" : "Press Ctrl+C"; btn.classList.toggle("ok", ok);
      setTimeout(() => { btn.textContent = old; btn.classList.remove("ok"); }, 1600); };
    if (navigator.clipboard) navigator.clipboard.writeText(txt).then(() => done(true)).catch(() => done(false));
    else done(false);
  });

  show("excava");
})();
