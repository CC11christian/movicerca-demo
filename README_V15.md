# MoviCerca v1.5 — diagnóstico Talismán

Esta versión NO soluciona todavía la falta de la red completa de transporte en CDMX. Corrige un fallo específico: al recuperar puntos del Atlas, la app podía sustituir estaciones de respaldo por registros no validados. Ahora se conservan los datos de referencia y se ofrece **Comprobar Talismán**.

## Prueba controlada
1. Publica en GitHub Pages, espera a que Actions muestre el despliegue correcto y abre la URL añadiendo `?v=15` al final.
2. Comprueba que el encabezado diga `v1.5 · Talismán`.
3. Pulsa **Comprobar Talismán**: establece un origen de referencia en la zona, radio 5 km y filtro Todos. Deben aparecer Metro Talismán y Metrobús Avenida Talismán. Las distancias son en línea recta y la ubicación es DEMOSTRATIVA.
4. Para tu propia dirección, utiliza Buscar y radio 5 km; después compara la distancia en línea recta. Si está a más de 2 km, un radio de 2 km puede ocultar la estación.
5. Si la prueba controlada no muestra ambas, revisa que el archivo principal de GitHub tenga el cambio y el icono de Actions esté verde. En Safari prueba una pestaña privada; una PWA instalada puede mantener recursos en caché.

## Pendiente crítico
La app depende de capas externas con formatos variables; sin un GTFS completo auditado, no cubre toda CDMX. Importar un GTFS en un solo navegador no lo distribuye automáticamente a otros usuarios. La siguiente versión deberá generar y versionar un catálogo estático servido con la aplicación, incluyendo procedencia y fecha.
