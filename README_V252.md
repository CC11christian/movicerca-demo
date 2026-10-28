# MoviCerca v2.5.2 — Corrección de origen erróneo

## Problema
El selector comienza en Glorieta de Insurgentes como demostración. Si una búsqueda no devolvía una coincidencia verificable, seguía mostrándose el transporte de esa zona, aunque el usuario hubiera escrito Observatorio o Pantitlán. Además, las búsquedas podían ejecutarse antes de cargar `stations_cdmx.json`.

## Cambios
- Al iniciar una búsqueda, **oculta la lista y comparación del origen anterior** hasta elegir una coincidencia válida. Si falla, mantiene el mapa anterior pero no presenta alternativas como si fueran del lugar buscado.
- Espera a que finalice la carga del catálogo Metro/Metrobús (hasta 6,5 segundos) antes de buscar coincidencias exactas de estaciones.
- Busca estaciones del Metro solo en Metro cuando la consulta empieza por `Metro`, y estaciones de Metrobús solo en Metrobús.
- Mantiene selección explícita de resultados de Nominatim, búsqueda GPS, transbordos, ECOBICI, distancia y demás funciones de v2.5.
- Incrementa la versión de caché PWA.

## Publicación
Sustituye `index.html` y `sw.js` en la raíz de GitHub Pages; conserva `data/`, `.github/` y `scripts/`. Comprueba en Safari privado que la cabecera sea v2.5.2.

## Prueba
1. Recarga página y espera a que el catálogo esté disponible. Busca `Metro Observatorio`. Confirma el origen o elige una coincidencia: **nunca** debe mostrar comparaciones de Insurgentes como si pertenecieran a Observatorio.
2. Repite `Metro Pantitlán`.
3. Busca un lugar inexistente. Debe informar que no se encontró y **no mostrar resultados del origen anterior**, hasta elegir una ubicación válida, usar GPS o borrar la búsqueda.
4. Verifica GPS, ECOBICI, y estaciones de transbordo.

**Límite:** no se ha probado en Safari real ni se ha publicado. Si el catálogo no se descarga y Nominatim no identifica el nombre, la app informará que no encontró la ubicación; no inventará coordenadas.
