# MoviCerca v2.2 — Ampliación prudente de movilidad CDMX

## Qué cambia
- Conserva el GPS, buscador, mapa Leaflet, catálogo Metro/Metrobús y ECOBICI GBFS de la versión v2.1.
- Admite `data/stations_secondary_cdmx.json` para RTP, Trolebús, Tren Ligero, Cablebús y concesionado, si GitHub Actions logra generarlo.
- Mantiene la carga externa progresiva como respaldo si el catálogo opcional no existe.
- No confunde registros de líneas o polígonos con estaciones. Solo importa puntos con nombre y coordenadas válidos.
- No afirma que una modalidad esté operando ni muestra esperas inventadas; los estados y llegadas reales siguen sin conexión.

## Publicación
Sube los archivos de este paquete a la raíz del repositorio, conservando `data/stations_cdmx.json` (catálogo Metro/Metrobús ya generado en el repositorio) y tu workflow existente que funciona. Comprueba que los archivos en `scripts/` y `.github/workflows/` mantengan sus rutas.

En Actions, ejecuta `Actualizar catalogo adicional CDMX`. Si termina en rojo, abre el paso «Validar y generar puntos adicionales». Puede ser que una capa no tenga puntos, esté inaccesible o contenga solo geometrías de ruta; en ese caso se conserva el comportamiento anterior y no se genera un catálogo falso.

Si se genera `data/stations_secondary_cdmx.json`, comprueba su número de puntos y fuentes antes de considerar la cobertura validada. Si alguna modalidad falta, debe tratarse como cobertura incompleta, no como ausencia de servicio.

## Pruebas
1. Busca Talismán y Polanco. Comprueba Metro/Metrobús y ECOBICI.
2. Busca una zona con Trolebús o Cablebús y observa las modalidades y «Estado de las fuentes».
3. Comprueba que los resultados se actualicen al terminar las peticiones sin repetir búsqueda.
4. Verifica el estado de las descargas y no supongas que se ha descargado el catálogo adicional hasta que aparezca el archivo.
5. Comprueba que `data/stations_cdmx.json` y la actualización habitual de Metro/Metrobús sigan funcionando.

## Límites
Las capas del Atlas pueden incluir líneas o polígonos en lugar de paradas. Una capa sin puntos identificables no puede servir como catálogo de estaciones. Esta versión NO garantiza cobertura completa de RTP, Cablebús, Trolebús o transporte concesionado. Las alertas y tiempos reales requieren fuentes independientes y fiables, con autorización cuando proceda.
