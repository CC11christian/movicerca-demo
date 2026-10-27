# MoviCerca v0.4 — PWA experimental

## Qué incluye
- Aplicación web adaptada a móvil, mapa interactivo Leaflet/OpenStreetMap cuando hay red.
- Configuración PWA: `manifest.webmanifest`, iconos, service worker con caché del núcleo local.
- Ubicación GPS opcional, zona predefinida y coordenadas manuales.
- Seis estaciones de muestra con enlaces a sus fuentes; radio y filtros, importación manual de `stops.txt` (GTFS).
- Distancia en línea recta, **no** rutas caminando ni horarios en vivo.

## Probar en computadora sin instalar nada
Extrae el ZIP y abre `index.html` en Chrome o Edge. El mapa usa internet. En modo archivo local (`file://`) el navegador normalmente no admite instalación PWA ni GPS.

## Probar como PWA en localhost
Con Python 3 instalado, abre una terminal en esta carpeta y ejecuta:

```sh
python -m http.server 8000
```

En el navegador abre http://localhost:8000/ . Si Chrome/Edge considera instalable el proyecto, mostrará la opción **Instalar MoviCerca** o el botón de instalación del navegador. En iPhone, normalmente usa Safari → Compartir → Añadir a pantalla de inicio, bajo HTTPS.

## Probar en un celular
Es necesario publicar los archivos estáticos en un proveedor de hosting con HTTPS para una experiencia de instalación y GPS. No se ha publicado ni conectado a terceros. Abre entonces la URL segura en Chrome (Android) o Safari (iOS).

## Limitaciones y privacidad
- El modo sin conexión es básico: se conserva la interfaz después de una primera visita correcta. La librería Leaflet y los mosaicos OpenStreetMap vienen de servicios externos y **no** se garantizan offline.
- Sin red, la importación del usuario solo dura la sesión (se almacena en memoria, no se envía ni se sincroniza).
- La localización permanece en memoria del navegador; no se envía a un backend MoviCerca. El proveedor de mosaicos sí recibe las peticiones de mapa; revisa su política de privacidad.
- No se han integrado rutas peatonales ni red completa GTFS; datos de muestra no equivalen a cobertura total.
- El uso comercial debe revisar licencias, disponibilidad, atribuciones y política de uso de mosaicos.

## Comprobaciones incluidas
Revisar manifest, iconos, registro condicionado del service worker, importación `stops.txt`, controles de ubicación y filtros. Pruebas sobre dispositivos reales aún pendientes.
