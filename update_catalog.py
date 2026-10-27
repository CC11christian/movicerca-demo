#!/usr/bin/env python3
"""MoviCerca: construir catalogo de estaciones, sin publicar datos incompletos.
Fuente: Atlas CDMX, capas 0 (Metro) y 2 (Metrobus).
"""
import datetime
import json
import pathlib
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent
BASE = 'https://serviciosatlas.sgirpc.cdmx.gob.mx/arcgis/rest/services/AtlasCapasPublicas/Movilidad_Integrada_CDMX/FeatureServer'
LAYERS = [(0, 'metro'), (2, 'metrobus')]


def fetch(url, params):
    query = urllib.parse.urlencode(params)
    request = urllib.request.Request(url + '?' + query, headers={
        'User-Agent': 'Mozilla/5.0 (compatible; MoviCercaCatalog/1.9)',
        'Accept': 'application/json',
    })
    try:
        with urllib.request.urlopen(request, timeout=40) as response:
            body = response.read()
        result = json.loads(body)
    if 'status' in result or 'messages' in result:
        raise RuntimeError(
            f"Respuesta del servidor: "
            f"status={result.get('status')}, "
            f"messages={result.get('messages')}"
        )
    except (urllib.error.URLError, ValueError) as exc:
        raise RuntimeError(f'No fue posible consultar {url}: {exc}') from exc
    if 'error' in result:
        raise RuntimeError(f'Error ArcGIS en {url}: {result["error"]}')
    return result


def records(layer):
    endpoint = f'{BASE}/{layer}/query'
    id_reply = fetch(endpoint, {'where': '1=1', 'returnIdsOnly': 'true', 'f': 'json'})
    ids = id_reply.get('objectIds')
    if isinstance(ids, list) and ids:
        print(f'Capa {layer}: {len(ids)} IDs; recuperando en lotes', flush=True)
        results = []
        for offset in range(0, len(ids), 150):
            batch = ids[offset:offset + 150]
            reply = fetch(endpoint, {'objectIds': ','.join(map(str, batch)), 'outFields': '*',
                                     'returnGeometry': 'true', 'outSR': 4326, 'f': 'json'})
            results.extend(reply.get('features') or [])
        return results
    print(f'Capa {layer}: respuesta sin objectIds (claves: {list(id_reply.keys())}); probando paginacion', flush=True)
    results = []
    for offset in range(0, 30000, 250):
        reply = fetch(endpoint, {'where': '1=1', 'outFields': '*', 'returnGeometry': 'true',
                                 'outSR': 4326, 'resultOffset': offset, 'resultRecordCount': 250, 'f': 'json'})
        batch = reply.get('features')
        if not isinstance(batch, list):
            raise RuntimeError(f'Capa {layer}: respuesta sin features (claves: {list(reply.keys())})')
        results.extend(batch)
        if len(batch) < 250 and not reply.get('exceededTransferLimit'):
            break
        if not batch:
            break
    print(f'Capa {layer}: recuperados {len(results)} registros con paginacion', flush=True)
    return results


def normalize(layer, typ):
    out = []
    for record in records(layer):
        attr = record.get('attributes') or {}
        geo = record.get('geometry') or {}
        try:
            lat, lng = float(geo['y']), float(geo['x'])
        except (KeyError, TypeError, ValueError):
            continue
        if not (19.0 < lat < 19.7 and -99.4 < lng < -98.7):
            continue
        name = str(attr.get('nombre') or attr.get('est') or '').strip()
        oid = attr.get('objectid')
        if oid is None:
            oid = attr.get('OBJECTID')
        if oid is None:
            oid = attr.get('id')
        if not name or oid is None:
            continue
        out.append({'id': f'cdmx-{typ}-{oid}', 'name': name, 'type': typ,
                    'line': str(attr.get('linea') or 'Línea sin especificar').strip(),
                    'lat': round(lat, 7), 'lng': round(lng, 7),
                    'source': f'{BASE}/{layer}', 'source_record': str(oid)})
    unique = {r['id']: r for r in out}
    if len(unique) < 100:
        raise RuntimeError(f'Capa {layer} ({typ}): solo {len(unique)} estaciones validas. No se reemplaza el catalogo.')
    return list(unique.values())


def main():
    all_stations = []
    counts = {}
    for layer, typ in LAYERS:
        stations = normalize(layer, typ)
        all_stations.extend(stations)
        counts[typ] = {'count': len(stations), 'layer': layer}
    names = lambda typ: ' '.join(s['name'].casefold() for s in all_stations if s['type'] == typ)
    for expected in ['talism', 'polanco', 'san joaqu', 'bellas artes']:
        if expected not in names('metro'):
            raise RuntimeError(f'Control de calidad: Metro no incluye {expected}')
    if 'talism' not in names('metrobus'):
        raise RuntimeError('Control de calidad: Metrobús no incluye Talismán')
    payload = {'schema_version': 1,
               'generated_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
               'source': BASE,
               'license_note': 'Verificar las condiciones y atribuir las fuentes originales.',
               'counts': counts, 'stations': all_stations}
    target = ROOT / 'data' / 'stations_cdmx.json'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')
    print(f'Catalogo generado: {len(all_stations)} estaciones; {target}', flush=True)

if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(f'ACTUALIZACION RECHAZADA: {exc}', file=sys.stderr)
        sys.exit(1)
