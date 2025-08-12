const CACHE_NAME = "portraitiste-cache-v3";

const urlsToCache = [
    "/",
    "/static/css/style.css",
    "/static/js/main.js",
    "/static/images/icon-192.png",
    "/static/images/icon-512.png",
    "/static/offline.html"
];

// Installation
self.addEventListener("install", event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => cache.addAll(urlsToCache))
    );
    self.skipWaiting();
});

// Activation
self.addEventListener("activate", event => {
    event.waitUntil(
        caches.keys().then(names => 
            Promise.all(names.filter(n => n !== CACHE_NAME).map(n => caches.delete(n)))
        )
    );
    self.clients.claim();
});

// Fetch avec fallback hors-ligne
self.addEventListener("fetch", event => {
    event.respondWith(
        fetch(event.request)
            .then(response => {
                // On met à jour le cache
                const responseClone = response.clone();
                caches.open(CACHE_NAME).then(cache => cache.put(event.request, responseClone));
                return response;
            })
            .catch(() => {
                // Si hors-ligne → on regarde dans le cache
                return caches.match(event.request).then(cachedResponse => {
                    // Si toujours rien → page hors-ligne
                    return cachedResponse || caches.match("/static/offline.html");
                });
            })
    );
});
