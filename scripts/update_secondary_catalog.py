#!/usr/bin/env python3
"""Generate a conservative *optional* snapshot for additional mobility modes.

No synthetic stations; never overwrite a prior good snapshot if any required layer fails.
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
    stations=[];counts={}
    for layer,typ in LAYERS:
        records,source_count=load(layer,typ)
        stations+=records;counts[typ]={'points':len(records),'source_records':source_count,'layer':layer}
        print(f'{typ}: {len(records)} verified points from {source_count} records',flush=True)
    payload={'schema_version':1,'generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':BASE,'coverage':'partial; named point features only; no live status, arrivals or payment verification','counts':counts,'stations':stations}
    destination=ROOT/'data'/'stations_secondary_cdmx.json'
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(json.dumps(payload,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf8')
    print(f'Additional catalog generated: {len(stations)} points at {destination}',flush=True)
if __name__=='__main__':
    try:main()
    except Exception as e:print('Secondary catalog NOT updated:',e,file=sys.stderr);sys.exit(1)
