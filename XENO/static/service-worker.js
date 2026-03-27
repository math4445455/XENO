self.addEventListener("install", event => {
  event.waitUntil(
    caches.open("lhama45-cache").then(cache => {
      return cache.addAll(["/"]);
    })
  );
});

self.addEventListener("fetch", event => {
  event.respondWith(
    fetch(event.request).catch(() => caches.match("/"))
  );
});