# MoviCerca v0.7 — revisión de Polanco y mapa móvil

- Incluye estaciones de respaldo verificadas para Metro Polanco y Metro San Joaquín (L7).
- Consulta las capas 0 y 2 del Atlas CDMX (Metro y Metrobús) en el navegador; la carga depende de disponibilidad y CORS.
- Si la consulta no funciona, se informa que se utiliza una muestra limitada y siguen las estaciones de respaldo.
- El mapa usa teselas Esri World Street Map con fines de prototipo. Revisar condiciones/licencia antes de producción.
- Radio inicial 2 km, nueva zona Polanco y mapa móvil corregido.
- GPS: requiere HTTPS, permisos del sistema y del navegador. No se guardan coordenadas en servidores propios.
- La distancia sigue siendo en línea recta y no prueba disponibilidad de vehículos.
- Si no ves cambios al subirlo a GitHub Pages, elimina el sitio de los datos de Safari o abre una ventana privada; el service worker cambia a v07.
- **Publicación**: subir todos los archivos de esta carpeta a la raíz del repositorio GitHub Pages, sin colocar la carpeta como subcarpeta.

Fuentes:
- https://serviciosatlas.sgirpc.cdmx.gob.mx/arcgis/rest/services/AtlasCapasPublicas/Movilidad_Integrada_CDMX/FeatureServer/layers
- https://metro.cdmx.gob.mx/la-red/linea-7/polanco
- https://metro.cdmx.gob.mx/la-red/linea-7/san-joaquin
