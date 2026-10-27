# MoviCerca v1.6 — Búsqueda y cobertura

- Botón **Borrar** para limpiar el campo sin perder la posición seleccionada.
- Geocodificación por calle, colonia, código postal o ciudad; consultas explícitas a Nominatim limitadas a México. Prueba primero el texto original, después añade Ciudad de México si es necesario y finalmente intenta el código postal.
- Al buscar dirección o seleccionar zona se ajusta el radio mínimo a **5 km** y se reactiva el filtro **Todos**, porque filtros/radios anteriores podían ocultar Metro y Metrobús Talismán.
- Sigue existiendo cobertura incompleta: no se incluye un GTFS completo validado.
- Nota: una consulta por colonia/código postal apunta al centro aproximado de esa zona, no a una casa exacta. La búsqueda con varias coincidencias elige la primera; verifica el marcador sobre el mapa.
- Conserva la corrección CSS de la bandera de Leaflet y enlaces para caminar.
- Para publicar, coloca todos los archivos en la raíz de GitHub Pages y comprueba Actions. Si Safari muestra una versión anterior, recarga o reinicia la PWA.
- Prueba: busca “Talismán, Gustavo A. Madero, Ciudad de México” y comprueba un radio de 5 km y filtro Todos sin tocar «Comprobar Talismán». Prueba “Polanco, Miguel Hidalgo, Ciudad de México” y el botón Borrar.
- Las fuentes externas pueden fallar o devolver coincidencias aproximadas; la ubicación residencial exacta no debe compartirse para diagnosticar.
