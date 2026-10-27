# MoviCerca v1.1 — acciones de estaciones

## Correcciones
- Se añadió el contenedor `stationDetail` que faltaba en v1.0 y que impedía que aparecieran los botones de la ficha.
- Al tocar el nombre de una estación en la lista o «Ver detalles» en el mapa, aparece una ficha con dos botones destacados:
  - **Cómo llegar caminando**: abre Google Maps Directions con modo `walking`, utilizando el origen seleccionado y las coordenadas de la estación.
  - **Ver en Google Maps**: abre la búsqueda de las coordenadas de la estación, sin elegir ruta.
- Los botones tienen tamaño cómodo para móvil.
- Se mantiene la corrección CSS de la bandera de Leaflet, el GPS y la búsqueda por dirección.
- Se cambió el identificador de caché para reducir el riesgo de servir una versión anterior.

## Publicar
Descomprime el ZIP y sube los archivos y la carpeta `icons` a la raíz del repositorio de GitHub Pages; confirma los cambios en `main`. Revisa `Actions`, abre la URL HTTPS en Safari y actualiza la página. Si la PWA instalada muestra una versión antigua, elimina el acceso directo y vuelve a instalarlo después de cargar la versión nueva.

## Probar
1. Buscar «Parques Polanco» o tocar Detectar mi ubicación.
2. Tocar el nombre de Metro Polanco en la lista de resultados, o un marcador y «Ver detalles».
3. Comprobar que aparece una ficha con los botones **Cómo llegar caminando** y **Ver en Google Maps**.
4. El primero debe abrir Google Maps solicitando recorrido a pie; el segundo solo ubicación.
5. Confirmar que el mapa no tiene barras ampliadas y que la búsqueda/GPS siguen operativos.

Las distancias en MoviCerca son en línea recta, las indicaciones peatonales se calculan en Google Maps. No hay disponibilidad de transporte en vivo ni cobertura exhaustiva. El origen seleccionado se comparte con Google Maps al solicitar indicaciones.
