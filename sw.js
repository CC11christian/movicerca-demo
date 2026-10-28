// MoviCerca v0.9: cache solo de interfaz local. No guarda coordenadas ni archivos importados.
const CACHE='movicerca-shell-v242';
const SHELL=['./','./index.html','./manifest.webmanifest','./icons/icon-192.png','./icons/icon-512.png'];
self.addEventListener('install',event=>event.waitUntil(caches.open(CACHE).then(cache=>cache.addAll(SHELL)).then(()=>self.skipWaiting())));
self.addEventListener('activate',event=>event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(key=>key.startsWith('movicerca-shell-')&&key!==CACHE).map(key=>caches.delete(key)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',event=>{
 const request=event.request;
 const url=new URL(request.url);
 if(request.method!=='GET'||url.origin!==self.location.origin)return;
 // External maps, APIs and dynamic imports are never intercepted.
 const isNavigation=request.mode==='navigate';
 event.respondWith(fetch(request).then(response=>response).catch(async()=>{
  if(isNavigation)return (await caches.match('./index.html'))||Response.error();
  return (await caches.match(request))||Response.error();
 }));
});
