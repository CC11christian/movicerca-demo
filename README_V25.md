# MoviCerca v2.5 — Comparación por modalidad

## Cambios
- Resumen de la parada más cercana **por modalidad**, ordenado por distancia en línea recta. No se trata de tiempo ni ruta peatonal.
- Botón de detalles en cada tarjeta de comparación.
- Etiquetas de procedencia: ubicación de referencia sin llegadas en vivo; ECOBICI muestra bicicletas y antigüedad solo cuando el GBFS tiene estado vigente (máximo 15 minutos).
- Preserva la lógica de agrupación Metro Consulado y Metrobús San Juan de Aragón de v2.4.2, GPS, búsquedas y catálogos.
- Nueva versión de caché PWA.

## Publicación
1. Sustituye **index.html** y **sw.js** en la raíz de GitHub Pages (rama main).
2. No elimines los JSON de `data/`, archivos `scripts/` ni los workflows de `.github/`.
3. Abre en Safari privado para comprobar la nueva versión.

## Pruebas
1. Comprueba que v2.5 y el resumen «Comparación por modalidad» aparecen.
2. Busca Consulado y San Juan de Aragón: la agrupación de líneas debe seguir funcionando.
3. Mueve el origen con GPS y con dirección; la comparación debe actualizarse.
4. En ECOBICI: verificar que las bicicletas solo se anuncian cuando hay estado vigente.
5. Comprobar que no se muestran supuestos tiempos de espera.

**Nota:** no se han conectado nuevos servicios en vivo ni se ha probado aún desde iPhone.
