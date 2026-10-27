# MoviCerca v1.8 — catálogo local de Metro y Metrobús

## Qué cambia
- Mantiene el GPS, búsqueda por dirección, mapa Leaflet corregido, fichas, pagos y rutas peatonales externas de v1.7.
- **Busca primero `data/stations_cdmx.json`**, un catálogo local que se puede generar con GitHub Actions.
- Si falta el catálogo o no supera controles mínimos, advierte de cobertura parcial e intenta las consultas externas anteriores.
- Incluye `scripts/update_catalog.py`, que obtiene estaciones de las capas 0 y 2 del Atlas de Movilidad CDMX por IDs y las guarda con nombre, línea, ubicación, fuente y fecha de generación.
- Valida cantidad de estaciones y presencia de Metro Talismán, Polanco, San Joaquín, Bellas Artes y Metrobús Talismán. Si hay fallos, **no sobrescribe el último catálogo válido**.

## Cómo publicar desde GitHub Pages
1. Conserva una copia del repositorio y sube a la raíz todos los archivos de este paquete, **incluida la carpeta oculta `.github/workflows/`** y `scripts/`.
2. En GitHub entra a `Actions > Actualizar catalogo de estaciones > Run workflow`. Si no aparece, comprueba que el archivo `.github/workflows/update-catalog.yml` se subió correctamente.
3. El workflow descargará y validará los datos. Si termina en verde, registrará `data/stations_cdmx.json` y GitHub Pages publicará la actualización.
4. Abre la aplicación y comprueba `Diagnóstico por modalidad`: deberá mostrar Metro y Metrobús, conteos y fecha de generación.
5. Si falla, abre el registro del workflow. El proceso está diseñado para no sustituir un catálogo válido con datos incompletos.
6. Si GitHub Actions no tiene permiso para registrar cambios: `Settings > Actions > General > Workflow permissions > Read and write permissions` (si tu cuenta lo permite). Otra alternativa es ejecutar el script en otro entorno conectado y subir el JSON revisado.

## Limitaciones importantes
- Esta entrega **no incluye el catálogo oficial completo descargado**, porque el servidor del Atlas no pudo resolverse desde el entorno de desarrollo. La descarga se ejecutará en GitHub Actions cuando autorices el workflow.
- El éxito de la descarga, la actualización del repositorio y la cobertura completa aún no se han verificado. Las capas de Atlas podrían carecer de estaciones nuevas.
- `generated_at` marca cuándo se generó el catálogo, **no** garantiza que el operador haya actualizado la información en esa fecha.
- No hay disponibilidad en vivo, estimaciones de espera, ni estados de operación verificables.
- La fuente oficial de capas es `https://serviciosatlas.sgirpc.cdmx.gob.mx/arcgis/rest/services/AtlasCapasPublicas/Movilidad_Integrada_CDMX/FeatureServer` (capas 0 y 2). Revisar sus términos de reutilización y mantener atribución al Atlas CDMX.
- El workflow se ejecuta una vez por semana; se puede usar manualmente para pruebas.

## Pruebas
- `python -m unittest discover -s scripts -p 'test_*.py' -v`
- `node --check` sobre el bloque JavaScript de `index.html`.
- Prueba manual: busca Talismán, Polanco y Centro Histórico sin utilizar el botón de diagnóstico. Compara los resultados con los mapas oficiales. Revisa distancias y líneas.
