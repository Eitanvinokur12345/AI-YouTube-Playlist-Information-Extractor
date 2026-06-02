// AI Skills Tracker dashboard — vanilla JS, no external libraries (works offline).
// Reads the committed JSON files from ../data (GitHub Pages must serve from repo root).
const DATA = "../data/";
const view = document.getElementById("view");
const meta = document.getElementById("meta");
const countersEl = document.getElementById("counters");

const state = { status: null, selectedCategory: "all", newsWindow: "weekly",
  stars: new Set(), hideLowQuality: false, dynamicTabs: [] };

// True if a skill/connector slug is starred (frozen, best-in-class — never auto-changed).
const isStarred = (s) =>
  (s && (s.starred === true || s.locked === true)) ||
  (s && s.slug && state.stars.has(String(s.slug).toLowerCase()));

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
}

// ── Tab: Skills Library ──────────────────────────────────────────────────────
function renderSkills(data) {
  const skills = (data && data.skills) || [];
  const rrAscii = state.status?.run_report?.ascii;
  let html = "";
  if (rrAscii) html += `<pre class="ascii">${esc(rrAscii)}</pre>`;
  if (!skills.length) return view.innerHTML = html + empty("No skills extracted yet.");

  const cats = ["all", ...Array.from(new Set(skills.map(s => s.category || "other"))).sort()];
  html += `<div class="subnav">` + cats.map(c =>
    `<button class="${state.selectedCategory === c ? "active" : ""}" data-cat="${esc(c)}">${esc(c)}</button>`
  ).join("") + `</div>`;

  // Video-quality filter: hide skills that came from low-quality source videos.
  const lowCount = skills.filter(s => s.low_quality_source).length;
  html += `<div class="subnav"><button class="${state.hideLowQuality ? "active" : ""}" data-toggle="lowq"
    title="Hide skills extracted from videos that scored below the quality threshold">
    ${state.hideLowQuality ? "&#10003; " : ""}Hide low-quality sources${lowCount ? ` (${lowCount})` : ""}</button></div>`;

  let list = skills.slice();
  if (state.selectedCategory !== "all")
    list = list.filter(s => (s.category || "other") === state.selectedCategory);
  if (state.hideLowQuality) list = list.filter(s => !s.low_quality_source);
  // Starred (frozen) skills first, then by quality score.
  list.sort((a, b) =>
    (isStarred(b) - isStarred(a)) || ((b.quality_score || 0) - (a.quality_score || 0)));

  html += list.map(s => `
    <div class="card ${isStarred(s) ? "starred" : ""} ${s.low_quality_source ? "lowq" : ""}">
      <h3>${isStarred(s) ? '<span class="star" title="Starred — kept in original form, never auto-changed">&#9733;</span>' : ""}<span class="score">${esc(s.quality_score ?? "?")}/10</span> ${esc(s.skill_name || s.slug)}
        <span class="pill">${esc(s.category || "other")}</span>
        <span class="pill">${esc(s.target_tool || "claude")}</span>
        ${s.open_source ? '<span class="pill">open source</span>' : ""}
        ${s.video_quality_score != null ? `<span class="vq ${s.low_quality_source ? "low" : ""}" title="Source video quality (AI content review + recency)">vid ${esc(s.video_quality_score)}/10</span>` : ""}
        ${s.low_quality_source ? '<span class="lowsrc" title="Extracted from a low-quality video — treat with caution; its score was capped">low-quality source</span>' : ""}
        ${isStarred(s) ? '<span class="frozenpill">frozen</span>' : ""}</h3>
      ${s.company ? `<div class="sub">${esc(s.company)}${s.country ? " · " + esc(s.country) : ""}</div>` : ""}
      <p>${esc(s.description || "")}</p>
      ${s.use_case ? `<p><b>Use case:</b> ${esc(s.use_case)}</p>` : ""}
      ${(s.tips && s.tips.length) ? `<p><b>Tips:</b> ${s.tips.map(esc).join(" · ")}</p>` : ""}
      ${s.source_video_id ? `<p><a href="${yt(s.source_video_id)}" target="_blank" rel="noopener">Source video</a></p>` : ""}
    </div>`).join("");

  view.innerHTML = html;
  view.querySelectorAll("[data-cat]").forEach(b =>
    b.addEventListener("click", () => { state.selectedCategory = b.dataset.cat; renderSkills(data); }));
  const tog = view.querySelector('[data-toggle="lowq"]');
  if (tog) tog.addEventListener("click", () => { state.hideLowQuality = !state.hideLowQuality; renderSkills(data); });
}

// ── Tab: Models Ranking ──────────────────────────────────────────────────────
function renderModels(data) {
  if (!data || !Object.keys(data).length) return view.innerHTML = empty("No model rankings yet.");
  view.innerHTML = Object.entries(data).map(([cat, blk]) => {
    const rows = (blk.full_ranking || []).map(r => `
      <tr><td>${esc(r.rank)}</td><td>${esc(r.name)} ${esc(r.version || "")}</td>
      <td>${esc(r.company || "")}</td><td>${esc(r.score)}</td>
      <td>${r.open_source ? "yes" : ""}</td></tr>`).join("");
    return `<div class="card"><h3>${esc(cat)}</h3>
      ${blk.ascii_podium ? `<pre class="ascii">${esc(blk.ascii_podium)}</pre>` : ""}
      <table><tr><th>#</th><th>Model</th><th>Company</th><th>Score</th><th>OSS</th></tr>
      ${rows || `<tr><td colspan="5" class="empty">No models.</td></tr>`}</table></div>`;
  }).join("");
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
  const byTool = (tips && tips.by_tool) || {}; const general = (tips && tips.general) || {};
  if (Object.keys(byTool).length) {
    html += `<div class="card"><h3>Tips by tool</h3>` + Object.entries(byTool).map(([t, arr]) =>
      `<p><b>${esc(t)}:</b> ${(arr || []).map(esc).join(" · ")}</p>`).join("") + `</div>`;
  }
  const gen = Object.entries(general).filter(([, a]) => (a || []).length);
  if (gen.length) {
    html += `<div class="card"><h3>General tips</h3>` + gen.map(([t, arr]) =>
      `<p><b>${esc(t)}:</b> ${(arr || []).map(esc).join(" · ")}</p>`).join("") + `</div>`;
  }
  const list = (cmds && cmds.commands) || [];
  html += `<div class="card"><h3>Slash commands (${list.length})</h3>` + (list.length ?
    `<table><tr><th>Command</th><th>Description</th><th>Tool</th></tr>` +
    list.map(c => `<tr><td><code>${esc(c.command)}</code></td><td>${esc(c.description || "")}</td>
      <td>${esc(c.tool || "")}</td></tr>`).join("") + `</table>` : empty("No commands yet.")) + `</div>`;
  view.innerHTML = html || empty("No tips or commands yet.");
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
  const entries = ventries.concat(wentries).sort((a, b) => ts(b.publishedAt) - ts(a.publishedAt));
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
  } else { html += empty(`No ${state.newsWindow} news entries.`); }
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
  const items = (data && data.connectors) || [];
  if (!items.length) return view.innerHTML = empty("No connectors or MCP servers tracked yet.");
  items.sort((a, b) =>
    (isStarred(b) - isStarred(a)) || ((b.quality_score || 0) - (a.quality_score || 0)));
  view.innerHTML = items.map(c => `<div class="card ${isStarred(c) ? "starred" : ""}">
    <h3>${isStarred(c) ? '<span class="star" title="Starred — frozen, never auto-changed">&#9733;</span>' : ""}<span class="score">${esc(c.quality_score ?? "?")}/10</span> ${esc(c.name)}
      <span class="pill">${esc(c.type || "")}</span>
      ${c.official ? '<span class="official">official</span>' : ""}
      ${isStarred(c) ? '<span class="frozenpill">frozen</span>' : ""}</h3>
    <div class="sub">${esc(c.provider || "")}${c.category ? " · " + esc(c.category) : ""}</div>
    <p>${esc(c.what_it_does || "")}</p>
    ${c.install_or_source ? `<p><b>Install/source:</b> ${esc(c.install_or_source)}</p>` : ""}
    ${c.source_video ? `<p><a href="${yt(c.source_video)}" target="_blank" rel="noopener">Source video</a></p>` : ""}
  </div>`).join("");
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
    html += `<div class="card"><h3>Data health</h3>${empty("No health report yet — runs daily, or force it with the MCP tool run_improve().")}</div>`;
  }

  // Suggestion queue (approve/dismiss are done from the MCP server — read-only here)
  const approved = new Set((apprData && apprData.approved_ids) || []);
  const dismissed = new Set((apprData && apprData.dismissed_ids) || []);
  const sugs = (sugData && sugData.suggestions) || [];
  const eff = (s) => approved.has(s.id) ? "approved" : dismissed.has(s.id) ? "dismissed" : (s.status || "pending");
  const pending = sugs.filter(s => eff(s) === "pending");
  html += `<div class="card"><h3>Suggestions awaiting your decision (${pending.length})</h3>
    <p class="hint">The daily self-improvement run proposes risky changes here; safe fixes it just makes.
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
  const [status, stars, extra] = await Promise.all([
    load("status.json"), load("stars.json"), load("extra_tabs.json")]);
  state.status = status;
  state.stars = new Set(((stars && stars.starred) || []).map(e => String(e.slug || "").toLowerCase()));
  // Only show active (not dismissed) auto-created trend tabs.
  state.dynamicTabs = (((extra && extra.tabs) || []).filter(t => (t.status || "active") === "active"));
  injectDynamicTabs();
  renderHeader(state.status);
  show("skills");
})();
