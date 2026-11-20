"""Offline bounded scientific reference casebooks, not physical laboratory experiments."""
import json
from .cases import casebook
from .v02_cases import casebook_v02
from .v03_cases import casebook_v03
r=[casebook(),casebook_v02(),casebook_v03()]
print(json.dumps({'editions':r,'total_constructed_cases':sum(x['count'] for x in r),'status':'passed' if all(x['status']=='passed' for x in r) else 'failed'},indent=2))
raise SystemExit(any(x['status']!='passed' for x in r))
