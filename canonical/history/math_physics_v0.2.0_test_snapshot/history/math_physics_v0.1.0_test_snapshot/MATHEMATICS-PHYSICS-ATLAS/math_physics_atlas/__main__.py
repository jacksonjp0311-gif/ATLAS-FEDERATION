"""Print authored mathematical reconstruction examples, offline."""
import json
from .cases import casebook
r=casebook();print(json.dumps(r,indent=2,default=str));raise SystemExit(r['status']!='passed')
