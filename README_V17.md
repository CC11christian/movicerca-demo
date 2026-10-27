# MoviCerca v1.7 — Pagos y estado de servicio

Esta versión mantiene las funciones de v1.6 y agrega **fichas informativas por operador** para Metro y Metrobús con formas de pago y enlaces a fuentes oficiales.

## Implementado
- Fichas de estación: estado **Sin información en vivo** en vez de inventar operación o cierres.
- Próxima llegada: **No disponible** hasta disponer de GTFS-RT autorizado.
- Pagos en Metro: Tarjeta MI y tarjetas bancarias contactless en líneas habilitadas.
- Pagos en Metrobús: Tarjeta MI, tarjetas contactless y billeteras en lectores habilitados.
- Enlaces a los operadores para consultar avisos.
- Cache PWA incrementada a v17.

## Limitaciones importantes
- No se ha integrado el GTFS completo de CDMX. Sigue siendo cobertura parcial; la consulta al Atlas puede fallar.
- Datos de pagos son generales por operador, no garantía de que todos los validadores tengan la misma tecnología.
- No hay estados operativos reales ni tiempos de llegada. Metrobús requiere **registro** para su API GTFS-RT: https://www.metrobus.cdmx.gob.mx/portal-ciudadano/datos-abiertos
- No deben colocarse claves API privadas en GitHub Pages. Se requeriría un backend o proceso servidor con credenciales protegidas, autorización y límites de consulta.

## Fuentes revisadas el 27/oct/2026
- Metro: https://www.metro.cdmx.gob.mx/comunicacion/nota/el-metro-da-la-bienvenida-las-tarjetas-bancarias-sin-contacto-como-medio-de-pago-del-servicio
- Metrobús: https://www.metrobus.cdmx.gob.mx/
- API Metrobús: https://www.metrobus.cdmx.gob.mx/portal-ciudadano/datos-abiertos
- GTFS CDMX: https://www.datos.cdmx.gob.mx/dataset/gtfs

## Actualizar GitHub Pages
Copia el contenido de esta carpeta (no la carpeta contenedora) a la raíz del repositorio, confirma el commit y comprueba GitHub Actions. Abre desde una pestaña nueva si tu PWA conserva la caché previa.

## Prueba de aceptación
Busca Talismán, abre Metro Talismán y Metrobús Avenida Talismán; verifica que ambas fichas muestren pago correspondiente, estado desconocido y llegada no disponible, con enlaces oficiales. Comprueba GPS, búsqueda, botones peatonales, mapa y botón Borrar.
