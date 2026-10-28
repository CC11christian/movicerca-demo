# MoviCerca v2.4 — Correspondencias de Metro

## Qué cambia
- Une registros de un mismo complejo de Metro cuando comparten nombre normalizado, están próximos y se trata de una correspondencia conocida (hasta 180 m).
- Conserva y muestra todas las líneas explícitas publicadas en los registros; no inventa líneas.
- Muestra «⇄ Transbordo» solo cuando se detectan dos o más líneas distintas de una correspondencia conocida.
- Mantiene el filtrado de duplicados de 35 m para otras estaciones, y las estaciones de ECOBICI siguen separadas por ID.
- Conserva GPS, búsqueda por dirección, mapa, catálogo local, ECOBICI y detalles de pago.
- Actualiza la caché de PWA a v24.

## Publicación
1. Extrae este ZIP.
2. Sube los archivos y carpetas a la raíz de `CC11christian/movicerca-demo`, respetando `.github/`, `scripts/`, `icons/` y los archivos de la PWA.
3. No elimines los catálogos `data/stations_cdmx.json` y `data/stations_secondary_cdmx.json` ya generados en GitHub (no están incluidos en este ZIP).
4. Espera la publicación de GitHub Pages; prueba en Safari en pestaña privada.

## Pruebas recomendadas
- Consulado: una ficha de Metro con las líneas 4 y 5 si el catálogo aporta ambas líneas.
- Pantitlán: agrupar líneas únicamente cuando el catálogo indique números explícitos y los puntos estén a 180 m o menos.
- Metro Insurgentes: sigue siendo estación individual.
- ECOBICI, Trolebús y Metrobús: no se agrupan entre modalidades.
- Cambio GPS/dirección y búsqueda inicial: deben conservar el comportamiento v2.3.

## Limitaciones
La agrupación de correspondencias no demuestra que las entradas estén físicamente conectadas ni que haya servicio activo. Los puntos a más de 180 m permanecen separados. Si una línea no viene explícitamente identificada, no se infiere. No se han modificado las capas de datos ni las automatizaciones.
