# MoviCerca v2.5.1 — Corrección de búsqueda por lugares

## Cambios
- Prioriza coincidencias exactas de estaciones existentes en los catálogos locales (Metro, Metrobús, Trolebús, Cablebús y Tren Ligero).
- Cuando hay varias estaciones del mismo nombre, pide elegir la opción.
- La búsqueda de Nominatim **nunca** cambia la ubicación automáticamente: pide seleccionar una coincidencia.
- Rechaza respuestas que no contienen términos significativos del lugar buscado; no inventa coordenadas.
- Al fallar una búsqueda conserva el origen anterior y lo comunica expresamente.
- Una búsqueda anterior no puede sobrescribir el origen seleccionado después.
- Renueva el caché de la PWA.

## Publicación
En GitHub Pages reemplaza únicamente `index.html` y `sw.js` en la raíz, confirma el commit y abre la web en Safari privado. No borres los archivos `data/*.json` ni los workflows.

## Pruebas
1. Busca `Metro Observatorio` y `Metro Pantitlán`: cuando el catálogo está cargado, se debe encontrar la estación correspondiente.
2. Busca una calle o lugar: selecciona expresamente la opción correcta antes de mover el mapa.
3. Escribe un lugar inexistente: el mapa y el origen no deben cambiar.
4. Busca una dirección y luego activa GPS: debe respetar tu última selección.
5. Comprueba Consulado, San Juan de Aragón, ECOBICI y comparación por modalidad.

Limitación: La coincidencia de nombre de estación depende de los datos y de la ortografía del catálogo. En las direcciones el usuario debe seleccionar el lugar; distancias en línea recta.
