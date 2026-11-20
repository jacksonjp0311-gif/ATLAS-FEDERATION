"""Local-only mathematical/reference CLI; never issues real hardware actions."""
import json,sys
from pathlib import Path
from .cases import casebook
from .extended_cases import casebook as extended_casebook
from .robust_cases import casebook as robust_casebook
from .advanced_cases import casebook as advanced_casebook
from .invariance_cases import casebook as invariance_casebook
from .output_feedback_cases import casebook as output_feedback_casebook
from .v1_cases import v1_casebook
from .empirical import parse_openmct,validate_openmct_identification
from .methods import ControlInputError
from . import __version__

CASEBOOKS={'casebook':casebook,'extended-casebook':extended_casebook,
   'robust-casebook':robust_casebook,'advanced-casebook':advanced_casebook,
   'invariance-casebook':invariance_casebook,'output-feedback-casebook':output_feedback_casebook,
   'v1-casebook':v1_casebook}

def main():
    args=sys.argv[1:]
    if len(args)==1 and args[0]=='describe':
        print(json.dumps({'name':'Control Atlas','version':__version__,
            'scope':'offline control theory and externally supplied log analysis; no plant safety certification',
            'openmct_real_data_run':False,'independent_review':False,'bitwork_integration':False},indent=2))
        return 0
    if len(args)==1 and args[0] in CASEBOOKS:
        r=CASEBOOKS[args[0]]();print(json.dumps(r,indent=2))
        return 0 if r.get('result',r.get('status'))=='passed' else 1
    if len(args)==2 and args[0] in ('openmct-review','openmct-fit'):
        path=Path(args[1]);
        try:
            if not path.is_file() or path.stat().st_size>60_000_000:raise ControlInputError('local file missing or over limit')
            parsed=parse_openmct(path.read_text(encoding='utf-8'))
            summary={k:v for k,v in parsed.items() if k not in ('samples','times_s')}
            if args[0]=='openmct-fit':
                summary['fit']=validate_openmct_identification(parsed)
            print(json.dumps(summary,indent=2));return 0
        except (ControlInputError,UnicodeError,OSError) as e:
            print(json.dumps({'status':'refused','reason':str(e),'safety_certification':False},indent=2));return 2
    print('Usage: python -m control_atlas casebook|extended-casebook|robust-casebook|advanced-casebook|invariance-casebook|output-feedback-casebook|v1-casebook|describe|openmct-review file|openmct-fit file',file=sys.stderr)
    return 2
if __name__=='__main__':raise SystemExit(main())
