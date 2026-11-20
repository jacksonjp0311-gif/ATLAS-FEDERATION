#!/usr/bin/env python3
"""Run the candidate checks on this actual host. Never labels Linux as Windows."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,os,platform,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]

def run(out:Path):
    if out.exists():raise ValueError('choose a fresh output directory; prior receipts are not overwritten')
    out.mkdir(parents=True)
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONPATH=os.pathsep.join([str(ROOT/'ATLAS-FORGE/src'),str(ROOT/'MEASUREMENT-ATLAS')]))
    stages=[('workflow',ROOT/'ATLAS-FORGE',['tools/run_workflow.py','--measurement',str(ROOT/'MEASUREMENT-ATLAS'),'--out',str(out/'workflow')]),
            ('practical_cases',ROOT/'MEASUREMENT-ATLAS',['tools/practical_casebook.py']),
            ('source_content',ROOT/'MEASUREMENT-ATLAS',['tools/check_content.py']),
            ('domain_queue',ROOT,['tools/validate_domain_queue.py']),
            ('readiness',ROOT,['tools/v1_readiness.py'])]
    results=[]
    for name,cwd,args in stages:
        p=subprocess.run([sys.executable,*args],cwd=cwd,env=env,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=300)
        log=out/(name+'.log');log.write_text(p.stdout+p.stderr,encoding='utf-8')
        results.append({'name':name,'exit_code':p.returncode,'log':log.name,'sha256':hashlib.sha256(log.read_bytes()).hexdigest()})
    report={'schema':'atlas.candidate-host-check/1','execution_kind':'local_actual','platform':platform.platform(),
            'sys_platform':sys.platform,'python':platform.python_version(),'recorded_at':datetime.now(timezone.utc).isoformat(),
            'result':'passed' if all(x['exit_code']==0 for x in results) else 'failed',
            'stages':results,'checks_are_not_final_v1_acceptance':True,'independent_review':False,
            'live_bitwork_run':False,'heldout_model_comparison':False,'desktop_or_remote_changes':False}
    (out/'host_receipt.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');return report
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,default=None);a=p.parse_args()
    out=a.out or ROOT/'ATLAS-FORGE/output'/('candidate-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%f'))
    try:r=run(out.resolve());print(json.dumps(r,indent=2));sys.exit(0 if r['result']=='passed' else 2)
    except (OSError,ValueError,subprocess.TimeoutExpired) as exc:print(json.dumps({'result':'failed','error':str(exc)}));sys.exit(2)
