# MoviCerca v0.5 · Publicación web (sin publicar automáticamente)

## Qué incluye
- `index.html`: aplicación que funciona con ubicación manual y filtros sobre seis estaciones de referencia. Mapa Leaflet si hay internet.
- `manifest.webmanifest`, `sw.js` e iconos: funciones PWA para alojamiento HTTPS.
- `.nojekyll`: compatibilidad con GitHub Pages.
- `LEEME_V04.md`: documentación anterior.

**Limitaciones:** no hay red completa, rutas caminando, horarios, disponibilidad de vehículos ni integración en vivo. El mapa base y Leaflet dependen de proveedores externos: no hay uso completo sin internet. El acceso GPS, la instalación PWA y el service worker dependen de HTTPS o localhost y permisos del navegador.

## Probar en computadora
1. Descomprime la carpeta.
2. Puedes abrir `index.html` para revisar la interfaz, aunque la instalación PWA y el GPS probablemente no funcionarán en `file://`.
3. Para probar PWA usa terminal dentro de esta carpeta: `python -m http.server 8080`.
4. Abre `http://localhost:8080/` en Chrome o Edge. Para ver service worker, abre las herramientas de desarrollador > Application.

## Publicar gratis con GitHub Pages
1. Crea una cuenta de GitHub si no tienes.
2. Crea un repositorio nuevo, por ejemplo `movicerca-demo`. **Si el repositorio es público, todos podrán ver el código y los archivos; no subas secretos ni datos personales.**
3. Sube todos los archivos de esta carpeta a la raíz del repositorio, incluido `.nojekyll`, `sw.js`, `manifest.webmanifest` y `icons/`.
4. En Settings > Pages, selecciona `Deploy from a branch`, rama `main`, carpeta `/ (root)` y guarda.
5. Espera a que GitHub informe de la publicación y abre la URL HTTPS que te muestre (habitualmente `https://USUARIO.github.io/movicerca-demo/`). No se ha creado ningún repositorio ni publicado esta aplicación como parte de esta entrega.
6. Verifica carga de mapa, filtros, ubicación manual, solicitud GPS y que el navegador ofrezca instalar cuando corresponda.

## Instalar en teléfono
- **Android:** abre URL HTTPS en Chrome, menú > `Instalar aplicación` o `Añadir a pantalla de inicio` (según dispositivo/navegador).
- **iPhone:** abre URL HTTPS en Safari, Compartir > `Añadir a pantalla de inicio` (las opciones varían con la versión de iOS).

## Pruebas recomendadas
- Sin GPS: cambiar zona, filtro y radio.
- Con permiso de GPS: comprobar precisión reportada; no asumir que hay cobertura alrededor.
- Sin red: la página precargada puede abrir, pero el mapa de calles y servicios externos no funcionarán.
- Comprobar consola y Application > Manifest/Service Workers en Chrome.

## Antes de uso comercial
Verificar licencia, atribución y vigencia de los catálogos de transporte y elegir un proveedor de mapas con condiciones de operación adecuadas. Obtener autorización para APIs de terceros. No presentar distancias en línea recta como recorridos a pie.
