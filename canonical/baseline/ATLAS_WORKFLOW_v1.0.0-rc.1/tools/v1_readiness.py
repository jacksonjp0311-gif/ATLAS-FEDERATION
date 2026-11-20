#!/usr/bin/env python3
"""Report real final-release gates. --require-final refuses incomplete v1 acceptance.

The report binds BOTH project source trees; this supplements the existing Forge
subject digest and never treats a local test count as independent review.
"""
from pathlib import Path
import argparse,json,sys,hashlib
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'ATLAS-FORGE/src'))
from atlas_forge.workflow import gate_report,subject_digest

def report(root=ROOT):
    forge=root/'ATLAS-FORGE';measurement=root/'MEASUREMENT-ATLAS'
    gates=gate_report(forge)
    measurement_subject=subject_digest(measurement)
    candidate=json.loads((root/'RELEASE_CANDIDATE.json').read_text(encoding='utf-8'))
    blockers=[{'gate':g['gate'],'status':g['status'],'remaining':g['remaining'],'errors':g['errors']} for g in gates['gates'] if g['status']!='passed']
    if not gates['criteria_frozen']:blockers.insert(0,{'gate':'CRITERIA','status':'not_frozen','remaining':['Record owner-approved scope and freeze the independent evaluation plan.'],'errors':[]})
    # Passed numerical/integration/evaluation/release receipts must also bind Measurement code.
    binding_errors=[]
    decisions=json.loads((forge/'workflow/gate_decisions.json').read_text(encoding='utf-8'))
    for key in ('G3','G6','G7','G8'):
        dec=decisions['gates'][key]
        if dec['status']=='passed':
            for entry in dec['evidence']:
                try:
                    receipt=json.loads((forge/entry['path']).read_text(encoding='utf-8'))
                    if receipt.get('measurement_subject_sha256')!=measurement_subject:binding_errors.append(key+': Measurement input binding absent or stale')
                except (OSError,ValueError,KeyError) as exc:binding_errors.append(key+': '+str(exc))
    if binding_errors:blockers.append({'gate':'CROSS_PROJECT_BINDING','status':'invalid','remaining':binding_errors,'errors':binding_errors})
    ready=bool(gates['v1_ready'] and not binding_errors)
    return {'schema':'atlas.v1-readiness/1','candidate_version':candidate['candidate_version'],
      'target_version':'1.0.0','status':'final_acceptance_supported' if ready else 'release_candidate_not_final',
      'v1_ready':ready,'next_domain_allowed':ready,
      'subjects':{'forge_sha256':subject_digest(forge),'measurement_sha256':measurement_subject},
      'criteria_sha256':gates['criteria_sha256'],'criteria_frozen':gates['criteria_frozen'],
      'gates':gates['gates'],'blockers':blockers,
      'limits':['Local evidence records are not cryptographic attestation of a reviewer or remote platform.',
                'A release-candidate version does not grant stable release or next-domain permission.']}
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--require-final',action='store_true');a=p.parse_args()
    try:
        r=report();print(json.dumps(r,indent=2));sys.exit(2 if a.require_final and not r['v1_ready'] else 0)
    except (ValueError,OSError,KeyError) as exc:print(json.dumps({'status':'invalid','error':str(exc)}));sys.exit(2)
