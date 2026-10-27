#!/usr/bin/env python3
"""Build a reviewed snapshot of Metro/Metrobus stations from CDMX Atlas ArcGIS.
Only writes data when both layers pass sanity checks. Python standard library only.
"""
import json, pathlib, urllib.parse, urllib.request, datetime, sys
ROOT = pathlib.Path(__file__).resolve().parent
BASE='https://serviciosatlas.sgirpc.cdmx.gob.mx/arcgis/rest/services/AtlasCapasPublicas/Movilidad_Integrada_CDMX/FeatureServer'
LAYERS=[(0,'metro','Metro'),(2,'metrobus','Metrobús')]
def fetch(url,params):
    query=urllib.parse.urlencode(params)
    req=urllib.request.Request(url+'?'+query,headers={'User-Agent':'MoviCercaCatalogUpdater/1.8 (public transit data)'})
    with urllib.request.urlopen(req,timeout=35) as res: data=json.load(res)
    if 'error' in data: raise RuntimeError(str(data['error']))
    return data

def download(layer,typ):
    endpoint=f'{BASE}/{layer}/query'
    ids_response=fetch(endpoint,{'where':'1=1','returnIdsOnly':'true','f':'json'})
    ids=ids_response.get('objectIds')
    if not isinstance(ids,list) or not ids: raise RuntimeError(f'Layer {layer}: no objectIds')
    output=[]
    for i in range(0,len(ids),250):
        block=ids[i:i+250]
        data=fetch(endpoint,{'objectIds':','.join(map(str,block)),'outFields':'*','returnGeometry':'true','outSR':'4326','f':'json'})
        for feature in data.get('features',[]):
            geom=feature.get('geometry') or {}; attrs=feature.get('attributes') or {}
            try: lat=float(geom['y']); lng=float(geom['x'])
            except (KeyError,ValueError,TypeError): continue
            if not (19.0<lat<19.7 and -99.4<lng<-98.7): continue
            name=str(attrs.get('nombre') or attrs.get('est') or '').strip()
            if not name: continue
            line=str(attrs.get('linea') or '').strip()
            oid=next((attrs[k] for k in ('objectid','OBJECTID','id') if k in attrs and attrs[k] is not None),None)
            if oid is None: continue
            output.append({'id':f'cdmx-{typ}-{oid}','name':name,'type':typ,'line':line or 'Línea sin especificar','lat':round(lat,7),'lng':round(lng,7),'source':f'{BASE}/{layer}','source_record':str(oid)})
    if len(output)<(100 if typ=='metro' else 100):
        raise RuntimeError(f'{typ}: solo {len(output)} registros; se conserva el catálogo anterior')
    return output,len(ids)

def build():
    stations=[];stats={}
    for layer,typ,label in LAYERS:
        items,total=download(layer,typ)
        stations+=items;stats[typ]={'count':len(items),'source_ids':total,'layer':layer}
    names=lambda typ: {x['name'].casefold() for x in stations if x['type']==typ}
    for expected,typ in [('Talismán','metro'),('Polanco','metro'),('San Joaquín','metro'),('Bellas Artes','metro')]:
        if expected.casefold() not in names(typ):raise RuntimeError(f'Control de calidad: falta {expected} ({typ})')
    # The source may call MB Talismán 'Avenida Talismán'; check substring only.
    if not any('talism' in x['name'].casefold() for x in stations if x['type']=='metrobus'):
        raise RuntimeError('Control de calidad: no aparece Talismán en Metrobús')
    result={'schema_version':1,'generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':BASE,'license_note':'Verificar y atribuir fuentes oficiales de CDMX; uso sujeto a condiciones del conjunto.','counts':stats,'stations':stations}
    target=ROOT/'data'/'stations_cdmx.json';target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(result,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
    print(f'Catálogo generado: {len(stations)} registros; {stats}')
if __name__=='__main__':
    try:build()
    except Exception as e: print('ACTUALIZACIÓN RECHAZADA:',e,file=sys.stderr);sys.exit(1)
