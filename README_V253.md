# MoviCerca v2.5.3 — ECOBICI sin refrescar manualmente

## Cambios
- La carga de ECOBICI GBFS y las demás fuentes externas comienza en paralelo con los catálogos locales, no después de ellos.
- ECOBICI reintenta automáticamente una vez ante un error transitorio, con una pausa de 1.5 segundos.
- Cada fuente que completa correctamente desencadena la reconstrucción y renderizado de las estaciones sobre la ubicación activa.
- Se conserva la búsqueda precisa v2.5.2, GPS, agrupación de correspondencias y comparación.
- Cache PWA actualizado a `movicerca-shell-v253`.

## Publicación
1. Subir **index.html** y **sw.js** a la raíz del repositorio, reemplazando ambos archivos.
2. Confirmar cambios en `main` y comprobar despliegue GitHub Pages.
3. En Safari privado verificar cabecera `v2.5.3`.
4. Buscar Polanco o Insurgentes una sola vez y observar si ECOBICI aparece sin tocar «Reintentar fuentes de transporte».
5. Si falla, abrir «Estado de las fuentes» y copiar el estado de `ECOBICI (GBFS)`.

No editar `data/stations_cdmx.json`, `data/stations_secondary_cdmx.json` ni GitHub Actions.

**Límite:** esta corrección maneja esperas y errores temporales. Si GBFS bloquea el navegador o permanece inaccesible, la interfaz mostrará el fallo; no inventa bicicletas disponibles.
