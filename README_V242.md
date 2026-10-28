# MoviCerca v2.4.2 — Correspondencias

## Qué se corrigió
- Consulado: agrupación de registros del Metro por nombre exacto normalizado hasta 1,200 metros, únicamente para nombres de correspondencias incluidos en la lista.
- San Juan de Aragón: agrupación explícita de la correspondencia Metrobús L5 y L6 hasta 250 metros. Las coordenadas del catálogo están separadas unos 128 metros.
- Se conservan los registros de origen en `transferEntries`; el resultado muestra sus líneas sin duplicar la ficha.
- No se fusionan modalidades diferentes ni se amplía el límite de 35 metros para otras paradas.
- Caché PWA v242.

## Publicación
Sustituye únicamente `index.html` y `sw.js` en la raíz del repositorio. No elimines los archivos JSON ni las automatizaciones. Confirma cambios a `main`, abre Safari en una pestaña privada y busca Consulado y San Juan de Aragón.

## Precaución
El agrupamiento es por complejo visual: los accesos y sentidos pueden ser físicamente distintos. Se requiere validación móvil.
