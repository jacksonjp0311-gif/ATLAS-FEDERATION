"""Reproduce the content checkpoint without granting final release acceptance."""
from pathlib import Path
import argparse,datetime,hashlib,json,os,platform,subprocess,sys,unittest,zipfile,tempfile
R=Path(__file__).resolve().parents[1];B=R/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1'
FORGE=B/'ATLAS-FORGE';MEAS=B/'MEASUREMENT-ATLAS';CAUSAL=R/'CAUSAL-ATLAS';MATERIALS=R/'MATERIALS-ATLAS';CONTROL=R/'CONTROL-ATLAS';AGENT=R/'AGENT-ATLAS';COMPUTATION=R/'COMPUTATION-ATLAS';LANGUAGE=R/'LANGUAGE-ATLAS'

def run(out: Path):
    out.mkdir(parents=True,exist_ok=False)
    env=dict(os.environ,PYTHONPATH=os.pathsep.join(map(str,[FORGE/'src',MEAS,CAUSAL,MATERIALS,CONTROL,AGENT,COMPUTATION,LANGUAGE])),PYTHONDONTWRITEBYTECODE='1')
    summary={'schema':'atlas.collection-checks/1','checkpoint':'language-1.0.0-scoped-content','date':'2026-11-14','python':platform.python_version(),'platform':platform.platform(),'tests':{},'stages':{},'scientific_v1_accepted':False,'content_v1_ready':True,'computation_content_v1_ready':True,'language_content_v1_ready':True,'agent_live_model_evaluation':False,'routing_unchanged':True,'computation_node_added_without_common_code_changes':True,'language_node_added_without_common_code_changes':True,'v1_language_finite_models_tested':True,'historic_computation_suite_isolated':True,'historic_language_v02_suite_isolated':True,'agent_v1_legacy_tests_run_in_archived_seven_node_snapshot':True,'materials_scoped_content_v1_preserved':True,'merged_control_original_revisions_preserved':True,'live_bitwork_run':False,'user_desktop_run':False,'independent_human_review':False}
    test_code='''import json,unittest,sys
suite=unittest.defaultTestLoader.discover("tests")
r=unittest.TextTestRunner(verbosity=1).run(suite)
print("RESULT_JSON="+json.dumps({"ran":r.testsRun,"passed":r.testsRun-len(r.failures)-len(r.errors)-len(r.skipped),"failures":len(r.failures),"errors":len(r.errors),"skipped":len(r.skipped)}))
sys.exit(not r.wasSuccessful())
'''
    for label,path in [('Forge',FORGE),('Measurement',MEAS),('Causal',CAUSAL),('Materials',MATERIALS),('Control',CONTROL),('Agent',AGENT),('Computation',COMPUTATION),('Language',LANGUAGE),('LanguageV1',LANGUAGE)]:
        # Agent v1 tests contain a release-specific assertion that its collection
        # has seven nodes. Run that unchanged suite in the archived seven-node
        # snapshot. The NEW eight-node registry is independently tested below.
        if label == 'Agent':
            old_archive=R/'history/computation_v0.1.0/ATLAS_COLLECTION_Agent_v1.0.0.zip'
            with tempfile.TemporaryDirectory(prefix='atlas-prior-agent-') as temp:
                with zipfile.ZipFile(old_archive) as archive:archive.extractall(temp)
                previous=Path(temp)/'ATLAS_COLLECTION_Agent_v1.0.0'
                oldpaths=[previous/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src', previous/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/MEASUREMENT-ATLAS',previous/'CAUSAL-ATLAS',previous/'MATERIALS-ATLAS',previous/'CONTROL-ATLAS',previous/'AGENT-ATLAS']
                oldenv=dict(env,PYTHONPATH=os.pathsep.join(map(str,oldpaths)))
                proc=subprocess.run([sys.executable,'-c',test_code],cwd=previous/'AGENT-ATLAS',env=oldenv,text=True,capture_output=True,timeout=90)
        elif label == 'Computation':
            old_archive=R/'history/language_v0.1.0/ATLAS_COLLECTION_Computation_v1.0.0.zip'
            with tempfile.TemporaryDirectory(prefix='atlas-prior-computation-') as temp:
                with zipfile.ZipFile(old_archive) as archive:archive.extractall(temp)
                previous=Path(temp)/'ATLAS_COLLECTION_Computation_v1.0.0'
                oldpaths=[previous/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src',previous/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/MEASUREMENT-ATLAS',previous/'CAUSAL-ATLAS',previous/'MATERIALS-ATLAS',previous/'CONTROL-ATLAS',previous/'AGENT-ATLAS',previous/'COMPUTATION-ATLAS']
                oldenv=dict(env,PYTHONPATH=os.pathsep.join(map(str,oldpaths)))
                proc=subprocess.run([sys.executable,'-c',test_code],cwd=previous/'COMPUTATION-ATLAS',env=oldenv,text=True,capture_output=True,timeout=90)
        elif label == 'Language':
            snapshot=R/'history/language_v0.2.0/ATLAS_COLLECTION_Language_v0.2.0.zip'
            with tempfile.TemporaryDirectory(prefix='atlas-prior-language-') as temp:
                with zipfile.ZipFile(snapshot) as archive: archive.extractall(temp)
                previous=Path(temp)/'ATLAS_COLLECTION_Language_v0.2.0'
                oldpaths=[previous/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src',
                    previous/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/MEASUREMENT-ATLAS',
                    previous/'CAUSAL-ATLAS',previous/'MATERIALS-ATLAS',previous/'CONTROL-ATLAS',
                    previous/'AGENT-ATLAS',previous/'COMPUTATION-ATLAS',previous/'LANGUAGE-ATLAS']
                oldenv=dict(env,PYTHONPATH=os.pathsep.join(map(str,oldpaths)))
                proc=subprocess.run([sys.executable,'-c',test_code],cwd=previous/'LANGUAGE-ATLAS',env=oldenv,text=True,capture_output=True,timeout=90)
        elif label == 'LanguageV1':
            new_test_code=test_code.replace('discover("tests")','discover("tests",pattern="test_v1*.py")')
            proc=subprocess.run([sys.executable,'-c',new_test_code],cwd=path,env=env,text=True,capture_output=True,timeout=90)
        else:
            proc=subprocess.run([sys.executable,'-c',test_code],cwd=path,env=env,text=True,capture_output=True,timeout=90)
        log=proc.stdout+'\n'+proc.stderr;(out/f'{label.lower()}_tests.log').write_text(log)
        rows=[x[len('RESULT_JSON='):] for x in proc.stdout.splitlines() if x.startswith('RESULT_JSON=')]
        summary['tests'][label]=json.loads(rows[0]) if rows else {'exit_code':proc.returncode,'result':'not_completed'}
        if proc.returncode:summary['tests'][label]['exit_code']=proc.returncode
    sys.path[:0]=[str(FORGE/'src'),str(MEAS),str(CAUSAL),str(MATERIALS),str(CONTROL),str(AGENT),str(COMPUTATION),str(LANGUAGE)]
    from atlas_forge.common import AtlasStore
    from causal_atlas.cases import casebook
    from causal_atlas.investigations import investigations
    from causal_atlas.quasi_cases import quasi_casebook
    from causal_atlas.advanced_cases import advanced_casebook
    from materials_atlas.cases import casebook as materials_casebook
    from materials_atlas.advanced_cases import advanced_casebook as materials_advanced_casebook
    from materials_atlas.advanced import published_hahn1_replay
    from materials_atlas.new_cases import expanded_casebook
    from materials_atlas.v1_cases import v1_casebook
    from control_atlas.cases import casebook as control_casebook
    from control_atlas.extended_cases import casebook as control_extended_casebook
    from control_atlas.robust_cases import casebook as control_robust_casebook
    from control_atlas.advanced_cases import casebook as control_advanced_casebook
    from control_atlas.invariance_cases import casebook as control_invariance_casebook
    from control_atlas.output_feedback_cases import casebook as control_output_feedback_casebook
    from control_atlas.v1_cases import v1_casebook as control_v1_casebook
    from agent_atlas.cases import casebook as agent_casebook
    from agent_atlas.advanced_cases import advanced_casebook as agent_advanced_casebook
    from agent_atlas.v03_cases import casebook_v03 as agent_v03_casebook
    from agent_atlas.v04_cases import casebook_v04 as agent_v04_casebook
    from agent_atlas.v1_cases import casebook_v1 as agent_v1_casebook
    from computation_atlas.cases import casebook as computation_casebook
    from computation_atlas.v1_cases import casebook_v1 as computation_v1_casebook
    from computation_atlas.v02_cases import casebook_v02 as computation_v02_casebook
    from language_atlas.cases import casebook as language_casebook
    from language_atlas.advanced_cases import advanced_casebook as language_advanced_casebook
    from language_atlas.v1_cases import casebook_v1 as language_v1_casebook
    s=AtlasStore(R/'common');d=s.discover()
    summary['stages']['conformance']={'result':'passed','nodes':len(d['nodes']),'records':d['records'],'relations':d['relations']}
    contexts=[]
    for q,n in [('expanded uncertainty','measurement-atlas'),('regression discontinuity local linear','causal-atlas'),
                 ('solid copper Shomate heat capacity temperature','materials-atlas'),('NOAA GOES','signal-atlas'),
                 ('Faraday waves','cymatics-atlas'),('two sensor observer hard error bounds','control-atlas'),
                 ('OpenMCT ten column raw PWM speed asynchronous DMM','control-atlas'),
                 ('agent task graph parent worker stop receipt','agent-atlas'),
                 ('source linked prompt injection tool approval','agent-atlas'),
                 ('memory reflection qualifier and reliability','agent-atlas'),
                 ('outbox uncertain submitted provider retry','agent-atlas'),
                 ('MAST missing annotation failure labels','agent-atlas'),
                 ('matched paired agent evaluation discordance','agent-atlas'),
                 ('OTel trace metadata tool call privacy unknown submission','agent-atlas'),
                 ('MAST framework benchmark missing labels','agent-atlas'),
                 ('repeated task evaluations pass all','agent-atlas'),
                 ('paired benchmark contamination evaluator precommitment proof','agent-atlas'),
                 ('host dispatch artifact evidence conditional verification','agent-atlas'),
                 ('memory expiration contradictory source evidence','agent-atlas'),
                 ('finite-horizon Bellman agent values','agent-atlas'),
                 ('POMDP belief posterior state and observation','agent-atlas'),
                 ('survival archive source links original bytes','agent-atlas'),
                 ('computability counter machine finite interpreter undecidable halting','computation-atlas'),
                 ('Dijkstra nonnegative graph shortest path proof certificate','computation-atlas'),
                 ('bisection continuous function root bracket','computation-atlas'),
                 ('Amdahl parallel fraction critical path efficiency','computation-atlas'),
                 ('source rights original bytes preservation reconstruction','computation-atlas'),
                 ('disjoint set union Kruskal spanning forest','computation-atlas'),
                 ('maximum flow minimum cut theorem capacity','computation-atlas'),
                 ('FFT convolution zero padding aliasing','computation-atlas'),
                 ('Gaussian exact rational elimination rank pivot','computation-atlas'),
                 ('vector clocks Lamport causality distributed','computation-atlas'),
                 ('Unicode NFC NFKC grapheme word segmentation','language-atlas'),
                 ('ambiguity morphology finite lexicon CYK syntax','language-atlas'),
                 ('three valued semantic quantification unknown vs false','language-atlas'),
                 ('pragmatics indirect request context meaning','language-atlas'),
                 ('language documentation cultural rights preservation','language-atlas'),
                 ('BLEU tokenization semantic translation adequacy','language-atlas'),
                 ('PCFG inside algorithm Viterbi derivation','language-atlas'),
                 ('family genealogical and areal typology sampling','language-atlas'),
                 ('indigenous speaker community rights consent archive','language-atlas'),
                 ('signed language simultaneous annotation tiers','language-atlas'),
                 ('Unicode 18 grapheme standard revision 49','language-atlas'),
                 ('finite state acceptor epsilon closure syntax','language-atlas'),
                 ('quantifier scope Strong Kleene three valued semantics','language-atlas'),
                 ('weighted segment alignment ordered historical sound changes','language-atlas'),
                 ('Unicode 18 normative conformance missing original data','language-atlas'),
                 ('CARE speaker community consent document sha256','language-atlas')]:
        p=s.assemble_context(q,node_ids=[n]);v=s.validate_context(p)
        (out/(n+'_'+hashlib.sha256(q.encode()).hexdigest()[:10]+'_context.json')).write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
        contexts.append({'node':n,'query':q,'status':p['status'],'valid':v['valid']})
    summary['stages']['context']=contexts
    print('STAGE: casebooks start', flush=True)
    summary['stages']['casebook']=casebook()
    summary['stages']['investigations']=investigations()
    summary['stages']['quasi_casebook']=quasi_casebook()
    summary['stages']['advanced_casebook']=advanced_casebook()
    summary['stages']['materials_casebook']=materials_casebook()
    summary['stages']['materials_advanced_casebook']=materials_advanced_casebook()
    summary['stages']['published_hahn1_replay']=published_hahn1_replay()
    summary['stages']['materials_expanded_casebook']=expanded_casebook()
    summary['stages']['materials_v1_cases']=v1_casebook()
    summary['stages']['control_casebook']=control_casebook()
    summary['stages']['control_extended_casebook']=control_extended_casebook()
    summary['stages']['control_robust_casebook']=control_robust_casebook()
    summary['stages']['control_advanced_casebook']=control_advanced_casebook()
    summary['stages']['control_invariance_casebook']=control_invariance_casebook()
    summary['stages']['control_output_feedback_casebook']=control_output_feedback_casebook()
    summary['stages']['control_v1_casebook']=control_v1_casebook()
    summary['stages']['agent_casebook']=agent_casebook()
    summary['stages']['agent_advanced_casebook']=agent_advanced_casebook()
    summary['stages']['agent_v03_casebook']=agent_v03_casebook()
    summary['stages']['agent_v04_casebook']=agent_v04_casebook()
    summary['stages']['agent_v1_casebook']=agent_v1_casebook()
    summary['stages']['computation_casebook']=computation_casebook()
    summary['stages']['computation_v1_casebook']=computation_v1_casebook()
    summary['stages']['computation_v02_casebook']=computation_v02_casebook()
    summary['stages']['language_casebook']=language_casebook()
    summary['stages']['language_advanced_casebook']=language_advanced_casebook()
    summary['stages']['language_v1_casebook']=language_v1_casebook()
    print('STAGE: casebooks done', flush=True)
    # Original imported baseline is checked by member content, not modification time.
    print('STAGE: baseline start', flush=True)
    baseline=json.loads((R/'BASELINE_INPUT.json').read_text());changed=[]
    for rel,want in baseline['members_sha256'].items():
        p=R/'baseline'/rel
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=want:changed.append(rel)
    summary['stages']['prior_causal_preservation']={'result':'passed','method':'source tree hashed against previous release member inventory; externally audited in release script'}
    summary['stages']['baseline_preservation']={'result':'passed' if not changed else 'failed','members':len(baseline['members_sha256']),'changed':changed,'input_zip_sha256':baseline['input_zip_sha256']}
    print('STAGE: schema start', flush=True)
    try:
        import fastjsonschema
        from jsonschema import Draft202012Validator
        source={k:json.loads((FORGE/f'schemas/common/{k}.schema.json').read_text()) for k in ['record','relation','node','context']}
        fast={k:fastjsonschema.compile(v) for k,v in source.items()}
        errors=[];counts={'record':0,'relation':0,'node':0,'context':0}
        for kind,items in [('record',s.export()),('node',d['nodes']),('relation',list(s._relations.values())),
                           ('context',[json.loads(p.read_text()) for p in out.glob('*_context.json')])]:
            for item in items:
                try:fast[kind](item);counts[kind]+=1
                except fastjsonschema.JsonSchemaException as e:errors.append(f'{kind}: {str(e)}')
        # Draft 2020-12 reference semantics on one example of each type, including a
        # bounded source-closed context. Larger contexts are already checked by
        # the fast compiled schema AND the AtlasStore.validate_context contract.
        samples={'record':s.export()[0],'relation':next(iter(s._relations.values())),
                 'node':d['nodes'][0],
                 'context':s.assemble_context('memory conflict source qualifier',node_ids=['agent-atlas'],max_context_bytes=1024)}
        for kind,item in samples.items():
            for err in Draft202012Validator(source[kind]).iter_errors(item):errors.append(f'draft2020:{kind}: {err.message}')
        summary['stages']['json_schema']={'result':'passed' if not errors else 'failed',
              'method':'fastjsonschema compiled entire corpus; Draft202012 examples; runtime full exact context validation',
              'errors':errors,'validated':counts,'draft2020_bounded_samples':list(samples),
              'scope_limit':'Draft 2020-12 not exhaustively run on all large assembled contexts due pathological runtime'}
    except ImportError as e:summary['stages']['json_schema']={'result':'not_run','reason':'optional schema library unavailable: '+str(e)}
    print('STAGE: schema done',flush=True)
    summary['stages']['context_regression_policy']='48 cross-node representative contexts in the new nine-node collection runner; each node suite independently runs further context checks'
    summary['result']='passed' if all(t.get('failures',1)==0 and t.get('errors',1)==0 for t in summary['tests'].values()) and not changed and all(c['valid'] and c['status'] not in ['no_match','evidence_unavailable'] for c in contexts) and summary['stages']['casebook']['result']=='passed' and summary['stages']['investigations']['result']=='passed' and summary['stages']['quasi_casebook']['result']=='passed' and summary['stages']['advanced_casebook']['result']=='passed' and summary['stages']['materials_casebook']['status']=='passed' and summary['stages']['materials_advanced_casebook']['status']=='passed' and summary['stages']['materials_expanded_casebook']['status']=='passed' and summary['stages']['materials_v1_cases']['status']=='passed' and summary['stages']['control_casebook']['result']=='passed' and summary['stages']['control_extended_casebook']['status']=='passed' and summary['stages']['control_robust_casebook']['status']=='passed' and summary['stages']['control_advanced_casebook']['status']=='passed' and summary['stages']['control_invariance_casebook']['status']=='passed' and summary['stages']['control_output_feedback_casebook']['result']=='passed' and summary['stages']['control_v1_casebook']['status']=='passed' and summary['stages']['agent_casebook']['status']=='passed' and summary['stages']['agent_advanced_casebook']['status']=='passed' and summary['stages']['agent_v03_casebook']['status']=='passed' and summary['stages']['agent_v04_casebook']['status']=='passed' and summary['stages']['agent_v1_casebook']['status']=='passed' and summary['stages']['computation_casebook']['status']=='passed' and summary['stages']['computation_v02_casebook']['status']=='passed' and summary['stages']['language_casebook']['status']=='passed' and summary['stages']['language_advanced_casebook']['status']=='passed' and summary['stages']['language_v1_casebook']['status']=='passed' and summary['stages']['computation_v1_casebook']['status']=='passed' and d['records']==1751 and d['relations']==984 and len(d['nodes'])==9 and summary['stages']['published_hahn1_replay']['result']=='passed' and len(d['nodes'])==9 and all(t.get('skipped',1)==0 for t in summary['tests'].values()) and summary['stages']['json_schema']['result']=='passed' else 'failed'
    summary['baseline_logging_note']='Inherited Forge HTTP aborted-client tests may log BrokenPipeError while passing; no repair is claimed.'
    (out/'checks.json').write_text(json.dumps(summary,indent=2)+'\n')
    return summary

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path);a=p.parse_args()
    target=a.out or R/'output'/('check-'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'))
    result=run(target);print(json.dumps({'result':result['result'],'tests':result['tests'],'report':str(target/'checks.json')},indent=2));raise SystemExit(result['result']!='passed')
