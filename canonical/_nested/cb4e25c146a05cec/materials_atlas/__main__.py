import json,sys
from .cases import casebook
if __name__=='__main__':
    if len(sys.argv)!=2 or sys.argv[1] not in ('casebook','describe'):
        print('Usage: python -m materials_atlas casebook|describe',file=sys.stderr);raise SystemExit(2)
    if sys.argv[1]=='casebook':
        out=casebook();print(json.dumps(out,indent=2));raise SystemExit(out['status']!='passed')
    print(json.dumps({'name':'Materials Atlas','version':'0.1.0','type':'reference + bounded calculators','not':'sample certified or independently validated material'},indent=2))
