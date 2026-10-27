# MoviCerca v2.1 — ECOBICI GBFS

Esta versión sustituye la consulta experimental de ECOBICI al Atlas por el feed oficial GBFS: `https://gbfs.mex.lyftbikes.com/gbfs/gbfs.json`. Descubre `station_information` y `station_status`, los une por `station_id` y permite mostrar bicicletas, anclajes y estado en la ficha de cicloestación.

**Aviso:** la información depende de que el feed permita peticiones directas desde Safari/Chrome (CORS) y de la calidad de sus marcas de tiempo. El código no garantiza la conectividad desde GitHub Pages. Ante fallos muestra un error en «Estado de las fuentes». Si las lecturas no son vigentes (umbral 15 minutos), no se muestran cifras como disponibles. Los datos no se guardan ni se inventan.

## Publicación

1. Guarda una copia de la versión estable.
2. Actualiza los archivos de esta carpeta en la raíz del repositorio, conservando `data/stations_cdmx.json` y el workflow que ya funciona.
3. Verifica el despliegue en Actions.
4. Abre MoviCerca en una pestaña nueva y selecciona filtro ECOBICI en Polanco o Insurgentes.
5. Abre «Estado de las fuentes». Verifica que se muestre `ECOBICI (GBFS)` con conteo o un error explícito; toca una cicloestación para ver disponibilidad, fuente y actualización.

El script no modifica GPS, geocodificación, mapa Leaflet ni catálogo Metro/Metrobús. La disponibilidad de bicicletas es información orientativa y puede cambiar rápidamente.

Fuente: https://ecobici.cdmx.gob.mx/datos-abiertos/
