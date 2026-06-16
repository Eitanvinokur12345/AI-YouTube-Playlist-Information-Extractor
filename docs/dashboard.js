// AI Skills Tracker dashboard — vanilla JS, no external libraries (works offline).
// Reads the committed JSON files from ../data (GitHub Pages must serve from repo root).
const DATA = "../data/";
const view = document.getElementById("view");
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

const esc = (s) => String(s ?? "").replace(/[&<>"]/g, c =>
  ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const empty = (msg) => `<p class="empty">${esc(msg)}</p>`;
const yt = (id) => `https://www.youtube.com/watch?v=${encodeURIComponent(id || "")}`;

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

// ── Quick-read: actually CONDENSE text (first sentence / ~24 words), not just CSS-clamp it ──
function summarizeText(t) {
  t = (t || "").trim().replace(/\s+/g, " ");
  if (!t) return t;
  const end = t.search(/[.!?](\s|$)/);          // first sentence boundary
  let s = (end > 20) ? t.slice(0, end + 1) : t;  // ignore a too-early period (e.g. "v3.")
  const w = s.split(" ");
  if (w.length > 24) s = w.slice(0, 24).join(" ") + "…";
  return s;
}
// Shorten the pure-text description paragraph of every card (skip labelled/structured lines).
function quickreadSummarize(on) {
  view.querySelectorAll(".card > p").forEach(p => {
    if (p.querySelector("b, span, a, code")) return;   // not a plain description
    if (on) {
      if (p.dataset.qrFull === undefined) p.dataset.qrFull = p.textContent;
      const short = summarizeText(p.dataset.qrFull);
      if (short && short.length < p.dataset.qrFull.length) p.textContent = short;
    } else if (p.dataset.qrFull !== undefined) {
      p.textContent = p.dataset.qrFull;
      delete p.dataset.qrFull;
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
        ${t.source_url ? `<p><a href="${esc(t.source_url)}" target="_blank" rel="noopener">Source</a></p>`
          : (t.source_video_id ? `<p><a href="${yt(t.source_video_id)}" target="_blank" rel="noopener">Source video</a></p>` : "")}
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
  const [vdata, wdata] = await Promise.all([load(vfiles[state.newsWindow]), load(wfiles[state.newsWindow])]);
  const ventries = (vdata && vdata.entries) || [];
  const wentries = (wdata && wdata.entries) || [];
  const ts = (s) => { const d = Date.parse(s || ""); return isNaN(d) ? 0 : d; };
  let entries = ventries.concat(wentries).sort((a, b) => ts(b.publishedAt) - ts(a.publishedAt));
  if (q()) entries = entries.filter(e => hit(e.title, e.summary, e.source_name, e.channel_name));
  const hdr = (vdata && vdata.header) || (wdata && wdata.header) || {};
  html += `<div class="sub">Window: ${esc(hdr.window || state.newsWindow)} ·
    ${ventries.length} from videos + ${wentries.length} from official sites</div>`;
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
    // Free / paid + which Claude surface it runs in (CLAUDE.md Step 8 extended fields).
    const freeRaw = String(c.free ?? "").toLowerCase();
    const freeMap = { yes: ["Free", "free-yes"], no: ["Paid", "free-no"], freemium: ["Freemium", "free-mid"] };
    const fm = freeMap[freeRaw];
    const freePill = fm ? `<span class="freepill ${fm[1]}">${fm[0]}</span>` : "";
    const works = c.works_in ? `<span class="workspill" title="Which Claude surface this runs in">${esc(c.works_in)}</span>` : "";
    const metaBits = [];
    if (c.free_tokens) metaBits.push(`<span class="metapill"><b>Free tier:</b> ${esc(c.free_tokens)}</span>`);
    if (c.paid_version) metaBits.push(`<span class="metapill"><b>Paid:</b> ${esc(c.paid_version)}</span>`);
    const metaRow = metaBits.length ? `<div class="connmeta">${metaBits.join("")}</div>` : "";
    const urlLine = c.url ? `<p><a href="${esc(c.url)}" target="_blank" rel="noopener">Website / repo</a></p>` : "";
    return `<div class="card ${isStarred(c) ? "starred" : ""}">
    <h3>${isStarred(c) ? '<span class="star" title="Starred — frozen, never auto-changed">&#9733;</span>' : ""}<span class="score">${esc(c.quality_score ?? "?")}/10</span> ${esc(c.name)}
      <span class="pill">${esc(c.type || "")}</span>
      ${freePill}
      ${works}
      ${c.official ? '<span class="official">official</span>' : ""}
      ${linkedPill(c)}
      ${isStarred(c) ? '<span class="frozenpill">frozen</span>' : ""}</h3>
    <div class="sub">${esc(c.provider || "")}${c.category ? " · " + esc(c.category) : ""}${c.source ? " · src: " + esc(c.source) : ""}</div>
    <p>${esc(c.what_it_does || "")}</p>
    ${metaRow}
    ${c.install_or_source ? `<p><b>Install / source:</b> ${esc(c.install_or_source)}</p>` : ""}
    ${urlLine}
    ${srcLine}
  </div>`;
  }).join("") || empty(`No connectors match "${esc(state.query)}".`);
}

// ── Tab: Self-Improvement (health + suggestion queue + audit) ─────────────────
async function renderSelfImprove() {
  const [health, sugData, apprData, audit, starsData, selfCheck, fixTasks, review] =
    await Promise.all([
      load("health.json"), load("improvement_suggestions.json"),
      load("approvals.json"), load("improvement_audit.json"), load("stars.json"),
      load("self_check.json"), load("improvement_tasks.json"), load("review_findings.json"),
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
}

// ── Tab: Grow Sources (suggest a channel when the playlist stalls) ────────────
async function renderSources() {
  const [data, gated] = await Promise.all([
    load("channel_suggestions.json"), load("comment_gated.json")]);
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
  view.innerHTML = html;
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
  home: "#f59e0b", hub: "#f59e0b", category: "#38bdf8", toolhub: "#a78bfa",
  skill: "#34d399", tool: "#f472b6", prompt: "#fbbf24", connector: "#60a5fa",
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
    .graphhint{font-size:11px;color:var(--muted,#94a3b8);margin:7px 0 0;opacity:.75}`;
  document.head.appendChild(st);
}
async function mountBrainGraph(host) {
  ensureGraphCss();
  const data = await load("brain_graph.json");
  if (!data || !(data.nodes || []).length)
    return host.innerHTML = empty("Graph not generated yet — runs from src/build_graph.py in the pipeline.");
  const c = data.counts || {};
  host.innerHTML = `
    <div class="graphbar">
      <span class="graphcount">${c.nodes || data.nodes.length} nodes · ${c.links || (data.links || []).length} links</span>
      <input class="graphsearch" placeholder="highlight…" aria-label="highlight nodes" />
      <button class="graphreset">reset view</button>
      <span class="graphlegend">
        <span><i style="background:${GRAPH_COLORS.skill};color:${GRAPH_COLORS.skill}"></i>skill</span>
        <span><i style="background:${GRAPH_COLORS.tool};color:${GRAPH_COLORS.tool}"></i>tool</span>
        <span><i style="background:${GRAPH_COLORS.prompt};color:${GRAPH_COLORS.prompt}"></i>prompt</span>
        <span><i style="background:${GRAPH_COLORS.connector};color:${GRAPH_COLORS.connector}"></i>connector</span>
        <span><i style="background:${GRAPH_COLORS.category};color:${GRAPH_COLORS.category}"></i>category</span>
        <span><i style="background:${GRAPH_COLORS.toolhub};color:${GRAPH_COLORS.toolhub}"></i>tool-hub</span>
      </span>
    </div>
    <canvas class="braincanvas"></canvas>
    <p class="graphhint">drag background to pan · scroll to zoom · drag a dot to move it · hover to focus · click a dot to open its source</p>`;
  const canvas = host.querySelector("canvas");
  const ctx = canvas.getContext("2d");
  const H = 600;
  canvas.width = canvas.clientWidth || 800;
  canvas.height = H;
  let W = canvas.width;

  const N = data.nodes.map(n => ({ ...n, x: (Math.random() - .5) * W, y: (Math.random() - .5) * H, vx: 0, vy: 0, deg: 0 }));
  const byId = {}; N.forEach(n => byId[n.id] = n);
  const L = data.links.map(l => ({ s: byId[l.source], t: byId[l.target] })).filter(l => l.s && l.t);
  const nbr = {}; N.forEach(n => nbr[n.id] = new Set());
  L.forEach(l => { l.s.deg++; l.t.deg++; nbr[l.s.id].add(l.t.id); nbr[l.t.id].add(l.s.id); });
  const isHub = n => n.group === "home" || n.group === "category" || n.group === "toolhub" || n.group === "hub";
  const rad = n => n.group === "home" ? 9 : isHub(n) ? 6 + Math.min(4, n.deg / 8) : 3 + Math.min(3, n.deg / 3);

  let scale = 0.8, ox = W / 2, oy = H / 2, alpha = 1;
  let hover = null, drag = null, panning = false, lastX = 0, lastY = 0, hl = "";
  let raf = null, running = false;

  function tick() {
    for (let i = 0; i < N.length; i++) { const a = N[i];
      for (let j = i + 1; j < N.length; j++) { const b = N[j];
        let dx = a.x - b.x, dy = a.y - b.y, d2 = dx * dx + dy * dy + .01;
        if (d2 < 40000) { const d = Math.sqrt(d2), f = 200 / d2; dx /= d; dy /= d;
          a.vx += dx * f; a.vy += dy * f; b.vx -= dx * f; b.vy -= dy * f; } } }
    for (const l of L) { let dx = l.t.x - l.s.x, dy = l.t.y - l.s.y, d = Math.sqrt(dx * dx + dy * dy) + .01;
      const f = (d - 62) * .02; dx /= d; dy /= d;
      l.s.vx += dx * f; l.s.vy += dy * f; l.t.vx -= dx * f; l.t.vy -= dy * f; }
    for (const n of N) { n.vx += -n.x * .002; n.vy += -n.y * .002;
      if (n === drag) continue;
      n.x += n.vx * alpha; n.y += n.vy * alpha; n.vx *= .85; n.vy *= .85; }
    alpha *= .985;
  }
  function draw() {
    ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.clearRect(0, 0, W, H);
    ctx.setTransform(scale, 0, 0, scale, ox, oy);
    const focus = hover ? nbr[hover.id] : null;
    const settled = !running;                          // glow only when not animating (perf-safe)
    // edges — WHITE on black; highlighted neighbours brighten, the rest recede
    for (const l of L) {
      const on = hover && (l.s === hover || l.t === hover);
      const fade = (hl || (hover && !on)) ? .045 : .12;
      ctx.strokeStyle = on ? "rgba(255,255,255,.95)" : `rgba(255,255,255,${fade})`;
      ctx.lineWidth = (on ? 1.5 : .7) / scale;
      ctx.beginPath(); ctx.moveTo(l.s.x, l.s.y); ctx.lineTo(l.t.x, l.t.y); ctx.stroke();
    }
    ctx.font = (11 / scale) + "px ui-sans-serif, system-ui";
    for (const n of N) {
      const dim = (hover && n !== hover && !focus.has(n.id)) ||
                  (hl && !(n.label || "").toLowerCase().includes(hl));
      ctx.globalAlpha = dim ? .12 : 1;
      const col = GRAPH_COLORS[n.group] || "#94a3b8";
      ctx.fillStyle = col;
      // soft glow on the anchors (hubs) + the hovered node = premium "constellation" feel
      if (settled && !dim && (isHub(n) || n === hover)) { ctx.shadowColor = col; ctx.shadowBlur = isHub(n) ? 16 : 11; }
      ctx.beginPath(); ctx.arc(n.x, n.y, rad(n), 0, 7); ctx.fill();
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
  window.__graphStop = () => { running = false; if (raf) cancelAnimationFrame(raf); };

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
  canvas.addEventListener("click", e => { const n = pick(e); if (n && n.url) window.open(n.url, "_blank", "noopener"); });
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
async function renderDevConstruction() {
  const data = await load("dev_construction.json");
  const secs = (data && data.sections) || [];
  let html = `<div class="sub">${esc((data && data.intro) || "")}</div>`;
  html += `<div class="card">
      <h3>🧠 Project knowledge graph — the Obsidian brain, live</h3>
      <div id="braingraph" class="braingraph"></div>
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
  const gh = document.getElementById("braingraph");
  if (gh) mountBrainGraph(gh);
}

// ── Tab: Effectiveness — how good & how rigid each retrieval/analysis lane is ──
// Measured scoreboard (data/effectiveness.json) that the self-improvement system targets.
const DIM_LABEL = { quality: "Quality", quantity: "Quantity", form: "Form", time: "Time",
  tokens: "Tokens", ease_external: "Ext.access", ease_project: "Proj.access", ease_user: "User access" };
async function renderEffectiveness() {
  const d = await load("effectiveness.json");
  if (!d || !d.lanes) {
    view.innerHTML = `<div class="card"><h3>Extraction Effectiveness</h3>${empty(
      "Scoreboard not generated yet — it runs every analysis cycle (~3h).")}</div>`;
    return;
  }
  const dims = d.dimensions || [];
  let html = `<div class="card"><h3>Extraction Effectiveness &amp; Rigidity</h3>
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

// ── tab router ───────────────────────────────────────────────────────────────
async function show(tab) {
  state.activeTab = tab;
  if (window.__graphStop) window.__graphStop();   // stop any running graph animation
  document.querySelectorAll("nav button").forEach(b =>
    b.classList.toggle("active", b.dataset.tab === tab));
  view.innerHTML = empty("Loading…");
  await renderTab(tab);
  // One bulleted "Updates: …" line at the very top of the tab (lists every update type).
  const c = cadenceLine(tab);
  if (c) view.insertAdjacentHTML("afterbegin", c);
  // If quick-read is on, actually condense the descriptions (not just CSS-clamp them).
  quickreadSummarize(document.body.classList.contains("quickread"));
}

async function renderTab(tab) {
  if (tab === "skills") return renderSkills(await load("skills.json"));
  if (tab === "tools" || tab === "models")
    return renderToolRating(await load("tools.json"), await load("models.json"));
  if (tab === "comingsoon") return renderComingSoon(await load("tools.json"));
  if (tab === "prompts") return renderPrompts(await load("prompts.json"));
  if (tab === "devbuild") return renderDevConstruction();
  if (tab === "improvement") return renderImprovement();
  if (tab === "tips") return renderTips();
  if (tab === "news") return renderNews();
  if (tab === "connectors") return renderConnectors(await load("connectors.json"));
  if (tab === "sources") return renderSources();
  if (tab === "selfimprove") return renderSelfImprove();
  if (tab === "effectiveness") return renderEffectiveness();
  if (tab && tab.startsWith("dyn:")) return renderDynamicTab(tab.slice(4));
}

document.querySelectorAll("nav button").forEach(b =>
  b.addEventListener("click", () => show(b.dataset.tab)));

(async () => {
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

  show("skills");
})();
