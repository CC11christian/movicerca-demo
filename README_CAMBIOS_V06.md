# MoviCerca v0.6 — Ajustes tras pruebas en celular

- Buscar calle, dirección o lugar mediante Nominatim (OpenStreetMap). La consulta se transmite al servicio externo solo cuando el usuario presiona Buscar; se añade México al texto. No usar autocompletado masivo por límites de uso del servicio público. Para operación comercial usar proveedor autorizado y cuotas adecuadas.
- El GPS requiere HTTPS o localhost, permiso del navegador, configuración de ubicación y señal disponible. Mensajes de error claros.
- Mapa más alto en móvil, opciones compactas y resultados debajo del mapa; coordenadas en apartado avanzado.
- El navegador necesita internet para mosaicos cartográficos, librería Leaflet y búsqueda de direcciones. El contenido base continúa disponible según su caché.
- Las seis estaciones siguen siendo muestra; no se ofrecen datos de llegadas. No almacena geolocalización ni direcciones en servidor MoviCerca, pero la consulta se envía a Nominatim y los mosaicos al servidor externo.
- Para actualizar GitHub Pages: reemplazar archivos en raíz y confirmar despliegue verde en Actions; en teléfono cerrar y volver a abrir la app si persiste caché anterior.
