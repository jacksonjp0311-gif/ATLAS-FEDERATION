"""Run explicit Materials operations, never retrieved node code."""
import json,sys
from .cases import casebook
from .advanced_cases import advanced_casebook
from .advanced import published_hahn1_replay
from .new_cases import expanded_casebook
from .hahn_diagnostics import hahn1_residual_diagnostics

def main():
 args=sys.argv[1:]
 choices=('casebook','advanced-cases','published-hahn1','expanded-cases','phase-diffraction-cases','hahn-diagnostics','describe')
 if len(args)!=1 or args[0] not in choices:
  print('Usage: python -m materials_atlas '+ '|'.join(choices),file=sys.stderr);return 2
 cmd=args[0]
 if cmd=='casebook':v=casebook();status=v['status']=='passed'
 elif cmd=='advanced-cases':v=advanced_casebook();status=v['status']=='passed'
 elif cmd=='published-hahn1':v=published_hahn1_replay();status=v['result']=='passed'
 elif cmd in ('expanded-cases','phase-diffraction-cases'):v=expanded_casebook();status=v['status']=='passed'
 elif cmd=='hahn-diagnostics':v=hahn1_residual_diagnostics();status=True
 else:
  v={'name':'Materials Atlas','version':'0.3.0','status':'content_development_not_scientific_v1',
  'physical_experiments':'none_this_release','functions':'explicit methods with bounded assumptions',
  'routing_changes':False};status=True
 print(json.dumps(v,indent=2));return 0 if status else 1
if __name__=='__main__':raise SystemExit(main())
