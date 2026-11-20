#!/usr/bin/env python3
"""Execute local Atlas-build checks without publishing or advancing the active domain.

Writes receipts to output/ by default, outside the immutable release manifest.
A successful check run does NOT satisfy the complete Measurement v1 gate.
"""
from pathlib import Path
import argparse,hashlib,json,os,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[1]

def run(measurement:Path,out:Path):
    if not (measurement/'measurement_atlas').is_dir():raise ValueError('Measurement source tree missing; supply --measurement PATH')
    if out.exists() and any(out.iterdir()):raise ValueError('output directory not empty; choose a new receipt directory')
    out.mkdir(parents=True,exist_ok=True)
    env=dict(os.environ);env['PYTHONPATH']=os.pathsep.join([str(ROOT/'src'),str(measurement)]);env['PYTHONDONTWRITEBYTECODE']='1'
    tasks=[('forge_unit',ROOT,['-m','unittest','discover','-s','tests','-v']),
           ('measurement_unit',measurement,['-m','unittest','discover','-s','tests','-v']),
           ('conformance',ROOT,['tools/workflow.py','conform']),('skills',ROOT,['tools/workflow.py','skills-check']),
           ('curation',ROOT,['tools/check_curation.py',str(measurement/'evidence/primary_reference_additions.json')]),
           ('context_diagnostic',ROOT,['tools/evaluate_common.py']),('synthetic_casebook',measurement,['tools/casebook.py']),
           ('content_reference_audit',measurement,['tools/check_content.py']),
           ('content_casebook',measurement,['tools/content_casebook.py']),
           ('published_calibration_case',measurement,['-m','measurement_atlas','published-case']),
           ('coverage_casebook',measurement,['tools/coverage_casebook.py']),
           ('inverse_interval_replay',measurement,['-m','measurement_atlas','inverse-interval']),
           ('practical_casebook',measurement,['tools/practical_casebook.py']),
           ('gate_status',ROOT,['tools/workflow.py','status'])]
    rows=[]
    for name,cwd,args in tasks:
        start=time.perf_counter();p=subprocess.run([sys.executable,*args],cwd=cwd,env=env,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=180)
        text=p.stdout+p.stderr;path=out/(name+'.log');path.write_text(text,encoding='utf-8')
        rows.append({'name':name,'command':[sys.executable,*args],'exit_code':p.returncode,'wall_seconds':time.perf_counter()-start,'log':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    p=subprocess.run([sys.executable,'tools/workflow.py','advance','--node','causal-atlas'],cwd=ROOT,env=env,capture_output=True,text=True,encoding='utf-8',timeout=60)
    path=out/'next_domain_guard.log';path.write_text(p.stdout+p.stderr,encoding='utf-8')
    guard=(p.returncode==2 and 'Measurement v1 acceptance incomplete' in p.stdout)
    result={'schema':'atlas.workflow-execution/1','result':'passed' if all(x['exit_code']==0 for x in rows) and guard else 'failed',
      'stages':rows,'next_domain_guard_worked':guard,'measurement_v1_accepted':False,'host_skills_installed':False,'remote_changes':False}
    (out/'summary.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');return result

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--measurement',type=Path,default=ROOT.parent/'MEASUREMENT-ATLAS');p.add_argument('--out',type=Path,default=ROOT/'output/workflow-check');a=p.parse_args()
    try:r=run(a.measurement.resolve(),a.out.resolve());print(json.dumps(r,indent=2));sys.exit(0 if r['result']=='passed' else 2)
    except (OSError,ValueError,subprocess.TimeoutExpired) as exc:print(json.dumps({'result':'failed','error':str(exc)}));sys.exit(2)
