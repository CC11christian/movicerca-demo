# MoviCerca v1.3 — Corrección de cobertura

## Cambios
- Conserva las funciones que funcionaron en v1.2: GPS, búsqueda de dirección, mapa corregido y navegación peatonal a Google Maps.
- Consultas ArcGIS mediante JSON con coordenadas WGS84; se normalizan atributos por capa.
- Más nombres alternativos de campos para las paradas.
- Reintentar fuentes sin recargar la PWA; diagnóstico por modalidad con recuento o error.
- Los puntos GTFS importados no se borran cuando termina una consulta de capas.
- Service worker versionado v13.

## Limitación importante
**No se consiguió descargar ni auditar el catálogo completo oficial en el entorno de creación.** Esta versión mejora la recuperación y el diagnóstico pero **no garantiza cobertura completa ni actualidad de rutas**. Las fuentes externas pueden fallar por conectividad/CORS. Los datos son estáticos: no se incluyen vehículos, llegadas ni horarios en tiempo real. La importación manual de `stops.txt` admite paradas pero no asigna automáticamente líneas o tipos; para hacerlo hay que relacionar `routes`, `trips`, `stop_times`, `agency`.

## Actualizar GitHub Pages
Extrae el ZIP y coloca su contenido (index.html, sw.js, manifest.webmanifest, icons/, documentos) en la raíz de tu repositorio. Haz commit, confirma despliegue verde en Actions y abre el sitio en pestaña privada. Si permanece una versión anterior, revisa la caché del service worker.

## Pruebas sugeridas
1. Busca Parques Polanco, y comprueba Metro Polanco y San Joaquín.
2. Abre Diagnóstico por modalidad y registra qué fuentes entregan puntos y cuáles fallan.
3. Toca Reintentar fuentes, prueba radios de 2 y 5 km.
4. Importa un `stops.txt` oficial y verifica que las paradas sigan visibles cuando finalice la consulta a fuentes.
5. Verifica que «Cómo llegar caminando» siga abriendo Google Maps.

Fuentes: https://serviciosatlas.sgirpc.cdmx.gob.mx/arcgis/rest/services/AtlasCapasPublicas/Movilidad_Integrada_CDMX/FeatureServer y https://datos.cdmx.gob.mx/dataset/gtfs.
