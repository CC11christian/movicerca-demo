# MoviCerca v1.2 — Cobertura multimodal CDMX

## Novedades
- Se consulta el Atlas Público de Movilidad Integrada de CDMX (FeatureServer) para ocho modalidades: Metro (0), Metrobús (2), RTP (4), Trolebús (6), Tren Ligero (8), Cablebús (10), ECOBICI (12) y transporte concesionado (15).
- Los filtros permiten separar cada modalidad. Cada capa puede fallar sin ocultar las demás.
- Se informa el número de fuentes que respondieron y las modalidades que no pudieron cargarse.
- Se pagina por bloques de 1000 registros hasta un máximo de 12000 por capa (límite de protección, no garantía de cobertura exhaustiva).
- Mantiene la búsqueda por dirección, geolocalización, fichas, Google Maps y corrección CSS del logo Leaflet.

## Limitaciones importantes
- Los datos se consultan en vivo desde el servicio cartográfico, **no** representan la operación de vehículos en vivo. Dependemos de la disponibilidad, CORS, calidad y actualización de los datos publicados.
- La consulta externa puede fallar o entregar campos con nombres diferentes. Cuando no hay información no se deduce que no existe transporte.
- No se garantiza que cada punto tenga nombre, línea, ruta o acceso peatonal preciso. La app omite puntos sin nombre verificable.
- No se incluyen horarios, tarifas ni tiempos de llegada. Distancias en línea recta. Indicaciones a pie en Google Maps externo.
- ECOBICI muestra ubicación de cicloestaciones, **no** disponibilidad de bicicletas.
- Transporte concesionado puede no incluir combis y rutas informales completas.

## Publicación
1. Haz copia del repositorio actual de GitHub Pages.
2. Descomprime el ZIP y sube el CONTENIDO de esta carpeta directamente a la raíz del repositorio, reemplazando `index.html`, `sw.js`, manifiesto e iconos.
3. Espera a que GitHub Actions indique publicación exitosa.
4. En iPhone prueba en una pestaña privada de Safari para descartar caché. Después actualiza o reinstala la PWA.
5. Prueba Parques Polanco, los ocho filtros y el botón «Cómo llegar caminando». Comprueba el estado «Con datos/Sin respuesta».

## Fuente
Servicio del Atlas de Movilidad Integrada CDMX: https://serviciosatlas.sgirpc.cdmx.gob.mx/arcgis/rest/services/AtlasCapasPublicas/Movilidad_Integrada_CDMX/FeatureServer
Verificar condiciones de reutilización antes de un uso comercial.

## Verificación de entrega
Validación estática de JavaScript, existencia de archivos PWA y ZIP. No se pudieron efectuar consultas directas a la API desde el entorno de construcción; la cobertura debe comprobarse desde el navegador publicado.
