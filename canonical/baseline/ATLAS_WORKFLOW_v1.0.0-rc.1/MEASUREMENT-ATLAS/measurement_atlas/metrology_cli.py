"""Explicit invocation of new metrology utilities; retrieval never calls these."""
import argparse
import json
from pathlib import Path
from .units import convert_quantity
from .certificates import review_certificate, specification_component, reported_standard_uncertainty
from .decisions import normal_conformance, guard_band_decision
OPERATIONS={'convert':convert_quantity,'certificate-review':review_certificate,
            'specification-component':specification_component,'reported-uncertainty':reported_standard_uncertainty,
            'conformance-probability':normal_conformance,'guard-band':guard_band_decision}

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation',choices=OPERATIONS)
    parser.add_argument('payload',nargs='?',help='JSON object of explicit parameters')
    parser.add_argument('--input',type=Path,help='JSON input file; alternative to payload')
    args=parser.parse_args(argv)
    try:
        if (args.payload is None)==(args.input is None):raise ValueError('supply one JSON payload or --input file')
        raw=args.payload if args.input is None else args.input.read_text(encoding='utf-8')
        if len(raw.encode('utf-8'))>65536:raise ValueError('input exceeds 64 KiB')
        obj=json.loads(raw)
        if not isinstance(obj,dict):raise ValueError('JSON object required')
        result=OPERATIONS[args.operation](**obj)
        print(json.dumps(result,indent=2,ensure_ascii=False,allow_nan=False))
        return 0
    except (OSError,ValueError,TypeError,OverflowError) as exc:
        print(json.dumps({'status':'invalid_input','error':str(exc)}));return 2
if __name__=='__main__':raise SystemExit(main())
