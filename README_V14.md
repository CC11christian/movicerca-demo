# MoviCerca v1.4 — Diagnóstico y recuperación de cobertura

## Hallazgo
La versión anterior usaba IDs fijos de capas ArcGIS y rechazaba geometrías que no fueran Point. Un filtro visible no implicaba que existiesen estaciones cargadas. El catálogo incorporado solo contenía ocho estaciones.

## Correcciones
- Referencias de Metro Talismán (L4) y Metrobús Avenida Talismán (L7), con ubicación documentada.
- Selector de zona Talismán.
- Importador de GTFS ZIP con clasificación preliminar usando agency/routes/trips/stop_times. Se lee **localmente**, no se sube a servidores de MoviCerca.
- Conservadas las funciones confirmadas: GPS, dirección, mapa, botones a pie y corrección Leaflet.

## Uso para ampliar la cobertura
1. Descargar el ZIP GTFS de la fuente oficial: https://datos.cdmx.gob.mx/dataset/gtfs o la versión de Metrobús https://hdtp.codeandomexico.org/datos/mex-cdmx-cdmx-metrobus. Comprobar fecha, licencia y procedencia.
2. En MoviCerca abrir «Importar un catálogo GTFS de paradas» y seleccionar ZIP.
3. Seleccionar zona Talismán o buscar una dirección y probar radio de 2–5 km.
4. Revisar las líneas: la relación se aproxima utilizando un viaje por parada. Una parada puede servir a múltiples rutas, todavía no se muestran todas.

## Límites
No hay catálogo ZIP adjunto por falta de acceso a su descarga desde el entorno de creación. Sin importación seguirá habiendo cobertura parcial. La lectura ZIP depende de JSZip vía CDN. Los feeds públicos pueden contener errores o información antigua. Este prototipo no contiene datos en tiempo real. Se conservan los controles de diagnóstico de ArcGIS, que aún podrían fallar por CORS, campos inesperados o geometrías no puntuales.

## Publicación
Sustituir en GitHub Pages los archivos de la raíz por los de esta carpeta y comprobar Actions. Para descartar caché antigua, probar en una pestaña privada de Safari.
