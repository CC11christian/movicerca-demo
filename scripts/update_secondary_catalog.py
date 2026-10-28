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
