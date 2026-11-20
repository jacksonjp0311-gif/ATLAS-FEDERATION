"""Print constructed offline casebook as JSON. No real equipment controlled."""
import json
from .cases import casebook
result=casebook()
print(json.dumps(result,indent=2))
raise SystemExit(result['status']!='passed')
