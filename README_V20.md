# MoviCerca v2.0 — carga progresiva

## Correcciones
- Se presenta cada modalidad del Atlas en cuanto su consulta termina; no es necesario repetir la búsqueda.
- La búsqueda y el mapa se actualizan automáticamente al entrar nuevos registros.
- El catálogo local de Metro y Metrobús permanece visible durante las consultas complementarias.
- Los resultados de una consulta anterior no reemplazan una recarga posterior.
- Indicador de carga y estado por modalidad; errores separados por fuente.
- Textos de versión actualizados y caché PWA v20.
- No se altera el GPS, Nominatim, Leaflet, pago o navegación peatonal.

## Publicación
Descomprime el ZIP y sube el contenido a la raíz de la rama main de GitHub Pages, conservando `data/stations_cdmx.json` y `.github/workflows/update-catalog.yml` actuales. No elimines el catálogo generado en GitHub. Tras la publicación comprueba que la cabecera indica v2.0 y que el indicador de fuentes cambia mientras se cargan. Si el navegador conserva la versión anterior, prueba en una pestaña privada o reinstala la PWA.

## Pruebas sugeridas
1. Busca Talismán y comprueba Metro/Metrobús.
2. Selecciona Trolebús y Cablebús: deben aparecer automáticamente tras cargar, sin repetir la búsqueda, **cuando el Atlas proporcione registros válidos**.
3. Verifica mensajes de error de cada fuente si falla.
4. Busca Polanco y comprueba GPS, mapa, pagos y enlaces peatonales.

## Límites
No se garantiza que las capas experimentales del Atlas respondan correctamente ni que sus rutas estén completas. No hay llegadas ni cierres en tiempo real. Si una capa falla, se muestra un mensaje explícito, sin inventar datos.
