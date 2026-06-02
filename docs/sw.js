// Minimal service worker for the AI Skills Tracker dashboard.
//
// Its only jobs are (1) make the dashboard installable as a PWA on a phone AND a
// computer, and (2) let the app SHELL load even with no connection. It deliberately
// does NOT cache ../data (the JSON results), which change constantly and live outside
// this service worker's scope anyway — those requests always go straight to the network
// so you always see fresh data. Bump CACHE_VERSION to force the shell to refresh.
const CACHE_VERSION = "ai-skills-shell-v1";
const SHELL = [
  "./", "./index.html", "./dashboard.js", "./manifest.webmanifest", "./icon.png",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_VERSION)
      .then((cache) => cache.addAll(SHELL))
      .then(() => self.skipWaiting())
      .catch(() => {})
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE_VERSION).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  // Only manage the static shell (html/js/manifest/png/css). Everything else — notably
  // the ../data/*.json results — falls through to the normal network fetch.
  if (!url.pathname.endsWith("/") && !/\.(html|js|webmanifest|png|css)$/.test(url.pathname)) return;
  // Network-first so shell updates appear promptly; fall back to cache when offline.
  event.respondWith(
    fetch(req)
      .then((resp) => {
        const copy = resp.clone();
        caches.open(CACHE_VERSION).then((c) => c.put(req, copy)).catch(() => {});
        return resp;
      })
      .catch(() => caches.match(req).then((m) => m || caches.match("./index.html")))
  );
});
