"""Optional full JSON Schema check in addition to dependency-free runtime checks."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
try:from jsonschema import Draft202012Validator
except ImportError:raise SystemExit('Install the optional jsonschema test dependency; do not report this check passed without running it.')
from atlas_forge.common import AtlasStore
s=AtlasStore();schemas={k:json.loads((ROOT/f'schemas/common/{k}.schema.json').read_text()) for k in ['record','node','context','relation']}
for schema in schemas.values():Draft202012Validator.check_schema(schema)
errors=[]
for r in s.export():errors.extend(f'{r["record_id"]}: {e.message}' for e in Draft202012Validator(schemas['record']).iter_errors(r))
for n in s.discover()['nodes']:errors.extend(f'{n["node_id"]}: {e.message}' for e in Draft202012Validator(schemas['node']).iter_errors(n))
for r in s._relations.values():errors.extend(e.message for e in Draft202012Validator(schemas['relation']).iter_errors(r))
for q in ['expanded uncertainty','Faraday waves','NOAA GOES','qzxvjk987654321']:
 ctx=s.assemble_context(q);errors.extend(f'{q}: {e.message}' for e in Draft202012Validator(schemas['context']).iter_errors(ctx))
print(json.dumps({'valid':not errors,'errors':errors,'records_checked':len(s.export()),'schemas_checked':len(schemas),'science_validated':False},indent=2));sys.exit(bool(errors))
