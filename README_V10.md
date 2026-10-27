# MoviCerca v1.0 — fichas de estaciones e indicaciones

## Qué cambió
- Los resultados de estaciones ahora son botones que abren una ficha con modalidad, línea/ruta cuando hay datos, distancia recta y enlace externo **Cómo llegar caminando**.
- Los marcadores del mapa tienen una acción **Ver detalles**.
- Indicaciones externas con Google Maps en modo walking; el trayecto y duración real son responsabilidad del proveedor.
- Se conserva la regla CSS que limita el SVG de respaldo: `.map > svg.movicerca-fallback-svg`. NO aplicar `.map svg {width:100%;height:100%}`.
- Se actualiza caché del service worker a v10.

## Datos y límites
- Incluye la misma muestra de estaciones y consulta opcional al Atlas público CDMX que v0.9. No hay cobertura nacional completa.
- La aplicación distingue distancia en línea recta de ruta peatonal ofrecida por Google Maps. El punto de una estación no siempre corresponde al acceso peatonal; verificar al viajar.
- Para GTFS importado solo con `stops.txt` no se puede conocer línea, ruta y dirección; se necesita unir `routes.txt`, `trips.txt`, `stop_times.txt` y `agency.txt`.
- No hay tiempos en vivo ni precios.
- PWA/GPS requieren HTTPS o localhost. Tras publicar en GitHub Pages, recarga o reinstala si Safari conserva la caché.

## Actualización de GitHub Pages
1. Descarga el ZIP y extrae la carpeta.
2. Sube **el contenido** de la carpeta a la raíz del repositorio, sustituyendo index.html, sw.js y los otros archivos de la PWA.
3. Revisa Actions y abre tu URL HTTPS.
4. Busca Parques Polanco o usa GPS, elige Polanco y toca su nombre o marcador; pulsa **Cómo llegar caminando**.

## Comprobaciones recomendadas
- Búsqueda por dirección y GPS; visualización sin bandas de Leaflet.
- Fichas Polanco y San Joaquín con Línea 7.
- Enlaces externos abren indicaciones a pie.
- Modo sin calles y estado de error del catálogo externo.
