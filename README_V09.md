# MoviCerca v0.9 — corrección del SVG de Leaflet

## Causa confirmada en el código

La regla `.map svg { width:100%; height:100% }` ampliaba cualquier SVG dentro del mapa, incluyendo el símbolo azul y amarillo de atribución de Leaflet. El enlace a leafletjs.com era parte de la atribución y no un anuncio.

## Corrección

- La regla de SVG de pantalla completa se aplica **únicamente** al SVG de respaldo propio (`.map > svg.movicerca-fallback-svg`).
- La bandera de atribución de Leaflet tiene un tamaño máximo definido expresamente.
- Se conserva la capa de calles, GPS, buscador y paradas.
- Se actualiza la caché del service worker a v09.

## Actualización de GitHub Pages

Sube los archivos del directorio de esta versión a la raíz del repositorio, reemplazando los de v0.8. Conserva `icons/` y `.nojekyll`. Comprueba en Actions que Pages publicó correctamente. En iPhone, abre la dirección con Safari y realiza una recarga; si se ha instalado como PWA y sigue mostrando la versión antigua, elimina la instalación anterior y vuelve a añadirla desde el navegador.

La versión no añade estaciones nuevas ni resuelve problemas de proveedor o red.
