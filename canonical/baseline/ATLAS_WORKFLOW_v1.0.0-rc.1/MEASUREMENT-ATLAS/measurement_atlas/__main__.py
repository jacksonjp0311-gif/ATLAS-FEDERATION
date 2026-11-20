import sys
if len(sys.argv)>1 and sys.argv[1] in ('convert','certificate-review','specification-component','reported-uncertainty','conformance-probability','guard-band'):
    from .metrology_cli import main
    raise SystemExit(main(sys.argv[1:]))
if len(sys.argv)>1 and sys.argv[1]=='inverse-interval':
    from .intervals import main
    raise SystemExit(main(sys.argv[2:]))
if len(sys.argv)>1 and sys.argv[1]=='published-case':
    from .published_case import main
    raise SystemExit(main(sys.argv[2:]))
if len(sys.argv)>1 and sys.argv[1]=='reference':
    from .reference import main
    raise SystemExit(main(sys.argv[2:]))
import argparse, json
from .uncertainty import type_a, combine_linear, expanded_uncertainty
from .budget import uncertainty_budget, type_b
from .traceability import audit_chain
p=argparse.ArgumentParser(description='Measurement Atlas: transparent numerical and documentation models, not certification')
p.add_argument('operation',choices=['type-a','combine','expand','type-b','budget','traceability'])
p.add_argument('json_input',help='JSON arguments appropriate to selected operation')
a=p.parse_args();obj=json.loads(a.json_input)
if a.operation=='type-a':r=type_a(obj)
elif a.operation=='combine':r=combine_linear(obj['sensitivities'],obj['covariance'])
elif a.operation=='expand':r=expanded_uncertainty(obj['uncertainty'],obj['k'])
elif a.operation=='type-b':r=type_b(obj['half_width'],obj['distribution'])
elif a.operation=='budget':r=uncertainty_budget(obj['components'],obj.get('correlations'),obj.get('output_unit'))
else:r=audit_chain(obj['nodes'],obj['edges'],measurement_id=obj['measurement_id'],as_of=obj.get('as_of'))
print(json.dumps(r,indent=2,sort_keys=True))
