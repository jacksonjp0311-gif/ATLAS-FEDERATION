"""Print 25 original bounded chemistry investigations as JSON."""
import json
from .cases import casebook
x=casebook()
print(json.dumps(x,indent=2))
raise SystemExit(x['status']!='passed')
