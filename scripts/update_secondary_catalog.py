#!/usr/bin/env python3
"""Generate a conservative *optional* snapshot for additional mobility modes.

No synthetic stations; retain prior good entries if individual layers fail.
This is a point catalog only, not a routing or live-status feed.
"""
import datetime, json, pathlib, sys, urllib.parse, urllib.request
ROOT=pathlib.Path(__file__).resolve().parents[1]
BASE='https://serviciosatlas.sgirpc.cdmx.gob.mx/arcgis/rest/services/AtlasCapasPublicas/Movilidad_Integrada_CDMX/FeatureServer'
LAYERS=[(4,'rtp'),(6,'trolebus'),(8,'trenligero'),(10,'cablebus'),(15,'concesionado')]

def query(layer,params):
    url=f'{BASE}/{layer}/query?'+urllib.parse.urlencode(params)
    req=urllib.request.Request(url,headers={'User-Agent':'MoviCercaCatalogUpdater/2.2 (public mobility data)'})
    with urllib.request.urlopen(req,timeout=40) as result:
        data=json.load(result)
    if not isinstance(data,dict) or ('error' in data) or ('status' in data and 'features' not in data and 'objectIds' not in data):
        raise RuntimeError(f'Layer {layer}: unexpected response: {str(data)[:300]}')
    return data

def get_field(attrs,choices):
    lookup={str(k).lower():v for k,v in attrs.items()}
    for key in choices:
        v=lookup.get(key)
        if v is not None and str(v).strip():return str(v).strip()
    return ''

def load(layer,typ):
    data=query(layer,{'where':'1=1','returnIdsOnly':'true','f':'json'})
    ids=data.get('objectIds')
    if not isinstance(ids,list) or not ids:raise RuntimeError(f'Layer {layer}: no objectIds; refusing empty update')
    entries=[]
    for idx in range(0,len(ids),200):
        portion=ids[idx:idx+200]
        page=query(layer,{'objectIds':','.join(map(str,portion)),'outFields':'*','returnGeometry':'true','outSR':'4326','f':'json'})
        if not isinstance(page.get('features'),list):raise RuntimeError(f'Layer {layer}: missing features')
        for item in page['features']:
            attrs=item.get('attributes') or {}; geom=item.get('geometry') or {}
            # Lines and polygons are not boarding stations. Do not invent centroids.
            if 'x' not in geom or 'y' not in geom:continue
            try:lat=float(geom['y']); lng=float(geom['x'])
            except (ValueError,TypeError):continue
            if not (18.7<lat<20 and -100<lng<-98):continue
            name=get_field(attrs,['nombre_estacion','nom_estacion','estacion','nombre','nom_parada','parada','name','denominacion','sitio','nom','est','nom_est','nombre_parada','n_estacion'])
            if not name:continue
            line=get_field(attrs,['linea','línea','ruta','nombre_ruta','nom_ruta','servicio','corredor','n_linea','n_ruta','linea_ruta'])
            oid=get_field(attrs,['objectid','fid','id','id_estacion','stop_id'])
            if not oid:continue
            entries.append({'id':f'secondary-{typ}-{oid}','name':name,'type':typ,'line':line or 'Ruta o línea no informada','lat':round(lat,7),'lng':round(lng,7),'source':f'{BASE}/{layer}','source_record':oid})
    if len(entries)<1:raise RuntimeError(f'Layer {layer} ({typ}) does not contain usable named POINT features; refusing update')
    return entries,len(ids)

def main():
    destination = ROOT / 'data' / 'stations_secondary_cdmx.json'
    prior = {}
    if destination.exists():
        try:
            raw = json.loads(destination.read_text(encoding='utf8'))
            for item in raw.get('stations', []):
                if item.get('type') in {t for _, t in LAYERS} and item.get('id'):
                    prior.setdefault(item['type'], []).append(item)
        except (OSError, ValueError, TypeError):
            print('WARNING: Existing catalog could not be read; no old data reused.', flush=True)
    stations = []
    counts = {}
    successes = 0
    for layer, typ in LAYERS:
        try:
            records, source_count = load(layer, typ)
        except Exception as exc:
            preserved = prior.get(typ, [])
            stations.extend(preserved)
            counts[typ] = {
                'points': len(preserved), 'layer': layer,
                'status': 'stale' if preserved else 'unavailable',
                'error': str(exc)[:250]
            }
            print(f'WARNING {typ}: {exc}. Previous records retained: {len(preserved)}', flush=True)
            continue
        successes += 1
        stations.extend(records)
        counts[typ] = {'points': len(records), 'source_records': source_count,
                       'layer': layer, 'status': 'updated'}
        print(f'{typ}: {len(records)} verified point records', flush=True)
    if successes == 0:
        raise RuntimeError('No modalities supplied new verified points. Catalog unchanged.')
    if not stations:
        raise RuntimeError('Catalog has no stations. Refusing to publish.')
    payload = {
        'schema_version': 1,
        'generated_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'source': BASE,
        'coverage': 'PARTIAL; only verified named point features; some modalities may be stale or unavailable',
        'counts': counts,
        'stations': stations
    }
    destination.parent.mkdir(parents=True, exist_ok=True)
    tmp = destination.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(payload, ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf8')
    tmp.replace(destination)
    print(f'Additional catalog generated: {len(stations)} points at {destination}', flush=True)

if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print('Secondary catalog NOT updated:', exc, file=sys.stderr)
        sys.exit(1)
