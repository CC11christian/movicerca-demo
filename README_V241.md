# MoviCerca v2.4.1 — corrección de transbordos

## Cambios

- Los identificadores de línea Metro que vienen como `04` y `05` se interpretan como líneas 4 y 5.
- Para estaciones de correspondencia conocidas con el mismo nombre normalizado se permite hasta 500 metros entre puntos; el resto conserva el criterio de 35 metros.
- No se combinan modos diferentes (Metro y Metrobús no se fusionan).
- Solo se etiqueta **Transbordo** cuando existen al menos dos líneas distintas identificadas.
- Nueva versión del caché PWA para la actualización.

## Publicación

Sube `index.html` y `sw.js` a la raíz de GitHub Pages. Conserva `data/stations_cdmx.json`, `data/stations_secondary_cdmx.json`, `.github/workflows/` y `scripts/`.

## Pruebas desde Safari

En pestaña privada busca Consulado: debe verse una sola ficha de Metro con líneas 4 y 5 si los registros están en el catálogo y sus coordenadas están dentro de 500 m. Revisa también que no se hayan fusionado estaciones de otros operadores y que ECOBICI, búsqueda por dirección y GPS sigan funcionando.

Nota: sin ejecución en Safari no se garantiza todavía el resultado con el catálogo publicado.
