# MoviCerca v1.9 — rutas y depuración de interfaz

## Cambios
- Retirado el botón de prueba **Comprobar Talismán** (la búsqueda normal permanece).
- Las fichas distinguen **línea/ruta publicada** de **sentido de circulación no verificado**. No se inventa el sentido a partir de la ubicación de una estación.
- Se mantienen filtros y conexiones experimentales de RTP, Trolebús, Tren Ligero, Cablebús, ECOBICI y transporte concesionado del Atlas; **no son catálogos completos ni garantizan su carga**.
- Se conserva el catálogo local `data/stations_cdmx.json` de Metro/Metrobús mediante el mecanismo existente.
- Se incrementó la versión de caché PWA a v19.

## Publicación
1. Antes de subir, descargar una copia ZIP del repositorio y comprobar que `data/stations_cdmx.json` está presente.
2. Sustituir los archivos de la PWA en GitHub por los de este paquete. **No borrar** la carpeta `data` ni el `update_catalog.py` o el workflow vigente.
3. Verificar Pages/Actions en verde y abrir en Safari con recarga.
4. Probar Talismán, Polanco y Centro Histórico. Revisar que ya no aparezca el botón de prueba.

## Limitaciones
No se integraron feeds GTFS adicionales de rutas ni sentidos. Los registros Metro/Metrobús siguen siendo *estaciones*, no trayectos. No hay información de servicio en vivo ni llegadas. Los datos de las otras modalidades siguen dependiendo de consultas externas al Atlas y podrían estar incompletos.
