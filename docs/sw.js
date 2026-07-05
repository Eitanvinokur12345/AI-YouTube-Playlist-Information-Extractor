// Service worker for the AI Skills Tracker (Excavatortron) dashboard.
//
// Jobs:
//   1. Make the dashboard installable as a PWA on phone AND desktop.
//   2. Cache the app SHELL so it loads instantly and works with no connection.
//   3. Cache DATA files (../data/*.json, config.json) so the dashboard shows
//      the LAST KNOWN data when offline â€” always tries the network first so
//      you always see fresh data when connected.
//
// Bump SHELL_CACHE to force the shell to refresh (after changing index.html/dashboard.js).
// DATA_CACHE version is independent; bump it to purge old data caches.
const SHELL_CACHE = "ai-skills-shell-v66";
const DATA_CACHE  = "ai-skills-data-v1";
const SHELL = [
  "./", "./index.html", "./dashboard.js", "./manifest.webmanifest", "./icon.png",
];

// â”€â”€ install: pre-cache the app shell â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(SHELL_CACHE)
      .then((cache) => cache.addAll(SHELL))
      .then(() => self.skipWaiting())
      .catch(() => {})          // never block install on a cache failure
  );
});

// â”€â”€ activate: evict caches from old versions â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(
        keys
          .filter((k) => k !== SHELL_CACHE && k !== DATA_CACHE)
          .map((k) => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

// â”€â”€ fetch â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);

  // â”€â”€ JSON data files (../data/*.json and ../config.json) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
  // Strategy: network-first, update cache on success, serve cached copy offline.
  // This means: when online, you always see the freshest data; when offline, you
  // see the last version that was loaded while online.
  if (url.pathname.endsWith(".json")) {
    event.respondWith(
      fetch(req)
        .then((resp) => {
          if (resp.ok) {
            const copy = resp.clone();
            caches.open(DATA_CACHE).then((c) => c.put(req, copy)).catch(() => {});
          }
          return resp;
        })
        .catch(() =>
          caches.open(DATA_CACHE)
            .then((c) => c.match(req))
            .then((m) => m || new Response("{}", {
              status: 200,
              headers: { "Content-Type": "application/json" },
            }))
        )
    );
    return;
  }

  // â”€â”€ App shell (html / js / manifest / images / css) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
  // Strategy: network-first so updates appear promptly; fall back to cache offline.
  if (!url.pathname.endsWith("/") && !/\.(html|js|webmanifest|png|css|svg|ico)$/.test(url.pathname)) {
    return; // everything else (YouTube links, etc.) goes straight to the network
  }
  event.respondWith(
    fetch(req)
      .then((resp) => {
        const copy = resp.clone();
        caches.open(SHELL_CACHE).then((c) => c.put(req, copy)).catch(() => {});
        return resp;
      })
      .catch(() =>
        caches.match(req).then((m) => m || caches.match("./index.html"))
      )
  );
});
