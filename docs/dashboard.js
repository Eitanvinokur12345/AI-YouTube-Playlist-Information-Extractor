// AI Skills Tracker dashboard — vanilla JS, no external libraries (works offline).
// Reads the committed JSON files from ../data (GitHub Pages must serve from repo root).
const DATA = "../data/";
const view = document.getElementById("view");
const meta = document.getElementById("meta");
const countersEl = document.getElementById("counters");

const state = { status: null, config: null, selectedCategory: "all", newsWindow: "weekly",
  stars: new Set(), hideLowQuality: false, multiToolOnly: false, dynamicTabs: [],
  query: "", activeTab: "skills" };

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

async function load(file) {
  try {
    const r = await fetch(DATA + file, { cache: "no-store" });
    if (!r.ok) return null;
    return await r.json();
  } catch { return null; }
}

const esc = (s) => String(s ?? "").replace(/[&<>"]/g, c =>
  ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const empty = (msg) => `<p class="empty">${esc(msg)}</p>`;
const yt = (id) => `https://www.youtube.com/watch?v=${encodeURIComponent(id || "")}`;

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
  return `<div class="podium">` + order.map(m => `
    <div class="podslot ${cls(m)}">
      <div class="podrank">#${esc(m.rank)}</div>
      <div class="podscore">${esc(m.score)}</div>
      <div class="podname">${esc(m.name)}${m.version ? " " + esc(m.version) : ""}</div>
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
  const el = document.getElementById("alert");
  if (!el) return;
  let kind = "", msg = "";
  if (status && status.analyze_ok === false) {
    kind = "bad";
    msg = `<span class="badge">PIPELINE ERROR</span> The last analyze run failed, so new skills ` +
      `aren’t being added. ` + esc(status.token_hint || "Check the GitHub Actions log for details.");
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
    `Last fetch: ${status.last_fetch || status.last_run || "?"} • ` +
    `Last analyze: ${status.last_analyze || "?"} • ` +
    `Next run: ${status.next_run || "?"} • TZ: ${rr.timezone || "America/New_York"}`;

  const c = [
    ["Analyzed this run", rr.analyzed_this_run ?? 0, true],
    ["Total analyzed (all time)", status.total_videos_analyzed ?? 0, true],
    ["Total skills", status.total_skills ?? 0, false],
    ["Videos seen", status.videos_seen ?? 0, false],
    ["New found (last fetch)", rr.new_found ?? 0, false],
    ["Pending to analyze", rr.pending_to_analyze ?? 0, false],
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

// ── Tab: Models Ranking ──────────────────────────────────────────────────────
function renderModels(data) {
  if (!data || !Object.keys(data).length) return view.innerHTML = empty("No model rankings yet.");
  const searching = !!q();
  const cards = Object.entries(data).map(([cat, blk]) => {
    let ranking = blk.full_ranking || [];
    if (searching) ranking = ranking.filter(r => hit(r.name, r.version, r.company, cat));
    if (searching && !ranking.length) return "";
    const rows = ranking.map(r => `
      <tr><td>${esc(r.rank)}</td><td>${esc(r.name)} ${esc(r.version || "")}</td>
      <td>${esc(r.company || "")}</td><td>${esc(r.score)}</td>
      <td>${r.open_source ? "yes" : ""}</td></tr>`).join("");
    // HTML podium rendered from data (Claude no longer writes ascii_podium); fall back to top 3.
    const podium = searching ? "" :
      podiumHtml(blk.podium && blk.podium.length ? blk.podium : ranking.slice(0, 3));
    return `<div class="card"><h3>${esc(cat)}</h3>
      ${podium}
      <table><tr><th>#</th><th>Model</th><th>Company</th><th>Score</th><th>OSS</th></tr>
      ${rows || `<tr><td colspan="5" class="empty">No models.</td></tr>`}</table></div>`;
  }).join("");
  view.innerHTML = cards || empty(`No models match "${esc(state.query)}".`);
}

// ── Tab: Improvement Log ─────────────────────────────────────────────────────
async function renderImprovement() {
  let merges = await load("merge_log.json"); let deleted = await load("deleted_skills.json");
  if (merges && !Array.isArray(merges)) merges = merges.merges || merges.entries || [];
  if (deleted && !Array.isArray(deleted)) deleted = deleted.deleted || deleted.entries || [];
  merges = merges || []; deleted = deleted || [];
  let html = `<div class="card"><h3>Merge log (${merges.length})</h3>` +
    (merges.length ? merges.map(e =>
      `<p>${esc(e.timestamp || "")}: <b>${esc(e.merged_from)}</b> → <b>${esc(e.merged_into)}</b>
       <span class="sub">${esc(e.reason || "")}</span></p>`).join("") : empty("No merges yet.")) + `</div>`;
  html += `<div class="card"><h3>Deleted / superseded (${deleted.length})</h3>` +
    (deleted.length ? deleted.map(e =>
      `<p><b>${esc(e.slug || e.skill_name || "?")}</b> — <span class="sub">${esc(e.reason || "")}</span></p>`
    ).join("") : empty("Nothing deleted yet.")) + `</div>`;
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
  const byToolEntries = Object.entries(byTool)
    .map(([t, arr]) => [t, filterTips(t, arr)]).filter(([, a]) => a.length);
  if (byToolEntries.length) {
    html += `<div class="card"><h3>Tips by tool</h3>` + byToolEntries.map(([t, arr]) =>
      `<p><b>${esc(t)}:</b> ${arr.map(esc).join(" · ")}</p>`).join("") + `</div>`;
  }
  const gen = Object.entries(general)
    .map(([t, arr]) => [t, filterTips(t, arr)]).filter(([, a]) => a.length);
  if (gen.length) {
    html += `<div class="card"><h3>General tips</h3>` + gen.map(([t, arr]) =>
      `<p><b>${esc(t)}:</b> ${arr.map(esc).join(" · ")}</p>`).join("") + `</div>`;
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
  const [vdata, wdata] = await Promise.all([load(vfiles[state.newsWindow]), load(wfiles[state.newsWindow])]);
  const ventries = (vdata && vdata.entries) || [];
  const wentries = (wdata && wdata.entries) || [];
  const ts = (s) => { const d = Date.parse(s || ""); return isNaN(d) ? 0 : d; };
  let entries = ventries.concat(wentries).sort((a, b) => ts(b.publishedAt) - ts(a.publishedAt));
  if (q()) entries = entries.filter(e => hit(e.title, e.summary, e.source_name, e.channel_name));
  const hdr = (vdata && vdata.header) || (wdata && wdata.header) || {};
  html += `<div class="sub">Window: ${esc(hdr.window || state.newsWindow)} ·
    ${ventries.length} from videos + ${wentries.length} from official sites</div>`;
  if (entries.length) {
    html += entries.map(e => {
      const web = e.source_type === "web" || (e.url && !e.video_id);
      const src = web ? (e.source_name || "web") : (e.channel_name || "");
      const link = web ? (e.url || "#") : yt(e.video_id);
      const label = web ? "Read" : "Watch";
      const tag = web ? '<span class="webpill">web</span>' : '<span class="vidpill">video</span>';
      const low = e.low_quality_source ? '<span class="lowsrc">low-quality source</span>' : "";
      return `<div class="card ${e.low_quality_source ? "lowq" : ""}">
        <h3>${esc(e.title || "?")} ${tag} ${low}</h3>
        <div class="sub">${esc(src)} · ${esc(e.publishedAt || "")}</div>
        <p>${esc(e.summary || "(summary pending)")}</p>
        <p><a href="${esc(link)}" target="_blank" rel="noopener">${label}</a></p></div>`;
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
  let html = `<div class="card"><h3>${esc(t.title || t.id)}</h3>
    <div class="sub">${esc(t.description || "")}</div>
    <p class="hint">Auto-created from a recurring trend across ${(t.evidence_video_ids || []).length}
    videos. Not useful? Dismiss it from the offline MCP:
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

// Add a nav button for each active dynamic tab (with a NEW badge if just created).
function injectDynamicTabs() {
  const nav = document.getElementById("tabs");
  if (!nav) return;
  nav.querySelectorAll("[data-dyntab]").forEach(b => b.remove());
  const weekAgo = Date.now() - 7 * 24 * 3600 * 1000;
  state.dynamicTabs.forEach(t => {
    const isNew = Date.parse(t.created_at || "") >= weekAgo;
    const btn = document.createElement("button");
    btn.dataset.tab = "dyn:" + t.id;
    btn.dataset.dyntab = t.id;
    btn.innerHTML = esc(t.title || t.id) + (isNew ? ' <span class="newbadge">NEW</span>' : "");
    btn.addEventListener("click", () => show(btn.dataset.tab));
    nav.appendChild(btn);
  });
}

// ── Tab: Connectors ──────────────────────────────────────────────────────────
function renderConnectors(data) {
  let items = (data && data.connectors) || [];
  if (!items.length) return view.innerHTML = empty("No connectors or MCP servers tracked yet.");
  if (q()) items = items.filter(c => hit(c.name, c.provider, c.what_it_does, c.category, c.type));
  items.sort((a, b) =>
    (isStarred(b) - isStarred(a)) || ((b.quality_score || 0) - (a.quality_score || 0)));
  view.innerHTML = items.map(c => {
    const via = c.via_video_id || c.source_video;
    const srcLine = (c.source_type === "linked_resource" && c.source_url)
      ? `<p><a href="${esc(c.source_url)}" target="_blank" rel="noopener">Linked resource</a>` +
        (via ? ` · <a href="${yt(via)}" target="_blank" rel="noopener">via video</a>` : "") + `</p>`
      : c.source_video ? `<p><a href="${yt(c.source_video)}" target="_blank" rel="noopener">Source video</a></p>`
      : c.source_url ? `<p><a href="${esc(c.source_url)}" target="_blank" rel="noopener">Source</a></p>` : "";
    return `<div class="card ${isStarred(c) ? "starred" : ""}">
    <h3>${isStarred(c) ? '<span class="star" title="Starred — frozen, never auto-changed">&#9733;</span>' : ""}<span class="score">${esc(c.quality_score ?? "?")}/10</span> ${esc(c.name)}
      <span class="pill">${esc(c.type || "")}</span>
      ${c.official ? '<span class="official">official</span>' : ""}
      ${linkedPill(c)}
      ${isStarred(c) ? '<span class="frozenpill">frozen</span>' : ""}</h3>
    <div class="sub">${esc(c.provider || "")}${c.category ? " · " + esc(c.category) : ""}</div>
    <p>${esc(c.what_it_does || "")}</p>
    ${c.install_or_source ? `<p><b>Install/source:</b> ${esc(c.install_or_source)}</p>` : ""}
    ${srcLine}
  </div>`;
  }).join("") || empty(`No connectors match "${esc(state.query)}".`);
}

// ── Tab: Self-Improvement (health + suggestion queue + audit) ─────────────────
async function renderSelfImprove() {
  const [health, sugData, apprData, audit, starsData] = await Promise.all([
    load("health.json"), load("improvement_suggestions.json"),
    load("approvals.json"), load("improvement_audit.json"), load("stars.json"),
  ]);
  let html = "";

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

  // Suggestion queue (approve/dismiss are done from the MCP server — read-only here)
  const approved = new Set((apprData && apprData.approved_ids) || []);
  const dismissed = new Set((apprData && apprData.dismissed_ids) || []);
  const sugs = (sugData && sugData.suggestions) || [];
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
}

// ── tab router ───────────────────────────────────────────────────────────────
async function show(tab) {
  state.activeTab = tab;
  document.querySelectorAll("nav button").forEach(b =>
    b.classList.toggle("active", b.dataset.tab === tab));
  view.innerHTML = empty("Loading…");
  if (tab === "skills") return renderSkills(await load("skills.json"));
  if (tab === "models") return renderModels(await load("models.json"));
  if (tab === "improvement") return renderImprovement();
  if (tab === "tips") return renderTips();
  if (tab === "news") return renderNews();
  if (tab === "connectors") return renderConnectors(await load("connectors.json"));
  if (tab === "selfimprove") return renderSelfImprove();
  if (tab && tab.startsWith("dyn:")) return renderDynamicTab(tab.slice(4));
}

document.querySelectorAll("nav button").forEach(b =>
  b.addEventListener("click", () => show(b.dataset.tab)));

(async () => {
  const [status, stars, extra, config] = await Promise.all([
    load("status.json"), load("stars.json"), load("extra_tabs.json"), loadRoot("config.json")]);
  state.status = status;
  state.config = config;
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
  }

  show("skills");
})();
