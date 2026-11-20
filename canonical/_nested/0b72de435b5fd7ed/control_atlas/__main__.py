"""Read-only local reference casebook CLI."""
import json,sys
from .cases import casebook
from . import __version__
if __name__=='__main__':
    if len(sys.argv)!=2 or sys.argv[1] not in ('casebook','describe'):
        print('Usage: python -m control_atlas casebook|describe',file=sys.stderr)
        raise SystemExit(2)
    if sys.argv[1]=='casebook':
        result=casebook();print(json.dumps(result,indent=2));raise SystemExit(result['result']!='passed')
    print(json.dumps({'name':'Control Atlas','version':__version__,
                      'readiness':'bounded content foundation, not scientifically reviewed or hardware tested'}))
