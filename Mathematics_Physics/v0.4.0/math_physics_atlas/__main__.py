"""Offline reproducible scientific reference cases; no physical experiments."""
import json
from .cases import casebook
from .v02_cases import casebook_v02
from .v03_cases import casebook_v03
from .v04_cases import casebook_v04
r=[casebook(),casebook_v02(),casebook_v03(),casebook_v04()]
print(json.dumps({'editions':r,'total_constructed_cases':sum(x['count'] for x in r),'status':'passed' if all(x['status']=='passed' for x in r) else 'failed'},indent=2))
raise SystemExit(any(x['status']!='passed' for x in r))
