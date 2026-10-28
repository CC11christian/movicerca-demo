# MoviCerca v2.3 — corrección de duplicados y origen de búsqueda

## Correcciones
- Deduplicación en la lista y en el mapa por modalidad, nombre normalizado y cercanía máxima de 35 metros. No fusiona estaciones ECOBICI ni paradas alejadas; la identidad cartográfica exacta requiere revisión de campo.
- Prioriza catálogos locales y conserva fuentes externas complementarias.
- Cambiar a GPS, zona, coordenadas o mapa borra el texto de dirección anterior.
- Una consulta pendiente de Nominatim no puede sustituir el origen tras cambiar de modalidad de búsqueda.
- El servicio PWA actualiza su identificador de caché a v23.

## Instalación
Sube los archivos del ZIP a la raíz del repositorio preservando sus carpetas. No borres data/stations_cdmx.json ni data/stations_secondary_cdmx.json y conserva GitHub Actions. En Safari prueba una pestaña privada para evitar interfaz antigua.

## Pruebas
1. En Talismán y Polanco compara el número de apariciones de estaciones Metro, Metrobús y Trolebús.
2. Busca una dirección y después usa GPS: debe limpiarse el campo y actualizarse el mapa.
3. Haz lo inverso, GPS y dirección: debe dominar la última acción.
4. Comprueba que ECOBICI sigue mostrando bicicletas y anclajes.

## Limitaciones
El criterio de 35 metros no captura todas las duplicaciones de nombres o accesos separados. No se han probado feeds en Safari automáticamente.
