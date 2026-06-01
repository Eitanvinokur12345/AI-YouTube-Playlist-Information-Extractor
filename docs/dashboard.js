// Minimal client-side dashboard. Reads the committed JSON files from ../data.
// Renders five tabs. Expanded once the pipeline produces real data.
const DATA = "../data/";
const view = document.getElementById("view");
const meta = document.getElementById("meta");

async function load(file) {
  try {
    const r = await fetch(DATA + file, { cache: "no-store" });
    if (!r.ok) return null;
    return await r.json();
  } catch { return null; }
}

function render(tab, data) {
  if (!data) { view.innerHTML = `<p class="empty">No data yet for "${tab}". Run the pipeline.</p>`; return; }
  view.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
}

const tabFiles = {
  skills: "skills.json",
  models: "models.json",
  merges: "merge_log.json",
  tips: "tips.json",
  news: "weekly_news.json",
};

async function show(tab) {
  document.querySelectorAll("nav button").forEach(b =>
    b.classList.toggle("active", b.dataset.tab === tab));
  render(tab, await load(tabFiles[tab]));
}

document.querySelectorAll("nav button").forEach(b =>
  b.addEventListener("click", () => show(b.dataset.tab)));

(async () => {
  const status = await load("status.json");
  meta.textContent = status?.last_run
    ? `Last run: ${status.last_run} • Videos seen: ${status.videos_seen ?? 0} • Skills: ${status.total_skills ?? 0}`
    : "No runs yet.";
  show("skills");
})();
